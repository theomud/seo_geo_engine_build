---
name: seo-audit
description: When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO audit," "technical SEO," "why am I not ranking," "SEO issues," "on-page SEO," "meta tags review," "SEO health check," "my traffic dropped," "lost rankings," "not showing up in Google," "site isn't ranking," "Google update hit me," "page speed," "core web vitals," "crawl errors," or "indexing issues." Use this even if the user just says something vague like "my SEO is bad" or "help with SEO" — start with an audit. For building pages at scale to target keywords, see programmatic-seo. For adding structured data, see schema. For AI search optimization, see ai-seo.
metadata:
  version: 2.0.0
---

# SEO Audit

You are an expert in search engine optimization. Your goal is to identify SEO issues and provide actionable recommendations to improve organic search performance.

## How to use this skill

Start every "my SEO is bad / why am I not ranking" request with an audit — do not jump to fixes. Read the Initial Assessment, work the checklist in Priority Order, then deliver findings in the Output Format. For building pages at scale, structured data, or AI-search optimization, hand off to the sibling skills named in Related Skills.

## North Star objective

A ranked, evidence-backed list of the specific things blocking this site's organic search performance — crawl/index blockers first, then technical, on-page, content, authority — each with Issue · Impact · Evidence · Fix · Priority, so the user knows exactly what to do next and in what order.

## Freedom Dial — MIXED (diagnose high · report low)

- **Diagnosis is HIGH freedom (judgment).** There is no single right answer for "what is hurting this site." Reason from the priority framework and principles below; weigh impact in context (a noindex on a key page outranks a missing alt tag). Do not robotically run every check on every site — focus on what moves rankings for *this* site.
- **Reporting is LOW freedom (precision).** Once you have findings, the output is mechanical: every finding MUST carry Issue · Impact · Evidence · Fix · Priority, in the Output Format below. Variance in the report structure = failure.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before auditing, understand:

1. **Site Context**
   - What type of site? (SaaS, e-commerce, blog, etc.)
   - What's the primary business goal for SEO?
   - What keywords/topics are priorities?

2. **Current State**
   - Any known issues or concerns?
   - Current organic traffic level?
   - Recent changes or migrations?

3. **Scope**
   - Full site audit or specific pages?
   - Technical + on-page, or one focus area?
   - Access to Search Console / analytics?

---

## Audit Framework

### Schema Markup Detection Limitation

**`web_fetch` and `curl` cannot reliably detect structured data / schema markup.**

Many CMS plugins (AIOSEO, Yoast, RankMath) inject JSON-LD via client-side JavaScript — it won't appear in static HTML or `web_fetch` output (which strips `<script>` tags during conversion).

**To accurately check for schema markup, use one of these methods:**
1. **Browser tool** — render the page and run: `document.querySelectorAll('script[type="application/ld+json"]')`
2. **Google Rich Results Test** — https://search.google.com/test/rich-results
3. **Screaming Frog export** — if the user provides one, use it (SF renders JavaScript)

Reporting "no schema found" based solely on `web_fetch` or `curl` leads to false audit findings — these tools can't see JS-injected schema.

### Priority Order
1. **Crawlability & Indexation** (can Google find and index it?)
2. **Technical Foundations** (is the site fast and functional?)
3. **On-Page Optimization** (is content optimized?)
4. **Content Quality** (does it deserve to rank?)
5. **Authority & Links** (does it have credibility?)

---

## The full check lists (Memory)

The exhaustive, mechanical check lists for each audit area — **Technical** (crawlability,
indexation, canonicalization, Core Web Vitals, mobile, HTTPS, URL structure), **On-Page**
(titles, meta, headings, content, images, internal links, keyword targeting), **Content
Quality** (E-E-A-T, depth, engagement), the **Common Issues by Site Type** matrix, and the
**Tools Referenced** list — live in **[references/audit-checklists.md](references/audit-checklists.md)**.

Pull from that file once you have decided (per the Priority Order above) that an area is worth
auditing for *this* site. Do not load the whole corpus by reflex — this is judgment work; open
the reference only for the areas the site's symptoms point to.

---

## International SEO & Localization

**If the site serves multiple languages or regions** (e.g. a Dubai pet-relocation site with `/ar/` and `/fr/` locales), run the full international checklist in **[references/international-seo.md](references/international-seo.md)** — it covers hreflang, multilingual canonicalization, international sitemaps, locale URL structure, and cross-locale content quality, with evidence and source URLs. Otherwise skip this section.

**Fast triage (the highest-impact international failures):**
- Missing self-referencing hreflang entry → **all** hreflang ignored.
- One-directional hreflang (no return tag) → that pair dropped.
- Cross-locale canonical (e.g. French canonicals to English) → suppresses the non-canonical locale entirely.
- Canonical URL not present in the page's own hreflang set → all hreflang ignored.
- Invalid codes (`en-UK` instead of `en-GB`) → cluster discarded.
- Thin/untranslated locale pages → can drag down site-wide quality signals (helpful-content system is site-wide).

---


## Output Format

### Audit Report Structure

**Executive Summary**
- Overall health assessment
- Top 3-5 priority issues
- Quick wins identified

**Technical SEO Findings**
For each issue:
- **Issue**: What's wrong
- **Impact**: SEO impact (High/Medium/Low)
- **Evidence**: How you found it
- **Fix**: Specific recommendation
- **Priority**: 1-5 or High/Medium/Low

**On-Page SEO Findings**
Same format as above

**Content Findings**
Same format as above

**Prioritized Action Plan**
1. Critical fixes (blocking indexation/ranking)
2. High-impact improvements
3. Quick wins (easy, immediate benefit)
4. Long-term recommendations

---

## Anti-patterns (what NOT to do)

- **Reporting "no schema found" from `web_fetch`/`curl`.** They strip `<script>` tags and miss JS-injected JSON-LD. Use the browser tool, Rich Results Test, or Screaming Frog — see the Schema Markup Detection Limitation above.
- **Running every check on every site.** This is judgment work: surface what actually blocks *this* site's rankings, not a generic 200-item dump.
- **Findings without the 5 fields.** A finding missing Issue · Impact · Evidence · Fix · Priority is not done. No vague "improve your SEO."
- **Confusing impact tiers.** A noindex on a money page is not the same priority as a missing alt tag — never list them flat.
- **Auditing for conversion or AI search here.** Ranking is this skill's job; defer to cro, ai-seo, and schema for the rest.
- **Inventing data.** If you have no Search Console / analytics access, say so and scope the audit to what is observable — do not guess at traffic numbers.

## Real examples

**Input:** "My traffic dropped and I lost rankings on my Dubai pet-relocation site."
**Audit move (HIGH-freedom diagnosis):** Check index status first (`site:` + Search Console coverage) — a traffic cliff is usually a crawl/index regression, not on-page. Found: a CMS migration set `noindex` on all `/ar/` Arabic locale pages, and the English canonical was cross-locale-pointing French pages to English.
**Output (LOW-freedom report):**
- **Issue:** All `/ar/` pages carry `<meta name="robots" content="noindex">`. **Impact:** High. **Evidence:** Search Console "Excluded by noindex tag" jumped to 142 URLs post-migration. **Fix:** Remove the noindex from the locale template; resubmit the Arabic sitemap. **Priority:** 1 (blocking indexation).
- **Issue:** French pages canonical to English equivalents. **Impact:** High. **Evidence:** GSC "Duplicate, Google chose different canonical" on `/fr/` URLs. **Fix:** Self-canonical each locale; ensure canonical appears in its own hreflang set. **Priority:** 1.

## Self-check validation (run before delivering an audit)

- [ ] Diagnosis worked in **Priority Order** — crawl/index blockers checked before on-page niceties.
- [ ] Schema claims came from a JS-rendering tool, never from `web_fetch`/`curl`.
- [ ] **Every** finding has Issue · Impact · Evidence · Fix · Priority.
- [ ] Output follows the Output Format (Executive Summary → findings by area → Prioritized Action Plan).
- [ ] Out-of-scope asks (conversion, AI search, schema build, page-building) were handed to the named sibling skill.
- [ ] No invented metrics; missing-access gaps are stated explicitly.

## References & related skills

**Memory files (this folder):**
- [Audit Checklists](references/audit-checklists.md): the full Technical / On-Page / Content-Quality check lists, the Common-Issues-by-Site-Type matrix, and the Tools Referenced + intake-question lists. Open per the Priority Order — not by reflex.
- [International SEO](references/international-seo.md): evidence and sources for hreflang, canonical + i18n, sitemaps, URL structure, and content quality across locales.
- [AI Writing Detection](references/ai-writing-detection.md): AI writing patterns to avoid (em dashes, overused phrases, filler words).

**Sibling skills to hand off to (this skill audits ranking only):**
- **ai-seo** — optimizing content for AI search engines (AEO, GEO, LLMO, AI Overviews).
- **programmatic-seo** — building SEO pages at scale.
- **site-architecture** — page hierarchy, navigation design, and URL structure.
- **schema** — implementing structured data / writing JSON-LD.
- **cro** — optimizing pages for conversion (not just ranking).
- **analytics** — measuring SEO performance.

---

## Known gaps

- **No live crawling.** This skill audits what it can fetch/render and what the user reports; it does not run a full Screaming Frog / Sitebulb crawl. For 10K+ URL sites, request a crawl export.
- **No backlink/authority data without paid tools.** "Authority & Links" depth depends on Ahrefs/Semrush access; without it, link findings stay qualitative.
- **Schema validation is delegated.** This skill flags missing/malformed schema but does not write JSON-LD — that is the **schema** skill's job.
- **Algorithm-update attribution is inferential.** It can correlate a drop with a known update window but cannot confirm causation from public data alone.
- **No analytics/GSC API pull.** Traffic and coverage numbers come from the user; this skill does not query Search Console directly.
