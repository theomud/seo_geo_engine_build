#!/usr/bin/env python3
"""
Content-Intelligence registry — the system's "memory".

Scans every built page, audits it (the 5-lens / 7-category QA), enriches it with the
content-asset JSON metadata (question, funnel stage, page type, monetization, status,
needs-verification flags), and emits one registry the whole operation reads from:
  sites/<site>/content/REGISTRY.md   (human table)
  sites/<site>/content/registry.csv  (data)
  sites/<site>/content/registry.json (machine)

This is the lean, flat-file version of the Content Intelligence Engine's database —
no Supabase needed until we run many sites. It is the single place to see, per asset:
what question it answers, its funnel stage, its status, its audit score, and whether its
claims are verified.

Usage:  py audit/registry.py [site]            (default: pawroute)
"""
from __future__ import annotations
import csv, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit import load, audit_page, LENSES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# workflow states from the Content Intelligence Engine doc
STATES = ["Idea", "Validated Question", "Researching", "Brief Ready", "Drafting",
          "Editing", "SEO/GEO Review", "QA Review", "Approved", "Published", "Refreshing", "Archived"]

def _content_meta(site: str):
    """Map url -> metadata from the content-asset JSON files."""
    cdir = ROOT / "sites" / site / "content"
    out = {}
    if not cdir.exists():
        return out
    for j in sorted(cdir.glob("*.json")):
        try:
            d = json.loads(j.read_text(encoding="utf-8"))
        except Exception:
            continue
        m = d.get("_meta", {}); seo = d.get("seo", {})
        url = (seo.get("canonical_path") or "").rstrip("/") + "/"
        if url == "/":
            continue
        out[url] = {
            "question": m.get("target_keyword", ""),
            "funnel": m.get("funnel_stage", ""),
            "page_type_doc": m.get("page_type", ""),
            "fear": m.get("primary_fear", ""),
            "monetization": m.get("monetization", m.get("objective", "lead_generation")),
            "json": j.name,
            "needs_verification": (d.get("grounding", {}) or {}).get("needs_verification", ""),
        }
    return out

def build(site: str = "pawroute"):
    dist = ROOT / "dist" / site
    if not dist.exists():
        sys.exit(f"no build at {dist} — run: py engine/build.py sites/{site}")
    cmeta = _content_meta(site)
    claims_audited = (ROOT / "sites" / site / "content" / "CLAIMS-AUDIT.md").exists()
    rows = []
    for f in sorted(dist.rglob("index.html")):
        rel = f.parent.relative_to(dist).as_posix()
        url = "/" if rel == "." else "/" + rel + "/"
        page = load(str(f))
        page.url = url  # use the web path (not the file path) so page-type detection sees /blog/, /destinations/…
        res = audit_page(page, "homepage" if url == "/" else None)
        cm = cmeta.get(url, {})
        q = res["lenses"].get("quality", {})
        rows.append({
            "status": "Published" if cm else "Published (no brief)",
            "grade": res["grade"], "score": res["score"],
            "quality": q.get("score"),
            "page_type": res["profile"],
            "page_type_doc": cm.get("page_type_doc", ""),
            "funnel": cm.get("funnel", ""),
            "question": cm.get("question", ""),
            "fear": cm.get("fear", ""),
            "monetization": cm.get("monetization", ""),
            "critical_fails": "; ".join(res["critical_fails"]),
            "content_json": cm.get("json", ""),
            "claims": ("CLAIMS-AUDIT.md" if (claims_audited and cm) else ""),
            "needs_verification": cm.get("needs_verification", ""),
            "title": res["title"], "url": url,
        })
    rows.sort(key=lambda r: r["score"])
    return {"site": site, "count": len(rows),
            "avg_score": round(sum(r["score"] for r in rows) / len(rows), 1) if rows else 0,
            "with_brief": sum(1 for r in rows if r["content_json"]),
            "assets": rows}

def write(reg, site: str):
    cdir = ROOT / "sites" / site / "content"
    (cdir / "registry.json").write_text(json.dumps(reg, indent=2), encoding="utf-8")
    cols = ["status", "grade", "score", "quality", "page_type", "funnel", "question",
            "monetization", "content_json", "claims", "needs_verification", "critical_fails", "url", "title"]
    with (cdir / "registry.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader(); w.writerows(reg["assets"])
    # markdown
    L = [f"# Content-Intelligence registry — {site}", "",
         f"The system's memory. {reg['count']} assets · avg audit **{reg['avg_score']}/100** · "
         f"{reg['with_brief']} with a content brief. Rebuild: `py audit/registry.py {site}`.", "",
         "| Status | Grade | Score | ✨Qual | Page type | Funnel | Question / keyword | Brief | Claims | ⚠ Verify |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in reg["assets"]:
        verify = "⚠" if r["needs_verification"] else ""
        L.append(f"| {r['status']} | {r['grade']} | {r['score']} | {r['quality']} | {r['page_type']} | "
                 f"{r['funnel'][:18]} | {(r['question'] or r['title'])[:42]} | "
                 f"{'✓' if r['content_json'] else '—'} | {'✓' if r['claims'] else '—'} | {verify} |")
    L += ["", "## Workflow states", "`" + " → ".join(STATES) + "`",
          "", "_Assets without a brief were built from page YAML directly; give them a content JSON to track question/funnel/monetization._"]
    (cdir / "REGISTRY.md").write_text("\n".join(L), encoding="utf-8")

def main(argv):
    site = argv[0] if argv else "pawroute"
    reg = build(site)
    write(reg, site)
    print(f"Registry: {reg['count']} assets · avg {reg['avg_score']} · {reg['with_brief']} with brief")
    print(f"-> sites/{site}/content/REGISTRY.md  registry.csv  registry.json")
    return 0

if __name__ == "__main__":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    raise SystemExit(main(sys.argv[1:]))
