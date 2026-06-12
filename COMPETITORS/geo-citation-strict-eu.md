# GEO / AI-Answer Citation Presence — Strict Destinations + UK/EU

**Project:** PawRoute (UAE pet relocation)
**Date:** 2026-06-09
**Scope:** Do AI answers appear for strict-destination + UK/EU regulatory queries, and do they cite GOVERNMENT regulators or AGGREGATORS (pettravel / petrelocation / moveconnector)?
**Method:** Ran a live WebSearch per query and inspected for a retrievable Google AI Overview / AI-answer block, recording cited source domains.
**Rubric:** Citation-likelihood inferred from the structural GEO profile per `GEO/geo-scoring-rubric.md` (S1–S5 signals + pyramid rung).

---

## CRITICAL TRUTH / TOOL LIMITATION (read first)

Google AI Overviews are **NOT programmatically retrievable** through the WebSearch tool in this
environment. WebSearch returns (a) a ranked list of organic result links and (b) a *tool-synthesised*
answer paragraph — **this synthesised paragraph is NOT a Google AI Overview** and must not be
reported as one. For every query below, the AI Overview is therefore **Not-retrievable — inferred**.
The cited-domain analysis is reasoned from the observable organic result set (which *is* real and
captured) plus each player's structural GEO profile per the rubric. No AI Overview or citation below
is fabricated; every "Observed" item is a real link returned by the search.

What WAS observed (real signal): the **organic result set** each query returns — a strong proxy for
the corpus an AI Overview draws from, since AIO citations are overwhelmingly pulled from top-ranking
organic pages on the same SERP.

---

## SUMMARY TABLE — citation profile per query

| Query | AI Overview | Gov domain in organic top set | Aggregators in top set | Inferred AIO citation lean |
|---|---|---|---|---|
| import a dog to Australia (requirements) | Not-retrievable — inferred | **Yes** — agriculture.gov.au (×3 incl. Group-3 dog guide), aphis.usda.gov | petrelocation.com, travelnuity, ferndalekennels, tailwindglobalpet | **GOV-led** (DAFF) + petrelocation as practice layer |
| how long is pet quarantine in Australia | Not-retrievable — inferred | aphis.usda.gov (US-export, tangential); **DAFF not in top 10** | worldcarepet, travelnuity (×2), petrelocation, dogtainers, jamescargo, ferndale, pettraveladvisors | **AGGREGATOR-led** (gov absent on this phrasing) |
| do I need a licence to import a dog to Singapore | Not-retrievable — inferred | **Yes** — avs.nparks.gov.sg (#1), customs.gov.sg, gobusiness.gov.sg, aphis.usda.gov | petadventures (×2), pettravel.com, petrelocation (×3) | **GOV-led** (AVS) + petrelocation/petadventures |
| bring a pet to the UK from a non-EU country | Not-retrievable — inferred | **Yes** — but indirect: europa.eu, food.ec.europa.eu, aphis.usda.gov; **gov.uk NOT in top 10** | petadventures, carrymypet, petsabroaduk, aldgatevet, leshuttle, pawsabroad, pettravel.com | **MIXED** — EU-gov + aggregators; UK-gov (gov.uk) notably absent |
| rabies titre test to bring a pet into the EU | Not-retrievable — inferred | **Yes, strong** — food.ec.europa.eu (×3), europa.eu, bmleh.de, ages.at | petabroad.eu (×2), pets2fly, tripadvisor | **GOV-led** (EC Food Safety dominates) |

**Headline pattern:** Pure-regulatory queries that name the *instrument or authority intent*
(requirements, licence, titre test) pull GOVERNMENT to the top of the organic set — so an AI Overview
on those is **most likely to cite the regulator**. The two queries where government **drops out of the
top set** are: (1) **"how long is pet quarantine in Australia"** (a day-count/practice question DAFF
answers tersely and aggregators answer in lead-first prose) and (2) the **UK** variant where
**gov.uk is absent** and EU-gov + aggregators fill the gap. Those two are the AI-citation openings.

---

## PER-QUERY ANALYSIS

### Q1 — "what are the requirements to import a dog to Australia"

**(a) AI Overview:** Not-retrievable — inferred.
**(b) Observed organic set (in order):** aphis.usda.gov (US→AU export), **agriculture.gov.au — Group-3
step-by-step dog guide**, petrelocation.com/country/australia, abf.gov.au, petrelocation.com (AU 2026
blog), **agriculture.gov.au — step-by-step hub**, **agriculture.gov.au — cats-dogs hub**, travelnuity,
ferndalekennels, tailwindglobalpet. → **GOVERNMENT (DAFF) appears 3× in the top set**, plus two other
gov domains (aphis, abf). This is a gov-saturated SERP.
**(c) Citation-likelihood ranking:**
1. **agriculture.gov.au (DAFF)** — Highest. Source of truth + appears 3× incl. the exact Group-3 dog
   guide; AIO almost certainly cites it for the named rules (microchip ISO, RNATT, 180-day, Brucella/
   Leishmania, Mickleham). Rung-1 regulator with maximal trust chain (S3=2, S4=2).
2. **petrelocation.com** — Medium-high. Appears 2× (country page + 2026 blog); lead-first, entity-dense
   practice layer (names CIV, Bravecto, exact day-counts) = strong S1/S2/S4; the likely *aggregator*
   AIO co-citation for "what actually happens."
3. **pettravel.com** — Low here (did not surface for this AU query; its strength is Singapore).
4. **moveconnector** — Very low. Absent; it ranks on *cost/route* intent, not "requirements."
**(d) PawRoute GEO gap (UAE-origin):** None of the cited pages answer **"import a dog to Australia from
the UAE / Dubai"** — UAE is **Group 3** (the hardest path). Build the definitive UAE→AU Group-3 page:
MOCCAE export health cert, UAE-approved RNATT lab, 180-day clock start, Brucella + Leishmania for intact
dogs. That origin-specific instance is whitespace DAFF and the US-centric aggregators never serve.

### Q2 — "how long is pet quarantine in Australia"

**(a) AI Overview:** Not-retrievable — inferred.
**(b) Observed organic set:** aphis.usda.gov, worldcarepet, transfuranimals, travelnuity (×2),
jamescargo, ferndalekennels, dogtainers, pettraveladvisors, petrelocation. → **DAFF (agriculture.gov.au)
is NOT in the top 10**; the only gov page is US-export APHIS (tangential). This SERP is **aggregator-
owned**.
**(c) Citation-likelihood ranking:**
1. **agriculture.gov.au (DAFF)** — *Should* be #1 but **is not ranking here**; its Mickleham/10-30-day
   facts live buried in step guides, not in a lead-first "how long" answer chunk (weak S1 for this
   intent). Citation-likely **only if** AIO reaches past the organic set to the authority.
2. **worldcarepet / petrelocation / travelnuity** — Medium-high. These give the **lead-first day-count
   answer** ("10 days… 30 days if identity check missed… up to 180") an AIO lifts verbatim (strong S1/S2).
   This is the classic case where aggregators out-*answer* the regulator and win the citation.
3. **pettravel.com** — Low (absent on this query).
4. **moveconnector** — Low (cost/route intent, not quarantine-duration).
**(d) PawRoute GEO gap:** A crisp, answer-first **"how long is Australia quarantine — and what makes it
10 vs 30 days"** chunk, keyed to UAE-origin (Group 3 = full 180-day RNATT wait *before* the 10-day
Mickleham stay). Lead-first table (scenario → days) + cited DAFF link = beats the prose aggregators on
S1+S3 while they have no UAE specificity. **High-probability AIO-citation target** precisely because
gov is absent here.

### Q3 — "do I need a licence to import a dog to Singapore"

**(a) AI Overview:** Not-retrievable — inferred.
**(b) Observed organic set (in order):** **avs.nparks.gov.sg (#1)**, petadventures, **customs.gov.sg**,
pettravel.com, petrelocation (Singapore blog), petrelocation (dog-licence update), petadventures (latest
guide), aphis.usda.gov, **gobusiness.gov.sg (the actual licence portal)**, petrelocation/country. →
**GOVERNMENT leads** (AVS #1) with two more gov domains (customs, gobusiness) covering the licence/permit
mechanics.
**(c) Citation-likelihood ranking:**
1. **avs.nparks.gov.sg (AVS)** — Highest. #1 organic, source of truth, fresh ("22 Apr 2026"),
   transactional (licence portals embedded). AIO almost certainly cites it for the licence/Schedule rules.
2. **pettravel.com** — Medium-high. This is pettravel's strongest route (it *outranks* AVS on the
   "requirements" phrasing per the teardown); 25-yr brand + JSON-LD + 7-step structure = strong S2/S3.
   Likely the aggregator AIO co-citation.
3. **petrelocation.com** — Medium. Appears 3× incl. a dedicated "Singapore dog licence" update — directly
   on-intent for *this* licence query; plausible co-citation.
4. **moveconnector** — Very low. Absent (UAE-cost intent, not Singapore-licence).
**(d) PawRoute GEO gap:** The licence answer everyone gives is generic; none address the **UAE-origin
Schedule** (Singapore treats UAE as a higher-risk schedule → long-titre + quarantine, like Australia).
Build "Do I need a licence to bring a dog from Dubai to Singapore?" answering both the **AVS import
licence + dog licence (residential SG address)** *and* the UAE-Schedule quarantine path in one lead-first
chunk. Gov is strong here, so win on **UAE-origin instance + format**, not raw licence facts.

### Q4 — "bring a pet to the UK from a non-EU country requirements"

**(a) AI Overview:** Not-retrievable — inferred.
**(b) Observed organic set (in order):** aphis.usda.gov, petadventures (UK-from-non-EU), **europa.eu /
Your Europe**, carrymypet, petsabroaduk, aldgatevet, leshuttle, **food.ec.europa.eu**, pawsabroad,
pettravel.com (UK requirements). → **gov.uk is NOTABLY ABSENT from the top 10** (the teardown's finding
holds — the word "requirements" pulls guide-style pages over the terse official gov.uk page). The gov
domains present are **EU** (europa.eu, food.ec.europa.eu) and **US** (aphis) — neither is the correct
UK authority for a UK-import question.
**(c) Citation-likelihood ranking:**
1. **gov.uk (DEFRA/APHA)** — *Should* be the authority, but **is absent from this SERP** → AIO may
   under-cite it on this exact phrasing. This is a real gov gap.
2. **petadventures / carrymypet / pettravel.com** — Medium-high. Lead-first "Part 1 / Part 2 / Not-listed"
   day-count answers (21 days vs 4 months, titre, tapeworm, manifested-cargo) = strong S1/S2; the likely
   AIO citations by default.
3. **europa.eu / food.ec.europa.eu** — Medium. Authoritative but **EU**, not UK — an AIO may pull them
   for rabies/titre framing yet they don't answer the GB-specific rule (5-day rule, GB health certificate,
   designated BCP).
4. **moveconnector** — Low/absent (its UK angle is the ToR/cost route, not "requirements").
**(d) PawRoute GEO gap:** **Largest opening of the five.** UK-gov is absent and the incumbents are
generic, US/EU-centric, and **none cite gov.uk/DEFRA**. Build "Bring a pet to the UK from the UAE (a
non-listed country) — requirements" with: the **4-months-before-travel rabies rule** that applies to
UAE (non-listed), GB pet health certificate, RNATT, praziquantel tapeworm, manifested-cargo + designated
BCP, all **citing gov.uk/DEFRA directly** (which no incumbent does). Lead-first + FAQ schema = out-signal
the lot on S1+S3. **Highest-probability AIO-citation win.**

### Q5 — "rabies titre test to bring a pet into the EU"

**(a) AI Overview:** Not-retrievable — inferred.
**(b) Observed organic set (in order):** **food.ec.europa.eu — designated labs**, **europa.eu / Your
Europe**, **food.ec.europa.eu — entry into the Union**, **bmleh.de (German fed. ministry)**, petabroad.eu,
pets2fly, **food.ec.europa.eu — bringing pet from non-EU**, tripadvisor, petabroad.eu, **ages.at
(Austrian gov agency)**. → **GOVERNMENT dominates** — EC Food Safety appears 3×, plus europa.eu, plus
two member-state gov agencies (bmleh.de, ages.at). Most gov-saturated SERP of the five.
**(c) Citation-likelihood ranking:**
1. **food.ec.europa.eu / europa.eu (EC)** — Highest. 4 EC pages in the top 10; cites the live instruments
   (Implementing Reg (EU) 2026/636, Reg 2017/625 Art 37, designated-lab list). AIO near-certainly cites
   EC for the 30-day-after-vaccination + 3-month-wait rules. Maximal S3/S4.
2. **petabroad.eu** — Medium. Appears 2× with a lead-first "titer test guide 2026"; the likely aggregator
   co-citation for a digestible walkthrough, but it competes against an unusually strong gov field.
3. **pettravel.com / petrelocation** — Low here (did not surface for this specific titre query).
4. **moveconnector** — Absent.
**(d) PawRoute GEO gap:** Gov owns the *generic* titre rule, so do **not** attack it head-on. Win on the
**UAE-origin instance**: "Rabies titre test for moving a pet from the UAE to the EU" — which UAE-approved/
designated lab, the 30-day-post-vaccination + 3-month-pre-travel clock mapped onto a UAE export timeline,
and how it chains into the EU AHC. Route-specific worked example + cited EC reg numbers = the lane the
generic EC pages and EU-centric aggregators leave open.

---

## CROSS-QUERY CONCLUSIONS

1. **Where government is cited (inferred):** the **named-rule / named-authority** queries — Australia
   *requirements* (DAFF ×3), Singapore *licence* (AVS #1), EU *titre test* (EC ×4). On these, an AI
   Overview is **most likely to cite the regulator first**, with petrelocation / pettravel / petabroad as
   the secondary "practice layer" co-citation. Attacking these head-on with a generic guide is low-yield.

2. **Where aggregators win the citation (inferred):** the **day-count / practice** query "how long is
   Australia quarantine" (**DAFF absent** from the SERP) and the **UK** query (**gov.uk absent**). On these,
   lead-first aggregator prose out-*answers* the regulator and is the likely AIO source. These are the two
   genuine AI-citation openings.

3. **Aggregator citation-likelihood, ranked overall:** **petrelocation.com** (broadest top-set presence:
   AU + SG) > **pettravel.com** (owns SG, strong on UK *requirements*) > **petabroad.eu** (EU titre niche)
   > **moveconnector** (never surfaced on these *regulatory* phrasings — it lives on *cost/route* intent
   only, so it is essentially absent from AI answers for strict-reg queries).

4. **PawRoute's GEO move (priority order):**
   - **(Highest) UK-from-UAE "requirements"** — gov.uk absent, incumbents generic and un-cited; win by
     citing gov.uk/DEFRA + UAE (non-listed) 4-month rabies rule + lead-first + FAQ schema.
   - **(High) "How long is Australia quarantine" UAE-origin** — DAFF absent; ship a lead-first scenario→
     days table (180-day RNATT + 10/30-day Mickleham) citing DAFF.
   - **(Medium) Singapore licence from Dubai** and **EU titre from UAE** — gov is strong, so win on the
     **UAE-origin instance + format**, not raw rule restatement.
   - Across all: PawRoute can only *earn* AIO citation by adding the **UAE-origin specificity + real
     practitioner layer (rungs 4–6)** the rubric rewards — generic restatement (rung 1) loses to the
     regulator every time.

**Truth note:** All AI Overviews here are **Not-retrievable — inferred** (the tool cannot fetch Google's
AIO). Organic result sets are **real/observed**; citation-likelihood is **inferred** from those sets +
the GEO rubric. No AI Overview or citation was fabricated.
