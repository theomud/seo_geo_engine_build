# G02 — High entity density lifts AI citation

**Claim:** Pages with high, well-disambiguated *entity density* — named airlines, breeds,
specific fees, document names, authorities, locations, timeframes — get cited by AI engines
more than otherwise-equivalent pages that talk in generic terms ("the airline," "the fee,"
"the document").

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.80 | Entity richness is one of Gemini's 5 GEO signals; named entities make a passage answerable and grounding-friendly for retrieval. |
| Claude | 0.62 | Agree entity grounding helps retrieval and makes a passage quotable, and it correlates with genuine specificity. But density alone can be confounded with *being more useful*; keyword/entity stuffing without real substance won't move citations and may read as spam. I bet the effect is real but mediated by accuracy and answerability, not raw entity count. |

## Divergence note
Gemini 0.80 vs Claude 0.62. The clean test isolates density from substance: same facts, one phrased with specific named entities, one generic.

## Success metric (resolve by 2027-01-09, post-launch)
- On a matched prompt set, the high-entity-density variant is cited in a higher share of probes than the low-density variant across ≥2 engines, with the entity-rich passage being the one quoted/linked. PARTIAL if lift appears on only one engine or is within noise.

## Measurement
`TRACKING/geo_visibility.csv` — `cited` / `source_url` rates per engine for the two variants; inspect which passage the engine quotes.

## Status
`open — awaiting live deployment`.

## Outcome
_TBD._
