#!/usr/bin/env python3
"""
Regulatory register — the auditable record of every verified regulatory claim.

Aggregates all evidence ledgers (audit/evidence/*/CLAIMS-LEDGER.json) into one register a
regulator could read: per claim — authority, source URL, verification status, screenshot,
date verified, version, reviewer, re-verify-by, and fact-vs-advice. This is Principle 13
(auditability) + Principle 7 (regulations change) made concrete.

Usage:  py audit/regulatory_register.py [site]   (default: pawroute)
"""
from __future__ import annotations
import csv, json, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def build(site="pawroute"):
    ev = ROOT / "audit" / "evidence"
    rows = []
    for ledger in sorted(ev.glob("*/CLAIMS-LEDGER.json")):
        try:
            data = json.loads(ledger.read_text(encoding="utf-8"))
        except Exception:
            continue
        setname = data.get("set", ledger.parent.name)
        for c in data.get("claims", []):
            rows.append({
                "set": setname,
                "kind": c.get("kind", "fact"),
                "authority": c.get("authority", c.get("host", "")),
                "claim": c.get("claim", ""),
                "status": c.get("status", ""),
                "verified": c.get("found") is True,
                "screenshot": c.get("screenshot") or "",
                "source_url": c.get("source_url", ""),
                "date_verified": c.get("checked", ""),
                "version": c.get("version", ""),
                "reviewer": c.get("reviewer", ""),
                "reverify_by": c.get("reverify_by", ""),
            })
    # staleness flag
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    for r in rows:
        r["stale"] = bool(r["reverify_by"]) and r["reverify_by"] < today
    rows.sort(key=lambda r: (r["set"], r["authority"]))
    return rows

def write(rows, site):
    cdir = ROOT / "sites" / site / "content"
    cdir.mkdir(parents=True, exist_ok=True)
    cols = ["set", "kind", "authority", "claim", "status", "verified", "screenshot",
            "source_url", "date_verified", "version", "reviewer", "reverify_by", "stale"]
    with (cdir / "regulatory-register.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    verified = sum(1 for r in rows if r["status"] == "VERIFIED")
    shots = sum(1 for r in rows if r["screenshot"])
    stale = sum(1 for r in rows if r["stale"])
    L = ["# Regulatory register — " + site, "",
         f"The auditable record (Principles 7 & 13). {len(rows)} claims · {verified} text-verified · "
         f"{shots} screenshotted · {stale} due for re-verification. "
         f"Rebuild: `py audit/regulatory_register.py {site}`.", "",
         "| Authority | Claim | Type | Status | Proof | Verified | Re-verify by | Reviewer |",
         "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        st = {"VERIFIED": "✅", "CAPTURED": "📸", "CAPTURED-NO-MATCH": "📸?",
              "BLOCKED-OR-ERROR": "⚠️", "REJECTED-NON-OFFICIAL": "✗"}.get(r["status"], r["status"])
        proof = f"[shot]({r['screenshot'].split('/')[-1]})" if r["screenshot"] else "—"
        flag = " ⏰" if r["stale"] else ""
        L.append(f"| {r['authority']} | {r['claim'][:64]} | {r['kind']} | {st} | {proof} | "
                 f"{r['date_verified']} | {r['reverify_by']}{flag} | {r['reviewer']} |")
    L += ["", "_Type = fact (a regulation) vs advice (our recommendation). "
          "⏰ = past its re-verify date — re-screenshot before relying on it. "
          "Reviewer '(pending human sign-off)' = AI-verified, awaiting the human gate (Principle 15)._"]
    (cdir / "REGULATORY-REGISTER.md").write_text("\n".join(L), encoding="utf-8")
    return len(rows), verified, shots, stale

def main(argv):
    site = argv[0] if argv else "pawroute"
    rows = build(site)
    n, v, s, st = write(rows, site)
    print(f"Regulatory register: {n} claims · {v} verified · {s} screenshotted · {st} stale")
    print(f"-> sites/{site}/content/REGULATORY-REGISTER.md  regulatory-register.csv")
    return 0

if __name__ == "__main__":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    raise SystemExit(main(sys.argv[1:]))
