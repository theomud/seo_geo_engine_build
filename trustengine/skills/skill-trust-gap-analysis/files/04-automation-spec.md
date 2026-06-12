---
Status: draft — built 2026-05-29
Area: skill-trust-gap-analysis
Depends on: skill-trust-gap-analysis/files/02-how-to-do-it-manually.md, skill-trust-gap-analysis/files/03-how-to-verify-it.md
Feeds into: skill-trust-gap-analysis/engines/engine-trust-gap-analysis.md
---

# Skill · File 04 — Automation Spec
## What the competitor-scoring engine does, and what stays human

---

## Automation target

**~70% of the work can be automated** once Step 0 (risk placement) is set, discovery is done, and the top 3 competitors are scored by hand to calibrate the standard. The engine scores the long tail; humans set the lens and own the interpretation. (Library: the engine operationalises **F-03 Trust Score Competitor Scoring** against **M-05 Trust Score Model**.)

What gets automated:
- Visiting each competitor URL (Playwright, headed where needed for JS-rendered pages).
- Full-page screenshot of every scored page (the audit evidence — **P-06**).
- Extracting visible page text.
- Scoring all 10 trust dimensions against the page text (Anthropic API), with a one-line evidence note per dimension.
- Writing score + per-dimension evidence + gap list to the scores file.
- Tallying the Content Gap Matrix (failures per dimension across all scored competitors).

What stays manual:
- **Step 0 — Risk Continuum placement** (sets the threshold the engine scores against). (**M-04**.)
- **Discovery**, especially community-only competitors the engine can't find.
- **Top-3 calibration** scoring (the standard the engine imitates).
- **Low-confidence review** and the final read of the matrix into a build order.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| Competitor list + the exact URL to score per competitor | `.txt` / list | discovery (community + Google) — *or* user-supplied (P-12: optional input) |
| Niche Risk Continuum level | one value | Step 0 (human) |
| Anthropic API key | env | `ANTHROPIC_API_KEY` in `.env` |

The engine does not discover competitors and does not set the risk level — both are human inputs it scores against.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Per-competitor 10-dimension score + evidence note per dimension | `data/scores/` |
| Gap list per competitor (dimensions scored 0) | `data/scores/` |
| Full-page screenshot per scored page | `data/screenshots/<competitor>-<date>.png` |
| Content Gap Matrix (failure counts, ranked) | `data/` |

The engine never decides the build order; it produces the scored data a human reads into the matrix and priorities.

---

## Engine flow per competitor

```
for each competitor (URL + risk_level):
    1. Playwright: goto(URL), wait for network idle
       - full-page screenshot -> data/screenshots/<competitor>-<date>.png
       - extract inner_text("body")
       - on load failure: log, mark "manual review", continue
    2. Anthropic API: scoring system prompt (below) + page_text + risk_level
       - parse JSON: { scores{1..10}, evidence{1..10}, total, gaps[], confidence }
    3. write score + evidence + gap list to data/scores/
    4. rate limit: 2s between page loads, 0.5s between API calls
after all competitors:
    5. tally failures per dimension -> Content Gap Matrix, ranked by frequency
```

(An implementation already exists — `engines/competitor_research_engine.py` — which auto-scored 6 of the 9 Dubai competitors, with 3 scored manually.)

---

## The scoring system prompt

```
You score a competitor page against a 10-dimension Trust Score for a market at
RISK_LEVEL (Low / Medium-Low / Medium-High / High). Higher risk demands harder proof.
You are given: PAGE_TEXT and RISK_LEVEL.

Return ONLY JSON:
{
  "scores": {"1":0|1, ... "10":0|1},
  "evidence": {"1":"<the on-page element justifying the score>", ...},
  "total": 0-10, "gaps": [list of dimension numbers scored 0], "confidence": 0.0-1.0
}

The 10 dimensions (1 point each, only if literally present):
1 Fear in first 100 words  2 Official source CITED (an actual gov/regulatory link — not
official-sounding claims)  3 Specific route/variant named  4 Step-by-step process with timing
5 Timeline with specific durations  6 Cost ranges with honest disclaimers  7 Common-mistakes
section  8 Original (non-stock) visuals  9 Help-feeling CTA  10 Proof interstitial THROUGHOUT
(beside claims, not a single testimonials block).

RULES:
- Award a point ONLY with specific supporting text in PAGE_TEXT; cite it in "evidence".
- Dimension 2: a claim that sounds official without a real source link scores 0.
- Dimension 10: a testimonials-only section scores 0.
- At High risk, do not reward polished but unproven reassurance.
- confidence < 0.6 -> route to human review; never guess.
```

---

## Test phase (3 competitors, then PAUSE)

Before the full run, the engine scores the **same 3 competitors a human scored manually** and stops. Compare dimension-by-dimension. If engine and human disagree on more than 1 dimension across the 3 pages, fix the prompt or the risk calibration before scoring the rest. Never scale an uncalibrated scorer.

---

## Audit (after the full run)

A sub-agent re-scores **20%** of competitors (minimum 3) blind and compares to the engine, per File 03's gates. Pass threshold: **90%** dimension-level agreement. Below 90% → halt and re-score against the File 02 rubric. (Library: **F-11 Forty-Five-Check Audit**.)

---

## When automation must hand back to humans

The engine flags `manual review` (never finalises) when:
- The page failed to load or returned < 200 characters of text.
- Confidence < 0.6 on the overall score.
- Dimension 2 (official source) or 10 (proof interstitial) is ambiguous — these two most distort the matrix when wrong.
- The competitor was discovered community-only and the URL is a social profile rather than a scorable page.

Regulated-market scoring has no acceptable "guessed" score — a wrong score mis-ranks the build.

---

## Files in this skill (created by the build)

```
skill-trust-gap-analysis/
├── README.md
├── .env.example
├── files/
│   ├── 01-what-is-this-skill.md
│   ├── 02-how-to-do-it-manually.md
│   ├── 03-how-to-verify-it.md
│   ├── 04-automation-spec.md            ← this file
│   └── 06-models-frameworks-principles.md
├── guides/
│   ├── trust-gap-analysis-study-manual.html
│   └── trust-gap-analysis-cheatsheet.html
├── data/
│   ├── scores/
│   └── screenshots/
└── engines/
    └── engine-trust-gap-analysis.md     (implemented by competitor_research_engine.py)
```
