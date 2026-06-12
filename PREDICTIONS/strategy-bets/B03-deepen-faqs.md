# B03 — Deepening one-sentence FAQ answers into full blocks improves ranking/PAA

**Claim:** Expanding the short toggle FAQ answers into comprehensive, multi-sentence answers will
reduce bounce and improve rankings / PAA capture.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.80 | "Thin content & engagement trap" — one-sentence answers make users bounce. |
| Claude | 0.55 | **Partial disagreement.** Depth helps only when it adds *information*, not words. For an answer-first GEO block, concision is often the asset, not the bug; padding risks diluting the extractable answer. I bet "add a second sentence of real substance" wins, but "expand every FAQ into paragraphs" has low marginal value and some downside. |

## Divergence note
Gemini 0.80 vs Claude 0.55 → meaningful gap. Test BOTH: a concise variant and a deepened variant of the same FAQ set.

## Success metric (resolve by 2026-12-09, post-launch)
- Deepened-FAQ variant outranks OR wins more PAA/AIO slots than the concise variant on the same query set across a 4-week probe window. PARTIAL if mixed by query.

## Measurement
A/B across two route variants → `TRACKING/experiments.csv` + citation probes.

## Status
`open — awaiting live deployment`.

## Outcome
_TBD._
