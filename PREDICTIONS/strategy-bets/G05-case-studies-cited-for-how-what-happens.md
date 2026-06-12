# G05 — Case-studies/outcomes content gets cited for "how/what-happens" queries

**Claim:** Pages built around real case studies and outcomes (anonymised real relocations:
what was done, what went wrong, how long it took, what it cost, how it resolved) get cited by
AI engines for "how does X work / what happens if / what should I expect" queries more than
rules-or-overview pages without outcome narratives.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.78 | Outcome/case-study content is a pyramid rung; it uniquely answers process- and consequence-shaped queries the gov source can't. |
| Claude | 0.60 | Agree case studies are well-matched to "what happens / how did it go" intents and supply the lived detail engines like to quote. Caveats: the win is intent-specific (won't help pure "what is the fee" lookups), and the benefit depends on the case studies being concrete, structured, and **genuinely real/anonymised — fabricated case studies are an immediate truth-policy breach and void the bet.** |

## Divergence note
Gemini 0.78 vs Claude 0.60 — moderate gap, mostly about how broad the effect is vs how intent-specific.

## Success metric (resolve by 2027-01-09, post-launch)
- On a "how / what-happens / what-should-I-expect" prompt set, the case-study/outcomes page is cited in a higher share of probes than a matched rules/overview page across ≥2 engines. PARTIAL if it leads only on the most narrative ("how did it go") prompts.

## Measurement
`TRACKING/geo_visibility.csv` — `cited` rates per engine on the process/consequence prompt set, case-study page vs overview page.

## Status
`open — awaiting live deployment`. Requires real, anonymised case studies before probing.

## Outcome
_TBD._
