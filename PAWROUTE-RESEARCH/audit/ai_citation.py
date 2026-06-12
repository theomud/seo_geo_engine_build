#!/usr/bin/env python3
"""
Live AI-citation test harness — are we cited by the answer engines?

For each target query, asks the AI engines we have keys for and checks whether OUR domain
appears in their cited sources. Emits a citation-share report + an append-only tracking log
(citation share is volatile — re-run regularly, per our KB caveat).

This measures the ONE thing our on-page auditor cannot: real GEO outcome. It needs the site
to be live + indexed first — until then it honestly reports a 0% baseline.

Engines (each gated on a key in .env; skipped cleanly if absent):
  - Perplexity   (PERPLEXITY_API_KEY)            -> returns citations
  - Gemini       (GEMINI_API_KEY / GOOGLE_API_KEY) with Google-Search grounding -> grounding sources
  - Google AI Overviews via SerpApi (SERPAPI_API_KEY) -> ai_overview references
ChatGPT web + live AI-Overviews in-browser aren't API-citable reliably -> capture manually.

Usage:
  py audit/ai_citation.py --domain pawroute.ae
  py audit/ai_citation.py --queries audit/queries/citation-targets.json
"""
from __future__ import annotations
import argparse, json, re, sys, datetime, urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_env():
    env = {}
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env

def _post(url, payload, headers, timeout=40):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json", **headers})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def _get(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": "GoldAuditor/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

# ---- engine adapters: return list[str] of cited URLs, or None if unavailable ----
def ask_perplexity(q, env):
    key = env.get("PERPLEXITY_API_KEY")
    if not key: return None
    try:
        d = _post("https://api.perplexity.ai/chat/completions",
                  {"model": "sonar", "messages": [{"role": "user", "content": q}]},
                  {"Authorization": "Bearer " + key})
        cites = d.get("citations") or d.get("search_results") or []
        return [c if isinstance(c, str) else c.get("url", "") for c in cites]
    except Exception as e:
        return {"error": str(e)[:120]}

def ask_gemini(q, env):
    key = env.get("GEMINI_API_KEY") or env.get("GOOGLE_API_KEY")
    if not key: return None
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + key
        d = _post(url, {"contents": [{"parts": [{"text": q}]}], "tools": [{"google_search": {}}]}, {})
        gm = (d.get("candidates") or [{}])[0].get("groundingMetadata", {})
        chunks = gm.get("groundingChunks", [])
        return [c.get("web", {}).get("uri", "") for c in chunks]
    except Exception as e:
        return {"error": str(e)[:120]}

def ask_serpapi_aio(q, env):
    key = env.get("SERPAPI_API_KEY") or env.get("SERPAPI_KEY")
    if not key: return None
    try:
        url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(
            {"engine": "google", "q": q, "api_key": key, "gl": "ae", "hl": "en"})
        d = _get(url)
        aio = d.get("ai_overview", {})
        refs = aio.get("references", []) or []
        return [r.get("link", "") for r in refs]
    except Exception as e:
        return {"error": str(e)[:120]}

ENGINES = {"perplexity": ask_perplexity, "gemini": ask_gemini, "ai_overview(serpapi)": ask_serpapi_aio}

def domain_in(urls, domain):
    pos = None
    for i, u in enumerate(urls):
        if domain.lower() in (u or "").lower():
            pos = i + 1; break
    return pos

def main(argv=None):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    ap = argparse.ArgumentParser(description="Live AI-citation test harness")
    ap.add_argument("--domain", help="your domain, e.g. pawroute.ae")
    ap.add_argument("--queries", help="JSON file: {domain, queries:[...]}")
    a = ap.parse_args(argv)

    spec = {}
    if a.queries and Path(a.queries).exists():
        spec = json.loads(Path(a.queries).read_text(encoding="utf-8"))
    qf = ROOT / "audit/queries/citation-targets.json"
    if not spec and qf.exists():
        spec = json.loads(qf.read_text(encoding="utf-8"))
    domain = a.domain or spec.get("domain") or "pawroute.ae"
    queries = spec.get("queries", [])
    if not queries:
        sys.exit("No target queries. Pass --queries or create audit/queries/citation-targets.json")

    env = load_env()
    active = [name for name, fn in ENGINES.items() if fn("ping", env) is not None]
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"AI-citation test · domain={domain} · {len(queries)} queries")
    print(f"Engines with keys: {', '.join(active) if active else 'NONE — add PERPLEXITY_API_KEY / GEMINI_API_KEY / SERPAPI_API_KEY to .env'}")

    rows, cited_count, checks = [], 0, 0
    for q in queries:
        for name, fn in ENGINES.items():
            res = fn(q, env)
            if res is None:
                continue  # no key
            if isinstance(res, dict) and res.get("error"):
                rows.append({"query": q, "engine": name, "status": "error", "detail": res["error"]})
                print(f"  ! {name:22} {q[:50]} — {res['error']}"); continue
            urls = [u for u in res if u]
            pos = domain_in(urls, domain)
            checks += 1
            if pos: cited_count += 1
            rows.append({"query": q, "engine": name, "cited": bool(pos), "position": pos,
                         "n_sources": len(urls), "sources": urls[:12]})
            print(f"  {'✓ CITED #'+str(pos) if pos else '✗ not cited'}  {name:22} {q[:50]} ({len(urls)} sources)")

    share = round(100 * cited_count / checks, 1) if checks else 0.0
    out = {"checked": ts, "domain": domain, "engines_active": active,
           "queries": len(queries), "checks": checks, "cited": cited_count,
           "citation_share_pct": share, "results": rows}
    outdir = ROOT / "audit/evidence/ai-citation"; outdir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    (outdir / f"report-{stamp}.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    log = outdir / "CITATION-LOG.md"
    head = "" if log.exists() else "# AI-citation tracking log\n\n| Date | Domain | Engines | Queries | Cited | Share % |\n|---|---|---|---|---|---|\n"
    with log.open("a", encoding="utf-8") as f:
        f.write(head + f"| {ts} | {domain} | {','.join(active) or '—'} | {len(queries)} | {cited_count}/{checks} | {share}% |\n")
    print(f"\nCitation share: {cited_count}/{checks} = {share}%  ->  audit/evidence/ai-citation/report-{stamp}.json")
    if not active:
        print("Baseline only — add an engine key, deploy + index the site, then re-run to measure real GEO citation.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
