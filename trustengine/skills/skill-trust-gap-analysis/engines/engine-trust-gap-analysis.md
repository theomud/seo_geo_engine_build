# Engine — Trust Gap Analysis
## Spec for the competitor-scoring engine (implemented by competitor_research_engine.py)

This engine automates Step 03 of the skill (see `files/04-automation-spec.md` for the full specification). It is the implementation companion to that spec — read File 04 first.

## What it does
For each competitor URL (human-supplied list + the niche Risk Continuum level):
1. **Playwright** visits the page and takes a full-page screenshot → `data/screenshots/`.
2. Extracts the visible page text.
3. **Anthropic API** scores all 10 trust dimensions with a one-line evidence note each, returning JSON (scores, evidence, total, gaps, confidence) per the scoring system prompt in File 04.
4. Writes the score + evidence + gap list → `data/scores/`.
5. After all competitors, tallies failures per dimension → the **Content Gap Matrix**.

## Implementation
`engines/competitor_research_engine.py` — Playwright + Anthropic. In the Dubai proof run it auto-scored **6 of 9** competitors; the top **3** were scored manually first to calibrate the standard.

## Inputs / outputs / guardrails
- **Inputs:** competitor list + per-competitor URL (human discovery — optional input per P-12), niche risk level (human, Step 0), `ANTHROPIC_API_KEY`.
- **Outputs:** `data/scores/*.json` + `*.txt`, `data/screenshots/`, the ranked Content Gap Matrix.
- **Hand back to human** (`manual review`, never finalised) when: page fails to load / <200 chars; confidence <0.6; dimension 2 (official source) or 10 (proof interstitial) ambiguous; competitor is community-only with no scorable page.
- **Test phase:** score the same 3 a human scored; if >1 dimension disagrees across the 3, fix the prompt/calibration before the full run.
- **Audit:** a sub-agent re-scores 20% (min 3) blind; ≥90% dimension-level agreement to pass (`files/03-how-to-verify-it.md`).

## Library codes
F-03 Trust Score Competitor Scoring · M-05 Trust Score Model · M-04 Risk Continuum · F-11 45-Check Audit · P-06 Screenshots Are Proof. Full citations in `MFP-LIBRARY.md`.
