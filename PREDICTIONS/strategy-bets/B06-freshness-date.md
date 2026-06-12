# B06 — A current-year freshness marker ("2026") improves ranking

**Claim:** Replacing a static "verified June 2024"-style line with a current, frequently-updated
freshness marker materially improves rankings via freshness signals.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.65 | "Tells a search engine your data might be two years out of date." |
| Claude | 0.35 | **Disagreement.** Freshness is a real but *minor* signal here, and our pages already carry honest `verified: June 2026` + JSON-LD `dateModified`. Marginal ranking lift from the date alone is small; content depth dominates. **Truth guardrail:** the date must reflect a real re-verification — bumping a date without re-checking the source violates the truth policy and is the wrong kind of "fresh." |

## Divergence note
Gemini 0.65 vs Claude 0.35 → real gap on *impact magnitude*.

## Success metric (resolve by 2026-12-09, post-launch)
- Isolating a freshness-marker change (content held constant) produces a measurable ranking lift on a matched query set. FALSE if no detectable movement.

## Measurement
`TRACKING/experiments.csv` (date-only change A/B).

## Status
`open — awaiting live deployment`.

## Outcome
_TBD._
