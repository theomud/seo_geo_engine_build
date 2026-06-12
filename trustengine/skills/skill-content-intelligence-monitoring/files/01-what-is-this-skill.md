---
Status: complete (PROVEN 47/47) — 2026-06-01
Area: skill-content-intelligence-monitoring
Depends on: skill-content-intelligence-monitoring/README.md
Feeds into: skill-content-intelligence-monitoring/files/02-how-to-do-it-manually.md, skill-content-intelligence-monitoring/files/04-automation-spec.md
---

# Skill · File 01 — What This Skill Is
## Niche-agnostic definition of Content Intelligence Monitoring

---

## The problem this skill solves

Every page you publish is true on the day you publish it and decaying from the next. The
regulation it cites gets amended; the airline rewrites its cargo policy; the fee it quotes goes up;
a competitor publishes the answer you were about to own; a community thread surfaces a fear nobody
has addressed. None of this announces itself. The page keeps sitting there looking authoritative
while it slowly stops being correct — and in a high-stakes niche, a page that is *quietly wrong* is
worse than no page at all, because someone trusts it. Wrong information here means a pet denied
entry at the border.

The naive responses both fail. Monitoring **nothing** means you find out a regulation changed when
a customer's pet is already stuck. Monitoring **everything and reacting to all of it** means you
drown — a hundred alerts a week, no way to tell the one that matters from the ninety-nine that
don't, and the quiet regulatory change (the most important signal) lost under the loud competitor
noise. Content Intelligence Monitoring solves both: it **watches broadly across 12 streams** so
nothing important is missed, and it **scores every signal by consequence** so you act on the few
that matter and let the rest wait.

---

## What this skill produces

| Output | What it is |
|--------|-----------|
| The monitoring engine | A runnable system: 12-stream config + RICE scoring + routing + report generation |
| The weekly intelligence report | Engine-generated: every signal RICE-scored, sorted, routed to a TODAY/48HR/week/month queue |
| The RICE scoring template | The decision framework — formula, factor scales, action bands, calibration rules |

The rule that makes it scorable: **every detected signal is RICE-scored by the engine and routed to
a service level in code; every signal traces to a verified source; and re-running the engine
reproduces the report exactly.** No hand-assigned priorities, no fabricated signals.

---

## The core idea — score by consequence, not by volume

*(Library: M-27 ICE/PIE/RICE Prioritisation.)* A monitor that surfaces signals without ranking them
just relocates the overwhelm. The breakthrough is a single scoring rule applied to everything:

```
RICE = (Reach × Impact × Confidence) ÷ Effort
```

**Reach** (how many customers/pages a signal touches), **Impact** (how bad the worst case is — a
pet denied entry is the maximum), and **Confidence** (how sure we are it's real and correct — an
official source earns more than a community rumour) push a signal *up*; **Effort** (days to act)
pushes it *down*. A cheap, certain, high-consequence fix outranks an expensive, speculative one —
automatically. `route()` then files the score into a service level: ≥20 act **today**, 15–19.99
within **48 hours**, 8–14.99 **this week**, below 8 the **monthly cycle**. *(Library: F-05
Dashboard-to-Action; F-12 Content Update Priority Matrix.)*

---

## The two components

1. **The 12-stream monitor** *(Library: F-10 Monthly Content Intelligence Cycle; F-39 Position-Drop
   Alerting; P-48 weekly AI-citation tracking.)* Four **regulatory** streams (MOCCAE, destination
   authorities, airline policies, broad UAE-gov signals — the ones where being wrong = real harm,
   so they run fastest), three **competitor** streams (content changes, monthly Trust-Score
   re-audit, pricing/positioning), two **search/AI** streams (GSC daily performance, AI-citation
   tracking), and three **community/market** streams (Reddit fear signals, reviews, industry
   chatter). Each has a cadence and a collector method.
2. **The RICE decision engine** *(Library: M-27; F-05; F-12.)* Every signal — wherever it comes from
   — passes through the same `rice_score()` + `route()` pair. This is what makes the output a
   *decision*, not a feed: the queue is sorted by consequence, and the rule is the same for a
   regulatory alert and a community grumble.

---

## A worked example (the proof niche)

The first real cycle (2026-06-01) scored **7 signals**. The top of the queue is a regulatory one:
three Source-Bank facts (C-019 titer required, C-003 the 500 AED release fee, C-010 the 90-day
permit) were verified 2026-05-28, and the 90-day re-verification clock (P-08) runs out 2026-08-26 —
`rice_score(9, 3, 0.9, 1) = 24.3` → **TODAY**. Just below it, the summer heat-embargo window is open
*as of today* → **18.9 / 48HR**. Genuine but lower-urgency moves — the AI-citation gap (11.47), the
confiscation-page gap the market leader leaves (9.6), recurring community price-gouging complaints
(9.6), the Etihad fee conflict (8.0) — land in **THIS WEEK**. The breed-restriction guide gap, real
but cheap to defer, scores **3.15** and correctly drops to the **monthly cycle**. The engine, not a
person's mood, decided every one of those placements.

---

## How it differs from neighbouring skills

| Skill | Owns |
|-------|------|
| Official Source Research | *originating* a verified fact and its C-ID (the source of truth) |
| Search Console Intelligence | the search-performance data feed (one input stream) |
| AI Citation & GEO | optimising a page to be cited, and its weekly citation check (one input stream) |
| **Content Intelligence Monitoring** | watching **all** the streams at once and **deciding what to act on first** |

The other skills produce facts and pages and individual feeds. This skill is the layer above them:
it watches everything they touch *plus* the regulators, competitors, and community, and turns the
combined firehose into a ranked action queue. It doesn't originate facts or write pages — it decides
which page needs attention today.

---

## Why this is a standalone skill

1. **It's a decision system, not a dashboard.** *(Market uniqueness 4/5.)* Anyone can set up alerts;
   the value is the RICE engine that turns alerts into a consequence-ranked queue, so the quiet
   high-stakes signal beats the loud trivial one.
2. **It's the freshness defence for a YMYL niche.** *(P-02; P-08.)* In a market where wrong = real
   harm, "monitor and re-verify on a cadence" isn't optional hygiene — it's the thing that stops a
   decayed page from hurting someone.
3. **It's portable and teachable.** Every business has signals that move and limited hours to react;
   list the streams, score by `(R × I × C) ÷ E`, route by band. Only the streams and sources change.

---

## In scope / out of scope

**In scope.** Defining the 12 streams (what to watch, cadence, collector); scoring every detected
signal with RICE; routing it to a service level; generating the weekly intelligence report; the
re-verification cadence that keeps the source of truth fresh (P-08).

**Out of scope.** Originating the verified facts themselves (the source-research skill owns the
C-IDs); writing or rewriting the pages an action queue points at (the content/copy skills); the
internal architecture of any single feed (GSC, AI-citation) beyond consuming it as a stream.

---

## What "good" looks like

- **Every signal RICE-scored and routed by the engine** — `(R × I × C) ÷ E` in code, a band from
  `route()`, never a hand-assigned priority.
- **Every signal traceable to a verified source** — a C-ID, the gap matrix, a real quote, the
  profile; zero fabricated signals.
- **All 12 streams represented with honest status** — an unconnected live collector contributes no
  data and says so.
- **A reproducible report** — fixed cycle date, byte-identical on re-run, therefore auditable.
- **The queue sorted by consequence** — the maximum-risk regulatory signal on top, the deferable
  content gap on the monthly cycle.

This skill is complete when the engine produces a weekly report meeting all four threshold gates and
the audit reproduces it. Connecting the live streams is the post-connection step the monitor runs
once the keys are set.
