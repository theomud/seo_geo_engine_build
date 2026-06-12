---
Status: complete (PROVEN 47/47) — 2026-06-01
Area: skill-website-audit
Depends on: skill-website-audit/files/01-what-is-this-skill.md, skill-website-audit/README.md
Feeds into: skill-website-audit/files/03-how-to-verify-it.md, skill-website-audit/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Running a complete 130-point trust audit of a website by hand — before any of it is automated

---

## Why manual first

The two acts that make an audit trustworthy are human judgements a script cannot fake: **reading a live
page and deciding what its words actually do to a frightened buyer**, and **assigning a /10 that you
can defend with a quote**. Automation can fetch the page, screenshot it, and do the RICE arithmetic —
but if a model *invents* the scores, you have a confident-looking report that audits nothing. So run a
full audit by hand first; the engine later just collects evidence faster and does the maths. *(Library:
P-01 Manual Before Automated; P-03 Proof Over Promise; P-07 Independent Verification.)*

Three things on the desk before you start:
1. **The site** — the URL plus its key pages (homepage, main service/offer page, one content/blog
   page, contact/about).
2. **The market's fears + verified facts** — the fear list (Column K) and the Source Bank C-IDs for
   this niche, from the customer-profile snapshot. These are the standard you score D1–D3 against.
3. **The report template** — `engines/AUDIT-REPORT-TEMPLATE.md`, which fixes the output structure.

---

## Step 1 — Set scope and calibrate the risk level (do this first)

Record the URL, the pages you will audit, and the market. Then calibrate the **risk level (M-04)** —
this sets the proof bar for the *entire* audit:

| Risk | Proof bar |
|------|-----------|
| Maximum (pet import, health, money) | every claim needs an official source; wrong info = real harm (P-02) |
| Med-High | sources required for safety/money claims |
| Med-Low / Low | reasonable sourcing; design-trust signals weigh more |

> DKC worked example: dkc.ae, market = Dubai pet relocation → **Maximum risk**. Every claim DKC makes
> about permits, vaccinations, or fees must be cited to an official source, or it loses points on D3.

---

## Step 2 — Visit the site and capture real evidence

Open the live pages and **capture evidence, not impressions**. For each key page, copy the **actual
opening line**, the headline, the CTA wording, and any factual claim with a number. Take a full-page
screenshot of each. You will quote this verbatim in the report — every score must trace to something
you can paste. **Never score from memory or assumption; if you didn't see it on the page, it doesn't
count.**

> DKC: capture the homepage opening line, the main relocation-service page, the CTA text, and any
> permit/fee/vaccination claim. Screenshot each.

---

## Step 3 — Score the 13 dimensions /10, each with quoted evidence

Score each dimension against its governing skill's standard. For every dimension write: **the /10, a
one-line status, and at least one quote from the live site** that justifies it. A score with no quote
is not a score.

| # | Dimension | What earns a high score | What costs points |
|---|-----------|-------------------------|-------------------|
| 1 | Fear Intelligence | the homepage/service page names the market's real fear in the customer's language, early | generic "your pet is family" copy that never names a fear |
| 2 | Trust Gap Score | clears the 10-point page score (below) | each missing point = −1 |
| 3 | Source Verification | every factual claim cited to an official source; honest hedges where none exists | uncited or wrong numbers on a max-risk site (P-02) |
| 4 | Content Structure | pages run fear → answer → proof → related → help-CTA | answer buried; no proof beside claims (F-08) |
| 5 | Editorial Quality | clears the 10-criteria rubric; no weak-AI patterns | hype, hedging, filler, "in today's world" openings |
| 6 | Conversion Copy | acknowledges the fear without exploiting it; help-first CTA (P-04) | fear-exploiting urgency, or "Get a Quote" with no help |
| 7 | Visual Evidence | real screenshots / real photography / data visuals | stock photos, no evidence imagery (M-13) |
| 8 | Site Architecture | navigable, ≤3 clicks to key pages, clean URLs, no orphans | deep/hidden pages, messy URLs |
| 9 | Authority Assets | case studies / guides that pass the Hormozi test (P-13) | claims of expertise with nothing an AI couldn't write |
| 10 | Email Nurture | email capture + evidence of a fear-named, help-first sequence | no capture, or capture with no nurture |
| 11 | AI Citation | answer-first, FAQ schema, one clear entity — citeable | answer buried, no schema, fragmented entity (M-22) |
| 12 | Monitoring Evidence | freshness dates, accurate current facts, responsiveness | stale/undated content, out-of-date regulations |
| 13 | Market Position | differentiated, Trust Score above market, AI-visible | undifferentiated; invisible in AI answers |

**Dimension 2 — the 10-point Trust Score breakdown (1 point each):** fear in first 100 words · official
source cited · specific route named · step-by-step process · timeline included · cost ranges shown ·
common-mistakes section · original visuals · CTA feels like help · proof throughout. *(Library: M-05;
F-03.)*

> DKC thread: a clean, professional site likely scores well on D4/D5/D8 — but score D1 against the
> fear list: does it name the airport-confiscation fear anywhere? (The gap matrix says no — 9/9
> competitors miss it, DKC included.) Quote DKC's actual homepage opening as the evidence.

---

## Step 4 — Total to /130 and assign the market position

Sum the 13 scores to an overall **/130** and translate it to a market position the owner understands
(e.g. *market leader with one critical gap* / *mid-pack* / *high risk*). Anchor it against the known
benchmark: DKC's prior 10-point Trust Score was 8.0/10, the market high; the market average was 3.9/10.

---

## Step 5 — Build the RICE-ranked action plan

List every gap the scoring surfaced. Score each with **RICE = (Reach × Impact × Confidence) ÷
Effort** *(Library: M-27)* — Reach 1–10 (pages/visitors affected), Impact 0.25–3 (3 = fixes a
real-harm/maximum-fear gap), Confidence 0.5–1.0 (1.0 = an official source backs the fix), Effort 1–5
(days). Sort descending; the top row is the **single most important action**. *(Library: F-05
Dashboard-to-Action — the audit must end in an ordered queue, not a list of observations.)*

> DKC: "Publish the airport-confiscation page" — high Reach (every anxious buyer), Impact 3 (the
> deepest fear, real-harm), Confidence high (the fear is documented + the facts are verified, C-003/
> C-010), Effort ~2 → tops the queue.

---

## Step 6 — Write the content brief for the top gap

For the #1 action, write a **complete 9-element prompt** for the missing page (Context, Role,
Objective, Audience, Inputs, Constraints, Examples, Output Format, Quality Criteria), with **Inputs
filled from the real data found during the audit** — the verified C-IDs, the verbatim fear quote, the
target keyword. It must be runnable as-is.

---

## Step 7 — Write the executive summary (apply the client-ready test)

Write the summary **last**, for a business owner who has not read the rest: overall /130 + market
position, top-3 strengths (with evidence), top-3 critical gaps (with evidence and consequence), and
the single most important action named with a specific page. **The client-ready test:** could the
owner act on this without you explaining the framework? If not, rewrite it.

---

## Step 8 — (Optional) Competitor comparison

Score one or two named competitors on the same 13 dimensions and table them side-by-side (/130 each).
This converts the audit from "you have gaps" to "here is exactly where you stand against the people
you lose customers to."

---

## Step 9 — Assemble into the report template

Pour everything into `engines/AUDIT-REPORT-TEMPLATE.md`: Site Audited → Executive Summary → Dimension
Scores table → Detailed Findings → Action Plan → Content Brief → Competitor Comparison → Sign-off.
Save as `data/audit-[site]-[date].md`.

---

## What you must not do

- **Do not score without a quote.** Every /10 cites text or a feature you actually saw on the live
  site. No evidence → no score.
- **Do not invent scores or evidence.** If a page wasn't visited, it isn't audited — say so.
- **Do not miscalibrate the proof bar.** A maximum-risk site is held to "official source for every
  claim"; passing it at low-risk standards is an audit failure.
- **Do not let the loudest gap win.** RICE decides the order; a cosmetic fix doesn't jump the
  market-deepest fear.
- **Do not ship a summary only the framework's author could act on.** It must pass the client-ready
  test.
- **Do not flatter.** "Clean and professional" is not a finding; "names no fear, cites no source" is.

---

## Output of this manual phase

A complete audit report in `data/audit-[site]-[date].md`: 13 dimensions scored /10 with site-quoted
evidence, an overall /130 + market position, a RICE-ranked action plan, a ready-to-execute content
brief for the top gap, and a client-ready executive summary (plus an optional competitor comparison).
That report is the real deliverable — the proof run is the live DKC audit — and the input to File 04,
where automation collects the evidence and does the RICE maths while the scoring judgement stays human.
