# GEO / AI-Answer Citation Presence — USA / Canada / India Regulatory Queries

Research date: 2026-06-09. For PawRoute (UAE pet relocation).
Method: WebSearch per query, capturing organic result domains and the search engine's
synthesized answer + its cited sources. Citation-likelihood inferred from
`GEO/geo-scoring-rubric.md`. Competitive context from
`COMPETITORS/usa-canada-india-regulations.md`.

> **TRUTH LABEL — read first.** Google's *AI Overview* (AIO) block is a distinct SERP
> surface that is **NOT exposed by the WebSearch tool**. The tool returns (a) the organic
> link list and (b) a model-written summary grounded in those links. That summary is a
> usable *proxy* for "what an answer engine cites when fed this query," but it is **not**
> a verbatim Google AIO. **No AI Overview was directly observed for any of the five
> queries.** Every AIO verdict below is therefore **"Not-retrievable — inferred"** and the
> cited-domain lists are taken from the WebSearch organic/grounding set, never fabricated.
> Where the synthesized answer contained a stale/wrong claim, that is recorded verbatim as
> a freshness finding.

---

## Query 1 — "what are the CDC rules to bring a dog to the USA"

**(a) AI Overview present?** Not-retrievable — inferred. (Tool returned organic links + a
grounded summary; no Google AIO block exposed.)

**(b) Cited / grounding domains, in returned order:**
1. cdc.gov (index — "Bringing a Dog into the U.S.")
2. cdc.gov (bringing-an-animal-into-the-us)
3. aphis.usda.gov (another-country-to-us-import/dogs)
4. cdc.gov (dog-import-form-instructions)
5. cdc.gov (rabies-free-low-risk-countries)
6. cdc.gov (faqs)
7. cdc.gov (us-vaccinated-high-risk-countries)
8. avma.org (vet-facing FAQ)
9. dvidshub.net (DoD news — "CDC sets new rules")
10. petsintransit.com (aggregator, 2025-09 dated)

- **CDC cited?** Yes — dominant (7 of top 10). **APHIS cited?** Yes (#3). **CFIA?** N/A.
- **Freshness:** Synthesized answer reflects the **CURRENT (Aug 2024) regime** — names the
  **CDC Dog Import Form** (the post-2024 instrument), the 6-month-age + microchip + healthy-
  on-arrival rules, and high-risk-vs-low-risk branching. No stale "USDA permit / 30-day"
  legacy language. **Fresh / correct.**

---

## Query 2 — "can I bring my dog to the US in 2026"

**(a) AI Overview present?** Not-retrievable — inferred.

**(b) Cited / grounding domains, in returned order:**
1. cdc.gov (dog-import-form-instructions)
2. aphis.usda.gov (another-country-to-us-import)
3. aphis.usda.gov (.../dogs)
4. worldcarepet.com (2026/05 — "Returning to the U.S. With a Dog: 2026")
5. patifyapp.com (aggregator — "9 CDC Mistakes…2026")
6. cdc.gov (index)
7. vetsaglik.com (aggregator — "CDC Dog Import Requirements 2026")
8. worldcarepet.com (2026/01 — "Take a Dog to USA…2026")
9. zoovettravel.com (aggregator, Peru-origin)
10. cbp.gov (Customs & Border Protection)

- **CDC cited?** Yes (#1, #6). **APHIS cited?** Yes (#2, #3). **CBP** also surfaces (#10).
- **Aggregator pressure is HIGHEST on this "…2026" query:** 5 of 10 are aggregators/
  relocators (worldcarepet ×2, patify, vetsaglik, zoovet). The year-stamped commercial
  pages crowd in precisely where the gov pages decline to keyword-stuff "2026."
- **Freshness:** Synthesized answer is **current** — Dog Import Form, ISO microchip,
  6-month age, high-risk branching, plus correct "check State + airline" caveat. Fresh.
  But note the *citation surface* is half-aggregator here, so a freshness-correct PawRoute
  page competes on a crowded, beatable field rather than against pure gov dominance.

---

## Query 3 — "requirements to import a pet to Canada"

**(a) AI Overview present?** Not-retrievable — inferred.

**(b) Cited / grounding domains, in returned order:**
1. inspection.canada.ca (CFIA — "Bringing animals to Canada")
2. cbsa-asfc.gc.ca (Canada Border Services Agency)
3. aphis.usda.gov (us-to-another-country-export/pet-travel-us-canada)
4. passpaw.com (aggregator)
5. chaudharylaw.com (immigration-law blog)
6. travel.gc.ca (Gov-of-Canada travel)
7. pettravel.com (aggregator)
8. tailwindglobalpet.com (relocator)
9. yourdogbutler.com (aggregator — "Ultimate Guide For 2025")
10. worldcarepet.com (relocator, 2025/03)

- **CFIA cited?** Yes — #1 (inspection.canada.ca). **APHIS** also present (#3, US-export
  side). Canadian gov breadth (CBSA #2, travel.gc.ca #6) is strong.
- **Freshness:** Synthesized answer is broadly correct (rabies cert, 30-days-before, age
  bands, rabies-free-country freedom certs, CBSA inspection). Canada's rules changed less
  than the US, so freshness is a weaker differentiator here — but the answer leans on
  aggregator phrasing ("age bands") that the CFIA tool itself routes via decision tree.
- **Aggregators present but ranked below the regulators** (4–5 of 10), consistent with the
  teardown's finding that CFIA owns the head term.

---

## Query 4 — "returning to India with a dog NOC requirements"

**(a) AI Overview present?** Not-retrievable — inferred.

**(b) Cited / grounding domains, in returned order:**
1. aphis.usda.gov (us-to-another-country-export/pet-travel-us-india)
2. tailwindglobalpet.com (relocator)
3. cgisf.gov.in (Consulate General of India, San Francisco)
4. odynovotours.com (travel blog)
5. furryflyers.com (relocator)
6. aqcsindia.gov.in (AQCS — the actual NOC issuer)
7. aphis.usda.gov (print/pdf node)
8. aphis.usda.gov (india-dogs-guidance.pdf — SOP)

- **CDC?** N/A. **APHIS cited?** Yes — and it OUTRANKS the Indian gov sources (#1, #7, #8
  all APHIS US-export pages). The actual NOC authority, **aqcsindia.gov.in, is only #6**,
  and the Indian consulate (cgisf.gov.in) #3.
- **Key gap confirmed:** the query intent is *resident returnee NOC*, but the top-cited page
  is framed as **US→India export**. No source owns the returnee NOC walkthrough. Relocators
  (tailwind #2, furryflyers #5) sit ABOVE the real Indian NOC issuer — the weakest, most
  exploitable citation field of the five.
- **Freshness:** Synthesized answer gives concrete mechanics (NOC from AQCS, 5 working days,
  15-day pre-import, DGFT license, microchip+rabies, disease-free list). Accurate but
  US-export-framed; the returnee angle (DGFT ANF-2M for residents, baggage-rule import) is
  thin. Freshness less the issue here than *intent-fit* and *journey ownership*.

---

## Query 5 — "Dubai to USA pet relocation requirements"  ← PawRoute's core SERP

**(a) AI Overview present?** Not-retrievable — inferred.

**(b) Cited / grounding domains, in returned order:**
1. opsmatters.com (PR/syndication)
2. universalrelocations.com (relocator)
3. moveconnector.com ("Pet Relocation UAE 2026")
4. carrymypet.ae (direct UAE rival)
5. petrelocation.com (US giant)
6. theglobeandmail.com (syndicated PR — "City-Specific Relocation Guide")
7. aphis.usda.gov (us-export/pet-travel-us-united-arab-emirates)
8. openpr.com (PR wire — same syndicated guide)
9. pawsabroad.co ("Leaving Dubai…2026")
10. samadubaimovers.com ("Pet Relocation From Dubai 2026")

- **CDC cited?** **NO** — cdc.gov is **absent** from the top 10 of PawRoute's money query.
  **APHIS** appears once (#7), and only as the US→UAE *export* page (wrong direction for an
  inbound-to-USA query). **CFIA** N/A.
- This is an **all-commercial / PR-wire field** — relocators + syndicated press releases,
  not regulators. Exactly the "weak and exploitable" SERP the teardown flagged.
- **FRESHNESS FAILURE (load-bearing finding):** the synthesized answer states *"You must
  apply for a CDC dog import **permit** at least six weeks before…"* — **this is STALE /
  WRONG.** Under the current (Aug 2024) regime there is **no CDC import permit** for the
  general case; the instrument is the free online **CDC Dog Import Form** (a receipt, not a
  pre-approved permit), and the "six-week permit" language is legacy/aggregator error. The
  commercial corpus feeding this query is propagating outdated rules. (It does correctly add
  the UAE-specific **MOCCAE export permit** and the CDC-approved-airport list.)
- **Implication:** on its single most important query, the AI-answer citation field cites
  **zero regulators**, is dominated by relocators + PR wire, and **carries a factual error
  about the changed CDC rule.** Highest-leverage opportunity of all five.

---

## (c) Citation-likelihood ranking of known players

Inferred from the GEO rubric (S1–S5 + pyramid cap) and the observed organic/grounding sets.
"Likelihood" = probability an answer engine cites this domain for these regulatory queries.

| Rank | Domain | Likelihood | One-line reason (rubric signal) |
|---|---|---|---|
| 1 | **cdc.gov** | Very high (USA queries) / nil (Canada, India, Dubai-export) | Primary source = max S3 trust-chain + dated authority; observed dominating Q1/Q2. Topic-bounded: invisible on non-US queries (absent from Q5). |
| 2 | **aphis.usda.gov** | High, broadest | The only domain cited across **all** geos (US-import, Canada-export, India-export, UAE-export). Strong S3/S4; SOP PDFs (India) lift S5. Weakness: export-framed, JS-heavy pages. |
| 3 | **inspection.canada.ca (CFIA)** | High on Canada only | #1 on Q3; decision-tree tool = strong S1 answerability + dated "modified" stamp. Bounded to Canada intent. |
| 4 | **pettravel.com** | Medium, broad | Aggregator with country-by-country breadth + tenure; cited #7 on Canada. Strong S4 entity coverage, weak S5 expertise → competes *below* regulators, *above* thin relocators. |
| 5 | **carrymypet.ae** | Low–medium, UAE-origin only | Cited #4 on Q5 (its home turf) but young domain (2023), no schema, no clickable gov citations, un-localized FAQ → caps low on S3/S5. Beatable on basics. |

> Note: on Q5 the *actual* cited set was PR-wire + relocators (opsmatters, moveconnector,
> universalrelocations, pawsabroad, samadubaimovers) — a low-S3/S5 field. None of the five
> "known players" except carrymypet.ae and APHIS even appeared, confirming how open this
> query is.

---

## (d) The GEO gap PawRoute can fill — the freshness / "what changed" angle

1. **Own the CDC-rule-change freshness story on the Dubai→USA page (top priority).** Q5's
   AI-answer field cites **no regulator** and actively repeats a **stale "CDC import permit /
   six weeks" error.** A PawRoute page with an answer-first **"What changed: Aug 1 2024 CDC
   Dog Import Form replaced the old process; Feb 5 2026 form got a new look, requirements
   unchanged"** changelog block — each line clickable to cdc.gov — corrects the misinformation
   the engines are currently grounding on. This is a rubric **S3 (trust-chain) + S2 (quotable
   dated claim)** win on the exact query where rivals are weakest. Rung 2→3 lift, cheap.

2. **Add a visible "Last updated" + "Sources verified" date.** The regulators win freshness
   with a single honest modified-date, not "2026" keyword-stuffing; commercial rivals
   (carrymypet.ae) show no date at all. A dated, source-chained PawRoute page out-signals
   both the stale aggregators and the date-silent relocators.

3. **Be the rabies-free simplifier.** UAE is low-risk/rabies-free → the CDC high-risk
   facility/titer steps **don't apply**. A crisp "Because your pet leaves from the UAE
   (rabies-free), you skip X, Y, Z" answer-block is exactly the self-contained, quotable
   chunk (S1+S2) engines lift — and no current cited source frames it from the UAE-origin side.

4. **Win the "returning to India NOC" intent (Q4).** The cited field there ranks relocators
   ABOVE the real AQCS issuer and is all US-export-framed. A genuine resident-returnee NOC
   walkthrough (DGFT ANF-2M → AQCS NOC 5-day/15-day timing → microchip+rabies), source-chained
   to aqcsindia.gov.in + the APHIS SOP PDF, fills an unowned, low-competition gap.

5. **Beat carrymypet.ae on E-E-A-T basics it omits:** clickable cdc.gov/aphis/CFIA citations,
   named author/vet reviewer, JSON-LD (FAQPage/HowTo/Org), and a localized (not India-on-a-
   USA-page) template. These lift S3/S5 against the incumbent for free.

> Truth-firewall reminder (per rubric): the "what changed" changelog and any timelines must
> be sourced to cdc.gov / aphis / CFIA / AQCS with verified dates. The freshness *angle* is
> the GEO move; fabricated "we relocated N pets in X days" figures would breach TRUTH_POLICY
> and demote the page — do not manufacture proprietary stats to climb rungs 4–6.
