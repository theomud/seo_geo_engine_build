# G04 — The "expertise layer" is the deciding GEO factor

**Claim:** The decisive driver of AI citation is the *expertise layer* — what the company
knows beyond the government/primary source (interpretation, edge cases, "what actually happens
in practice," practitioner judgement). Holding answerability and structure constant, pages
that add a real expertise layer out-cite pages that merely repackage the official source.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.80 | The apex of the pyramid: engines cite the page that adds knowledge the canonical source lacks; pure repackaging loses to the canonical source itself. |
| Claude | 0.55 | **Partial disagreement on the word "deciding."** I agree an expertise layer helps and can be the differentiator on practice/edge-case queries. But I doubt it is *the* single deciding factor across the board — answerability/extractability (G03) and authority/trust often dominate for plain factual prompts, and engines frequently cite the authoritative source even when a richer page exists. I expect expertise to be decisive on a *subset* of intents (judgement/edge-case/"what happens if"), not universally. **The expertise must be REAL practitioner knowledge, never invented authority.** |

## Divergence note
Gemini 0.80 vs Claude 0.55 → a crux of the pyramid thesis. Tests cleanly only when answerability and entity density are matched, so the expertise layer is the sole varying factor.

## Success metric (resolve by 2027-01-09, post-launch)
- With structure/answerability held constant, the expertise-layer variant is cited in a higher share of probes than the repackaged-official control across ≥2 engines AND is cited preferentially on judgement/edge-case prompts. TRUE if it leads broadly; PARTIAL if the lift is confined to edge-case/"what happens" intents (which would still vindicate the layer but not the word "deciding"); FALSE if no citation lift.

## Measurement
`TRACKING/geo_visibility.csv` — `cited` rates per engine and per prompt-type for expertise vs repackaged variants.

## Status
`open — awaiting live deployment`. Gated on a real, sourced expertise layer.

## Outcome
_TBD._
