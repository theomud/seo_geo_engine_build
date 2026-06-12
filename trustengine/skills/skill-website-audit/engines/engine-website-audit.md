# ENGINE — Website Audit
## The scoring methodology + the runnable Claude Code prompt (read files/04-automation-spec.md first; output structure = engines/AUDIT-REPORT-TEMPLATE.md)

This engine scores any website on all 13 Trust Engine skills (130 points), backs every score with
evidence quoted from the live site, RICE-ranks the gaps, and produces a client-ready report in the
fixed template. It **collects, checks, computes, and assembles — the /10 scores and the client-ready
sign-off stay human** (an act of evidenced judgement, not a checklist a model can fake). Automation
4/5. Built on F-11 (the audit discipline) with E-E-A-T / Trust-at-the-centre (M-24, P-22) as the
parent model. *Validated on the live DKC audit → `data/audit-dkc-2026-06-01.md`, 67/130.*

---

## USAGE (paste as the Claude Code / sub-agent instruction)

```
You are an independent website auditor using the Trust Engine 13-skill framework.
You did not build the site. Score only what you can see on the LIVE site.

Audit the site at: [URL]  (key pages: home, main service/offer, one content page, about/contact)

Method:
1. Calibrate the risk level (M-04) FIRST — it sets the proof bar for the whole audit.
2. Fetch each key page live; capture the exact opening line, headline, CTA wording,
   every numeric claim, schema, nav/internal links, and any freshness date. Screenshot each.
3. Score each of the 13 dimensions /10 using the rubric below. EVERY score must cite at least
   one piece of evidence QUOTED from the live site. No quote → the dimension is unscored, not guessed.
4. Total to /130; assign a market position.
5. RICE-score every gap: (Reach × Impact × Confidence) ÷ Effort. Sort. Name the #1 action.
6. Write a 9-element content brief for the #1 gap, Inputs filled with real audit data.
7. Write the executive summary LAST; apply the client-ready test.
8. Assemble into engines/AUDIT-REPORT-TEMPLATE.md → data/audit-[site]-[date].md.

Never invent a score or a quote. A page you cannot fetch is "not retrieved," never scored.
Hand the /10 scoring and the client-ready judgement to a human; the engine collects and computes.
```

---

## STEP 1 — Calibrate the proof bar (M-04, before scoring)

| Risk | Proof bar applied to every claim |
|------|----------------------------------|
| Maximum (health/money/safety — e.g. pet import) | official source required for **every** claim; wrong info = real harm (P-02) |
| Med-High | sources required for safety/money claims |
| Med-Low / Low | reasonable sourcing; design-trust signals weigh more |

---

## STEP 2 — The 13-dimension scoring rubric (score /10, each with a quote)

Each dimension uses the same band logic: **0–3 = absent/weak · 4–6 = present but partial · 7–10 =
strong, evidenced.** A score is valid only with a quote from the live site.

| # | Dimension | Governing skill · MFP | 7–10 (strong) | 0–3 (weak) |
|---|-----------|-----------------------|---------------|------------|
| 1 | Fear Intelligence | Customer Fear Intel · P-04 | names the market's real fears in the customer's language, early | brand/feature copy that names no fear |
| 2 | Trust Gap Score | Trust Gap · M-05/F-03 | clears most of the 10-point page score (below) | misses fear-first, sourcing, steps, proof |
| 3 | Source Verification | Official Source · P-02/M-13/P-07 | every claim cited to an official source (inline) | uncited/wrong claims on a high-risk site |
| 4 | Content Structure | Content Structure · F-08 | fear → answer → proof → related → help-CTA | answer buried, proof siloed |
| 5 | Editorial Quality | Editorial Judgment · M-10/F-06 | clears the 10 criteria; no weak-AI patterns | hype/hedging/filler openings |
| 6 | Conversion Copy | Conversion Copy · P-04 | acknowledges fear without exploiting; help-first CTA | ignores fear, or manufactures urgency |
| 7 | Visual Evidence | Visual Evidence · M-13/F-08 | real screenshots/photography/data | stock imagery, no evidence visuals |
| 8 | Site Architecture | Content Architecture · M-24 | ≤3 clicks, clean URLs, logical nav, no orphans | deep/hidden pages, messy URLs |
| 9 | Authority Assets | Authority Assets · P-13/M-13 | case studies/guides that pass the Hormozi test | generic "expert team" an AI could write |
| 10 | Email Nurture | Email Nurture · F-05 | email capture + fear-named, help-first sequence | no capture; no nurture |
| 11 | AI Citation | AI Citation · M-22 | answer-first + valid FAQ schema + clear entity | answer buried, no schema, fragmented entity |
| 12 | Monitoring Evidence | Monitoring · M-27/F-05 | freshness dates, current facts, responsiveness | undated/stale content, out-of-date facts |
| 13 | Market Position | synthesis · M-24/P-22 | differentiated, above-market, AI-visible | undifferentiated, invisible in AI answers |

**Dimension 2 — the 10-point Trust Score breakdown (1 pt each):** fear in first 100 words · official
source cited · specific route named · step-by-step process · timeline included · cost ranges shown ·
common-mistakes section · original visuals · CTA feels like help · proof throughout. *(M-05; F-03.)*

---

## STEP 3 — The action plan (M-27 RICE · F-05)

For every gap: **RICE = (Reach × Impact × Confidence) ÷ Effort.** Reach 1–10 (pages/visitors
affected); Impact 0.25–3 (3 = fixes a real-harm / market-deepest-fear gap); Confidence 0.5–1.0 (1.0 =
an official source backs the fix); Effort 1–5 (days). Sort descending; the top row is the single most
important action. The report must terminate in this ordered queue, not a list of observations (F-05).

```python
def rice(reach, impact, confidence, effort):
    if effort <= 0: raise ValueError("effort must be > 0")
    return round((reach * impact * confidence) / effort, 2)
```

---

## STEP 4 — The content brief + the client-ready test

For the #1 gap, write a complete **9-element prompt** (Context, Role, Objective, Audience, Inputs,
Constraints, Examples, Output Format, Quality Criteria) with **Inputs filled from real audit data**
(verified facts/C-IDs, the verbatim fear quote, the target keyword) — runnable as-is. Then write the
executive summary and apply the **client-ready test:** could a business owner act on it without the
framework explained? If not, rewrite.

---

## Inputs / outputs / guardrails

- **Inputs:** the site URL + key pages; the market's fears (Column K) + verified facts (C-IDs); the
  risk level; per-gap R/I/C/E; optional keys (`ANTHROPIC_API_KEY` draft assist, `SERPAPI_KEY` for
  D11/D13). `PROJECT_ROOT`.
- **Outputs:** `data/audit-[site]-[date].md` in the template structure (exec summary + 13 scores +
  detailed findings + RICE plan + content brief + competitor comparison + sign-off).
- **Never** invents a score or a quote; **never** scores a page it could not fetch (mark "not
  retrieved"); **never** miscalibrates the proof bar; **never** assigns a /10 by model impression
  instead of quoted evidence.
- **Hand back to human:** the risk calibration; each dimension's /10; the D3 source re-trace; the
  fear/copy/authority judgements (D1, D6, D9 — P-04, P-13); the content brief; the exec summary; the
  client-ready sign-off.

---

## POST-RUN AUDIT CHECKLIST (the sub-agent re-checks)

- [ ] All 13 dimensions scored /10, **each with a quote re-findable on the live site** (re-open and confirm).
- [ ] No fabricated quote; no page scored that wasn't retrieved.
- [ ] Proof bar matches the site's calibrated risk level (M-04).
- [ ] 3–4 dimensions re-scored blind land within ±1 of the report.
- [ ] Every action-plan gap has a RICE value; the ranking follows the arithmetic.
- [ ] One content brief, 9 elements, Inputs filled with real data, runnable.
- [ ] Executive summary passes the client-ready test.
Pass threshold: all of the above. A fabricated quote, an unscored dimension, a miscalibrated bar, or a
jargon-only summary is a hard fail.

---

## STATUS

**Spec complete; the engine was run on a real site (the proof).** The live audit of **DKC (dkc.ae)**
scored **67/130** with all 13 dimensions evidenced from quoted on-site text, a RICE-ranked action plan
(top action 12.15 — the airport-confiscation page), a 9-element content brief, and a client-ready
executive summary → `data/audit-dkc-2026-06-01.md`. The score reconciles with DKC's prior 8.0/10
relative Trust Score (best in a weak market, real absolute gaps). The engine collected and computed;
the /10 scores and the verdict were the auditor's evidenced judgement.

## Library codes
M-04 Risk Continuum · M-05 Trust Score · M-10 Ten-Criteria Quality · M-13 Proof Density · M-24
E-E-A-T · M-27 RICE · F-03 Trust Score Competitor Scoring · F-05 Dashboard-to-Action · F-06 Seven-Step
Editorial · F-08 Proof Interstitial · F-11 Forty-Five-Check Audit · P-02 Wrong Information Causes Real
Harm · P-03 Proof Over Promise · P-04 Fear-Acknowledging Not Fear-Exploiting · P-07 Independent
Verification · P-13 Hormozi Test · P-22 Trust Is the Centre. Full citations in `MFP-LIBRARY.md`.
