# B07 — THE CRUX: a comprehensive long-form guide out-ranks a concise answer-first page

**Claim:** For this high-anxiety route intent, a long, comprehensive "definitive technical
documentation" page out-ranks (and out-converts) a concise, answer-first "cheat-sheet" page.

This is the central disagreement between Gemini's blueprint and our current architecture.

## Forecasts (locked 2026-06-09)
| Source | P(TRUE) | Rationale |
|---|---|---|
| Gemini | 0.80 | "Search engines want comprehensive answers"; concise pages get out-depthed by heavy-hitters. |
| Claude | 0.45 | **Genuine disagreement.** Gemini conflates *comprehensive* (covers all intents) with *long* (more words). I bet the winner is **concise-but-complete + strong trust + the missing intents added (B01/B02)** — not bloating existing sections. Helpful-content systems can penalise padding; answer-first concision is a GEO asset for extraction. I expect "add missing intents" to win and "lengthen existing copy" to be neutral-to-negative. |

## Divergence note
Gemini 0.80 vs Claude 0.45 → **highest-information bet in the ledger.** Per the "mix it up" rule, build BOTH:
1. **Variant C (concise):** current answer-first architecture + missing intents (heat, cost, airlines) added tightly.
2. **Variant L (long):** Gemini's full comprehensive-guide blueprint.
3. Optional **Variant M (mix):** answer-first lead + progressive depth on demand.

## Success metric (resolve by 2027-01-09, post-launch)
- Head-to-head on a matched query set over a 4-week probe + ranking window: which variant ranks higher AND drives more quote-form conversions. Scored on BOTH ranking and conversion; PARTIAL if they split (e.g. long ranks but concise converts).

## Measurement
`TRACKING/experiments.csv` (variant A/B) + `TRACKING/live_tracker.csv` + conversion events + citation probes.

## Status
`open — awaiting live deployment`. This is the flagship experiment.

## Outcome
_TBD._
