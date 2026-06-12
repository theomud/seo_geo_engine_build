---
Status: active — capture spec for operations
Area: GEO / proprietary data
Priority: high
Activation: immediate (log from relocation #1)
Last updated: 2026-06-09
Depends on: GOVERNANCE/TRUTH_POLICY.md, ENGINE/measurement_plan.md, trustengine/customer-profile/01-master-customer-profile.md
Feeds into: GEO content pages, route guides, cost pages, airline pages, fear-resolution pages
---

# PawRoute — Proprietary Data Capture Plan

## Purpose

The GEO gold standard is content backed by **real proprietary operational data** that no
competitor and no public source can reproduce: our own median approval times per route, our
own delay-reason frequencies, our own airline acceptance patterns, our own success rate.

We do **not** have this data yet — operations are early. The
[Truth Policy](../GOVERNANCE/TRUTH_POLICY.md) forbids inventing it. Gemini's illustrative
figures ("183 imports", "average approval 4.2 days") are **fabricated examples** and must
**never** be copied into live content.

This plan defines what to **start logging now**, from the very first relocation, so that at
3 / 6 / 12 months PawRoute genuinely holds elite, citable, PRIMARY-tier data — earned, not
invented.

**The core discipline:** every future published claim must trace back to a row (or set of
rows) in this log, carry its sample size (N), and carry an as-of date. If it can't, it does
not get published. (Truth Policy: *"If we cannot prove it, we do not publish it as fact."*)

---

## Part 1 — Capture Schema (log one row per relocation)

Recommended store: a single shared spreadsheet or lightweight DB, one **case row** per
relocation, plus a child **delay-event** sheet (a relocation can have multiple delays).
Every field below should be filled from operational reality at the moment it becomes known —
not reconstructed later, not estimated.

### 1a. Case table — one row per relocation

| # | Field | Type | Notes / allowed values |
|---|-------|------|------------------------|
| 1 | `case_id` | string (PK) | e.g. `PR-2026-0001`. Immutable. |
| 2 | `direction` | enum | `import` (to UAE) / `export` (from UAE) / `road` (UAE↔Oman) |
| 3 | `origin_country` | string | ISO country |
| 4 | `destination_country` | string | ISO country |
| 5 | `route_key` | derived string | `{origin}->{destination}`, normalised (e.g. `ZA->AE`). Grouping key for all route metrics. |
| 6 | `departure_airport` | enum | `DXB` / `SHJ` / `AUH` / other. Critical — the Sharjah hack is a known differentiator. |
| 7 | `species` | enum | `dog` / `cat` / `other` |
| 8 | `breed` | string | Free text, but normalise spelling |
| 9 | `breed_class` | enum | `standard` / `brachycephalic` / `restricted` / `large` / `senior`. Multiple may apply — store as list or flags. Drives breed-restriction content. |
| 10 | `weight_kg` | number | Pet weight; drives crate/cargo-vs-cabin path |
| 11 | `travel_class` | enum | `cabin` / `checked_baggage` / `manifest_cargo` / `road` |
| 12 | `airline` | string | Operating airline. Normalise (Emirates, Etihad, Turkish, Royal Jordanian, Air Cairo, Lufthansa, Flydubai...) |
| 13 | `airline_was_first_choice` | bool | Did we use the airline we first intended, or switch? Captures forced re-routing. |
| 14 | `airline_switch_reason` | enum (nullable) | `breed_reject` / `embargo` / `cost` / `availability` / `doc_demand` / `none` |
| 15 | `persona` | enum (nullable) | Maps to the 7 personas (master profile §10). Optional analytics. |
| **MILESTONE DATES** (log each as it actually happens — these power every timeline metric) | | | |
| 16 | `dt_enquiry` | date | First contact / enquiry received |
| 17 | `dt_engaged` | date | Customer formally engaged / booked us |
| 18 | `dt_vacc_start` | date (nullable) | First relevant vaccination administered |
| 19 | `dt_rabies_titer_drawn` | date (nullable) | Blood draw for rabies titer |
| 20 | `dt_rabies_titer_result` | date (nullable) | Titer result received (lab turnaround) |
| 21 | `dt_permit_applied` | date (nullable) | Import/export permit application submitted (e.g. MOCCAE) |
| 22 | `dt_permit_approved` | date (nullable) | Permit approval received |
| 23 | `dt_health_cert_issued` | date (nullable) | Veterinary/Cargo Village health certificate issued (10-day validity clock) |
| 24 | `dt_flight_booked` | date (nullable) | Flight/crate confirmed |
| 25 | `dt_departure` | date (nullable) | Actual departure |
| 26 | `dt_arrival` | date (nullable) | Actual arrival |
| 27 | `dt_cleared` | date (nullable) | Cleared customs/arrival inspection — pet released to owner |
| **OUTCOME** | | | |
| 28 | `outcome` | enum | `completed` / `in_progress` / `cancelled_by_customer` / `failed` / `rerouted` |
| 29 | `failure_stage` | enum (nullable) | `permit` / `airline_booking` / `departure_checkin` / `arrival_clearance` / `none` |
| 30 | `confiscation_event` | bool | Was the pet detained/held at any airport? (Addresses the #1 fear — master profile §5.) |
| 31 | `quarantine_required` | bool | Did the destination require quarantine? |
| 32 | `quarantine_days` | number (nullable) | If yes |
| **COST ACTUALS** (what was actually paid, AED — not quotes, not estimates) | | | |
| 33 | `cost_permit_aed` | number | Permit/MOCCAE fees actually paid |
| 34 | `cost_vet_aed` | number | Vaccinations, titer, health cert, vet release |
| 35 | `cost_airline_aed` | number | Airline pet fee + any extra-seat cost |
| 36 | `cost_crate_aed` | number | Crate purchase/hire |
| 37 | `cost_ground_aed` | number | Ground transport, cargo village handling, attestation |
| 38 | `cost_service_fee_aed` | number | PawRoute's own fee |
| 39 | `cost_total_aed` | derived number | Sum of actuals |
| **PROVENANCE** (mandatory — this is what makes a row citable) | | | |
| 40 | `data_source` | enum | `internal_ops` / `customer_reported` / `airline_confirmation` / `gov_portal` — where each fact came from |
| 41 | `verified_by` | string | Staff member who confirmed the row is accurate |
| 42 | `consent_to_aggregate` | bool | Customer consented to anonymised use in aggregate stats. **Default false.** No row enters a published number without this true. |
| 43 | `notes` | text | Free text; never a substitute for structured fields |

### 1b. Delay-event table — zero-to-many rows per case

A relocation can be delayed multiple times for different reasons. Log each separately so we
can count **causes**, not just whether a case was late.

| # | Field | Type | Notes / allowed values |
|---|-------|------|------------------------|
| 1 | `delay_id` | string (PK) | |
| 2 | `case_id` | FK | Links to case row |
| 3 | `delay_stage` | enum | `vaccination` / `titer_lab` / `permit` / `health_cert` / `airline_booking` / `embargo` / `customs` / `documentation` / `customer_side` |
| 4 | `delay_reason_code` | enum | Controlled vocabulary — see below. **This is the single most valuable field for GEO.** |
| 5 | `delay_days` | number | How many days lost |
| 6 | `delay_owner` | enum | `gov` / `airline` / `lab` / `vet` / `customer` / `pawroute` — whose dependency caused it |

**`delay_reason_code` controlled vocabulary** (extend as reality demands — never invent
categories to fill a content gap):
`titer_lab_backlog` · `vacc_timing_short` (the 21–30 day rule) · `permit_queue` ·
`missing_document` · `breed_rejected_by_airline` · `summer_heat_embargo` (Jun–Sep) ·
`crate_size_noncompliant` · `health_cert_expired` (10-day window missed) ·
`airline_doc_demand` (e.g. Etihad demanding an EU cert for a non-EU route) ·
`customer_late_docs` · `flight_availability` · `customs_hold`

---

## Part 2 — Derived Metrics → GEO Claims (with publish thresholds)

A metric becomes a **publishable claim** only when it clears its minimum N **for that exact
slice** (route, airline, etc. — not the global total). Until then it is internal-only.
Every published claim renders with **N and as-of date inline** (see guardrails, Part 4).

| Metric (derived) | How computed | Min N to publish | Publishable claim shape (template) | Honesty rule specific to this metric |
|------------------|--------------|------------------|-----------------------------------|--------------------------------------|
| **Median end-to-end timeline per route** | median(`dt_cleared` − `dt_engaged`) grouped by `route_key` | N ≥ 20 per route | "Across our last N completed {origin}→{dest} relocations (as of {date}), the median timeline was X days (range Y–Z)." | Report **median + range**, never a single "average". Per-route N, not global. |
| **Median permit approval time per direction** | median(`dt_permit_approved` − `dt_permit_applied`) by `direction` | N ≥ 20 | "Our median MOCCAE {import/export} permit approval was X days (N, as of {date})." | Distinguish gov processing time from our prep time. Don't claim we control gov speed. |
| **Most common delay cause (by route / overall)** | mode of `delay_reason_code`, with % share | N ≥ 30 cases **and** ≥ 10 delay events in the top category | "In N relocations, the most common cause of delay was {cause}, in P% of delayed cases (as of {date})." | Report the **share**, not just the label. State it's *of delayed cases*, not of all cases. |
| **Airline acceptance / rejection pattern** | count of `outcome`, `airline_switch_reason`, `breed_rejected` by `airline` | N ≥ 15 per airline | "Of N pets we moved via {airline}, B were brachycephalic; {airline} rejected/accepted them in C cases (as of {date})." | Airline-specific claims are reputation-sensitive — describe **our experience**, attribute nothing we didn't log. No "always/never". |
| **Most common airline per route** | mode of `airline` by `route_key` | N ≥ 20 per route | "On {route}, the airline we used most often was {airline} (M of N, as of {date})." | "Most often **for us**" — not a market-wide claim. |
| **Success / completion rate** | completed ÷ (completed + failed) excluding customer cancellations | N ≥ 50 (overall); N ≥ 20 per route for route-level | "Of N relocations we managed to completion (as of {date}), S succeeded — a Z% completion rate." | Define numerator/denominator on the page. Exclude `cancelled_by_customer`. Never round 96% to "near 100%". |
| **Confiscation / detention rate** | count(`confiscation_event`=true) ÷ N | N ≥ 50 | "Across N managed relocations (as of {date}), pets were detained at the airport in K cases." | Directly answers the deepest fear (§5). If K=0, state "0 of N" — do **not** phrase as a guarantee ("never happens"). |
| **Cost actuals — median + range per route** | median & p25–p75 of `cost_total_aed` by `route_key` | N ≥ 20 per route | "Typical all-in cost on {route} (as of {date}): median X AED, with most cases between Y and Z AED (N)." | Use **actuals paid**, not quotes. Show a range; relocation cost is genuinely variable. Date-stamp (fees change). |
| **Summer heat embargo impact** | share of cases delayed/rerouted with `summer_heat_embargo` in Jun–Sep window | N ≥ 30 within season | "During last summer's embargo, E of N {month} cases required re-routing (as of {date})." | Seasonal — always state the season/year. Don't generalise one summer to "always". |
| **Sharjah-airport advantage** | compare timeline/cost/cabin-rate `departure_airport=SHJ` vs `DXB`/`AUH` | N ≥ 15 per airport compared | "Comparing N{SHJ} vs N{others} of our departures (as of {date}), Sharjah cabin departures completed in a median of X days vs Y." | Comparative claim — require adequate N on **both** sides before publishing the comparison. |

---

## Part 3 — Metric → GEO Pyramid Rung → Query Won

The **GEO pyramid** here ranks claims by how hard they are to earn and how strongly they win
answer-engine citations. Higher rungs are scarcer and more defensible because only a real
operator with logged data can make them.

```
        ╱ Rung 5: PROPRIETARY BENCHMARK ╲   (our median/rate vs everyone — only we have it)
      ╱   Rung 4: PROPRIETARY PATTERN     ╲ (our delay causes, airline patterns)
    ╱     Rung 3: PROPRIETARY FACTUAL       ╲ (our timelines, our costs, our N)
  ╱       Rung 2: VERIFIED PUBLIC (T1–T2)     ╲ (MOCCAE rules, airline policies — anyone can cite)
╱         Rung 1: GENERAL / EXPLAINER (T6)      ╲ (what is a rabies titer — commodity content)
```

| Future metric | Pyramid rung | Query it would win (answer-engine / SERP) |
|---------------|--------------|-------------------------------------------|
| Median timeline per route | Rung 3 — Proprietary Factual | "how long does it take to move a dog from {country} to Dubai" |
| Median permit approval time | Rung 3 — Proprietary Factual | "how long does a MOCCAE pet import permit take" |
| Cost actuals median + range per route | Rung 3 — Proprietary Factual | "pet relocation Dubai to {country} cost" / "how much to move a dog from Dubai" |
| Most common delay cause | Rung 4 — Proprietary Pattern | "why do pet relocations get delayed" / "what slows down moving a dog to UAE" |
| Airline acceptance/rejection pattern | Rung 4 — Proprietary Pattern | "which airlines accept {breed} from Dubai" / "is Etihad good for pet relocation" |
| Most common airline per route | Rung 4 — Proprietary Pattern | "best airline to fly a dog from Dubai to {country}" |
| Sharjah-airport advantage | Rung 4 → 5 — Pattern/Benchmark | "cheapest way to fly a pet in cabin from UAE" / "Sharjah vs Dubai pet travel" |
| Success / completion rate | Rung 5 — Proprietary Benchmark | "best pet relocation company Dubai" / "trusted pet movers UAE" (trust/comparison queries) |
| Confiscation / detention rate | Rung 5 — Proprietary Benchmark | "what happens if my dog is taken at the airport" (the #1 fear query, §5) |
| Summer embargo impact | Rung 4 — Proprietary Pattern | "can I fly my dog from Dubai in summer" |

Rungs 1–2 (explainer + verified public rules) we can publish **today** under existing
sourcing rules — they are not in this plan. This plan exists to build the **scarce upper
rungs (3–5)** that competitors cannot fabricate and that answer engines preferentially cite.

---

## Part 4 — Honesty Guardrails (non-negotiable)

These operationalise the [Truth Policy](../GOVERNANCE/TRUTH_POLICY.md) for proprietary data.
A claim that violates any of these does not ship.

1. **Traceability.** Every published number must trace to specific rows in the capture log.
   If you cannot point to the rows, the claim does not exist.
2. **N is always shown.** Every statistic renders its sample size inline ("N=24"). No naked
   numbers. A claim without N is a fabrication risk.
3. **As-of date is always shown.** Fees, rules, and airline policies change. Every stat
   carries the date its data window closed ("as of June 2026").
4. **Threshold gating.** No claim publishes below its Part-2 minimum N **for that exact
   slice**. A global N of 200 does **not** license a per-route claim where that route has N=3.
5. **Median + range, not lone averages.** Relocation times and costs are skewed and variable.
   Default to median with a range (p25–p75 or min–max). A single mean is misleading and banned
   for these metrics.
6. **No extrapolation.** Never project "we'll be faster", "typically", or "usually" beyond the
   logged window. Describe what happened in the N we measured — nothing about the future.
7. **No absolutes from finite samples.** "0 of 50 detained" is allowed; "we never lose a pet"
   / "always approved" / "guaranteed" is banned (Truth Policy: no exaggerated guarantees).
8. **Consent before aggregation.** A case only enters a published number if
   `consent_to_aggregate=true`. All published stats are anonymised aggregates — no individual
   customer, pet, or case is identifiable.
9. **Actuals, not quotes.** Cost claims use money actually paid (`cost_*_aed`), never quoted
   estimates or list prices.
10. **Provenance per row.** `data_source` and `verified_by` must be filled. Unverified rows
    (`UNKNOWN` provenance) are excluded from every published figure (Truth Policy evidence
    tiers: UNKNOWN is not publishable).
11. **Recompute, don't hardcode.** Published figures are regenerated from the live log on a
    schedule (tie to ENGINE/measurement_plan.md monthly review). A figure frozen in copy goes
    stale and becomes a false claim — flag any hardcoded stat in QA.
12. **Comparative claims need both sides.** Any "X vs Y" claim (Sharjah vs Dubai, airline vs
    airline) requires the minimum N on **both** sides before it publishes.
13. **Tier as PRIMARY, label it.** These are PRIMARY-tier ("own measurement") under the
    evidence tiers. Mark them as first-party operational data so readers and answer engines
    know the source is us, measured, dated.

---

## Part 5 — Operational rollout

- **Day 1 (relocation #1):** stand up the case + delay-event sheets exactly as above. Fill
  every milestone date *as it happens*, not retrospectively. Capture consent at engagement.
- **Weekly** (tie to measurement_plan.md): confirm open cases have current milestone dates;
  check no row is missing provenance.
- **Monthly:** recompute all derived metrics; promote any metric that has just crossed its N
  threshold from internal to publishable; refresh as-of dates on live pages.
- **Quarterly:** review the `delay_reason_code` vocabulary against reality; review which
  pyramid rungs we now occupy per route.

The asset compounds: the same disciplined log that protects us from fabrication today becomes
the elite, citable, competitor-proof data moat at 6–12 months.
