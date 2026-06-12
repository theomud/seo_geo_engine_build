# B05 — Named-author trust architecture lifts E-E-A-T ranking

**Claim:** Adding a real named relocation specialist (bio, credentials, verification stamp,
compliance signal) instead of the generic "team" byline will lift rankings on this YMYL topic.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.70 | High-anxiety, legal/financial risk → trust signals matter; no author bio today. |
| Claude | 0.60 | Agree E-E-A-T helps on YMYL, but **hard constraint**: `site.yml` deliberately uses the team byline because we will not invent a fake person (truth policy penalises fake authorship). This bet only fires IF a real named specialist with verifiable credentials exists. Without one, it's unbettable. |

## Blocker
Requires a real person + verifiable `same_as` (LinkedIn/credential). Until then this is a *capability gap*, not a test we can run.

## Success metric (resolve by 2027-03-09, post-launch + real author)
- With a real named author live, pages authored by them outrank equivalent team-bylined pages on a matched query set. PARTIAL if weak/mixed.

## Measurement
`TRACKING/experiments.csv` (author A/B) once a real specialist is onboarded.

## Status
`blocked — needs a real named specialist (do not fabricate)`.

## Outcome
_TBD._
