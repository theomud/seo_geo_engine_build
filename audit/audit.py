#!/usr/bin/env python3
"""
Gold-standard page auditor — Website · SEO · GEO · Lead-gen/Trust.

A unified, evidence-tiered on-page auditor. Keeps the Trust Engine's best ideas
(evidence tiers, verified-vs-heuristic tagging, coverage→confidence, Not-Measurable
never zeroed, SEO≠GEO decoupling, risk caps) and adds a scored Lead-gen/Trust lens
with the 9 gold-standard moves baked in.

Stdlib only — no paid API keys required. Audits a live URL or a local HTML file
(or every page in a built dist/ folder).

Usage:
    py audit/audit.py https://example.com/page
    py audit/audit.py dist/pawroute/destinations/uae-to-uk/index.html
    py audit/audit.py dist/pawroute --site            # audit every page, roll up
    py audit/audit.py <target> --json out.json --html report.html
"""
from __future__ import annotations
import argparse, html as _html, json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------- #
# 1. Page model — regex HTML parse (no bs4 dependency)
# --------------------------------------------------------------------------- #
_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")

class Page:
    def __init__(self, html: str, url: str = ""):
        self.html = html or ""
        self.url = url
        self.title = self._first(r"<title[^>]*>(.*?)</title>")
        self.meta_desc = self._attr(r'<meta[^>]+name=["\']description["\'][^>]*>', "content")
        self.canonical = self._attr(r'<link[^>]+rel=["\']canonical["\'][^>]*>', "href")
        self.has_viewport = bool(re.search(r'<meta[^>]+name=["\']viewport["\']', html, re.I))
        self.h1 = self._all(r"<h1[^>]*>(.*?)</h1>")
        self.h2 = self._all(r"<h2[^>]*>(.*?)</h2>")
        self.h3 = self._all(r"<h3[^>]*>(.*?)</h3>")
        self.headings = self.h2 + self.h3
        self.imgs = re.findall(r"<img\b[^>]*>", html, re.I)
        self.links = re.findall(r'<a\b[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.I | re.S)
        self.jsonld = re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.I | re.S)
        self.schema_types = self._schema_types()
        # body text (strip script/style/tags)
        body = re.sub(r"<(script|style|noscript)[^>]*>.*?</\1>", " ", html, flags=re.I | re.S)
        self.text = _WS.sub(" ", _html.unescape(_TAG.sub(" ", body))).strip()
        self.words = self.text.split()
        self.word_count = len(self.words)
        self.first100 = " ".join(self.words[:100]).lower()
        self.paragraphs = [p for p in re.findall(r"<p[^>]*>(.*?)</p>", html, re.I | re.S)]
        self.lists = len(re.findall(r"<(ul|ol|table)\b", html, re.I))

    def _first(self, pat):
        m = re.search(pat, self.html, re.I | re.S)
        return _WS.sub(" ", _html.unescape(_TAG.sub("", m.group(1)))).strip() if m else ""
    def _all(self, pat):
        return [_WS.sub(" ", _html.unescape(_TAG.sub("", x))).strip()
                for x in re.findall(pat, self.html, re.I | re.S)]
    def _attr(self, tagpat, attr):
        m = re.search(tagpat, self.html, re.I)
        if not m: return ""
        a = re.search(attr + r'=["\']([^"\']*)["\']', m.group(0), re.I)
        return _html.unescape(a.group(1)).strip() if a else ""
    def _schema_types(self):
        types = set()
        for block in self.jsonld:
            for t in re.findall(r'"@type"\s*:\s*"([^"]+)"', block):
                types.add(t)
        return types
    def internal_external_links(self):
        internal = external = 0
        host = re.sub(r"^https?://([^/]+).*", r"\1", self.url) if self.url.startswith("http") else None
        for href, _txt in self.links:
            if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
                continue
            if href.startswith("http"):
                if host and host in href: internal += 1
                else: external += 1
            else:
                internal += 1
        return internal, external

# --------------------------------------------------------------------------- #
# 2. Check helpers
# --------------------------------------------------------------------------- #
NUM_UNIT = re.compile(r"\b\d+(?:[.,]\d+)?\s?(?:%|million|billion|kg|km|cm|days?|weeks?|months?|years?|hours?|aed|usd|gbp|eur|\$|£|€)\b", re.I)
MONEY = re.compile(r"(?:aed|usd|gbp|eur|\$|£|€)\s?\d|\d+\s?(?:aed|usd|gbp|eur)", re.I)
CITE = re.compile(r"\b(according to|source:|per the|as published|official|\[\d+\])\b", re.I)
STOCK = re.compile(r"shutterstock|istockphoto|gettyimages|stock\.adobe|unsplash|pexels", re.I)
ANSWERY = re.compile(r"^(how|what|why|when|where|is|are|can|do|does|will|should)\b", re.I)
QUOTE_GATE = re.compile(r"get a quote|request a quote|contact us for|enquire|get in touch", re.I)
HELP_CTA = re.compile(r"download|checklist|guide|calculator|estimate|free .*(guide|checklist|report)", re.I)
PROOF = re.compile(r"review|rating|testimonial|\bIPATA\b|\bIATA\b|certified|years|customers|\d{3,}\+", re.I)

def pct(n, d): return 0.0 if d <= 0 else max(0.0, min(1.0, n / d))

# ---- Content-quality signals (the 7-category QA: Human · Original · Helpful) ----
AI_TELL = re.compile(
    r"\b(in today'?s (world|fast-paced|digital age|landscape)|it'?s (important|worth) (to note|noting)|"
    r"furthermore|moreover|in conclusion|navigating the|delve into|dive into|when it comes to|"
    r"rest assured|look no further|unlock(?:ing)? (?:the|your)|elevate your|in the realm of|"
    r"a myriad of|tapestry|testament to|game[- ]?changer|cutting[- ]?edge|seamless(?:ly)?|"
    r"ever[- ]?evolving|the world of|plays a (?:crucial|vital|key|pivotal) role|first and foremost|"
    r"need(?:less)? to say|at the end of the day)\b", re.I)
FIRST_PERSON = re.compile(r"\b(?:we|our|we've|we found|we've seen|in our experience)\b", re.I)
IMPERATIVE = re.compile(r"(?:^|\.\s|<li[^>]*>)\s*(start|add|use|check|avoid|make|book|download|confirm|ask|send|pick|get|do|don'?t|never|always|ensure|choose|plan|verify|budget)\b", re.I)

def c_human_voice(p):
    hits = len(AI_TELL.findall(p.text))
    return max(0.0, 1.0 - 0.18 * hits), (f"{hits} AI-cliché phrase(s)" if hits else "no AI clichés detected")
def c_original_insight(p):
    sig = 0
    if re.search(r"worked example|case[- ]study", p.html, re.I): sig += 2
    if re.search(r'class="story"|story-arc', p.html, re.I): sig += 2  # a narrative story is original content (Human Writing System L4/L7)
    if "<table" in p.html.lower(): sig += 1
    if len(FIRST_PERSON.findall(p.text)) >= 3: sig += 1
    if len(NUM_UNIT.findall(p.text)) >= 6: sig += 1
    return min(1.0, sig / 3), f"{sig} originality signals (data/story/example/experience)"
def c_helpful(p):
    lists = len(re.findall(r"<(?:ul|ol|table)\b", p.html, re.I))
    items = len(re.findall(r"<li\b", p.html, re.I))
    imp = len(IMPERATIVE.findall(p.text))
    score = min(1.0, (min(lists, 3) / 3) * 0.5 + (min(imp, 6) / 6) * 0.5)
    return score, f"{lists} lists/tables, {items} items, {imp} actionable cues"

# Principle #12 (outcomes, not features) and #15 (write for one person — "you" focus)
OUTCOME = re.compile(r"\b(peace of mind|confiden\w+|stress[- ]free|without (?:the )?(?:worry|stress|hassle)|"
                     r"safely|reassur\w+|no surprises|no hidden|avoid|protect|sorted|so you can|so your|"
                     r"home safely|home and dry|done right|never (?:worry|guess))\b", re.I)
READER = re.compile(r"\b(?:you|your|you're|you'll|you've)\b", re.I)
BIZ_WE = re.compile(r"\b(?:we|our|us|the company)\b", re.I)

def c_outcome_focus(p):
    n = len(OUTCOME.findall(p.text))
    return min(1.0, n / 3), f"{n} outcome/benefit cues (vs feature-only)"
def c_reader_focus(p):
    you = len(READER.findall(p.text)); we = len(BIZ_WE.findall(p.text))
    if you + we == 0: return 0.4, "no personal address (no 'you'/'we')"
    ratio = you / (you + we)
    return max(0.0, min(1.0, ratio * 1.3)), f"{you}× 'you' vs {we}× 'we' ({int(ratio*100)}% reader-focused)"

# Layer 4 — storytelling (narrative teaches; Morgan Housel)
NARR = re.compile(r"\b(one (?:owner|customer|client|family|developer)|a (?:client|customer|owner|family) who|"
                  r"when .{0,40}?(?:arrived|landed|called|asked|tried)|last (?:year|month|summer|week)|"
                  r"we once|picture this|imagine|true story|for example,|here's what happened|the (?:day|morning) )\b", re.I)
def c_story(p):
    if re.search(r'class="story"|story-arc', p.html, re.I): return 1.0, "narrative story block present"
    n = len(NARR.findall(p.text))
    return min(1.0, n / 2), (f"{n} narrative cue(s)" if n else "no story / narrative — uses facts only")

# Eddie Shleyner — curiosity / promise headline (open loop)
def c_headline(p):
    t = (p.h1[0] if p.h1 else p.title) or ""
    if not t: return 0.0, "no headline"
    sig = 0
    if re.match(r"^\s*(?:how|why|what|when|where)\b", t, re.I): sig += 1
    if re.search(r"\d", t): sig += 1
    if re.search(r"\bthat (?:most|few|nobody|no one|stops|costs?|delays?|trips?|surprises?)\b|\bthe (?:one|only|#?\d+)\b", t, re.I): sig += 1
    if re.search(r"\b(?:cost|price|safely|mistake|avoid|guide|real|without|before|secret|truth)\b", t, re.I): sig += 1
    if "?" in t or ":" in t or "—" in t: sig += 1
    return min(1.0, sig / 2), f"{sig} headline hook(s)"

# --------------------------------------------------------------------------- #
# 3. The rubric — 4 lenses. Each check: fn(page)->(score|None, detail).
#    meta: id, lens, weight, tier, kind(verified/heuristic), title, fix
# --------------------------------------------------------------------------- #
def c_title(p):
    if not p.title: return 0.0, "no <title>"
    n = len(p.title); s = 1.0 if 15 <= n <= 60 else (0.6 if n <= 70 else 0.3)
    return s, f"title {n} chars"
def c_meta(p):
    if not p.meta_desc: return 0.0, "no meta description"
    n = len(p.meta_desc); return (1.0 if 50 <= n <= 160 else 0.6), f"meta {n} chars"
def c_h1(p):
    if len(p.h1) == 1: return 1.0, "single H1"
    return (0.0 if not p.h1 else 0.4), f"{len(p.h1)} H1 tags"
def c_hier(p):
    return (1.0 if len(p.headings) >= 3 else pct(len(p.headings), 3)), f"{len(p.headings)} H2/H3"
def c_scann(p):
    longp = sum(1 for x in p.paragraphs if len(_TAG.sub('', x).split()) > 90)
    s = 1.0 if (p.lists >= 2 and longp == 0) else (0.6 if p.lists >= 1 else 0.3)
    return s, f"{p.lists} lists/tables, {longp} long paras"
def c_alt(p):
    if not p.imgs: return None, "no images"
    withalt = sum(1 for i in p.imgs if re.search(r'alt=["\'][^"\']+["\']', i, re.I))
    return pct(withalt, len(p.imgs)), f"{withalt}/{len(p.imgs)} imgs alt"
def c_viewport(p): return (1.0 if p.has_viewport else 0.0), "viewport" if p.has_viewport else "no viewport meta"
def c_canonical(p): return (1.0 if p.canonical else 0.5), "canonical" if p.canonical else "no canonical"
def c_internal(p):
    i, _ = p.internal_external_links(); return (1.0 if i >= 3 else pct(i, 3)), f"{i} internal links"
def c_schema(p): return (1.0 if p.schema_types else 0.0), ("schema: " + ",".join(sorted(p.schema_types))) if p.schema_types else "no JSON-LD"
def c_weight(p):
    kb = len(p.html) / 1024; return (1.0 if kb < 120 else (0.6 if kb < 300 else 0.3)), f"{kb:.0f}KB html"

def c_intent(p):
    if not p.title or not p.h1: return None, "no title/H1"
    t = set(re.findall(r"[a-z]{4,}", p.title.lower())); h = set(re.findall(r"[a-z]{4,}", (p.h1[0] if p.h1 else '').lower()))
    return pct(len(t & h), max(1, min(len(t), 4))), "title↔H1 overlap"
def c_depth(p):
    facts = len(NUM_UNIT.findall(p.text)); density = facts / max(1, p.word_count / 500)
    base = 1.0 if p.word_count >= 600 else pct(p.word_count, 600)
    return max(base * 0.5, min(1.0, base * 0.6 + min(0.4, density * 0.1))), f"{p.word_count}w, {facts} facts"
def c_anchors(p):
    desc = sum(1 for _h, t in p.links if len(_TAG.sub('', t).split()) >= 2 and not re.search(r"click here|here|read more", t, re.I))
    return (1.0 if desc >= 3 else pct(desc, 3)), f"{desc} descriptive anchors"
def c_author(p):
    has = bool(re.search(r'rel=["\']author["\']|by [A-Z][a-z]+ [A-Z][a-z]+|reviewed by|author', p.html, re.I))
    return (1.0 if has else 0.0), "author signal" if has else "no named author (E-E-A-T gap)"
def c_outbound(p):
    auth = sum(1 for h, _t in p.links if re.search(r"\.gov|\.edu|\bgov\.|moccae|iata|apha|cdc|agriculture\.gov", h, re.I))
    return (1.0 if auth >= 2 else pct(auth, 2)), f"{auth} authoritative outbound links"
def c_freshness(p):
    has = bool(re.search(r"updated|last reviewed|verified [A-Z]|20\d\d", p.text[:1500], re.I)) or "dateModified" in " ".join(p.jsonld)
    return (1.0 if has else 0.0), "freshness signal" if has else "no visible date/updated"
def c_faq(p):
    has = "FAQPage" in p.schema_types or len(re.findall(r"<(summary|dt)\b", p.html, re.I)) >= 3
    return (1.0 if has else 0.0), "FAQ present" if has else "no FAQ"

def c_answer_first(p):
    para = _TAG.sub("", p.paragraphs[0]) if p.paragraphs else (p.text[:200])
    first = para.strip().split(".")[0]
    s = 1.0 if (len(first.split()) <= 28 and (NUM_UNIT.search(first) or re.search(r"\b(is|are|costs?|takes?|needs?|requires?)\b", first, re.I))) else 0.4
    return s, "answer-first opening" if s == 1.0 else "opening not a self-contained answer"
def c_stats(p):
    n = len(NUM_UNIT.findall(p.text)); return min(1.0, n / 8), f"{n} stats w/ units"
def c_citations(p):
    n = len(CITE.findall(p.text)) + sum(1 for h, _ in p.links if re.search(r"\.gov|moccae|iata|apha|cdc", h, re.I))
    return min(1.0, n / 4), f"{n} citation signals"
def c_quotable(p):
    q = sum(1 for s in re.split(r"(?<=[.!?])\s", p.text) if 5 <= len(s.split()) <= 30 and re.search(r"\d|[A-Z][a-z]{3,}", s))
    return min(1.0, q / 12), f"{q} quotable sentences"
def c_entity(p):
    ents = set(re.findall(r"\b(MOCCAE|APHA|IATA|CDC|DAFF|Emirates|Etihad|Dubai|UAE|rabies|microchip|quarantine|titer|titre)\b", p.text, re.I))
    return min(1.0, len(ents) / 6), f"{len(ents)} key entities"
def c_definition(p):
    has = bool(re.search(r"\bis (a|an|the)\b|refers to|means that|defined as", p.text[:600], re.I))
    return (1.0 if has else 0.4), "definition block" if has else "no quotable definition"

def c_fear_first(p):
    has = bool(re.search(r"worried|afraid|fear|scared|terrified|nervous|anxious|don'?t know|what if|will my|risk", p.first100, re.I))
    return (1.0 if has else 0.0), "names a fear early" if has else "no fear/empathy in first 100 words"
def c_cost(p):
    if MONEY.search(p.text): return 1.0, "shows real prices"
    if QUOTE_GATE.search(p.text): return 0.2, "price gated behind 'get a quote'"
    return 0.5, "no pricing either way"
def c_single_cta(p):
    ctas = len(re.findall(r'class=["\'][^"\']*\bbtn\b[^"\']*["\']|<button\b', p.html, re.I))
    return (1.0 if 1 <= ctas <= 8 else (0.5 if ctas == 0 else 0.6)), f"{ctas} button/CTA elements"
def c_help_cta(p):
    return (1.0 if HELP_CTA.search(p.text) else 0.4), "help-first CTA (download/checklist)" if HELP_CTA.search(p.text) else "only high-commitment CTA"
def c_proof(p):
    n = len(PROOF.findall(p.text)); return min(1.0, n / 3), f"{n} proof/trust signals"
def c_objection(p):
    has = bool(re.search(r"\bwhat if\b|common mistake|don'?t worry|no hidden|is it safe|will my pet", p.text, re.I))
    return (1.0 if has else 0.3), "handles objections" if has else "objections not addressed"
def c_visuals(p):
    if not p.imgs: return 0.4, "no images"
    if any(STOCK.search(i) for i in p.imgs): return 0.3, "stock imagery detected"
    return 1.0, "original/non-stock imagery"

RISK = re.compile  # marker
def risk_thin(p): return p.word_count < 250
def risk_stuff(p):
    # Genuine stuffing, not natural topical repetition: a single 4+ letter token must dominate
    # well past what a central place/brand name does (e.g. "Dubai" ~6% on a Dubai page is fine).
    toks = re.findall(r"[a-z]{4,}", p.text.lower())
    if len(toks) < 50: return False
    from collections import Counter
    top, n = Counter(toks).most_common(1)[0]
    return (n / len(toks)) > 0.07 and n > 20
def risk_fakeschema(p):
    return bool(p.schema_types) and ("FAQPage" in p.schema_types) and len(re.findall(r"<(summary|dt)\b", p.html, re.I)) < 2
def risk_nocta(p):
    return not re.search(r"<button|\bbtn\b|mailto:|tel:|wa\.me|get a quote|contact", p.html, re.I)

#  (id, lens, weight, tier, kind, title, fn, fix)
CHECKS = [
 # ---- WEBSITE ----
 ("title","website",2,"T2","verified","SEO title present & ≤60 chars",c_title,"Write a ≤60-char title with the primary keyword."),
 ("meta","website",1.5,"T2","verified","Meta description ≤160 chars",c_meta,"Add a 50–160 char meta description with a hook + CTA."),
 ("h1","website",1.5,"T2","verified","Exactly one H1",c_h1,"Use one H1 containing the primary keyword."),
 ("hierarchy","website",1,"T1","verified","Scannable heading structure",c_hier,"Add descriptive H2/H3 sub-headings."),
 ("scannability","website",1.5,"T1","heuristic","Scannable (short paras, lists)",c_scann,"Break long paragraphs; use bullets/tables (users read ~20–28%)."),
 ("img_alt","website",1,"T2","verified","Images have alt text",c_alt,"Add descriptive alt text to every image."),
 ("viewport","website",1,"T2","verified","Mobile viewport meta",c_viewport,"Add a responsive viewport meta tag."),
 ("canonical","website",0.5,"T2","verified","Canonical URL",c_canonical,"Add a canonical link."),
 ("internal_links","website",1,"T1","verified","Internal links present",c_internal,"Link to related/money pages (hub-and-spoke)."),
 ("schema","website",1.5,"T2","verified","Structured data (JSON-LD)",c_schema,"Add JSON-LD (Service/FAQ/LocalBusiness/Breadcrumb)."),
 ("page_weight","website",0.5,"T2","verified","Lean page weight",c_weight,"Reduce HTML/asset weight for Core Web Vitals."),
 # ---- SEO ----
 ("intent_match","seo",2,"T1","heuristic","Title matches search intent",c_intent,"Mirror the literal query in the title + H1."),
 ("topical_depth","seo",2,"T1","heuristic","Topical depth / info density",c_depth,"Add substance: data, specifics, sub-questions (not just length)."),
 ("descriptive_anchors","seo",1,"T1","verified","Descriptive internal anchors",c_anchors,"Use keyword-rich anchor text, not 'click here'."),
 ("eeat_author","seo",1.5,"T2","verified","Named author / E-E-A-T",c_author,"Add a named, credentialed author + bio (the niche is anonymous)."),
 ("outbound_authority","seo",1,"T1","verified","Authoritative outbound links",c_outbound,"Link to official sources (MOCCAE/APHA/IATA…)."),
 ("freshness","seo",1.5,"T2","verified","Visible freshness/date",c_freshness,"Show 'Updated [Month Year]' — the niche hides dates."),
 ("faq","seo",1,"T2","verified","FAQ / sub-question coverage",c_faq,"Add an FAQ answering fan-out sub-questions."),
 # ---- GEO ----
 ("answer_first","geo",2,"PRIMARY","heuristic","Answer-first opening",c_answer_first,"Open with a one-sentence, self-contained, liftable answer."),
 ("statistics","geo",1.5,"T4","verified","Statistics with units",c_stats,"Add concrete numbers with units (GEO lever +24.9%)."),
 ("source_citations","geo",2,"T4","verified","Cited sources",c_citations,"Cite official sources inline (GEO lever +27.8%)."),
 ("quotable_facts","geo",1.5,"T4","heuristic","Quotable self-contained facts",c_quotable,"Write standalone, quotable sentences AI can lift."),
 ("entity_coverage","geo",1,"T1","heuristic","Entity coverage",c_entity,"Name the key entities (regulators, airlines, terms)."),
 ("definition","geo",1,"T4","heuristic","Quotable definition block",c_definition,"Add a dictionary-style definition sentence."),
 ("faq_schema","geo",1,"T2","verified","FAQ schema for extraction",c_faq,"Mark FAQs with FAQPage schema."),
 # ---- LEAD-GEN / TRUST (our moat) ----
 ("fear_first","trust",2,"T4","heuristic","Names the customer's fear early",c_fear_first,"Open by naming the real fear (Tannenbaum: acknowledge → resolve)."),
 ("cost_transparency","trust",2,"PRIMARY","verified","Transparent pricing",c_cost,"Show real numbers — don't gate price behind 'get a quote'."),
 ("help_first_cta","trust",1.5,"T6","heuristic","Help-first CTA / lead magnet",c_help_cta,"Offer a checklist/calculator (capture the 95% not ready to quote)."),
 ("single_cta","trust",1,"T2","verified","Clear primary CTA",c_single_cta,"Lead with one primary CTA; avoid competing CTAs."),
 ("social_proof","trust",1.5,"T1","heuristic","Social proof / trust signals",c_proof,"Add reviews, certifications, real numbers near claims."),
 ("objection_handling","trust",1,"T6","heuristic","Handles objections",c_objection,"Answer 'what if…' fears and common mistakes."),
 ("original_visuals","trust",1,"T6","verified","Original (non-stock) visuals",c_visuals,"Use original photos/screenshots, not stock."),
 # ---- CONTENT QUALITY (the 7-category QA: Human · Original · Helpful) ----
 ("human_voice","quality",2,"T6","heuristic","Sounds human (no AI clichés)",c_human_voice,"Cut AI tells ('in today's world', 'it's important to note', 'delve', 'seamless')."),
 ("original_insight","quality",2,"T6","heuristic","Original insight / proprietary value",c_original_insight,"Add a case study, your own data, or first-hand experience competitors lack."),
 ("helpful_actionable","quality",1.5,"T6","heuristic","Genuinely helpful / actionable",c_helpful,"Give concrete steps, lists and direct answers — not generic description."),
 ("outcome_focus","quality",1,"T6","heuristic","Sells outcomes, not features",c_outcome_focus,"Sell the destination, not the vehicle — confidence, peace of mind, home safely (Principle 12)."),
 ("reader_focus","quality",1,"T6","heuristic","Written for one person ('you')",c_reader_focus,"Address the reader directly — more 'you' than 'we'; write for one specific person (Principle 15)."),
 ("storytelling","quality",1,"T6","heuristic","Uses a story, not just facts",c_story,"Attach the lesson to a story (Problem→Mistake→Discovery→Result→Lesson) — stories teach, facts get forgotten."),
 ("headline_hook","quality",1,"T6","heuristic","Headline creates curiosity / promise",c_headline,"Make the headline an open loop or clear result ('The one form that delays most pet relocations')."),
]

RISKS = [
 ("thin_content","Thin content (<250 words)",risk_thin,50,"Expand to a substantial, useful page."),
 ("keyword_stuffing","Keyword stuffing",risk_stuff,45,"Write naturally for meaning, not repetition."),
 ("fake_schema","FAQ schema without visible FAQ",risk_fakeschema,60,"Only mark up content that's actually on the page."),
 ("no_conversion","No CTA / contact path",risk_nocta,55,"Add a clear way to convert (CTA/contact/WhatsApp)."),
]

LENSES = {"website":("🌐 Website","Technical, structure & UX"),
          "seo":("🔍 SEO","Ranking & topical authority"),
          "geo":("🤖 GEO","AI-citation readiness"),
          "trust":("💛 Lead-gen / Trust","Fear-led conversion (our moat)"),
          "quality":("✨ Quality","Human · original · helpful")}
LENS_WEIGHT = {"website":0.15,"seo":0.25,"geo":0.25,"trust":0.20,"quality":0.15}

# --------------------------------------------------------------------------- #
# Page-type profiles — different pages have different jobs (from the 598 briefs:
# Reassurance · Trust-comparison · Alternative · Step-by-step · Service · Blog).
# Each profile re-weights the lenses, marks irrelevant checks N/A, and names the
# checks that are CRITICAL for that page's strategy.
# --------------------------------------------------------------------------- #
PROFILES = {
 "reassurance":      {"label":"Reassurance / fear-resolution",
    "lenses":{"website":0.15,"seo":0.25,"geo":0.25,"trust":0.35},
    "exclude":set(), "critical":{"fear_first","objection_handling","source_citations","help_first_cta"}},
 "trust_comparison": {"label":"Trust comparison / cost",
    "lenses":{"website":0.15,"seo":0.30,"geo":0.20,"trust":0.35},
    "exclude":set(), "critical":{"cost_transparency","social_proof","source_citations","objection_handling"}},
 "alternative":      {"label":"Alternative / competitor",
    "lenses":{"website":0.15,"seo":0.30,"geo":0.20,"trust":0.35},
    "exclude":set(), "critical":{"social_proof","objection_handling","help_first_cta","fear_first"}},
 "guide":            {"label":"Step-by-step / informational guide",
    "lenses":{"website":0.20,"seo":0.30,"geo":0.35,"trust":0.15},
    "exclude":{"cost_transparency"}, "critical":{"answer_first","source_citations","statistics","faq","freshness"}},
 "service":          {"label":"Service / money page",
    "lenses":{"website":0.20,"seo":0.30,"geo":0.20,"trust":0.30},
    "exclude":set(), "critical":{"cost_transparency","single_cta","social_proof","schema"}},
 "blog":             {"label":"Blog post",
    "lenses":{"website":0.12,"seo":0.25,"geo":0.25,"trust":0.13,"quality":0.25},
    "exclude":set(), "critical":{"answer_first","source_citations","eeat_author","freshness","help_first_cta","human_voice","original_insight"}},
 "homepage":         {"label":"Homepage",
    "lenses":{"website":0.25,"seo":0.25,"geo":0.20,"trust":0.30},
    "exclude":{"freshness","cost_transparency"}, "critical":{"single_cta","social_proof"}},
 "hub":              {"label":"Listing / hub page",
    "lenses":{"website":0.35,"seo":0.30,"geo":0.10,"trust":0.10,"quality":0.15},
    "exclude":{"answer_first","statistics","source_citations","quotable_facts","definition","faq",
               "faq_schema","topical_depth","eeat_author","freshness","story","original_insight",
               "fear_first","cost_transparency","objection_handling"},
    "critical":{"internal_links","single_cta"}},
 "default":          {"label":"General page",
    "lenses":dict(LENS_WEIGHT), "exclude":set(), "critical":set()},
}

# Map the 598-brief page types → our audit profiles (the strategy contract)
BRIEF_PAGETYPE = {
 "reassurance page":"reassurance","trust comparison":"trust_comparison",
 "alternative page":"alternative","step-by-step guide":"guide","service page":"service",
 "action page":"service","prevention guide":"guide","process clarity page":"guide",
}
_STOP = set("the a an and or of to for in on with your you my our that this is are be will "
            "from at it as i'm afraid here how what why when can do does pet pets relocation".split())

def _content_words(s):
    return [w for w in re.findall(r"[a-z']{4,}", (s or "").lower()) if w not in _STOP]

def load_brief(keyword: str, csv_path: str = None):
    import csv
    p = Path(csv_path) if csv_path else (ROOT / "sites/pawroute/research/trustengine-page-briefs.csv")
    if not p.exists(): return None
    kw = keyword.lower(); best = None; bestn = 0
    with p.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            k = (row.get("Keyword","") or "").lower()
            if not k: continue
            if kw in k or k in kw: return row
            n = len(set(_content_words(kw)) & set(_content_words(k)))
            if n > bestn: best, bestn = row, n
    return best

def align_to_brief(page, brief: dict) -> dict:
    text = page.text.lower(); top = " ".join(page.words[:300]).lower()
    # 1. page-type match (is the page built as the brief intends?)
    want = BRIEF_PAGETYPE.get((brief.get("Page Type","") or "").strip().lower(), "default")
    got = detect_profile(page)
    type_ok = 1.0 if got == want else (0.5 if "default" in (got, want) else 0.0)
    # 2. fear addressed (the assigned customer fear appears in the copy)
    fw = set(_content_words(brief.get("Customer Fear","")))
    fear = pct(len(fw & set(re.findall(r"[a-z']{4,}", text))), max(3, len(fw)//2)) if fw else None
    # 3. fear named EARLY (reassurance/alternative pages must open on the fear)
    fear_early = pct(len(fw & set(re.findall(r"[a-z']{4,}", top))), max(2, len(fw)//3)) if fw else None
    # 4. CTA intent matches the brief's primary CTA
    cw = set(_content_words(brief.get("Primary CTA","")))
    cta = 1.0 if (cw and cw & set(re.findall(r"[a-z']{4,}", text))) else (0.3 if cw else None)
    parts = [x for x in (type_ok, fear, fear_early, cta) if x is not None]
    overall = round(100*sum(parts)/len(parts),1) if parts else None
    return {"keyword":brief.get("Keyword"),"intent":brief.get("Intent"),
            "want_type":want,"got_type":got,"customer_fear":brief.get("Customer Fear"),
            "primary_cta":brief.get("Primary CTA"),
            "checks":{"page_type_match":type_ok,"fear_addressed":fear,
                      "fear_named_early":fear_early,"cta_aligned":cta},
            "alignment":overall,
            "on_strategy": overall is not None and overall>=70 and type_ok>=0.5}

def detect_profile(page) -> str:
    u = (page.url or "").lower().replace("\\", "/"); t = (page.title or "").lower(); blob = u + " " + t
    # URL-structural checks win first — a blog about cost is still a blog
    if re.search(r"/blog/?$|/articles/?$|/about/?$|/contact/?$", u): return "hub"   # index/trust pages — judged as hubs, not content
    if re.search(r"/blog/.+|/articles/.+", u): return "blog"
    if re.search(r"/destinations/[a-z]+-to-[a-z]", u): return "service" if "cost" not in u else "trust_comparison"
    if re.search(r"/destinations/[a-z-]+/?$", u) and "-to-" not in u: return "hub"   # single-country hub (e.g. /destinations/uk/)
    if re.search(r"taken at|airport|quarantine|summer|rejected|banned|afraid|what happens if|will my (pet|dog|cat)", blob): return "reassurance"
    if re.search(r"\bcost\b|price|pricing|how much|cheap|fees?\b", blob): return "trust_comparison"
    if re.search(r"alternative|\bvs\b|reviews?|dkc|sandy ?paws|carry ?my ?pet|blue ?sky|competitor", blob): return "alternative"
    if re.search(r"/destinations/[a-z]+-to-[a-z]", u): return "service"
    if re.search(r"/blog/|/articles/", u): return "blog"
    if re.search(r"requirement|how[- ]it[- ]works|how to|step|process|guide|regulation|checklist|faq", blob): return "guide"
    return "default"

# --------------------------------------------------------------------------- #
# 4. Scoring
# --------------------------------------------------------------------------- #
def audit_page(page: Page, profile: str = None) -> dict:
    pname = profile or detect_profile(page)
    prof = PROFILES.get(pname, PROFILES["default"])
    lens_w = prof["lenses"]; exclude = prof["exclude"]; critical = prof["critical"]
    results = []
    for cid, lens, w, tier, kind, title, fn, fix in CHECKS:
        if cid in exclude:
            score, detail = None, f"n/a for {prof['label']}"
        else:
            try: score, detail = fn(page)
            except Exception as e: score, detail = None, f"err:{e}"
        results.append({"id":cid,"lens":lens,"weight":w,"tier":tier,"kind":kind,
                        "title":title,"score":score,"detail":detail,"fix":fix,
                        "measurable":score is not None,"critical":cid in critical})
    # lens scores over measurable checks
    lens_scores = {}
    for lens in LENSES:
        items = [r for r in results if r["lens"]==lens]
        meas = [r for r in items if r["measurable"]]
        earned = sum(r["score"]*r["weight"] for r in meas)
        possible = sum(r["weight"] for r in meas)
        full = sum(r["weight"] for r in items)
        lens_scores[lens] = {"score": round(100*pct(earned,possible),1) if possible else None,
                             "coverage": round(100*pct(possible,full),1),
                             "measured": len(meas), "total": len(items)}
    # overall = profile-weighted lenses (measurable)
    num = den = 0.0
    for lens, ls in lens_scores.items():
        w = lens_w.get(lens, LENS_WEIGHT.get(lens, 0))  # profiles inherit global weight for unlisted lenses (e.g. quality)
        if ls["score"] is not None:
            num += w*ls["score"]; den += w
    raw = round(num/den,1) if den else 0.0
    # risk caps
    caps = []
    for rid, rtitle, rfn, cap, rfix in RISKS:
        try: hit = rfn(page)
        except Exception: hit = False
        if hit: caps.append({"id":rid,"title":rtitle,"cap":cap,"fix":rfix})
    final = min([raw]+[c["cap"] for c in caps]) if caps else raw
    # coverage / confidence
    meas = [r for r in results if r["measurable"]]
    total_w = sum(r["weight"] for r in results); meas_w = sum(r["weight"] for r in meas)
    coverage = round(100*pct(meas_w,total_w),1)
    vmeas = sum(r["weight"] for r in meas if r["kind"]=="verified")
    vtot = sum(r["weight"] for r in results if r["kind"]=="verified")
    verified_cov = round(100*pct(vmeas,vtot),1)
    conf = "High" if coverage>=85 else "Moderate" if coverage>=65 else "Limited" if coverage>=45 else "Low"
    grade = lambda s: "A" if s>=90 else "B" if s>=80 else "C" if s>=70 else "D" if s>=60 else "E" if s>=40 else "F"
    # prioritized fixes: CRITICAL-for-this-page-type first, then lowest score × highest weight
    fixes = sorted([r for r in meas if r["score"]<0.7],
                   key=lambda r:(not r["critical"], r["score"], -r["weight"]))
    crit_fail = [r["title"] for r in meas if r["critical"] and r["score"]<0.7]
    return {"url":page.url,"title":page.title,"word_count":page.word_count,
            "profile":pname,"profile_label":prof["label"],
            "score":final,"raw":raw,"grade":grade(final),"caps":caps,
            "coverage":coverage,"verified_coverage":verified_cov,"confidence":conf,
            "lens_weights":lens_w,"critical_fails":crit_fail,
            "lenses":lens_scores,"checks":results,
            "top_fixes":[{"title":r["title"],"lens":r["lens"],"detail":r["detail"],"fix":r["fix"],"critical":r["critical"]} for r in fixes[:10]]}

# --------------------------------------------------------------------------- #
# 5. Fetch / load
# --------------------------------------------------------------------------- #
def load(target: str) -> Page:
    if target.startswith("http"):
        req = urllib.request.Request(target, headers={"User-Agent":"GoldAuditor/1.0"})
        with urllib.request.urlopen(req, timeout=30) as r:
            return Page(r.read().decode("utf-8","replace"), target)
    p = Path(target)
    return Page(p.read_text(encoding="utf-8", errors="replace"), str(p))

def main(argv=None):
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    ap = argparse.ArgumentParser(description="Gold-standard Website/SEO/GEO/Trust auditor")
    ap.add_argument("target", help="URL, local .html file, or a dist/ folder with --site")
    ap.add_argument("--site", action="store_true", help="audit every index.html under a folder")
    ap.add_argument("--profile", help="force a page-type profile: "+", ".join(PROFILES))
    ap.add_argument("--brief", help="audit a page against its intended brief (keyword from the 598 page-briefs)")
    ap.add_argument("--json", help="write JSON result")
    ap.add_argument("--html", help="write HTML report")
    a = ap.parse_args(argv)

    from report import render_report  # local
    if a.site:
        base = Path(a.target)
        pages = sorted(base.rglob("index.html"))
        results = []
        for f in pages:
            pg = load(str(f))
            prof = a.profile or ("homepage" if f.parent == base else None)
            results.append(audit_page(pg, prof))
        site = {"site":str(base),"pages":results,
                "score":round(sum(r["score"] for r in results)/len(results),1) if results else 0,
                "count":len(results)}
        print(f"SITE {base}  avg {site['score']}  ({len(results)} pages)")
        for r in sorted(results,key=lambda x:x["score"]):
            cf = f"  ⚠ {len(r['critical_fails'])} critical" if r['critical_fails'] else ""
            print(f"  {r['grade']} {r['score']:5}  {Path(r['url']).parent.name or '/':22} [{r['profile']:16}]{cf}")
        out = a.json or "audit_site.json"; Path(out).write_text(json.dumps(site,indent=2),encoding="utf-8")
        html = a.html or "audit_site.html"; Path(html).write_text(render_report(site,site=True),encoding="utf-8")
        print(f"-> {out}  {html}")
        return 0
    page = load(a.target)
    brief = None
    if a.brief:
        brief = load_brief(a.brief)
        if brief:
            a.profile = a.profile or BRIEF_PAGETYPE.get((brief.get("Page Type","") or "").strip().lower())
    res = audit_page(page, a.profile)
    if brief:
        res["brief_alignment"] = align_to_brief(page, brief)
    print(f"{res['grade']}  {res['score']}/100  ·  page type: {res['profile_label']}  ·  {res['confidence']} confidence (coverage {res['coverage']}%)")
    if res.get("brief_alignment"):
        ba = res["brief_alignment"]
        flag = "ON-STRATEGY ✓" if ba["on_strategy"] else "OFF-STRATEGY ✗"
        print(f"  BRIEF '{ba['keyword']}' → alignment {ba['alignment']}/100  [{flag}]")
        print(f"    intended: {ba['want_type']} | got: {ba['got_type']} | fear: {ba['customer_fear'][:50]}")
    for lens,ls in res["lenses"].items():
        w = res['lens_weights'].get(lens, LENS_WEIGHT.get(lens, 0))
        print(f"  {LENSES[lens][0]:20} {ls['score']}   (weight {int(w*100)}%)")
    if res["critical_fails"]: print("  ⚠ CRITICAL for this page type:", "; ".join(res["critical_fails"]))
    if res["caps"]: print("  RISK CAPS:", ", ".join(c["id"] for c in res["caps"]))
    print("  Top fixes:")
    for f in res["top_fixes"][:5]: print(f"   • [{f['lens']}] {f['fix']}")
    if a.json: Path(a.json).write_text(json.dumps(res,indent=2),encoding="utf-8")
    out_html = a.html or "audit_report.html"
    Path(out_html).write_text(render_report(res),encoding="utf-8"); print(f"-> {out_html}")
    return 0

if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
