# GEO / AI-Answer Citation Presence — UAE Pet Relocation Queries

**Research date:** 2026-06-09
**For:** PawRoute (UAE pet relocation)
**Method:** WebSearch (US-region) per query + targeted WebFetch structural reads of the key players. Citation-likelihood scored against `GEO/geo-scoring-rubric.md` (S1–S5) and cross-checked against `COMPETITORS/uae-import-and-local.md`.

> ## TRUTH FIREWALL — read this first
> **No live Google AI Overview was retrievable for ANY query.** The `WebSearch` tool returns organic links plus a *tool-synthesised* answer; it does **NOT** expose Google's live AI Overview (AIO) block, its presence flag, or its citation chips. Google AIO is personalised/geo-varying (this bot searches US-region, not a Dubai IP) and is not programmatically retrievable here.
> Therefore **every "AI Overview present?" below is `Not-retrievable — inferred`.** I have **not** fabricated a single AIO or citation. Where I rank "who AI is likely to cite," that is an **inference from observable page structure only** (answer-first extractability, schema, official-source citations, entity density, freshness), not an observed citation.
>
> One genuine observable signal: the WebSearch-synthesised answers (a reasonable *proxy* for what a retrieval-augmented answer engine pulls) consistently drew language from **aggregators (pettravel.com, petrelocation.com), origin-side gov (USDA APHIS)**, and a rotating cast of **relocator blogs** — and **never** lifted text directly from MOCCAE. That pattern is consistent across all five queries.

---

## Scoring inputs (observed via WebFetch, 2026-06-09)

| Player | Answer-first | Freshness (date) | Official link (MOCCAE/gov) | Entity density | Schema | Notes |
|---|---|---|---|---|---|---|
| **pettravel.com** (UAE page) | Strong (7-step lead checklist + tables) | **Yes** — modified 2026-02-16, pub 2024-11-26 | **No direct link** (names MOCCAE only) | High (15+ breeds, 21-day, AED fees in comments) | **JSON-LD present** (breadcrumb/WebPage) | De-facto FAQ via 31+ comments. Strongest aggregator structurally. |
| **petrelocation.com** (UAE country page) | Moderate (prose interleaved) | **No dates** | **No** official UAE citation | Moderate (0.5 IU/ml, 21d) | None detected | FAQ links out to /common-concerns. US-origin lean. |
| **carrymypet.ae** (pet-import) | Strong (3-step + doc icons + vax tables) | **No dates** | Names MOCCAE/IATA, **no links** | Good (30-day, 2/yr, 0.5 IU/ml) | None detected | No pricing. 4 inline FAQs. |
| **MOCCAE** (gov service card) | Bureaucratic service prose | n/a (gov) | **is** the source | Rule values present | n/a | Authoritative but unusable for a nervous expat; **blocked the bot** on direct fetch. Says permit **90 days**. |
| **pawsomepets.ae** | (not re-fetched today; per existing teardown) | — | named-not-linked | — | none | Review moat (4.8★/246), thin technical SEO. |
| **DKC (dkc.ae)** | 35+ FAQ pairs, no tables | **No dates** | MOCCAE/Municipality named-not-linked | High | **No FAQ schema** (lane sitting empty) | Tenure 2004, physical moat. |

**Live trust wound observed again today:** pettravel.com, carrymypet.ae and petrelocation-aligned guides assert the import permit is valid **30 days**; MOCCAE's own service card says **90 days** (per `uae-import-and-local.md`). The web consensus an AI answer would synthesise is **wrong** vs the regulator. This is PawRoute's single highest-leverage wedge.

---

## QUERY 1 — "what documents do I need to import a dog to Dubai"

**(a) AI Overview present?** Not-retrievable — inferred.
**(b) Cited domains (observed):** None observable (no AIO retrievable). Organic set, in order: aphis.usda.gov, furry.ae, aphis.usda.gov (PDF), airtransportanimal.com, carrymypet.ae, gestoriaiberico.com, petrelocation.com, remitly.com, **pettravel.com**, dkc.ae. The synthesised proxy answer leaned on APHIS + pettravel + aggregator language.
**(c) Citation-likelihood ranking:**
1. **pettravel.com** — answer-first 7-step checklist, tables, dated 2026-02, JSON-LD, dense breed/day/fee entities → most extractable doc-list on the web.
2. **MOCCAE** — regulator authority, but service-card prose, no consumer doc-checklist, blocks crawlers → cited as *named authority* more than *quoted source*.
3. **petrelocation.com** — strong domain authority, US-origin doc list, but undated and no UAE official link.
4. **carrymypet.ae** — clean 3-step + doc icons, but undated and no links → local but weaker freshness/trust-chain.
5. **pawsomepets.ae** — review moat doesn't help a "documents" query; thin structured doc list.
6. **DKC** — buried inside 8.5k-word FAQ; no schema, no doc-list block → low extractability.
**(d) GEO gap?** **Yes, wide.** No page pairs a clean extractable document checklist **with** deep-linked MOCCAE citation + a last-updated dateline. A `HowTo`/`FAQPage`-schema'd, screenshot-cited doc list is open green field.

---

## QUERY 2 — "do I need a rabies titre test to bring a pet to the UAE"

**(a) AI Overview present?** Not-retrievable — inferred.
**(b) Cited domains (observed):** None observable. Organic, in order: **petrelocation.com** (blog "New Pet Import Rules"), aphis.usda.gov, aphis PDF, unitedpetexpress.com, anvispetrelocation.com, dpetsquad.com, **pettravel.com**, petraveller.com.au, travelnuity.com, carrymypet.ae (rabies-titre service page). Proxy answer pulled the high-risk/low-risk + 21-day + 0.5 IU/ml framing common to petrelocation/pettravel.
**(c) Citation-likelihood ranking:**
1. **petrelocation.com** — owns the "new rules" explainer; the precise titre conditional (high-risk vs low-risk, 0.5 IU/ml, 21-day) is its quotable strength.
2. **pettravel.com** — enumerates low-risk country list + titre window (12wk–12mo) in extractable form; dated.
3. **carrymypet.ae** — has a **dedicated rabies-titre service page** (exact-intent match) → strong topical match, but undated/unlinked.
4. **MOCCAE** — the country-risk classification is *its* call, but it's not framed as a citable titre answer → named authority, low quote-likelihood.
5. **pawsomepets.ae** — no titre-specific extractable block surfaced.
6. **DKC** — titre buried in FAQ mass; low standalone extractability.
**(d) GEO gap?** **Yes.** This query is a **conditional** ("only if from a high-risk country") — perfect for an answer-first decision block + the authoritative country-risk list with a MOCCAE citation. No incumbent presents the high-risk/low-risk list cleanly with a source link. A titre **timeline/countdown** tool (vaccinate → 21-day wait → draw blood → 3–12mo validity window) is uncontested.

---

## QUERY 3 — "how much does it cost to relocate a pet from Dubai"

**(a) AI Overview present?** Not-retrievable — inferred.
**(b) Cited domains (observed):** None observable. Organic, in order: bayut.com (MyBayut), transconpet.com, iss-relocations.com, 0xcargo.com, petfirst.ae, pawsabroad.co, relocatemena.com, noblevetclinic.com, emiratesbusinesssetup.com, iss-relocations.com. **Notably: no pettravel/petrelocation/MOCCAE/DKC in the top set** — cost is an editorial-blog space, not a gov/aggregator one.
**(c) Citation-likelihood ranking:**
1. **bayut.com (MyBayut)** — high-DA UAE lifestyle publisher with an AED cost breakdown → most likely cited for a price range.
2. **pettravel.com / petrelocation.com** — *low* on this query; their pages are compliance-focused, not priced (pettravel only has fees in comments) → unlikely to be cited for cost.
3. **carrymypet.ae** — **no pricing on page** (observed) → cannot be cited for cost.
4. **MOCCAE** — publishes only the *permit fee* (AED 500), not total relocation cost → narrow citation at best.
5. **pawsomepets.ae / DKC** — quote-on-request model, no published price grid → low cost-citation likelihood.
6. **Origin-gov (APHIS)** — no cost data.
**(d) GEO gap?** **Widest of all five.** The cost SERP is owned by generic blogs giving vague AED 2,000–20,000 ranges. **PawRoute already has a live-validated UAE cost model + calculator** (per memory `project_pet-relocation-setup` / E1 cost build). A schema'd, itemised, **interactive cost calculator** with sourced per-line fees (permit AED 500, inspection AED 1,000/dog vs AED 500/cat, titre, crate, cargo) is content no incumbent produces — and calculators are disproportionately surfaced/cited.

---

## QUERY 4 — "can my pet fly in the cabin from Dubai"

**(a) AI Overview present?** Not-retrievable — inferred.
**(b) Cited domains (observed):** None observable. Organic, in order: **pettravel.com** (flydubai policy), petrelocation.com (Emirates), dubaipackersandmovers.com, **pettravel.com** (Emirates), **etihad.com** (official airline), pawsandplanes.ae, seatmaestro.com, bringfido.com, travelnuity.com. Proxy answer leaned on pettravel airline-policy pages + etihad.com.
**(c) Citation-likelihood ranking:**
1. **pettravel.com** — per-airline policy pages (flydubai, Emirates) are the canonical extractable answer ("Emirates: no cabin"; "flydubai: no pets") → highest quote-likelihood.
2. **etihad.com (official)** — first-party airline source; the 8kg cabin rule is authoritative and directly quotable.
3. **petrelocation.com** — Emirates booking explainer, decent authority.
4. **pawsandplanes.ae / travelnuity.com** — listicle "which airlines allow cabin" → good intent match, mid authority.
5. **carrymypet.ae / pawsomepets.ae / DKC** — none surfaced a cabin-policy page → low likelihood.
6. **MOCCAE** — irrelevant (airline cabin policy, not import regulation) → not a player here.
**(d) GEO gap?** **Partial.** The hard truth ("from Dubai, Emirates/flydubai do NOT allow cabin; pets move as **manifest cargo**, not baggage") is the key answer — and it's scattered. A single, current, source-linked **"cabin vs cargo from DXB/AUH/DWC, by airline" matrix** (with the Emirates/dnata cargo reality and the Etihad 8kg ex-AUH exception) is a clean opening. Risk: airline first-party pages (etihad.com) are strong incumbents on their own policy — compete on the **synthesis/matrix**, not on restating one airline.

---

## QUERY 5 — "moving to Dubai with a dog requirements"

**(a) AI Overview present?** Not-retrievable — inferred.
**(b) Cited domains (observed):** None observable. Organic, in order: twocontinents.com, **petrelocation.com** (country page + blog), bayut.com, aparthotel.com, **bluehavenfrenchbulldogs.com**, noblevetclinic.com, tekce.com. Note the existing teardown's finding holds: the head info term is held by soft non-relocators (a Dubai travel agency, a **French-bulldog breeder**, an apartment-rental site).
**(c) Citation-likelihood ranking:**
1. **petrelocation.com** — highest-DA dedicated UAE requirements page → most likely synthesised, despite no dates/official links.
2. **bayut.com** — high-DA UAE publisher, structured requirements list.
3. **pettravel.com** — strong structured requirements doc (overlaps Query 1), dated/schema'd.
4. **MOCCAE** — the permit authority, cited by name; not a consumer "moving with a dog" narrative → named not quoted.
5. **carrymypet.ae** — solid requirements page, but undated; mid-likelihood.
6. **DKC / pawsomepets.ae** — strong brands, but requirements buried/under-structured → low extractability.
**(d) GEO gap?** **Yes — the softest #1 in the cluster** (an off-topic breeder ranks). A purpose-built, schema'd, dated, MOCCAE-deep-linked "moving to Dubai with a dog" guide — ideally split **per-origin** (UK→UAE, India→UAE, AU→UAE) since APHIS only serves US-origin — should out-structure every incumbent.

---

## CROSS-QUERY CONCLUSIONS

1. **Aggregators are the structural favourites, not the locals.** Across all five, **pettravel.com** (answer-first + dated + JSON-LD + dense) and **petrelocation.com** (high DA) are the most citation-ready. The UAE locals (**carrymypet.ae, pawsomepets.ae, DKC**) win on services/reviews/tenure but lose on the GEO mechanics that actually drive AI citation — **none had a last-updated dateline, deep MOCCAE links, or FAQ/HowTo schema.**

2. **MOCCAE is cited as a *name*, not a *quote*.** It blocks crawlers and presents bureaucratic service-card prose; answer engines reference "MOCCAE" but lift their actual sentences from aggregators — which is exactly why the wrong **"30-day" permit figure propagates** while MOCCAE says **90 days**.

3. **The cost query is the biggest open field** — owned by generic blogs with vague ranges; PawRoute's live cost model + calculator can own it outright.

4. **No incumbent does the GEO basics.** FAQPage/HowTo/Article JSON-LD, visible author + last-updated datelines, and deep-linked screenshot-verified official citations are uncontested across the entire cluster (DKC has 35 FAQs and *zero* FAQ schema).

**SINGLE CLEAREST OPENING:** A **screenshot-sourced, MOCCAE-deep-linked, schema'd answer-block set** that (i) **corrects the 30-vs-90-day permit contradiction**, (ii) ships an **interactive sourced cost calculator** (cost query is wide open), and (iii) presents **per-origin** requirements (UK/India/AU → UAE) — combining the trust-chain (S3) and freshness the aggregators lack with the local relevance the foreign aggregators lack.
