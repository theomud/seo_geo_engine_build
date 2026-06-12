# SEO Engine — Learner Manual

The SEO engine scores how Google's organic ranking machine sees a page: Topicality (T*), Quality/Authority (Q*) and Technical. It is deliberately SEPARATE from the GEO engine — ranking and AI-citation are decoupled. Live SERP (P4) and backlink signals need APIs and are shown as Not Measurable here.

## How to run the engine
- Score a page: `python skill-engines/seo/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/seo/engine.py --serve 8110`
- These docs: `python skill-engines/seo/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Topicality (T*) · intent match

**How we measure it:** Main content answers the target intent

**Why it works:** Maps to T* = ABC signals (Kim/Nayak, T1)

**What to do:** Make the page directly answer its target query.

## Example (what NOT to do -> what to do)
- DON'T: Page rambles off-topic.
- DO: Page directly answers its target query.

## 2. Topicality (T*) · body depth

**How we measure it:** Depth, sub-topic & entity coverage (BERT/RankEmbed)

**Why it works:** Maps to T* = ABC signals (Kim/Nayak, T1)

**What to do:** Add depth — entities and quantified facts, not fluff.

## Example (what NOT to do -> what to do)
- DON'T: 300 words of fluff.
- DO: Depth with entities + quantified facts.

## 3. Topicality (T*) · internal anchors

**How we measure it:** Internal anchor text accurately describes targets

**Why it works:** Maps to T* = ABC signals (Kim/Nayak, T1)

**What to do:** Use descriptive internal anchor text.

## 4. Topicality (T*) · inbound anchors

**How we measure it:** Inbound anchors topically coherent, not over-optimised

**Why it works:** Maps to T* = ABC signals (Kim/Nayak, T1)

**What to do:** (needs a backlink data source)

## 5. Topicality (T*) · title meta signal

**How we measure it:** Compelling accurate title/meta (Navboost C proxy)

**Why it works:** Maps to T* = ABC signals (Kim/Nayak, T1)

**What to do:** Write a compelling, accurate title + meta description.

## Example (what NOT to do -> what to do)
- DON'T: Untitled / 'Home'.
- DO: Accurate, compelling title + meta description.

## 6. Topicality (T*) · topical focus

**How we measure it:** Site focused on topic (siteFocusScore proxy)

**Why it works:** Maps to T* = ABC signals (Kim/Nayak, T1)

**What to do:** Keep the page and site focused on the topic.

## 7. Quality & Authority (Q*) · eeat author

**How we measure it:** Named, credentialed author / expertise

**Why it works:** Maps to Q* = siteAuthority + PageRank-distance + rater IS + spam (T1/T3)

**What to do:** Add a credentialed, named author.

## Example (what NOT to do -> what to do)
- DON'T: No author named.
- DO: By a named, credentialed author + Person schema.

## 8. Quality & Authority (Q*) · trust signals

**How we measure it:** HTTPS, privacy, terms, contact, transparency

**Why it works:** Maps to Q* = siteAuthority + PageRank-distance + rater IS + spam (T1/T3)

**What to do:** Add HTTPS, privacy, terms, contact and an about page.

## Example (what NOT to do -> what to do)
- DON'T: No HTTPS / no contact.
- DO: HTTPS, privacy, terms, contact, about.

## 9. Quality & Authority (Q*) · business legit

**How we measure it:** Verifiable entity, consistent NAP, schema-to-reality

**Why it works:** Maps to Q* = siteAuthority + PageRank-distance + rater IS + spam (T1/T3)

**What to do:** Add Organization schema + a consistent verifiable NAP.

## 10. Quality & Authority (Q*) · inbound authority

**How we measure it:** Quality/relevance of inbound links (not volume)

**Why it works:** Maps to Q* = siteAuthority + PageRank-distance + rater IS + spam (T1/T3)

**What to do:** (needs a backlink data source)

## 11. Quality & Authority (Q*) · ymyl handling

**How we measure it:** Appropriate caution/sourcing for YMYL topics

**Why it works:** Maps to Q* = siteAuthority + PageRank-distance + rater IS + spam (T1/T3)

**What to do:** Add sourcing and disclaimers for YMYL topics.

## 12. Quality & Authority (Q*) · brand demand

**How we measure it:** Branded search / direct / brand-mention signal

**Why it works:** Maps to Q* = siteAuthority + PageRank-distance + rater IS + spam (T1/T3)

**What to do:** (needs analytics/SERP data)

## 13. Technical & Page Experience · indexability

**How we measure it:** No accidental noindex/robots block; canonical ok

**Why it works:** Maps to Crawl, index, page experience, structured data (T2)

**What to do:** Ensure no accidental noindex; set the canonical correctly.

## Example (what NOT to do -> what to do)
- DON'T: Accidental noindex.
- DO: Indexable with a correct canonical.

## 14. Technical & Page Experience · core web vitals

**How we measure it:** LCP/CLS/INP proxies (weight, render-blocking)

**Why it works:** Maps to Crawl, index, page experience, structured data (T2)

**What to do:** Cut page weight and render-blocking scripts.

## Example (what NOT to do -> what to do)
- DON'T: 4MB of blocking scripts.
- DO: Lean page, no render-blocking.

## 15. Technical & Page Experience · mobile friendly

**How we measure it:** Responsive, viewport, tap targets

**Why it works:** Maps to Crawl, index, page experience, structured data (T2)

**What to do:** Add a responsive viewport meta.

## Example (what NOT to do -> what to do)
- DON'T: No viewport meta.
- DO: Responsive viewport + tap targets.

## 16. Technical & Page Experience · structured data

**How we measure it:** Valid schema present

**Why it works:** Maps to Crawl, index, page experience, structured data (T2)

**What to do:** Add valid schema (Organization/Article/FAQ).

## Example (what NOT to do -> what to do)
- DON'T: No schema.
- DO: Valid Organization/Article schema.

## 17. Technical & Page Experience · site architecture

**How we measure it:** Logical URLs, internal linking, one-domain

**Why it works:** Maps to Crawl, index, page experience, structured data (T2)

**What to do:** Use shallow URLs and internal linking.

## 18. Technical & Page Experience · crawl hygiene

**How we measure it:** Sitemap, clean robots, no orphans

**Why it works:** Maps to Crawl, index, page experience, structured data (T2)

**What to do:** Add an XML sitemap and a clean robots.txt.

## Example (what NOT to do -> what to do)
- DON'T: No sitemap, messy robots.
- DO: XML sitemap + clean robots.txt.

## P4 · ranks target (human-judged)

Live SERP ranking outcome — PRIMARY via SERP API.

## P4 · ranking breadth (human-judged)

Live SERP ranking outcome — PRIMARY via SERP API.

## P4 · serp features (human-judged)

Live SERP ranking outcome — PRIMARY via SERP API.

## P4 · branded mix (human-judged)

Live SERP ranking outcome — PRIMARY via SERP API.
