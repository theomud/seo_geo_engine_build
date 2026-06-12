# G01 — Experience/proprietary-data content gets cited more than regulations-only

**Claim:** A page that wraps the official rules in real company experience and *real*
proprietary data (e.g. our own observed processing times, cost actuals, failure-mode logs)
gets cited by AI engines (ChatGPT, Perplexity, Gemini, AIO) more often than a page that only
restates the government regulations. This is the base of Gemini's "GEO pyramid" thesis.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.85 | Core of the pyramid thesis — AI engines reward the layer the source can't get from the gov site itself; experience is the differentiator. |
| Claude | 0.68 | Directionally agree: distinctive, hard-to-replicate content is a genuine citation magnet, and regulations-only pages compete with the primary source (which engines often cite instead). But many AI answers still cite the canonical/authoritative page for a pure-rules query, so the lift is real but not universal — it shows up most on "in practice / what actually happens" intents. **Hard constraint: the proprietary data must be REAL and verifiable; a fabricated stat invalidates the test and breaches the truth policy.** |

## Divergence note
Gemini 0.85 vs Claude 0.68 → meaningful gap. Build BOTH where feasible: a regulations-only control page and an experience+data variant on a matched topic, then probe identical prompts.

## Success metric (resolve by 2027-01-09, post-launch)
- Over a fixed prompt set run across ≥2 AI engines, the experience/proprietary-data variant is cited (brand mentioned AND/OR `source_url` = our page) in a strictly higher share of probes than the regulations-only control. TRUE if it wins on ≥2 of the engines; PARTIAL if it splits or only narrowly leads.

## Measurement
`TRACKING/geo_visibility.csv` — compare `cited` / `brand_mentioned` rates per `engine` for the two page URLs on a matched `prompt` set.

## Status
`open — awaiting live deployment`. Requires the experience layer to be backed by real, sourced data before probing.

## Outcome
_TBD._
