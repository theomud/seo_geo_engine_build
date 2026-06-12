# Prompt Engineering (output clarity) — Engine Spec

Does the page read like a clear, well-briefed output — structured, specific, machine-readable?


---

# Models, Frameworks & Principles (that govern this engine)

> Each must FIT this engine. If one does not, research a fitting one from books + tier-one papers via `research/openalex.py` and tier it before use (see /department/mfp-fit-rule.md).

# 06 — Models, Frameworks & Principles
## Skill — Prompt Engineering
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES), each ≥3 entries. Codes reference **MFP-LIBRARY.md**.
## Rebuilt 2026-05-29 against the canonical MFP library. `⟳` = updated citation.

---

## MODELS — the data structures and mental models this skill uses

- **M-09 ⟳ — Nine-Element Prompt Model** (Context, Role, Objective, Audience, Inputs, Constraints, Examples, Output Format, Quality Criteria). *Update:* show derivation over Google's canonical 4 elements (Role/Task/Context/Format). *Source:* Google Prompt Engineering Guide 2nd ed.
- **M-16 — COSTAR Prompt Model** (Context, Objective, Style, Tone, Audience, Response). *Source:* Sheila Teo, GovTech Singapore (competition winner).
- **M-17 — PICO/TCEPFT Prompt Model.** *Source:* NIH PMC12058339 (PICO applied to prompting).

## FRAMEWORKS — the decision systems and processes

- **F-09 — Nine-Element Prompt Revision Loop.** Plan for 2–3 rounds; each revision states what to change AND what to keep. *Source:* internal; Google "prompting is iterative."
- **F-17 — Agile Prompt Engineering Loop** (iterate → evaluate → refine with relevance/actionability scores). *Source:* Stefan Wolpers, Scrum.org.
- **F-31 — "Who / How / Why" Self-Assessment Loop** (applied to output). The Quality-Criteria element checks who it's for, how it'll be judged, why it works. *Source:* Google Search Central.

## PRINCIPLES — the non-negotiable rules

- **P-14 — Vague Prompt = Generic Output.** Specificity and structure are what move output to 70%+ usable. *Source:* Google — "clarity, specificity, and iteration."
- **P-16 — Ban Generic Language / Prohibit Phrases.** Explicitly forbid filler in the Constraints element. *Source:* Scrum.org Agile Prompt Engineering Framework.
- **P-11 — Real Examples Mandatory.** The Inputs/Examples elements must carry real facts and a real style sample, never placeholders. *Source:* Ogilvy — "no substitute for homework."

---
*Skill-map row:* M-09⟳, M-16, M-17 · F-09, F-17 · P-14, P-16 — extended to ≥3-per-section with genuinely-used codes F-31, P-11. The Minimum Viable Prompt (Context+Role+Objective+Format) is this skill's internal reduction of M-09. Full citations in `MFP-LIBRARY.md`.
