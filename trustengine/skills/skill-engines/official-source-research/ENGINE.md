# Official Source Research — Engine Spec

Is every claim traced to a named, dated, official source — or just asserted?


---

# Models, Frameworks & Principles (that govern this engine)

> Each must FIT this engine. If one does not, research a fitting one from books + tier-one papers via `research/openalex.py` and tier it before use (see /department/mfp-fit-rule.md).

# 06 — Models, Frameworks & Principles
## Skill — Official Source Research
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES), each ≥3 entries. Codes reference **MFP-LIBRARY.md**.
## Rebuilt 2026-05-29 against the canonical MFP library. `⟳` = updated with an external citation; `★` = one of the 6 highest-leverage library additions.

---

## MODELS — the data structures and mental models this skill uses

- **M-01 — Verified Fact Model.** Every claim traces to a named, dated official source; nothing publishes that cannot. *Source:* aligns with Google QRG factual-accuracy requirement.
- **M-06 — Source Bank Model.** One row per claim: URL + date + exact quote + plain-English translation — the only approved source of truth for writers. *Source:* internal.
- **M-31 — YMYL Topic Classification.** Pet relocation is YMYL-adjacent (animal welfare, government compliance, large outlays), so this skill carries the maximum proof burden. *Source:* Google QRG (expanded 9/2025).

## FRAMEWORKS — the decision systems and processes

- **F-04 — Source Verification Framework.** Map claim → authority hierarchy → visit in a real browser → extract verbatim quote → screenshot → record status. *Source:* internal; QRG "link to your sources."
- **F-35 — Quarterly Refresh Cadence.** Re-verify the Source Bank against live official URLs every quarter. *Source:* Semrush 2025.
- **F-31 — "Who / How / Why" Self-Assessment Loop.** Each verified row answers who published it, how it was confirmed, why it is authoritative. *Source:* Google Search Central.

## PRINCIPLES — the non-negotiable rules

- **P-07 — Independent Verification.** Verified only when confirmed directly at the official source — never via a competitor or forum repeating it. *Source:* QRG.
- **P-08 ⟳ — Government Sites Break — Re-verify Every 90 Days.** Cadence is quarterly. *Source:* Semrush 2025 quarterly-refresh data; Ahrefs July 2025 AI-freshness study.
- **P-09 — Community Data Is Not Official Data.** Community facts are documented but never asserted as official; conflicts recorded as `Conflicting`. *Source:* QRG YMYL standards.

---
*Skill-map row:* M-01, M-06 · F-04 · P-07, P-08⟳, P-09 — extended to meet the ≥3-per-section standard with genuinely-used codes M-31, F-35, F-31. Full citations in `MFP-LIBRARY.md`.
