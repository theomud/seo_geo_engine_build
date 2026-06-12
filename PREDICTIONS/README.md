# PREDICTIONS — the probability-based "who called it right" ledger

When two advisors (Gemini, Claude, a human SEO, a future model) disagree about what will
rank or convert, we don't argue. We **write down each prediction as a falsifiable bet with a
probability**, ship the test, then score everyone. Over time, calibration tells us whose
judgment to weight.

This is Tetlock-style forecasting applied to our SEO/GEO engine. It is the resolution layer
for the 5-architecture test and the citation-probe loop.

---

## Two layers — never mix them

| Layer | What it is | When it resolves | Folder |
|---|---|---|---|
| **Fact-checks** | Checkable claims of *fact* (a fee, a rule, a timeline) | **Now** — against official/screenshot-verified sources | `fact-checks/` |
| **Strategy bets** | Probabilistic claims about what will *rank/convert* | **Later** — once live, indexed, and measured | `strategy-bets/` |

**A fact is not a bet.** "The permit is 200 AED" is true or false today; you don't assign it
60% and wait. It goes to `fact-checks/`, scored against the [truth policy](../GOVERNANCE/TRUTH_POLICY.md)
(official source + screenshot). Unverified factual claims are routed to the claim-audit queue —
**they never enter published copy on confidence alone.** This is the firewall that caught two
Gemini errors on day one (see `fact-checks/gemini-pakistan-2026-06-09.md`).

A **strategy bet** ("deepening the FAQs will win us PAA boxes") is genuinely uncertain and
*should* carry a probability. That's the real ledger.

---

## How a strategy bet works

Each file in `strategy-bets/` is one bet with:

- **Claim** — a single falsifiable statement.
- **Forecasts** — each source's probability (0–1) that the claim resolves TRUE.
- **Success metric** — the exact, measurable resolution condition.
- **Measurement** — which `TRACKING/*.csv` or citation probe resolves it.
- **Resolve by** — a date.
- **Outcome** — TRUE/FALSE/PARTIAL once measured, with the evidence.
- **Brier** — per source, computed on resolution.

### Scoring (Brier)

`Brier = (probability − outcome)²`, where outcome = 1 (TRUE) or 0 (FALSE). **Lower is better.**
- Confidently right (0.9 on a TRUE) → 0.01. Excellent.
- Confidently wrong (0.9 on a FALSE) → 0.81. Punished hard.
- Hedging (0.5) → always 0.25. The cost of no opinion.

A source's score = mean Brier across its resolved bets. We also watch **calibration**
(do its 70%s come true ~70% of the time?) and **resolution** (does it take strong positions?).

### "Mix it up"

When two sources diverge a lot (e.g. Gemini 0.80 vs Claude 0.45 on the crux bet), that bet is
the **highest-information experiment** — build BOTH variants and let reality referee. Synthesis
("mix") is allowed as its own forecaster: a blended variant can be a third entry.

---

## Resolution discipline (so we don't cheat)

- Probabilities are **locked when filed** — no editing a forecast after the fact. Corrections
  go in as a new dated forecast, leaving the original visible.
- Most bets **cannot resolve until the site is live, indexed, and measured** — our own content
  confidence notes say exactly this. Until then: `status: open — awaiting live deployment`.
- A bet with no measurable success metric is not a bet. Rewrite it or drop it.

## Files

- `ledger.csv` — every prediction, machine-readable, one row each.
- `scorecard.md` — running tally per source.
- `poker-table.md` — the bets staked as chips: pots sized by disagreement, settled by Brier. Where
  the biggest pots sit (B07, B06, B03, G04) is where to build experiments first. **Theo has an open seat.**
- `bankroll.csv` — chip stacks per player.
- `fact-checks/` — checkable claims, scored now.
- `strategy-bets/` — the probabilistic forecasts (B-series = SEO, G-series = GEO), scored later.

## Related (the GEO build this ledger measures)

- `../GEO/geo-scoring-rubric.md` — the 0–10 GEO score the bets are scored against.
- `../GEO/geo-content-audit-2026-06-09.md` — where our real pages sit on the GEO pyramid.
- `../GEO/proprietary-knowledge-we-already-have.md` — citable operational knowledge we already hold.
- `../GEO/proprietary-data-capture-plan.md` — what to log now to reach elite-tier GEO honestly.
- `../audit/claims/gemini-conflicts-2026-06-09.md` — factual conflicts queued for official re-verification.
