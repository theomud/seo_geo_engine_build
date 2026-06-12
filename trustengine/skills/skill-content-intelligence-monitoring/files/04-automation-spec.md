---
Status: complete (PROVEN 47/47) — 2026-06-01
Area: skill-content-intelligence-monitoring
Depends on: skill-content-intelligence-monitoring/files/02-how-to-do-it-manually.md, skill-content-intelligence-monitoring/files/03-how-to-verify-it.md
Feeds into: skill-content-intelligence-monitoring/engines/engine-monitoring-system.py
---

# Skill · File 04 — Automation Spec
## What the monitoring engine collects, scores, routes and writes — and what stays human

---

## Automation target

**This is the most automatable skill in the program (Automation 5/5).** The collection (webhooks and
API polls), the scoring (`rice_score()`), the routing (`route()`), and the report generation are all
machine work — the engine runs a full cycle end to end and writes
`data/weekly-intelligence-report.md` with no human in the loop. What stays human is the part that
makes the scores *mean* something: **calibrating each signal's Impact and Confidence**, and
**deciding a borderline signal is real** before it enters the queue. *(Library: M-27; F-05; P-07;
P-02.)*

What gets automated:
- **Collection** — Visualping webhooks (streams 1–3, 5), SerpApi (5), Anthropic re-audit (6), Reddit
  PRAW (7, 10), GSC API (8), Perplexity (9), GBP API (11), Google Alerts review (4, 12). Each live
  collector is real in shape and gated on its env key.
- **Scoring** — `rice_score(reach, impact, confidence, effort)` → one comparable number.
- **Routing** — `route(score)` → TODAY / 48HR / THIS WEEK / MONTHLY.
- **Report generation** — the RICE table (sorted), the action queue (grouped by SLA), the 12-stream
  connection status; written deterministically so it reproduces on re-run.

What stays manual:
- **Calibrating Impact and Confidence** — how bad is the worst case (is it real harm, P-02?), how
  sure are we (official source vs community, P-07)? A human sets R/I/C/E; the engine does the
  arithmetic.
- **Deciding a signal is real** — a webhook fires on a cosmetic page edit as readily as a regulation
  change; a human confirms it's a genuine signal before it's scored.
- **Working the action queue** — the engine says *what* to do first; a human does it.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| The 12-stream config (id, category, cadence, method, env key) | dataclass list | this skill |
| Each signal's R/I/C/E and source | per-signal record | a human, against the rubric |
| Live-collector readings (optional) | API/webhook payloads | GSC / Reddit / Perplexity / GBP / Visualping |
| `PROJECT_ROOT`, `MONITOR_REPORT_DATE`, the optional API keys | env | `.env` |

The engine is **forbidden** from inventing a signal or a live reading — a stream with no key is
recorded *awaiting connection* and contributes nothing.

---

## Outputs

| Output | Destination |
|--------|-------------|
| RICE decision table (sorted by score) | `data/weekly-intelligence-report.md` |
| Action queue grouped by SLA band | same report |
| 12-stream connection status (connected / awaiting / manual) | same report |
| Per-cycle band counts | stdout (`TODAY:n · 48HR:n · …`) |

The engine never declares a priority by hand — it computes the score, routes the band, and reports
the coverage honestly.

---

## Engine flow

```
load STREAMS config (12 streams: id, category, name, cadence, method, env_key)
for each signal (human-supplied R, I, C, E, finding, source):
    score = (R * I * C) / E          # rice_score(); raises if effort <= 0
    band  = route(score)             # >=20 TODAY · >=15 48HR · >=8 THIS WEEK · else MONTHLY
collect_live(STREAMS):
    for each stream with an env_key:
        key set  -> "CONNECTED"      # a real run calls the collector here and appends signals
        key unset-> "awaiting connection"   # never fabricates a signal
    streams with no key -> "manual/alerts"
generate_report(): RICE table (sorted) + action queue (by band) + 12-stream status
write data/weekly-intelligence-report.md   (fixed REPORT_DATE -> reproducible)
```

## The RICE core (deterministic)
```python
def rice_score(reach, impact, confidence, effort):
    if effort <= 0:
        raise ValueError("effort must be > 0")
    return round((reach * impact * confidence) / effort, 2)

def route(score):
    if score >= 20: return ("TODAY", "act today")
    if score >= 15: return ("48HR",  "within 48 hours")
    if score >= 8:  return ("THIS WEEK", "within this week")
    return            ("MONTHLY", "monthly review")
```

The honesty rule lives in `collect_live()`: a live collector with no key set is **skipped and
logged** "awaiting connection — no data this cycle"; it never fabricates a signal. The signals scored
in the first report are all real, each traceable to a verified in-repo source.

---

## Worked example (the first cycle)

Fed the 7 verified signals, the engine: scores the re-verification signal `(9×3×0.9)÷1 = 24.3` →
TODAY; the summer-embargo signal `18.9` → 48HR; the AI-citation gap `11.47`, the confiscation gap
`9.6`, the price-gouging pattern `9.6`, the Etihad conflict `8.0` → THIS WEEK; the breed-restriction
gap `3.15` → MONTHLY. `collect_live()` finds no keys set → all 10 live streams *awaiting connection*,
streams 4 and 12 *manual/alerts* → "0/10 live connected this cycle", stated in the report. It writes
the report; a re-run produces a byte-identical file.

---

## Test phase (one cycle, then PAUSE)

Run the engine on the 7 verified signals; confirm the 7 scores re-compute, the 4 bands match
`route()`, and the 12-stream status is honest (0/10 connected). Re-run and diff — confirm byte-for-
byte reproducibility. Only after the env keys + Visualping webhook are set does a cycle produce live
detected changes; pre-connection it records the verified-signal baseline. **Then pause for the
audit.**

---

## Audit (after a build)

A sub-agent re-computes every RICE score, re-derives every band, re-traces every source, and re-runs
the engine to confirm reproducibility. A typed (non-computed) score, a chosen (non-routed) band, a
sourceless signal, a fabricated live reading, or a non-reproducible report is a **hard fail**
regardless of the rest. *(Library: P-07 Independent Verification.)*

---

## When automation must hand back to humans

- **Calibrating Impact and Confidence** — always human; the engine does arithmetic, not judgement.
- **Deciding a borderline signal is real** — a human confirms before it's scored.
- **Confirming a regulatory change is what it appears to be** — re-verify against the official
  source (the source-research skill) before acting.
- **Working the queue** — the engine ranks; a person acts.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| RICE scoring + routing + report generation | milliseconds (local arithmetic + string build) |
| Live collection (when connected) | a handful of API calls/webhooks per stream per cadence — cents/week |
| Human cost | weekly: set R/I/C/E for new signals, confirm they're real, work the queue |

---

## Files in this skill (created by the build)

```
skill-content-intelligence-monitoring/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   ├── weekly-intelligence-report.md   ← engine-generated real output
│   └── rice-scoring-template.md         ← the decision framework
└── engines/
    └── engine-monitoring-system.py      ← the runnable engine (config + RICE + routing + report)
```
