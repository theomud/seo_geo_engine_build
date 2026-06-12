---
Status: complete (PROVEN 47/47) — 2026-06-01
Area: skill-content-intelligence-monitoring
Depends on: skill-content-intelligence-monitoring/files/01-what-is-this-skill.md, skill-content-intelligence-monitoring/README.md
Feeds into: skill-content-intelligence-monitoring/files/03-how-to-verify-it.md, skill-content-intelligence-monitoring/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Running the 12-stream monitor and the RICE queue by hand — before any of it is automated

---

## Why manual first

You can automate the *collection* (a webhook fires, an API returns numbers) but the two acts that
make the system trustworthy are human judgements: **scoring a signal's Impact and Confidence**, and
**deciding it's real before you act**. *(Library: P-01 Manual Before Automated; P-07 Independent
Verification.)* Do those by hand until the rubric is calibrated, and the automation later just
*applies* a judgement you've already proven sound. Run a full cycle on paper first; the engine is
the same cycle, faster.

Three things on the desk before you start:
1. **The 12-stream list** — what you watch, how often, and how you'd detect a change (the config).
2. **The verified source of truth** — the Source Bank (C-IDs), the competitor gap matrix, the
   community research, the customer profile. Every signal must point back to one of these.
3. **The RICE rubric** — the factor scales and bands from `data/rice-scoring-template.md`.

---

## Step 1 — Set up the 12 streams (what to watch, how often, how)

Write down each stream with a **cadence** and a **collector method**. Regulatory streams run fastest
because being wrong there = real harm; content streams can run weekly or monthly.

| # | Category | Stream | Cadence | How (manual → later automated) |
|---|----------|--------|---------|--------------------------------|
| 1 | Regulatory | MOCCAE import portal | 48h | Visualping page-change watch → webhook |
| 2 | Regulatory | Destination country authorities | weekly | Visualping watch per destination |
| 3 | Regulatory | Airline pet/cargo policies | weekly | Visualping watch per carrier |
| 4 | Regulatory | UAE-gov broader signals | weekly | Google Alerts (manual review) |
| 5 | Competitor | Competitor content changes | weekly | Visualping + a SerpApi SERP check |
| 6 | Competitor | Trust-Score re-audit | monthly | re-run the competitor scoring (Anthropic) |
| 7 | Competitor | Competitor pricing/positioning | weekly | Reddit + Alerts (named-fee mentions) |
| 8 | Search/AI | GSC daily performance | daily | Search Console (position/click drops) |
| 9 | Search/AI | AI-citation tracking | weekly | the AI-citation skill's 10-query check |
| 10 | Community | Community fear signals | weekly | Reddit PRAW + Facebook groups (verbatim quotes) |
| 11 | Community | Review monitoring | weekly | Google Business Profile + manual scan |
| 12 | Market | Industry signals | weekly | Google Alerts (manual review) |

*(Library: F-10 Monthly Content Intelligence Cycle; F-39 Position-Drop Alerting; P-48 weekly
AI-citation tracking.)* The four regulatory streams are first on purpose — that's where P-02 lives.

---

## Step 2 — Record each detected signal with its source

When a stream surfaces something, write it as one signal with a **finding** (what changed / what's
true) and a **source** (the verifiable origin — a C-ID, the gap matrix, a named community quote, the
profile). *(Library: P-07.)* A signal with no traceable source is a rumour, not a signal — either
verify it into one or drop it. This is the line that keeps the queue honest: the engine literally
stores a `source` field on every signal, and the audit re-traces all of them.

> Example: *"Source Bank C-019/C-003/C-010 verified 2026-05-28 — the 90-day re-verify clock (P-08)
> ends 2026-08-26."* Source: the Source Bank + the P-08 rule. Traceable, so it's a real signal.

---

## Step 3 — Score the signal with RICE (the four questions)

For each signal, answer four questions and compute `(R × I × C) ÷ E`. *(Library: M-27; F-12.)*

1. **Reach (1–10)** — how many customers or pages does this touch? 10 = every import customer; 1 = a
   single edge case.
2. **Impact (0.25 / 0.5 / 1 / 2 / 3)** — if you ignore it, how bad is the worst case? **3 = massive**
   (wrong regulation → a pet denied entry, the YMYL bar); 2 = high; 1 = medium; 0.5 = low; 0.25 =
   minimal. *(Library: P-02 Wrong Information Causes Real Harm.)*
3. **Confidence (0.5–1.0)** — how sure are we it's real and correct? **1.0 = an official source**
   (MOCCAE/airline page); ~0.8 = a strong community pattern; 0.5 = a single unverified report.
   *(Library: P-07 — confidence is capped by the source; community can't exceed ~0.8.)*
4. **Effort (1–5)** — relative days to act. 1 = a same-day page edit; 5 = a new comprehensive asset.

> Worked: the re-verification signal → `(9 × 3 × 0.9) ÷ 1 = 24.3`. High reach, massive impact,
> official-source confidence, one day to act → it tops the queue.

---

## Step 4 — Route the score to a service level

Map the number to an SLA with the bands. *(Library: F-05; F-12.)* **Don't argue the band — let the
number decide.** That is the entire point of the engine.

| RICE score | Band | Act |
|------------|------|-----|
| ≥ 20 | TODAY | same-day (regulatory / time-critical) |
| 15 – 19.99 | 48HR | within 48 hours |
| 8 – 14.99 | THIS WEEK | within the week |
| < 8 | MONTHLY | enters the monthly content cycle (F-10) |

---

## Step 5 — Write the weekly intelligence report

Produce one report per cycle with three parts: (a) the **RICE table** sorted by score; (b) the
**action queue** grouped by SLA band (TODAY first), each item showing its finding *and* its source;
(c) the **12-stream connection status** — for every stream, is it connected (key set) or *awaiting
connection*? An unconnected live stream contributes **no** signal and says so. *(Library: F-05
Dashboard-to-Action — a dashboard that doesn't end in an action queue is just decoration.)*

---

## Step 6 — Run the action loop and re-verify on cadence

Work the queue top-down: clear TODAY, then 48HR, then the week. The **re-verification signals
re-enter the queue at full impact every 90 days** — government sites change silently, so a fact
verified today is a signal again in 90 days. *(Library: P-08 Re-verify Every 90 Days; F-35 Quarterly
Refresh Cadence.)* Then the next cycle starts: streams surface new signals, RICE scores them, the
queue re-sorts. The monitor never "finishes"; it cycles.

---

## Worked example — the first real cycle (7 signals)

| Signal | R | I | C | E | RICE | Band |
|--------|---|---|---|---|------|------|
| Source-Bank re-verification due (C-019/C-003/C-010, 90-day clock) | 9 | 3 | 0.9 | 1 | **24.3** | TODAY |
| Summer heat-embargo window open (today is 2026-06-01) | 7 | 3 | 0.9 | 1 | **18.9** | 48HR |
| AI-citation gap — publish the 4 GEO pages (9/9 omit) | 9 | 3 | 0.85 | 2 | **11.47** | THIS WEEK |
| Market leader DKC still omits the confiscation fear | 8 | 3 | 0.8 | 2 | **9.6** | THIS WEEK |
| Recurring community price-gouging complaints | 6 | 2 | 0.8 | 1 | **9.6** | THIS WEEK |
| Etihad fee conflict ($399 vs ~$1,500) still active | 5 | 2 | 0.8 | 1 | **8.0** | THIS WEEK |
| Breed-restriction guide gap (lower urgency) | 6 | 1.5 | 0.7 | 2 | **3.15** | MONTHLY |

Each row traces to a source (Source Bank, gap matrix, community quotes, profile §16) and each band
is the number's verdict, not a preference. That table *is* the manual output — and it's exactly what
the engine reproduces.

---

## What you must not do

- **Do not act on the loudest signal.** Score it; a loud competitor grumble (RICE 8) waits behind a
  quiet regulatory change (RICE 24.3).
- **Do not hand-assign a band.** Compute the score and let `route()` decide. The discipline is the
  product.
- **Do not record a sourceless signal.** No C-ID / quote / matrix reference → it's a rumour; verify
  or drop it.
- **Do not score community-only signals above ~0.8 Confidence.** Only an official source earns 1.0.
- **Do not fabricate a live reading.** If the stream isn't connected, the report says *awaiting
  connection* and the signal count is honest.
- **Do not let a verified fact age past 90 days unchecked.** P-08 — it re-enters the queue at full
  impact.

---

## Output of this manual phase

A weekly intelligence report with every signal RICE-scored, sourced, and routed to an SLA band, plus
the 12-stream status. That output is the real deliverable (`data/weekly-intelligence-report.md`) and
the exact thing File 04's automation reproduces — the engine applies the same `rice_score()` +
`route()` you just did by hand, and the human keeps the two jobs automation can't have: calibrating
Impact/Confidence and deciding a signal is real.
