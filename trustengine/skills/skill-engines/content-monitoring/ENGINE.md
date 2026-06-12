# Content Monitoring (freshness) — Engine Spec

Does the page show it's kept current — visible dates, recent facts, review markers?


---

# Models, Frameworks & Principles (that govern this engine)

> Each must FIT this engine. If one does not, research a fitting one from books + tier-one papers via `research/openalex.py` and tier it before use (see /department/mfp-fit-rule.md).

# 06 — Models, Frameworks & Principles
## Skill — Content Intelligence Monitoring
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES), each ≥3 entries. Codes reference **MFP-LIBRARY.md**.
## Built 2026-06-01 against the canonical MFP library. `★` = one of the highest-leverage codes for this skill.

---

## MODELS — the data structures and mental models this skill uses

- **M-27 ★ — ICE / PIE / RICE Prioritisation Models.** The governing model: score every signal
  `(Reach × Impact × Confidence) ÷ Effort` so the action queue is sorted by *consequence*, not
  volume. Reach/Impact/Confidence push a signal up, Effort pushes it down — a cheap, certain,
  high-consequence fix outranks an expensive, speculative one, automatically. This is the model the
  whole engine operationalises (`rice_score()` + `route()`). *Source:* Optimizely & Hotwire (CXL
  Live); RICE popularised by Intercom (Sean McBride).
- **M-31 ★ — YMYL Topic Classification.** Pet import is "Your Money or Your Life" — health, safety,
  and money. This is *why* the Impact scale tops out at 3 = real harm (a pet denied entry) and why
  the four regulatory streams run fastest: in a YMYL niche a decayed page doesn't just underperform,
  it hurts someone. *Source:* Google Search Quality Rater Guidelines; expanded 9/2025.
- **M-41 — SERP-Feature Tracking Model.** Search visibility is no longer one ranked list — it's
  organic + AI Overviews + Featured Snippet + PAA + Local Pack. The search/AI streams (8, 9) track
  this whole surface, which is why a position drop *and* a lost AI citation are both monitorable
  signals that feed the same queue. *Source:* Semrush / Ahrefs documentation.

*Also used:* **M-30** Algorithmic Trinity (Index + Knowledge Graph + LLM — the three systems a
change can ripple through) · **M-47** NAP Consistency (the review/entity surface stream 11 watches).
*Sources:* Jason Barnard / 3stepsdigital; BrightLocal.

## FRAMEWORKS — the decision systems and processes

- **F-05 ★ — Dashboard-to-Action Framework.** The framework that makes this a system, not a
  dashboard: every monitored signal must terminate in a *decision* (a band + an SLA), not a chart. A
  dashboard that doesn't end in an action queue is decoration; F-05 is why the report's centrepiece
  is the action queue grouped by service level. *Source:* internal; Google Looker Studio GSC+GA4
  template.
- **F-10 — Monthly Content Intelligence Cycle.** The recurring loop the 12 streams run on: collect →
  score → act → re-verify → repeat. It defines the cadence layer (48h / daily / weekly / monthly per
  stream) and is where the lowest-RICE signals land for the monthly review. *Source:* aligned to the
  GSC + GA4 dual-source pattern (Google Search Central).
- **F-12 — Content Update Priority Matrix.** The matrix that decides *which* page gets attention when
  several signals compete — the routing logic `route()` implements. The matrix decides, not the
  mood. *Source:* internal.
- **F-39 — Position-Drop Alerting Workflow.** The detection pattern behind the search streams: watch
  Search Console for position/click-pattern drops and raise them as scored signals rather than
  waiting for a quarterly review. *Source:* Search Console performance-pattern detection.

*Also used:* **F-35** Quarterly Refresh Cadence (Semrush 2025: quarterly refreshes yield 42% better
results than annual — the cadence backbone) · **F-21** RAG / Open-World Citation Loop (the
publish → observe → strengthen → re-check loop the AI-citation stream feeds). *Sources:* Semrush;
Mersel.ai.

## PRINCIPLES — the non-negotiable rules

- **P-02 ★ — Wrong Information Causes Real Harm.** The principle that sets the Impact scale: in this
  niche, wrong information = a pet denied entry. It's why regulatory signals carry Impact 3 and run
  on the fastest cadence, and why the whole skill exists — a *quietly wrong* page is the worst state,
  because someone trusts it. *Source:* operational expression of YMYL (Google QRG).
- **P-07 — Independent Verification.** Every signal must trace to a verifiable source, and Confidence
  is capped by that source — a community-only signal can't exceed ~0.8; only an official source earns
  1.0. It's why the engine stores a `source` field on every signal and the audit re-traces all of
  them; a sourceless signal is a rumour, not a signal. *Source:* Google QRG, "link to your sources."
- **P-08 — Government Sites Break — Re-verify Every 90 Days.** The cadence rule that keeps the source
  of truth fresh: a verified fact re-enters the queue at full Impact every 90 days, because
  government and airline pages change silently. It's the top signal in the first cycle (the 90-day
  clock on C-019/C-003/C-010). *Source:* consistent with Semrush quarterly-refresh data and Ahrefs'
  "AI assistants prefer fresher content" study (2025).
- **P-48 — Track Citation Frequency Across ChatGPT / Perplexity / Gemini Weekly.** The rule behind
  the AI-citation stream (9): a weekly check of the target queries across the engines, raised as a
  scored signal with an action loop when a citation is lost. *Source:* AI-Magicx 2026 GEO guide.

*Also used:* **P-01** Manual Before Automated (run a full cycle by hand to calibrate the rubric
before trusting the engine) · **P-09** confidence is capped by source verifiability (the calibration
ceiling on community signals). *Sources:* internal; Google QRG.

---
*Skill-map row (MFP-LIBRARY.md):* M-27★ · F-05★, F-10, F-12, F-39 · P-02★, P-07, P-08, P-48 —
extended to the ≥3-per-section house standard with M-31★, M-41 and the also-used codes (all
genuinely used). The two components — the 12-stream monitor (F-10/F-39/M-41/P-48) and the RICE
decision engine (M-27/F-05/F-12) — are governed by the YMYL harm bar (M-31/P-02) and the freshness
cadence (P-08/F-35), with P-07 keeping every signal sourced. Full citations in `MFP-LIBRARY.md`.
