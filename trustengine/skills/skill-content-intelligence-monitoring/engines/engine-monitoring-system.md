# Engine — Content Intelligence Monitoring
## Spec for the 12-stream monitor + RICE scoring + routing + report generator (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md` and is realised in
`engine-monitoring-system.py` (the runnable file in this folder). It **collects, scores, routes, and
reports** — it never fabricates a signal and never assigns a priority by hand. Automation 5/5 (the
highest in the program): the collection, the `(R × I × C) ÷ E` scoring, the band routing, and the
report generation are all machine work; what stays human is calibrating each signal's Impact and
Confidence and deciding a borderline signal is real.

## What it does
1. **Hold the 12-stream config** — id, category, name, cadence, method, and (where live) the env key
   each stream needs. Four regulatory (fastest cadence — P-02 lives here), three competitor, two
   search/AI, three community/market.
2. **Score every signal** — `rice_score(reach, impact, confidence, effort)` = `(R × I × C) ÷ E`,
   rounded to 2 dp; raises if effort ≤ 0. *(M-27.)*
3. **Route every score** — `route(score)`: ≥20 TODAY · 15–19.99 48HR · 8–14.99 THIS WEEK · <8
   MONTHLY. The band is the number's verdict, never chosen. *(F-05; F-12.)*
4. **Collect live (honestly)** — `collect_live()` reports each stream's status: a live collector with
   its key set is CONNECTED (a real run calls the collector and appends detected signals); with no
   key it is *awaiting connection* and contributes nothing; a no-API stream is *manual/alerts*. It
   **never fabricates a reading**. *(P-07.)*
5. **Generate the report** — the RICE table (sorted by score), the action queue (grouped by SLA
   band), and the 12-stream connection status, written to `data/weekly-intelligence-report.md`. A
   fixed `REPORT_DATE` (not `Date.now()`) makes it reproduce byte-for-byte on re-run.

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
# a signal's band is route(rice_score(...)) — no hand-assignment anywhere.
```

## Inputs / outputs / guardrails
- **Inputs:** the 12-stream config; each signal's R/I/C/E + finding + source (human-supplied, against
  the rubric); optional live-collector readings; `PROJECT_ROOT`, `MONITOR_REPORT_DATE`, and the
  optional API keys (`VISUALPING_WEBHOOK_URL`, `SERPAPI_KEY`, `ANTHROPIC_API_KEY`, `REDDIT_CLIENT_ID`,
  `GSC_REFRESH_TOKEN`, `PERPLEXITY_API_KEY`, `GBP_API_KEY`).
- **Outputs:** `data/weekly-intelligence-report.md` (RICE table + action queue by SLA + 12-stream
  status) and a stdout band-count line.
- **Never** invents a signal or a live reading (no key → *awaiting connection*); **never** assigns a
  band by hand (always `route(score)`); **never** scores a community-only signal above ~0.8
  Confidence (P-07); **never** uses a wall-clock date (reproducibility).
- **Hand back to human:** calibrating Impact (is it real harm, P-02?) and Confidence (official vs
  community, P-07); deciding a borderline signal is real; working the action queue.
- **Audit:** a sub-agent re-computes every RICE score, re-derives every band from `route()`,
  re-traces every source, and re-runs the engine to confirm byte-for-byte reproducibility. A typed
  score, a chosen band, a sourceless signal, a fabricated live reading, or a non-reproducible report
  is a hard fail.

## Status
**Spec complete; the engine was run and produced the real output (the proof).** The first cycle
(`data/weekly-intelligence-report.md`) scores **7 verified signals** — each traceable to an in-repo
source (Source Bank C-019/C-003/C-010/C-022/C-015/C-001, the content-gap matrix 9/9, real community
quotes, the master profile §16) — into TODAY (1) / 48HR (1) / THIS WEEK (4) / MONTHLY (1), with all
12 streams at honest connection status (0/10 live connected this cycle). Re-running reproduces the
report exactly. Connecting the live streams (set the env keys + Visualping webhook) so detected
changes flow through the same RICE engine is the post-connection step — the engine scores and routes;
the Impact/Confidence judgement and the acting stay human.

## Library codes
M-27 ICE/PIE/RICE Prioritisation · M-31 YMYL · M-41 SERP-Feature Tracking · M-30 Algorithmic Trinity ·
F-05 Dashboard-to-Action · F-10 Monthly Content Intelligence Cycle · F-12 Content Update Priority
Matrix · F-39 Position-Drop Alerting · F-35 Quarterly Refresh · F-21 RAG/Open-World Citation Loop ·
P-02 Wrong Information Causes Real Harm · P-07 Independent Verification · P-08 Re-verify Every 90 Days ·
P-48 Weekly AI Citation Tracking · P-01 Manual Before Automated. Full citations in `MFP-LIBRARY.md`.
