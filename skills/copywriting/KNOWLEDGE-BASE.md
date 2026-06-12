# The Web Persuasion & Content Engineering Knowledge Base

> **Canonical, validated reference.** Source of truth for the engine's writing half.
> Imported from the Numini Research Elevator (`research_elevator/Web_Persuasion`), 9 Jun 2026.
> Gold-standard certified: every evidence bullet passed a validation gate, is graded
> HIGH/MODERATE, cites a tier-one (first-party / peer-reviewed / named-expert) source, and —
> where it states a figure — has that figure confirmed against the fetched primary source.
> Weak/vendor/quarantined items are isolated in Appendix A. The AI writer RAGs over the
> backing `claim_bank.csv`; this is the human-readable book.
> Companion files here: `SKILL.md` (the 26-skill map), `EVIDENCE.md` (the tiered claim table),
> `BLOG-PLAYBOOK.md` (the gold-standard blog moves + niche audit). The `audit/` tool enforces these rules.

*Numini Research Elevator -- a validated, tier-one expert reference for web design, copywriting, blogging, AI-assisted writing, SEO, GEO, the underlying psychology, and editing. Built for a lead-generation deployment.*

**Primary objective of this deployment: `lead_generation`.** Success is measured in qualified leads and cost-per-lead, not pageviews. Every recommendation below is oriented to moving a reader along a funnel toward a quote/enquiry, not to maximising traffic.

> **Gold-standard certification.** Every evidence bullet in this book passed a validation gate, is graded HIGH or MODERATE, cites a tier-one first-party/peer-reviewed or named-expert source, and -- where it states a figure -- has that figure confirmed against the fetched primary source. Nothing weak, unverified, vendor-asserted, or quarantined appears in the body; such items are listed separately in Appendix A.

## How to read this

Each chapter runs: **definition -> why it works -> what the evidence says -> practical rules -> pitfalls -> checklist -> lead-gen application.** Evidence bullets carry a plain-language confidence label and the source; we deliberately do not print internal reliability codes. Confidence means:

- **strong, well-established evidence** -- relied upon with high confidence.
- **good supporting evidence** -- sound, but context matters.
- **limited / emerging evidence** -- directional; treat as a hypothesis to test.
- **weak -- illustrative only** -- never load-bearing (kept in the appendix).

## Standing caveats (do not overstate)

- The F-pattern is ONE of several scanning patterns, not a design goal. It is a sign of skimming, and good layout (front-loading, headings, bullets) can prevent or reshape it.
- E-E-A-T is NOT a direct ranking factor. It is a quality framework used by human raters; 'Trust' is its most important component, and the Helpful Content System was folded into core ranking in March 2024 (no longer a standalone signal).
- GEO uplift figures are domain-dependent. The widely quoted 'up to 40%' is a CEILING measured on the GEO-bench benchmark, not a guaranteed result for any given page.
- Readability formulas (Flesch, Flesch-Kincaid) are heuristics, not ground truth; recent work shows formulas and even LLMs are weak predictors of true reading ease. Use them as a guide, never a target to game.
- A/B 'peeking' (stopping a test when it first looks significant) inflates false positives. Fix the sample size in advance, or use sequential testing with Type-I / FDR control.
- Conversion-uplift numbers from vendor case studies are context-specific. Treat them as Tier-3 unless independently reproduced, and attribute any figure to the specific test, not a universal law.
- CRO, lead-gen and landing-page evidence is largely Tier-2 practitioner consensus (Baymard, CXL, Unbounce), not peer-reviewed RCT. State it as expert consensus graded MODERATE, not as proven science.

---

## 1. Reading & attention psychology

**Definition.** How people actually consume web pages: they scan rather than read, sampling a fraction of the words, guided by headings, links, bold text and position. Attention is scarce and front-loaded.

**Why it works.** Reading on screens is costly and goal-driven, so the brain conserves effort by skimming for relevance cues. Working memory is narrow, so dense, unstructured text overflows it and the reader bails. Layout that surfaces the answer early and chunks the rest lets a skimmer extract value without reading linearly.

**What the evidence says.**

- On the web, users typically read only about 20-28% of the words on a page during an average visit; reading share falls as word count rises. *(strong, well-established evidence; Nielsen Norman Group -- How Little Do Users Read?, 2008.)*
  - Caveat: Figure is an estimate that varies by page and intent; directionally robust.
- Front-loading conclusions and key information first (inverted pyramid) suits web skimming better than building up to a conclusion. *(strong, well-established evidence; Nielsen Norman Group -- Inverted Pyramid writing for the web, 2017.)*
- The F-shaped scanning pattern is ONE of several gaze patterns, not a design goal; it is a sign of skimming that good layout (front-loading, headings, bullets) can prevent or reshape. *(good supporting evidence; Nielsen Norman Group -- F-Shaped Pattern of Reading (2017 update), 2017.)*
- Working memory is sharply limited (classically about 7 plus or minus 2 items, with later estimates near 4 chunks), so interfaces should chunk information rather than present long undifferentiated lists. *(good supporting evidence; Miller, The Magical Number Seven, Plus or Minus Two, 1956.)*

**Practical rules.** 1. Front-load the conclusion. 2. Write scannable structure (headings, short paragraphs, bullets, bold). 3. Cut word count. 4. Use the inverted pyramid. 5. Chunk into labelled groups.
**Pitfalls.** Designing for the F-pattern as a target; burying the CTA below the fold; walls of text.
**Checklist.** Core answer in first screen · descriptive headings · short paras + emphasis · word count justified.
**Lead-gen application.** Front-load the outcome + primary CTA on money pages; informational posts answer fast then hand the warm reader to the service page.

---

## 2. Persuasion & behavioural science

**Definition.** Evidence-based levers that move people to act -- Cialdini's principles, Fogg's behaviour model, Kahneman's dual-process view -- applied ethically.

**What the evidence says.**

- Cialdini's seven principles -- reciprocity, commitment/consistency, social proof, authority, liking, scarcity, unity (unity added 2016). *(strong; Cialdini, Influence 1984 / Pre-Suasion 2016.)*
- Persuasion becomes a deceptive 'dark pattern' when it manipulates choice against the user's interest; ethical influence makes the better choice easier, not the worse one harder to avoid. *(strong; NN/G / Brignull, 2023.)*
- Fogg B=MAP: behaviour occurs only when motivation, ability and a prompt converge; if it fails, raise ability (reduce friction) or improve the prompt before adding motivation. *(strong; Fogg, 2009.)*

**Practical rules.** Social proof near the decision · authority signals where trust is decided · reduce friction before motivation · honest scarcity only · unmissable prompt at the moment of M+A.
**Pitfalls.** Dark patterns; over-stacking tactics (reactance); adding promises when the blocker is friction.
**Lead-gen application.** High trust stakes (people's animals): surface genuine reviews, route experience, credentials beside the quote CTA; minimise the form, let the bot qualify.

---

## 3. Conversion copywriting

**What the evidence says.**

- Checkout/cart abandonment averages ~70%, driven substantially by trust, unexpected cost, and account-creation friction. *(strong; Baymard Institute, 2024.)*
- A/B 'peeking' inflates false positives; fix sample size in advance or use sequential testing. *(strong; Kohavi/Tang/Xu 2020; Larsen et al. 2024.)*
- Conversion pages perform best with a single primary CTA; competing CTAs dilute the goal. *(good; CXL/GoodUI consensus, 2023.)*
- Specific, benefit-led copy naming a concrete outcome beats vague feature lists. *(good; CXL/Copyhackers consensus, 2022.)*

**Practical rules.** Value prop names outcome + who · features → benefits, made specific · pre-empt top objections · one primary CTA · trust signals beside the action.
**Lead-gen application.** The money page has one job — get the quote/enquiry. Strip secondary links, make the one CTA obvious, answer cost/safety/timeline objections.

---

## 4. Blogging & content strategy

**What the evidence says.**

- Berger's STEPPS predicts sharing; high-arousal emotion (awe, anger, anxiety) increases sharing, low-arousal sadness decreases it — arousal, not positivity, drives transmission. *(strong; Berger & Milkman 2012; Contagious.)*
- Pillar page + interlinked cluster builds topical authority and aids ranking + navigation. *(good; topic-cluster model, HubSpot + SEO practitioners, 2023.)*

**Practical rules.** Plan in clusters (pillar + supporting) · match content type to intent · engineer shareability (STEPPS) · build an email list from day one · interlink every post to its pillar and a money page.
**Lead-gen application.** Clusters funnel demand into route/service pages — never a dead-end read.

---

## 5. Web/UX design

**What the evidence says.**

- Nielsen's 10 usability heuristics remain the baseline expert evaluation checklist. *(strong; NN/G, 2020.)*
- Core Web Vitals 'good': LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 (INP replaced FID, Mar 2024). *(strong; web.dev, 2024.)*
- Hick's Law (more choices → slower decisions) and Fitts's Law (target size/distance) justify fewer options and large, close primary targets. *(strong; Laws of UX, Hick 1952 / Fitts 1954.)*

**Practical rules.** Clear visual hierarchy · reduce choices on conversion paths + large reachable targets · Nielsen review before launch · hit CWV thresholds · WCAG 2.2 (also machine-readable structure).
**Lead-gen application.** A slow, cluttered quote page leaks leads silently — hit CWV, make the CTA the visual focus, keep the form reachable on mobile.

---

## 6. SEO (2026)

**What the evidence says.**

- The Helpful Content System was folded into core ranking (Mar 2024 core update) — no longer a standalone signal. *(strong; Google Search Central, 2024.)*
- Local SEO signals (complete Google Business Profile, consistent NAP, genuine reviews, LocalBusiness/Service schema) materially affect location-qualified queries. *(strong; Google + practitioner corroboration, 2024.)*
- E-E-A-T is a quality framework in the rater guidelines, NOT a direct ranking factor; Trust is its most important component. *(good; Google Search Central, 2024.)*
- Search intent splits into informational / commercial-investigation / transactional / navigational; map each query to the page type that satisfies it. *(good; Google + Aleyda Solís / Lily Ray, 2023.)*

**Practical rules.** Map query → intent → page type · demonstrate genuine experience/trust · LocalBusiness/Service/FAQ schema · invest in local SEO · keep technical SEO healthy.
**Lead-gen application.** Commercial-investigation + transactional queries ('best pet relocation Dubai to UK', 'pet relocation quote') → money pages, backed by local trust signals.

---

## 7. GEO -- Generative Engine Optimization

**What the evidence says.**

- Numini measurement (Jun 2026, SerpApi AI Overviews): for 'pet relocation dubai to uk' the AI Overview cited 14 sources, 8 in the top-10 organic — engines draw heavily from but also beyond the classic top 10. *(strong; Numini own measurement, 2026.)*
- GEO methods (Cite Sources, Quotation Addition, Statistics Addition — strongest combined) reach up to ~40% visibility uplift on GEO-bench. *(good; Aggarwal et al., KDD 2024.)*
  - Caveat: '40%' is a CEILING, domain-dependent — NOT a guarantee. (Figure confirmed verbatim in the full paper.)
- Clear entity definition + consistent facts across the site and wider web improve retrieval/citation. *(good; Aleyda Solís; iPullRank/Mike King, 2024.)*

**Practical rules.** Apply GEO methods (cite sources, quotable statements, statistics, fluent authoritative prose) · unambiguous, consistent entities · self-contained single-question chunks · measure AI-citation share · still earn top-10 organic (it feeds AIO citation).
**Lead-gen application.** People research via AI assistants then convert — BE a cited source for the money query, then capture the click.

---

## 8. AI-assisted writing & editing

**What the evidence says.**

- RAG supplies updatable citable knowledge; prompting controls behaviour/voice; fine-tuning durably encodes voice. Strongest default: RAG + structured prompting. *(strong; Lewis et al. RAG 2020 + guidance.)*
- LLMs hallucinate plausible-but-false facts; mitigate by grounding in a verified source (RAG), requiring citations, and refusing un-banked facts. *(strong; hallucination/factuality literature, 2023.)*
- Editing proceeds structural → line → copy edit, plus plain-language/readability for the web. *(good; CMOS + plainlanguage.gov, 2023.)*
- Readability formulas are heuristics, weak predictors of true reading ease — guide, don't game. *(good; arXiv:2502.11150, 2025.)*

**Lead-gen application.** The AI writer is RAG-bound to the claim bank: funnel-aware posts, links to money pages, refuses unverified figures — protecting trust where a wrong import-rule fact is costly.

---

## 9. Blog purpose & business model -- what different blogs are FOR

**What the evidence says.**

- A blog is a different machine depending on its job: ad/affiliate optimises pageviews/RPM; a lead-gen/service blog optimises qualified enquiries and CPL — metric, architecture and CTA all change with the objective. *(good; CMI/HubSpot canon reconciled with the lead-gen objective, 2023.)*
  - Caveat: most published blog advice optimises for traffic; that is NOT this deployment's objective.

**Lead-gen application.** Unambiguously lead generation: a post with 50,000 reads and zero quotes has failed; 400 reads and 12 qualified enquiries has succeeded. Architecture and CTAs follow from that.

---

## 10. Lead-generation content system & funnel (PRIMARY)

**What the evidence says.**

- Lead-capture forms convert better with fewer fields, reduced friction, and trust signals near the form. *(strong; Baymard form usability research, 2024.)*
- Content maps to funnel stages — TOFU informational, MOFU commercial-investigation, BOFU transactional — each post tagged to a stage and the money page it feeds. *(good; TOFU/MOFU/BOFU + intent model, 2023.)*
- Route/service pages are the money pages; blog posts are demand capture that must internally link into them — an informational post must never be a dead end. *(good; topical-cluster + internal-linking consensus, 2023.)*

**Practical rules.** Tag every post to a stage + money page · route/service pages are conversion assets, never dead-end a post · conversion pages → 1:1 attention ratio, message match, single CTA · minimise form friction + trust signals + bot handoff · nurture not-ready leads; report leads/CPL/drop-off/quality, not traffic.
**Lead-gen application.** Informational posts feed route money pages; quote form / WhatsApp bot qualifies; ready leads fulfilled or resold; the rest nurtured.

---

## Appendix A -- Quarantined & practitioner-asserted claims
Recorded for completeness, NOT treated as fact in the body (vendor-reported / unverified figures / dated tactics / design assertions awaiting validation):
- Kahneman System 1/2 framing — *reject; numeric figure not confirmed against the primary source* (framing stands; use as illustrative).
- WCAG 2.2 usability/SEO overlap — *reject; numeric figure not confirmed* (still good practice).
- 2000s ad/affiliate tactics (Digg, trackbacks) don't transfer; build an email list — *quarantine; tier-3, illustrative.*
- Attention ratio ~1:1 on conversion pages — *reject; figure not confirmed* (treat as expert consensus, MODERATE).
- WhatsApp/Telegram bot handoff + nurture — *quarantine; practitioner-asserted, unvalidated (this deployment's design).*
- 'Leads not pageviews; 50k reads + 0 quotes = failure' — *reject; numeric figure not confirmed* (the objective stands).
- Vendor conversion-uplift %s — *quarantine; tier-3, not independently reproduced; attribute to the specific test.*

## Appendix B -- How the Numini AI writer uses this base
The AI writer runs RAG over `claim_bank.csv`: it may assert only what the bank supports, cites the matching claim, and refuses figures that are not verified. It self-checks each draft for readability, GEO tactics, and E-E-A-T signals, and — because `blog_objective=lead_generation` — writes every post to a funnel stage, links to a money page, and ends with the right CTA/handoff.
