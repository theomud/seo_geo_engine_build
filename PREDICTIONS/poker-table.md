# The Poker Table — bet your edge, settle on reality

The ledger says *what* each forecaster predicts. The table says *how much they're willing to put
on it.* Poker players don't just call the odds — they size bets by edge and live or die by results.
Same here.

---

## The rules

- **Bankroll:** every forecaster starts with **1000 chips**. (Gemini, Claude — and Theo can take a
  seat any time by dropping his own probability on any hand; the pot re-sizes.)
- **The pot = the disagreement.** A hand's pot is `round(200 × |p_A − p_B|) + 40`. The more two
  players disagree, the bigger the pot — because one of them is clearly wrong, and that's where the
  money is. Agreement hands are small antes; the crux hands are where the stack moves.
- **Each player commits pot/2 at stake** when the hand is dealt (chips conserved, escrowed until the
  board runs out).
- **Settlement = Brier.** When the hand resolves, each player's `Brier = (their p − outcome)²`.
  **Lower Brier takes the whole pot.** Ties chop it. Confidently-wrong is the felt-your-stack
  moment: a 0.85 on something that resolves FALSE = Brier 0.72, you're paying.
- **No re-railing.** Probabilities lock when the hand is dealt (ledger filing date). You can't
  re-buy a better line after the flop.

**Why this is better than a scoreboard:** it forces *conviction sizing.* It's easy to say "I think
concise wins." It's another thing to put 55 chips in the middle against Gemini's 55. The pots tell
you, at a glance, which experiments to build first — **follow the money.**

---

## Leaderboard (2026-06-09)

| Player | Bankroll | Chips committed (in play) | Hands | Pots won | Net |
|---|---|---|---|---|---|
| Gemini | 1000 | 418 | 11 | 0 | 0 |
| Claude | 1000 | 418 | 11 | 0 | 0 |

Even stacks — nothing has resolved (most hands need the site live + indexed + probed). The fact
layer already ran, though: on checkable Pakistan facts Gemini went **5-correct / 2-wrong / 1-partial**
(see `fact-checks/`). If we'd been playing facts for chips, Gemini would already be down on F06 and F07.

---

## The big hands on the table (build these first — biggest pots, biggest disagreement)

### 🂡 B07 — "Comprehensive long guide vs concise answer-first"  · POT 110 (the main event)
- **Gemini:** 0.80 — bets long/comprehensive wins; "search engines want comprehensive answers."
- **Claude:** 0.45 — bets concise-but-complete + missing-intents-added wins; says Gemini conflates
  *comprehensive* with *long*.
- **Board that resolves it:** build Variant L (long) and Variant C (concise) of the same route, run
  4-week rank + citation + conversion probe. Pot to whoever's Brier is lower.
- **Read:** this is the philosophical crux of the whole project. Whoever wins this hand wins the
  house style.

### 🂮 B06 — "A freshness date alone moves rankings" · POT 100
- **Gemini:** 0.65 · **Claude:** 0.35. Date-only A/B, content held constant.

### 🂭 B03 — "Deepening short FAQs helps (vs bloats)" · POT 90
- **Gemini:** 0.80 · **Claude:** 0.55. Deepened vs concise FAQ variant, same query set.

### 🂫 G04 — "The expertise layer is *the deciding* GEO factor" · POT 90
- **Gemini:** 0.80 · **Claude:** 0.55. Expertise variant vs repackaged-official control, structure held constant.

---

## The rest of the table

| Hand | Question | Gemini | Claude | Pot | Who's pot-committed |
|---|---|---:|---:|---:|---|
| B01 | Summer-heat content captures intent | 0.85 | 0.80 | 50 | both long — small pot, build it anyway |
| B02 | Operational keywords (airlines+cost) win | 0.80 | 0.75 | 50 | both long |
| B04 | Bolded FAQ answers win snippets | 0.75 | 0.65 | 60 | both long |
| B05 | Named-author trust lifts ranking | 0.70 | 0.60 | 60 | **blocked** — needs a real specialist (no fabrication) |
| G01 | Experience > regulations-only for citation | 0.85 | 0.68 | 74 | both long |
| G02 | Entity density lifts citation | 0.80 | 0.62 | 76 | both long |
| G03 | Answer-first blocks out-cite narrative | 0.82 | 0.72 | 60 | both long — Claude's strongest GEO conviction |
| G05 | Case-studies cited for how/what-happens | 0.78 | 0.60 | 76 | both long |

---

## Theo's open seat

Want skin in the game? Drop your own probability on any hand and you're in the pot 3-way — settled
the same way (lowest Brier takes it). The most interesting seat is **B07**: if your gut says one of
us is bluffing, put chips on it. I'll re-size the pot and log your line.

> The pot is the tell. Where Gemini and I have stacked the most chips against each other — B07, B06,
> B03, G04 — that's where reality has the most to teach us. Build those variants first.
