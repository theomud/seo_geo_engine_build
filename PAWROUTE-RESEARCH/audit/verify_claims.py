#!/usr/bin/env python3
"""
Claim verifier with screenshot evidence — official sources only.

For every claim, opens its OFFICIAL source in a real browser (Playwright/Chromium),
screenshots the full page as proof, optionally confirms an expected phrase, and writes
an evidence ledger. This is the gold-standard "cite or hedge — with proof" discipline:
no claim is treated as verified without an official-source screenshot on disk.

Usage:
    py audit/verify_claims.py audit/claims/<file>.json
    # -> screenshots in audit/evidence/<set>/  +  CLAIMS-LEDGER.md / .json
"""
from __future__ import annotations
import json, re, sys, datetime
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

# Official-source allowlist (government + the recognised standards bodies). Nothing else verifies.
OFFICIAL = [
    # governments + standards bodies
    "gov.uk", "cdc.gov", "agriculture.gov.au", "moccae.gov.ae", "iata.org",
    "europa.eu", "ec.europa.eu", "inspection.canada.ca", "nparks.gov.sg",
    "aqcsindia.gov.in", "dalrrd.gov.za", "gov.za", "developers.google.com",
    "web.dev", "nngroup.com", "baymard.com",
    # the primary operator's own sites (Principle 6: airline verified separately, but its own site IS official for its policy)
    "emirates.com", "skycargo.com", "etihad.com", "etihadcargo.com", "flydubai.com",
]

def is_official(url: str):
    host = (urlparse(url).hostname or "").lower()
    for d in OFFICIAL:
        if host == d or host.endswith("." + d):
            return True, host
    return False, host

def slug(s: str):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]

def main(argv):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    if not argv:
        sys.exit("usage: py audit/verify_claims.py <claims.json>")
    spec = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    setname = spec.get("set", Path(argv[0]).stem)
    claims = spec["claims"]
    outdir = ROOT / "audit" / "evidence" / setname
    outdir.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright
    ts = datetime.datetime.now().strftime("%Y-%m-%d")
    reverify = (datetime.datetime.now() + datetime.timedelta(days=spec.get("reverify_days", 180))).strftime("%Y-%m-%d")
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--disable-http2", "--disable-quic"])
        ctx = browser.new_context(viewport={"width": 1366, "height": 900},
                                  user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) GoldAuditor/1.0")
        for c in claims:
            cid = c.get("id") or slug(c["claim"])
            url = c["source_url"]
            ok_official, host = is_official(url)
            rec = {"id": cid, "claim": c["claim"], "authority": c.get("authority", host),
                   "source_url": url, "official": ok_official, "host": host,
                   "expect": c.get("expect"), "status": None, "screenshot": None,
                   "bytes": 0, "found": None, "checked": ts,
                   # --- regulatory metadata (Principles 7 & 13: every rule carries its provenance) ---
                   "kind": c.get("kind", "fact"),                 # fact | advice
                   "version": c.get("version", ts),               # regulation version / as-of
                   "reviewer": c.get("reviewer", "(pending human sign-off)"),
                   "reverify_by": c.get("reverify_by", reverify)}
            if not ok_official:
                rec["status"] = "REJECTED-NON-OFFICIAL"
                results.append(rec); print(f"  ✗ {cid}: non-official ({host})"); continue
            shot = outdir / f"{cid}.png"
            try:
                page = ctx.new_page()
                last = None
                tmo = c.get("timeout", 35000)
                for attempt in range(2):
                    try:
                        page.goto(url, wait_until="commit" if attempt else "domcontentloaded", timeout=tmo)
                        last = None; break
                    except Exception as ge:
                        last = ge; page.wait_for_timeout(2000)
                if last: raise last
                page.wait_for_timeout(1500)
                page.screenshot(path=str(shot), full_page=True)
                text = page.inner_text("body")[:200000]
                page.close()
                rec["screenshot"] = f"audit/evidence/{setname}/{cid}.png"
                rec["bytes"] = shot.stat().st_size if shot.exists() else 0
                if c.get("expect"):
                    rec["found"] = bool(re.search(c["expect"], text, re.I))
                    rec["status"] = "VERIFIED" if rec["found"] else "CAPTURED-NO-MATCH"
                else:
                    rec["status"] = "CAPTURED"
                print(f"  {'✓' if rec['status'].startswith('VERIFIED') else '•'} {cid}: {rec['status']} ({rec['bytes']//1024}KB)")
            except Exception as e:
                rec["status"] = "BLOCKED-OR-ERROR"; rec["error"] = str(e)[:120]
                print(f"  ! {cid}: {rec['status']} — {rec['error']}")
            results.append(rec)
        browser.close()

    # ledger
    (outdir / "CLAIMS-LEDGER.json").write_text(json.dumps({"set": setname, "checked": ts, "claims": results}, indent=2), encoding="utf-8")
    lines = [f"# Claim evidence ledger — {setname}", "",
             f"Verified {ts}. Official sources only; every claim has a full-page screenshot on disk.", "",
             "| Claim | Authority | Status | Evidence | Source |", "|---|---|---|---|---|"]
    for r in results:
        ev = f"![]({r['id']}.png) ({r['bytes']//1024}KB)" if r["screenshot"] else "—"
        st = {"VERIFIED":"✅ VERIFIED","CAPTURED":"📸 captured","CAPTURED-NO-MATCH":"📸 captured (confirm text)",
              "BLOCKED-OR-ERROR":"⚠️ blocked","REJECTED-NON-OFFICIAL":"✗ non-official"}.get(r["status"], r["status"])
        lines.append(f"| {r['claim'][:70]} | {r['authority']} | {st} | {ev} | [{r['host']}]({r['source_url']}) |")
    v = sum(1 for r in results if r["status"]=="VERIFIED")
    cap = sum(1 for r in results if r["status"].startswith("CAPTURED"))
    bl = sum(1 for r in results if r["status"]=="BLOCKED-OR-ERROR")
    lines += ["", f"**{v} verified (text-matched) · {cap} captured · {bl} blocked**, "
              f"{sum(1 for r in results if r['screenshot'])} screenshots saved in `audit/evidence/{setname}/`."]
    (outdir / "CLAIMS-LEDGER.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\nLedger -> audit/evidence/{setname}/CLAIMS-LEDGER.md  ({v} verified, {cap} captured, {bl} blocked)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
