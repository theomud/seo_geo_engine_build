# RICE Scoring Template — the decision engine
## Content Intelligence Monitoring · the framework every signal is scored against
## Built 2026-06-01 · implemented in engines/engine-monitoring-system.py (`rice_score()` + `route()`)

---

## Why this exists

A 12-stream monitor produces more signals than anyone can act on at once. Without a scoring
rule, the loudest signal wins instead of the most important one — and in this niche the most
important signal (a regulation changed) is often the quietest. RICE turns every signal into one
comparable number, so the queue is sorted by *consequence*, not by volume. *(Library: M-27
ICE/PIE/RICE Prioritisation; F-05 Dashboard-to-Action; F-12 Content Update Priority Matrix.)*

---

## The formula

```
RICE = (Reach × Impact × Confidence) ÷ Effort
```

| Factor | Scale | What it means here |
|--------|-------|--------------------|
| **Reach** | 1–10 | Share of customers / pages a signal affects. 10 = every import customer; 1 = a single edge case. |
| **Impact** | 0.25 / 0.5 / 1 / 2 / 3 | Minimal → Massive. **3 = massive** (e.g. wrong regulation → a pet denied entry, P-02); 2 = high; 1 = medium; 0.5 = low; 0.25 = minimal. |
| **Confidence** | 0.5–1.0 | How sure we are. **1.0 = official source** (MOCCAE/airline page); ~0.8 = strong community pattern; 0.5 = a single unverified report. |
| **Effort** | 1–5 | Relative days to act. 1 = a same-day page edit; 5 = a new comprehensive asset. |

Reach, Impact and Confidence push a signal **up**; Effort pushes it **down** — a cheap, certain,
high-consequence fix outranks an expensive, speculative one.

---

## The action bands (routing)

`route(score)` maps the number to a service level:

| RICE score | Band | Act |
|------------|------|-----|
| **≥ 20** | TODAY | Same-day — regulatory / time-critical |
| **15 – 19.99** | 48HR | Within 48 hours |
| **8 – 14.99** | THIS WEEK | Within the week |
| **< 8** | MONTHLY | Enters the monthly content cycle (F-10) |

---

## Worked examples (from the first real cycle, 2026-06-01)

| Signal | R | I | C | E | RICE | Band |
|--------|---|---|---|---|------|------|
| Source Bank re-verification due (C-019/C-003/C-010, 90-day cycle) | 9 | 3 | 0.9 | 1 | **24.3** | TODAY |
| Summer heat-embargo window open (today is 2026-06-01) | 7 | 3 | 0.9 | 1 | **18.9** | 48HR |
| AI-citation gap — publish the 4 GEO pages (9/9 competitors omit) | 9 | 3 | 0.85 | 2 | **11.47** | THIS WEEK |
| Market leader DKC still omits the confiscation fear | 8 | 3 | 0.8 | 2 | **9.6** | THIS WEEK |
| Recurring community price-gouging complaints | 6 | 2 | 0.8 | 1 | **9.6** | THIS WEEK |
| Etihad fee conflict ($399 vs $1,500) still active | 5 | 2 | 0.8 | 1 | **8.0** | THIS WEEK |
| Breed-restriction guide gap (lower urgency) | 6 | 1.5 | 0.7 | 2 | **3.15** | MONTHLY |

Each row is reproducible: `rice_score(9, 3, 0.9, 1) == 24.3`. The maximum-risk regulatory signal
(massive impact, official-source confidence, cheap to act) correctly tops the queue; the genuine
but lower-urgency content gap correctly drops to the monthly cycle.

---

## How to score a new signal (the 4 questions)

1. **Reach** — how many customers or pages does this touch? (1–10)
2. **Impact** — if we ignore it, how bad is the worst case? (0.25–3; a pet denied entry = 3)
3. **Confidence** — how sure are we it's real and correct? (0.5–1.0; official source = 1.0)
4. **Effort** — how many days to act? (1–5)

Then `RICE = (R × I × C) ÷ E`, and `route()` files it in the queue. Don't argue the band — let
the number decide; that is the point of the engine. *(Library: F-12 — the matrix decides, not the
mood.)*

---

## Calibration rules (so scores stay honest)

- **Confidence is capped by the source.** A community-only signal cannot be scored above ~0.8,
  however loud — only an official source earns 1.0. *(P-07 Independent Verification.)*
- **Impact 3 is reserved for real harm.** Use it only where being wrong endangers the pet or the
  customer's money (the YMYL bar). *(P-02 Wrong Information Causes Real Harm.)*
- **Effort is honest days, not hope.** A "new definitive guide" is a 4–5, not a 1.
- **Re-score on the cycle.** Re-verification signals re-enter at full impact every 90 days. *(P-08.)*
