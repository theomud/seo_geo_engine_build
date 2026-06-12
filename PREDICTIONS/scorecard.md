# Scorecard — who's calling it right

Updated 2026-06-09. Brier on strategy bets is computed only on resolution (most are post-launch).

## Fact layer (resolved now)

| Source | Checkable claims | Correct | Incorrect | Partial | Accuracy |
|---|---|---|---|---|---|
| Gemini (Pakistan, 2026-06-09) | 8 (F01–F08) | 5 | 2 | 1 | ~69% |

**Read:** Gemini is strong on verifiable MOCCAE specifics but produced two confident errors
(F06 min-age, F07 cabin-vs-baggage) that contradict our screenshots. **Treat Gemini as a fact
*lead generator*, not a source of record.** F09/F10 are unverified leads in the claim-audit queue.

## Strategy layer (pending — post-launch)

Forecasts locked for B01–B07. None resolved yet (need live + indexed + measured).

**Biggest divergences — the highest-information experiments to build first:**
| Bet | Gemini | Claude | Gap | What it tests |
|---|---|---|---|---|
| B07 (flagship) | 0.80 | 0.45 | 0.35 | comprehensive long guide vs concise answer-first |
| B06 | 0.65 | 0.35 | 0.30 | does a freshness date alone move rankings |
| B03 | 0.80 | 0.55 | 0.25 | does deepening short FAQs help or bloat |

Where we agree (B01 heat, B02 operational keywords): build with confidence — low experimental value, high expected payoff.

## Forecaster running totals

| Source | Resolved bets | Mean Brier | Calibration | Notes |
|---|---|---|---|---|
| Gemini | 0 | — | — | facts: ~69% |
| Claude | 0 | — | — | — |

**GEO bets G01–G05 now filed** (from the GEO fan-out). Biggest GEO divergence: **G04** (expertise
is *the deciding* factor) — Gemini 0.80 / Claude 0.55, gap 0.25. Lowest divergence / shared
conviction: **G03** (answer-first blocks out-cite narrative) — both above 0.72, build with confidence.

## Poker view

All 11 open strategy bets are also staked as chips on `poker-table.md`. Stacks even at 1000 each
(nothing resolved). Total chips in play ≈ 418/side; the fattest pots — B07 (110), B06 (100), B03 (90),
G04 (90) — mark the highest-information experiments. Theo has an open seat on any hand.
