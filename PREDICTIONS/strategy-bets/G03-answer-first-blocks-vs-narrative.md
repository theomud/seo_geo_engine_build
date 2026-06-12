# G03 — Answer-first extractable blocks get cited more than narrative prose

**Claim:** Content structured as answer-first, self-contained extractable blocks (a direct
lead sentence, then bullets/tables/steps) gets cited by AI engines more than the same
information delivered as flowing narrative prose.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.82 | Answerability is a top GEO signal; extractable chunks map to how retrieval/grounding selects passages. |
| Claude | 0.72 | Strong agreement and it's consistent with our concise-extraction thesis (cf. B04/B07). Self-contained chunks that answer the query in the first sentence are easy for an engine to lift and attribute. Main caveat: engines also synthesise across prose, so the lift is clearest on direct factual/"what is / how much / what are the steps" intents. This is one of my higher-confidence GEO bets. |

## Divergence note
Low divergence (0.82 vs 0.72) — both sources expect this to hold; it doubles as a high-confidence calibration check.

## Success metric (resolve by 2027-01-09, post-launch)
- On a matched factual/procedural prompt set, the answer-first/extractable-block variant is cited in a higher share of probes than the narrative variant across ≥2 engines. PARTIAL if it wins on extraction-style prompts but not on open-ended ones.

## Measurement
`TRACKING/geo_visibility.csv` — `cited` rates per engine for block vs narrative variants on matched prompts.

## Status
`open — awaiting live deployment`.

## Outcome
_TBD._
