#!/usr/bin/env python3
"""
Generate a content-brief JSON for each route money page, so the Content-Intelligence
registry tracks its question / funnel / page-type / monetization.

Reads sites/<site>/pages/destinations/<origin>-to-<country>.yml and writes a lean brief to
sites/<site>/content/route-<country>.json keyed by the page's canonical path.

Usage:  py audit/gen_route_briefs.py [site]
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

# route-specific fear (the dominant worry per destination)
FEAR = {
    "uk": "the UK's strict rules (tapeworm timing, APHA vet) mean I'll get it wrong",
    "australia": "the months-long titer + quarantine process is overwhelming and hugely expensive",
    "usa": "the new CDC dog-import rules will trip me up",
    "germany": "the EU paperwork is confusing and I'll miss a step",
    "france": "the EU paperwork is confusing and I'll miss a step",
    "netherlands": "the EU paperwork is confusing and I'll miss a step",
    "canada": "I'll misread the CFIA rules and my pet gets held",
    "india": "the documentation and customs will be chaotic",
    "singapore": "the titer test + 30-day quarantine and the cost",
    "south-africa": "the import permit and disease tests will go wrong",
}

def brief_for(yml_path: Path, pages_dir: Path):
    d = yaml.safe_load(yml_path.read_text(encoding="utf-8"))
    # routes derive their URL from the file path when no explicit url: field
    url = d.get("url") or ("/" + yml_path.relative_to(pages_dir).with_suffix("").as_posix() + "/")
    m = re.search(r"-to-([a-z-]+)", yml_path.stem)
    country = m.group(1) if m else yml_path.stem
    pretty = country.replace("-", " ").title()
    return country, {
        "_meta": {
            "produced_by": "gen_route_briefs.py (route money-page brief)",
            "blog_objective": "lead_generation",
            "funnel_stage": "MOFU→BOFU (commercial-investigation → transactional)",
            "page_type": "service (route money page)",
            "target_keyword": f"pet relocation dubai to {country.replace('-', ' ')}",
            "intent": "commercial",
            "primary_fear": f"I'm afraid that {FEAR.get(country, 'the destination rules will go wrong and cost a fortune')}",
            "monetization": "lead_generation (route enquiry → WhatsApp quote)",
        },
        "seo": {
            "title": d.get("title", ""),
            "meta_description": d.get("meta_description", ""),
            "canonical_path": url,
        },
        "_note": f"Route brief for Dubai → {pretty}. Content lives in the page YAML; this brief lets the registry track question/funnel/monetization.",
    }

def main(argv):
    site = argv[0] if argv else "pawroute"
    pages = ROOT / "sites" / site / "pages"
    cdir = ROOT / "sites" / site / "content"
    cdir.mkdir(parents=True, exist_ok=True)
    n = 0
    for yml in sorted((pages / "destinations").glob("*-to-*.yml")):
        if "cost" in yml.stem:  # the cost page already has a hand-written brief
            continue
        country, brief = brief_for(yml, pages)
        (cdir / f"route-{country}.json").write_text(json.dumps(brief, indent=2, ensure_ascii=False), encoding="utf-8")
        n += 1
        print(f"  brief -> route-{country}.json  ({brief['seo']['canonical_path']})")
    print(f"{n} route briefs written to sites/{site}/content/")
    return 0

if __name__ == "__main__":
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    raise SystemExit(main(sys.argv[1:]))
