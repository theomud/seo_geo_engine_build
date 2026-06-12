---
Status: active — reusable scoring rubric
Area: GEO / scoring
Priority: high
Last updated: 2026-06-09
Depends on: GOVERNANCE/TRUTH_POLICY.md, GEO/proprietary-data-capture-plan.md, GEO/geo-content-audit-2026-06-09.md
Feeds into: TRACKING/content_registry.csv (geo_score), PREDICTIONS/strategy-bets/G01–G05
Resolves against: TRACKING/geo_visibility.csv (citation probes)
---

# GEO Scoring Rubric — a reusable 0–10 score the engine can apply to any page

**Purpose.** Turn Gemini's GEO model into one concrete, repeatable number. Any page (route
page, FAQ, blog, guide, case study) can be scored 0–10 for *AI-citation readiness* — how
likely an answer engine (ChatGPT, Perplexity, Gemini, Google AIO) is to surface and cite it.

The score is a **leading indicator** (a prediction). The **lagging truth** lives in
`TRACKING/geo_visibility.csv`. Use this rubric to prioritise and to forecast; use the citation
probes to *resolve* whether the rubric was right (see the G-series bets,
`PREDICTIONS/strategy-bets/G01–G05`). The rubric is itself a hypothesis, scored like
everything else in this ledger.

> ## Truth firewall (non-negotiable)
> Bands that reward "company experience," "proprietary data," or "case studies / outcomes"
> require **REAL, verifiable, sourced** material — held knowledge the team can attest to, data
> traced to rows in `GEO/proprietary-data-capture-plan.md` (with N + as-of date), or real
> anonymised cases with consent. Inventing a statistic, a credential, a case, or an authority
> to climb a band is a `GOVERNANCE/TRUTH_POLICY.md` breach, **not** a GEO win. Unverifiable
> claims go to the claim-audit queue; they never earn a band and never enter published copy on
> confidence alone. **A high GEO score on fabricated content is a failing score, and the page
> is demoted to rung 1 and flagged.** (Gemini's "47 relocations / 4.2 days"–style figures are
> fabricated illustrations and must never be scored as real.)

---

## Part 1 — The five signals (Gemini's model), each scored 0–2

Score every page on five signals. Each is **0, 1, or 2**. Sum = the **raw signal score (0–10)**.

| # | Signal | What it measures | 0 (absent) | 1 (partial) | 2 (strong) |
|---|---|---|---|---|---|
| S1 | **Answerability** | Can a model lift a complete answer to a real query from one self-contained chunk? | Buries answers in prose; reader must synthesise. | Answers present but not lead-first; some chunks self-contained. | Answer-first lead per section + extractable bullets/tables/steps; each chunk stands alone. |
| S2 | **Citation potential** | Is there a specific, quotable, attributable statement worth citing? | Generic restatement of common knowledge; nothing quote-worthy. | Some quotable lines mixed with filler/hedging. | Dense with crisp standalone claims (numbers, named rules, thresholds, dates) a model would quote verbatim. |
| S3 | **Trust chain** | Is each factual claim traceable to a verifiable source? | Unsourced assertions. | Sources named but not linked/verified, or partial coverage. | Each material fact links to an official/primary source, screenshot-verified per TRUTH_POLICY; page→authority→named instrument is traceable. |
| S4 | **Entity density** | Are real, disambiguated entities named (airlines, breeds, fees, authorities, documents, places, dates)? | Generic ("the airline," "the fee," "the form"). | Some named entities, inconsistent. | Specific named entities throughout, disambiguated, with concrete values + timeframes (no stuffing). |
| S5 | **Expertise** | Does the page add what the company KNOWS beyond the primary source? | Pure repackaging of the gov/source page. | Light interpretation or a few practical notes. | Real practitioner knowledge: edge cases, "what actually happens," outcomes, judgement — anchored to real experience/data. |

**Raw signal score = S1 + S2 + S3 + S4 + S5 (0–10).**

### Anti-gaming guards (apply BEFORE summing)
- **S2 / S5 fabrication check:** any "proprietary" stat, credential, or case that is not real
  and sourced → that signal scores **0**, and the page is flagged to the claim-audit queue.
- **S4 stuffing check:** entities that aren't load-bearing (jammed in for density) do **not**
  count; S4 caps at 1 if specificity isn't backing real substance.
- **S3 gate:** if any material factual claim is unsourced, S3 cannot score 2.

---

## Part 2 — The GEO pyramid (6 rungs) → a content-tier ceiling

Gemini's pyramid (as applied in `GEO/geo-content-audit-2026-06-09.md`) describes *what kind of
content* a page is. Higher rungs are harder to replicate and — per the thesis — get cited
more. The rung sets a **ceiling** on the score: signals only pay off when the content actually
carries that altitude, so a page cannot score above its rung's cap.

| Rung | Tier (audit vocabulary) | Description | Cap on score |
|---|---|---|---|
| 1 | **regulations** | Restates official rules; no value over the primary source. | ≤ 4 |
| 2 | **+explained** | Rules organised, structured, answer-first, well-linked. | ≤ 6 |
| 3 | **+examples** | Worked examples / the timing-trap callouts that show the rule in action. | ≤ 7 |
| 4 | **+company experience** | Real held knowledge: "what actually happens," named-vet shortlists, pitfalls, method. | ≤ 8 |
| 5 | **+proprietary data** | Real first-party data: our observed timelines, cost actuals, delay-cause shares, success/detention rates (with N + as-of date). | ≤ 9 |
| 6 | **+case studies / outcomes** | Real, anonymised, consented end-to-end cases with outcomes a model can narrate. | ≤ 10 |

> **Rungs 4–6 require REAL material** (see firewall). A page claiming rung 5/6 on invented data
> is demoted to **rung 1** and flagged. Fabrication lowers, never raises, the score. Rungs 5–6
> draw on `GEO/proprietary-data-capture-plan.md` — a metric is only "real" once it clears its
> publish threshold there.

---

## Part 3 — Final GEO score (0–10) and bands

**GEO score = min( raw signal score , pyramid cap ).**

| Band | Score | Meaning | What earns it |
|---|---|---|---|
| **Cite-magnet** | 9–10 | Top citation candidate across engines. | Strong on all 5 signals AND rung 5–6 content (real proprietary data and/or real consented case studies), answer-first, fully source-chained. |
| **Strong** | 7–8 | Likely cited on practice / edge-case intents. | 4–5 signals strong AND rung 3–4 (worked examples + a real company-experience layer); minor gaps only. |
| **Competitive** | 5–6 | Cited sometimes; competes with the canonical source. | Well-structured organised reference (rung 2), answer-first and sourced, but little/no expertise layer. |
| **At risk** | 3–4 | Usually loses to the primary source. | Regulations-only or thin; weak answerability or unsourced. |
| **Not citable** | 0–2 | Effectively invisible to engines. | Generic, unsourced, narrative; no distinct value. |

### How each band maps to the G-series bets
- Moving a page **At risk → Strong/Cite-magnet** by adding a real expertise/data layer is bets **G01** and **G04**.
- Lifting **S4** without lifting raw substance tests **G02** (entity density).
- Lifting **S1** (answer-first blocks vs narrative) tests **G03**.
- Reaching rung 6 (case studies) and probing "how / what-happens" prompts tests **G05**.

---

## Part 4 — Applying it (engine workflow)

1. **Score each page** on S1–S5 (apply the anti-gaming guards), then determine its pyramid rung
   (the highest rung it *genuinely* reaches).
2. **GEO score = min(sum, cap).** Record per page in `TRACKING/content_registry.csv` (add
   `geo_score` + `geo_rung` fields) so the score is tracked alongside the content.
3. **Prioritise** lowest-scoring high-value pages first. The cheapest lifts are usually S1
   (answer-first restructuring) and S3 (source-chaining), then surfacing already-verified
   first-party facts (the highest-leverage move identified in the content audit), then the
   real-content rungs 4–6.
4. **Predict, don't assert.** The rubric *predicts* citability; whether the lift is real is a
   **bet**, resolved by `TRACKING/geo_visibility.csv` probes — log identical prompts across ≥2
   engines and compare `cited` / `brand_mentioned` / `source_url` rates before vs after.
5. **Calibrate the rubric itself.** Once G01–G05 resolve, check whether higher GEO scores
   actually correlate with higher citation rates. If a signal doesn't predict citation,
   re-weight it.

---

## Quick reference (one line)

`GEO = min( Answerability + CitationPotential + TrustChain + EntityDensity + Expertise ,
PyramidCap )` — where every point above rung 3 must be backed by **real, sourced** material.
