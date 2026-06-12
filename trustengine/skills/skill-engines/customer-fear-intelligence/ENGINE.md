# Customer Fear Intelligence — Engine Spec

Does the page speak to the customer's real fears and the questions they actually ask?


---

# Models, Frameworks & Principles (that govern this engine)

> Each must FIT this engine. If one does not, research a fitting one from books + tier-one papers via `research/openalex.py` and tier it before use (see /department/mfp-fit-rule.md).

# 06 — Models, Frameworks & Principles
## Skill — Customer Fear Intelligence
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES), each ≥3 entries. Codes reference **MFP-LIBRARY.md**.
## Rebuilt 2026-05-29 against the canonical MFP library. `★` = one of the 6 highest-leverage additions.

---

## MODELS — the data structures and mental models this skill uses

- **M-02 — Fear Hierarchy Model.** Ranks customer fears by depth/severity (the 8-rank hierarchy in the customer-profile snapshot). *Source:* maps to PMT severity hierarchy (Rogers 1975).
- **M-03 — Intent × Fear Matrix.** Intent (Col J, 8 types) + fear (Col K) → page type. *Source:* extends Google search-intent classification with PMT threat appraisal.
- **M-20 ★ — Protection Motivation Theory** (severity, susceptibility, response efficacy, self-efficacy). Governs every fear-acknowledging classification. *Source:* Rogers 1975, *J. Psychology*; Tanner, Hunt & Eppright 1991, *J. Marketing* 55(3).

## FRAMEWORKS — the decision systems and processes

- **F-02 — Five-Phase Research Methodology.** Multi-source collection (Autocomplete + PAA + Related + Reddit + Facebook) → intent → fear → sort → validate. *Source:* internal.
- **F-15 — Keyword-to-Content Matrix.** Each keyword row carries intent + fear + volume, routing it to a page priority. *Source:* compatible with HubSpot/Semrush topic-cluster grouping.
- **F-31 — "Who / How / Why" Self-Assessment Loop** (applied to fear statements). Every fear traces to a documented community quote (who said it, where, why it is real). *Source:* Google Search Central.

## PRINCIPLES — the non-negotiable rules

- **P-04 — Fear-Acknowledging Not Fear-Exploiting.** Map the fear to resolve it with a verified solution — never amplify it to sell. *Source:* PMT — fear without efficacy produces denial, not action.
- **P-09 — Community Data Is Not Official Data.** Fear *language* comes verbatim from community sources; the *facts* that resolve it must come from the Source Bank. *Source:* Google QRG YMYL.
- **P-05 — One Fear Per Page.** Each keyword maps to one primary fear; secondary fears become separate rows/pages. *Source:* PMT (one threat-coping pair per appeal).

---
*Skill-map row:* M-02, M-03, M-20★ · F-02, F-15 · P-04 — extended to ≥3-per-section with genuinely-used codes F-31, P-09, P-05. The Fear Formula ("I'm afraid that…") and the 8-intent decision process are this skill's internal operationalisation of M-02/M-03. Full citations in `MFP-LIBRARY.md`.
