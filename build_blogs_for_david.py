#!/usr/bin/env python3
"""
Build the de-branded blog package for David (the website-build partner).

Produces 16 self-contained JSON files in blogs-for-david/: 8 outbound (Dubai → X) converted
from the route-blog YAMLs, + 8 inbound (X → Dubai) from the content JSONs. Every file is:
  - DE-BRANDED (no "PawRoute" / "Numini" — David applies his own brand)
  - enriched with a `method` block (structure logic, GEO/SEO rationale, how+why we audit)
  - carries its `sourcing` block (verified-100% vs to-verify vs not-sure)
Content + images only — NOT live pages.

Workflow:
  1. Screenshot every official source first via `py audit/verify_claims.py audit/claims/<x>.json`
  2. Run the page audit next via `py audit/audit.py <page-or-dist> [--site]`
  3. Engineer the final de-branded JSON output from the library with `py build_blogs_for_david.py`
"""
import json, re, glob
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "blogs-for-david"; OUT.mkdir(exist_ok=True)

DEBRAND = [
    ("the PawRoute relocation team", "our relocation specialists"),
    ("PawRoute relocation team", "our relocation specialists"),
    ("the PawRoute team", "our team"),
    ("PawRoute cost model", "our cost model"),
    ("PawRoute service fee", "Relocation service fee"),
    ("PawRoute", "our service"),
    ("/assets/blog/", "images/"),
    ("images/pawroute/to-dubai/", "images/"),
    ("images/pawroute/blog/", "images/"),
    ("images/pawroute/", "images/"),
    ("Numini AI Writer", "AI-assisted writing (official-source verified)"),
    ("Numini", "AI-assisted"),
]

def debrand(o):
    if isinstance(o, str):
        for a, b in DEBRAND:
            o = o.replace(a, b)
        return o
    if isinstance(o, list):
        return [debrand(x) for x in o]
    if isinstance(o, dict):
        return {k: debrand(v) for k, v in o.items()}
    return o

METHOD = {
    "structure_logic": "2026 article anatomy: headline (curiosity/result) -> answer-first opening (the liftable answer in the first lines) -> key takeaways -> table of contents -> scannable H2/H3 -> a visual (data table or flow) -> original insight or a story -> FAQ -> official sources -> one help-first CTA. Why: web readers scan ~20-28% of words (Nielsen Norman Group), so the answer is front-loaded; a story is remembered where bare facts are forgotten; one page = one job + a single CTA converts. These choices recur across every source in our research (see SOURCING-METHOD.md).",
    "geo_seo_rationale": "What we believe helps. GEO (being cited by AI answer engines): answer-first self-contained chunks, cited statistics, official-source citations, consistent entities, FAQ schema -- and citation is decoupled from ranking (~66% of AI-Overview citations come from outside the top-20), so strong content can be cited even before it ranks. SEO: intent-matched title+H1, topical depth, internal links into the money page, visible freshness dates, structured data (Article/FAQ/Breadcrumb/LocalBusiness). HONEST CAVEAT: these are evidence-based best practices, NOT guaranteed results -- ranking also needs off-page authority/backlinks/indexing not built here, and GEO citation is plausible but unproven until measured with a live AI-citation test.",
    "how_and_why_we_audit": "Each page is scored by a 5-lens auditor -- Website, SEO, GEO, Lead-gen/Trust, Quality -- which together cover the 7-category QA (Helpful, Human, Original, Trustworthy, SEO, GEO, Conversion). Why this way: (1) page-type profiles judge a page against ITS job (a reassurance page is weighted differently from a money page); (2) every check carries an evidence tier (T1 sworn -> T6 practitioner) and a verified-vs-heuristic tag; (3) not-measurable checks are excluded, never zeroed (a coverage->confidence label); (4) risk caps catch keyword-stuffing, thin content, fake schema, no-CTA. The score is an on-page QUALITY PROXY, not a measured ranking/citation outcome.",
    "what_we_are_sure_of": "100% sure = a fact screenshot-verified against its official source as of a date (see sourcing.verified_100pct) + that the method was applied. NOT sure = that it ranks or gets cited (unproven until the site is live, indexed and measured).",
    "how_we_verify": "Every factual/regulatory claim is verified against an OFFICIAL source only -- government bodies, recognised standards bodies (IATA), or the operator's own site (e.g. the airline). Never blogs, forums, competitors, or AI. Each verified claim is captured as a full-page SCREENSHOT and logged in a regulatory register with: source, URL, date verified, version, reviewer, and a re-verify-by date (because regulations change). Anything we could not confirm from an official source is HEDGED or flagged 'confirm with [authority]', never asserted (see sourcing.stated_but_unverified). Tooling: a Playwright screenshot verifier with an official-domain allowlist + the regulatory register. Facts are kept separate from advice ('the authority requires X' vs 'we recommend X'). AI never makes the final call -- a human reviews and signs off before publish.",
}

OUTBOUND_SOURCING = {
    "how_we_derived_this": "Built from recurring patterns across our research corpus (SOURCING-METHOD.md): answer the fear not the keyword, front-load the answer, official sources only, a route-specific story, single help-first CTA into the money page.",
    "verified_100pct": [
        {"fact": "Where this route's facts were screenshot-verified, the evidence is in audit/evidence/* and the regulatory register (e.g. UK tapeworm + XL Bully ban, US CDC dog rules, EU titre timing, IATA, Emirates travel methods).", "source": "see regulatory register", "as_of": "2026-06-09"}
    ],
    "stated_but_unverified": [
        {"claim": "Route-specific cost ranges are a model estimate (stated as ranges)", "action": "Re-validate quarterly vs live airline cargo quotes"},
        {"claim": "Any specific not screenshot-verified (e.g. Australia DAFF, South Africa DALRRD, India AQCS detail)", "action": "Confirm + screenshot the official source before publish"}
    ],
    "confidence": "100% sure of: the screenshot-verified facts (regulatory register) + that the method was applied. NOT sure of: ranking/citation -- unproven until the site is live, indexed and measured.",
}

def conv_block(b, out):
    t = b.get("type")
    if t == "article_header":
        out["hero"] = {"eyebrow": b.get("category"), "h1": b.get("h1"), "standfirst": b.get("standfirst"),
                       "image": b.get("image"), "image_alt": b.get("image_alt")}
        by = []
        if b.get("author"): by.append("By " + b["author"])
        if b.get("date"): by.append(b["date"])
        if b.get("reviewed"): by.append(b["reviewed"])
        out["byline"] = " · ".join(by)
        if b.get("image"):
            out["images"].append({"role": "hero", "file": b["image"], "alt": b.get("image_alt"), "status": "rendered (low-res)"})
    elif t == "hero":
        out["hero"] = {"eyebrow": b.get("eyebrow"), "h1": b.get("heading"), "standfirst": b.get("subheading"),
                       "image": b.get("image"), "image_alt": b.get("image_alt")}
        if b.get("image"):
            out["images"].append({"role": "hero", "file": b["image"], "alt": b.get("image_alt"), "status": "rendered (low-res)"})
    elif t == "key_facts":
        out["key_facts"] = {"answer": b.get("answer"), "stats": b.get("stats")}
    elif t == "takeaways":
        out["takeaways"] = b.get("items", [])
    elif t == "prose":
        sec = {"type": "prose"}
        for k in ("eyebrow", "heading", "paragraphs", "bullets"):
            if b.get(k): sec[k] = b[k]
        out["sections"].append(sec)
    elif t == "table":
        out["sections"].append({"type": "table", "heading": b.get("heading"), "columns": b.get("columns"),
                                "rows": b.get("rows"), "note": b.get("note")})
    elif t == "flow":
        out["sections"].append({"type": "flow", "heading": b.get("heading"), "body": b.get("body"), "steps": b.get("steps")})
    elif t == "callout":
        out["sections"].append({"type": "callout", "style": b.get("style"), "heading": b.get("heading"), "body": b.get("body")})
    elif t == "compliance":
        out["sections"].append({"type": "compliance", "heading": b.get("heading"), "facts": b.get("facts"),
                                "advice": b.get("advice"), "note": b.get("note")})
    elif t == "case_study":
        out["sections"].append({"type": "case_study", "heading": b.get("heading"), "subheading": b.get("subheading"),
                                "rows": b.get("rows"), "result": b.get("result"), "note": b.get("note")})
    elif t == "story":
        out["story"] = {k: b.get(k) for k in ("tag", "lead", "problem", "mistake", "discovery", "result", "lesson") if b.get(k)}
    elif t == "faq":
        out["faqs"] = [{"q": i.get("q"), "a": i.get("a")} for i in b.get("items", [])]
    elif t == "sources":
        out["sources"] = b.get("items", [])
    elif t == "cta":
        out["cta"] = {"heading": b.get("heading"), "body": b.get("body"), "ctas": b.get("ctas")}
    # tool/nav blocks (cost_calc, related, lead_form, etc.) are not blog prose -> skipped

def from_yaml(path):
    y = yaml.safe_load(path.read_text(encoding="utf-8"))
    out = {"_meta": {"content_format": "blog", "direction": "outbound (Dubai -> destination)",
                     "target_keyword": (y.get("title") or "").split(":")[0],
                     "note": "De-branded content asset for site build. Render images from the images/ folder."},
           "seo": {"title": y.get("title"), "meta_description": y.get("meta_description"),
                   "og_title": y.get("og_title"), "canonical_path": y.get("url")},
           "hero": {}, "byline": "", "key_facts": {}, "takeaways": [], "sections": [], "story": {},
           "faqs": [], "sources": [], "cta": {}, "images": [],
           "method": METHOD, "sourcing": OUTBOUND_SOURCING}
    for b in y.get("blocks", []):
        conv_block(b, out)
    return out

# route-blog YAML -> clean output name
OUTBOUND = {
    "dubai-to-uk-tapeworm-window": "dubai-to-uk",
    "dubai-to-usa-cdc-rules": "dubai-to-usa",
    "dubai-to-australia-six-months": "dubai-to-australia",
    "dubai-to-singapore-quarantine": "dubai-to-singapore",
    "dubai-to-eu-pet-rules": "dubai-to-eu",
    "dubai-to-canada-cfia": "dubai-to-canada",
    "dubai-to-india-return": "dubai-to-india",
    "dubai-to-south-africa-permit": "dubai-to-south-africa",
}

n = 0
pages = ROOT / "sites/pawroute/pages/blog"
for src, name in OUTBOUND.items():
    f = pages / (src + ".yml")
    if not f.exists():
        print("MISSING", f); continue
    d = debrand(from_yaml(f))
    (OUT / (name + ".json")).write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    n += 1; print(" outbound ->", name + ".json")

for f in sorted(glob.glob(str(ROOT / "sites/pawroute/content/blogs-to-dubai/*.json"))):
    d = json.loads(Path(f).read_text(encoding="utf-8"))
    d["method"] = METHOD
    d = debrand(d)
    name = Path(f).stem  # already X-to-dubai
    (OUT / (name + ".json")).write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    n += 1; print(" inbound  ->", name + ".json")

print(f"\n{n} de-branded JSON files -> blogs-for-david/")
