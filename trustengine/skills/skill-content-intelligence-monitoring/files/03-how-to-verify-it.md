---
Status: complete (PROVEN 47/47) — 2026-06-01
Area: skill-content-intelligence-monitoring
Depends on: skill-content-intelligence-monitoring/files/02-how-to-do-it-manually.md
Feeds into: skill-content-intelligence-monitoring/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that prove the report is engine-scored, fully sourced, honest about coverage, and reproducible

---

## Why verification matters

A monitoring system fails in ways that look like success. A report can *feel* thorough — long,
confident, full of findings — yet hand-assign the priorities to match someone's gut (so the queue is
opinion, not consequence), carry a finding no source backs (so the queue acts on a rumour), quietly
present a live reading from a stream that was never connected (so the queue trusts a fabrication), or
shift between runs (so it can't be audited at all). Each failure is invisible until it hurts you.
Verification proves the four things that make the output a *decision system*: **the engine scored
it, every signal is sourced, the coverage status is honest, and the report reproduces exactly.**

---

## Gate set A — per-signal integrity (run on each signal)

| Gate | Passes when |
|------|-------------|
| A1 · Engine-scored | The RICE score is computed by `rice_score()` from its R/I/C/E, not typed in by hand; `(R × I × C) ÷ E` re-computes to the printed value. *(M-27)* |
| A2 · Routed by band | The SLA band is assigned by `route()` from the score, not chosen; the score falls inside the band's range. *(F-05, F-12)* |
| A3 · Sourced | The signal carries a verifiable in-repo source — a C-ID, the gap matrix, a named community quote, or the profile. No sourceless signal. *(P-07)* |
| A4 · Calibrated | Confidence ≤ 0.8 for community-only signals (only official sources earn 1.0); Impact 3 only where being wrong = real harm. *(P-02, P-07)* |

A1/A2 catch the hand-tuned queue; A3 catches the rumour; A4 catches the inflated score that games
the band.

---

## Gate set B — the threshold check

The output clears the README's Functional Quality Threshold, counted across the cycle's signals:

1. **Every signal RICE-scored and routed by the engine** — **7/7**.
2. **Every signal traceable to a verified in-repo source** — **7/7**.
3. **All 12 streams represented with an honest connection status** — **12/12** (0/10 live connected
   this cycle, stated, not hidden).
4. **The report reproduces byte-for-byte on re-run** — fixed cycle date, deterministic output.

Any gate unmet = the output is not done. A hand-assigned band, a sourceless signal, a fabricated live
reading, or a report that drifts between runs each fail the threshold on their own.

---

## The independent re-check (the core check)

A second party (a sub-agent or a different human) verifies **blind to the builder's notes**:

- **Re-compute every RICE score** from the R/I/C/E in the table — does `(R × I × C) ÷ E` equal the
  printed value? A mismatch means the score was typed, not computed (A1 fail).
- **Re-derive every band** from the score against the rubric — does the printed band match what
  `route()` would assign? A mismatch means the band was chosen (A2 fail).
- **Re-trace every signal to its source** — open the C-ID / gap matrix / quote / profile reference
  and confirm it exists and says what the signal claims. A dead reference is a sourceless signal (A3
  fail).
- **Check each Confidence against its source type** — a community-only signal scored above 0.8, or
  an Impact 3 on something that isn't real harm, fails A4.
- **Re-run the engine and diff the report** — any byte difference (other than a deliberately changed
  `MONITOR_REPORT_DATE`) fails the determinism gate.

This is the gate polish can't fake: the arithmetic either reproduces or it doesn't, and a source
either exists or it doesn't.

---

## The audit sub-agent — verifying the verifier

After the build, a sub-agent re-runs A1–A4 on every signal, re-computes the scores and bands,
re-traces the sources, and re-runs the engine to confirm the report reproduces. *(Library: P-07
Independent Verification.)* Pass threshold: **7/7** scored & routed, **7/7** sourced, **12/12**
streams honest, reproducible. A typed score, a chosen band, a sourceless signal, a fabricated live
reading, or a non-reproducible report is a **hard fail** — a strong score elsewhere does not rescue
it.

---

## The post-connection check (the live-stream step)

The gates above are everything the skill *controls* with no external dependency — the deterministic
core. The thing they're built to feed — a live monitor catching real changes — can only be verified
**after the streams are connected**: set the env keys + the Visualping webhook, run a cycle, and
confirm that a detected change (a GSC position drop, a new competitor page, a fresh community thread)
is captured, RICE-scored by the same engine, and routed into the same queue. *(Library: F-39
Position-Drop Alerting; P-48; F-21 the open-world citation loop.)* This is flagged **NOT YET
CONFIRMED** until the keys are set — the monitoring analogue of the independence test. The
deterministic threshold fully passes before this step; this step is what turns a scored report into
a live monitor.

---

## Worked check (the first cycle)

A blind re-checker: A1 — re-computes `9 × 3 × 0.9 ÷ 1 = 24.3`, `7 × 3 × 0.9 ÷ 1 = 18.9`, … all 7
match the printed scores ✔; A2 — 24.3 ≥ 20 → TODAY, 18.9 ∈ [15,20) → 48HR, the four mid-scores ∈
[8,15) → THIS WEEK, 3.15 < 8 → MONTHLY, all match ✔; A3 — opens C-019/C-003/C-010, the gap matrix
(9/9), the 7Ssisi / IrbisKat / unnnabear quotes, profile §16, all present ✔; A4 — the community
signals sit at 0.8, the Impact-3s are all real-harm regulatory/confiscation items ✔; determinism —
re-runs the engine, diff is empty ✔. Result: **7/7, 7/7, 12/12, reproducible** → threshold
**passes**; live streams **NOT YET CONFIRMED** pending keys.

---

## What downgrades / forces a rewrite

- A RICE score that doesn't re-compute from its R/I/C/E (typed, not engine-scored).
- A band that doesn't match `route()` (chosen, not routed).
- A signal with no traceable in-repo source (a rumour in the queue).
- A community-only signal scored above 0.8 Confidence, or Impact 3 on a non-harm item.
- A live reading shown for a stream that was never connected (a fabrication).
- A report that changes between runs with no deliberate date change (not auditable).

---

## Output of the verification phase

Every signal is engine-scored, engine-routed, sourced, and calibrated; all 12 streams report honest
status; the report reproduces byte-for-byte; an independent re-check reproduces 7/7, 7/7, 12/12. That
verified discipline is what makes File 04's automation safe — the engine applies `rice_score()` +
`route()` exactly as the manual cycle did, and the live-stream outcome is tracked honestly until the
keys are connected.
