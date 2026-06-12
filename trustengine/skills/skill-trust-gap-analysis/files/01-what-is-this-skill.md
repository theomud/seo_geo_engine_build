---
Status: draft — built 2026-05-29
Area: skill-trust-gap-analysis
Depends on: skill-trust-gap-analysis/README.md
Feeds into: skill-trust-gap-analysis/files/02-how-to-do-it-manually.md, skill-trust-gap-analysis/files/04-automation-spec.md
---

# Skill · File 01 — What This Skill Is
## Niche-agnostic definition of Trust Gap Analysis

---

## The problem this skill solves

Most competitor research tells you what competitors **publish**. This skill tells you what they **fail to say** — and why that silence is worth money.

In markets where customers make high-stakes decisions — pet relocation, immigration, medical travel, legal, financial — trust is the primary conversion factor. Customers choose the provider they trust most, not the cheapest and not the one with the most keywords. So the winning move is not to out-publish competitors; it is to find every place they leave a customer's fear unacknowledged or a claim unproven, and to be the first to fill that gap with verified, proof-backed content.

Trust Gap Analysis is the discipline that finds those gaps systematically: it scores every competitor on ten trust dimensions, identifies every unacknowledged fear and uncited claim, and converts each gap into a ranked content opportunity you can build first.

---

## What this skill produces

Three artefacts:

1. **A Trust Score per competitor** (out of 10) — an objective, repeatable score across the ten trust dimensions, with a screenshot and a documented gap list for each page.
2. **The Content Gap Matrix** — every gap ranked by how many competitors miss it, turned into a build order.
3. **A risk-calibrated proof threshold** for the whole niche — how much proof every page in this market must carry to win.

The output is not a report that gets read once; it is the prioritised list of pages to build, and the benchmark every new page is measured against.

---

## Step 0 — the Risk Continuum (before scoring anyone)

Before a single competitor is visited, the niche is placed on the **Risk Continuum**, which sets the proof threshold for the whole market:

| Level | What the user risks | Proof threshold |
|-------|--------------------|-----------------|
| Low — Entertainment | Seconds of time | Low — personality wins |
| Medium-Low — B2C education | Appearance / minor habits | Moderate — live demo beats text |
| Medium-High — B2C financial/legal | Real money / legal standing | High — third-party credentials |
| High — Regulated services | Irreversible harm | Maximum — every claim traces to an official source |

**Dubai pet relocation sits at maximum risk** — a pet confiscated at the border because of wrong advice is catastrophic. That placement is *why* generic reassurance fails and why most competitors score low: they provide information but zero proof it is correct.

---

## The 10-Point Trust Score

One point per page for each dimension present:

1. Fear in the first 100 words · 2. Official source cited · 3. Specific route/variant named · 4. Step-by-step process · 5. Timeline included · 6. Cost ranges shown (with honest disclaimers) · 7. Common-mistakes section · 8. Original visuals (not stock) · 9. CTA that feels like help · 10. **Proof interstitial** (proof embedded beside each claim, not in one testimonials block).

Score bands: **0–2** displace immediately · **3–4** weak, exploit gaps · **5–6** decent, target specific gaps · **7–8** strong, study and surpass · **9–10** excellent, learn from everything.

---

## How it differs from generic competitor research

| Generic competitor research | Trust Gap Analysis |
|-----------------------------|--------------------|
| Lists what competitors publish | Surfaces what they fail to say |
| Keyword / backlink focused | Trust-and-proof focused |
| No proof-threshold concept | Sets the threshold via the Risk Continuum first |
| "They rank, we should too" | "They left this fear unproven — we own it first" |
| Output is a slide deck | Output is a ranked build order (the Gap Matrix) |

---

## The 4 steps inside this skill

1. **Step 00 — Risk Continuum placement** (set the proof threshold before visiting any site).
2. **Step 01 — Competitor discovery** (Google *and* community research — Facebook groups, Reddit — because community surfaces competitors Google tools miss).
3. **Step 02 — Manual scoring of the top 3** (calibrate judgment; screenshot and score every dimension by hand).
4. **Step 03 — Automated scoring of the rest** (Playwright + Anthropic against all 10 dimensions), then **Step 04 — the Gap Matrix** (count failures per dimension; most failures = highest-priority pages).

---

## In scope / out of scope

**In scope.** Placing the niche on the Risk Continuum, discovering competitors, scoring pages on the 10 trust dimensions, and ranking the resulting gaps into a build order.

**Out of scope.** Verifying the facts themselves (`skill-official-source-research`), mapping the customer fears (`skill-customer-fear-intelligence`), and building the pages that fill the gaps (`skill-content-structure`). This skill finds and ranks the gaps; other skills prove the facts and build the pages.

---

## What "good" looks like

A Trust Gap Analysis is good when: the niche is correctly placed on the Risk Continuum; every discovered competitor (including community-only ones) is scored on all 10 dimensions with a screenshot; the Gap Matrix ranks gaps by failure frequency; and the universal gaps (those missed by nearly every competitor) are identified as the first pages to build.

**Proven on Dubai pet relocation (May 2026):** 9 of 21 competitors scored (avg 3.9/10; benchmark DKC 8/10), **4 universal gaps** found that all 9 competitors missed (airport confiscation, summer embargo, titer cost+timeline, airport comparison). Confirmed Skill Value Score: **20/25**.
