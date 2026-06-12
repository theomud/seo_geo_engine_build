# AI Citation Readiness — Engine Spec

How likely AI answer engines are to quote this page — and exactly what to fix.


---

# Models, Frameworks & Principles (that govern this engine)

> Each must FIT this engine. If one does not, research a fitting one from books + tier-one papers via `research/openalex.py` and tier it before use (see /department/mfp-fit-rule.md).

# 06 — Models, Frameworks & Principles
## Skill — AI Citation & Generative Engine Optimisation
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES), each ≥3 entries. Codes reference **MFP-LIBRARY.md**.
## Built 2026-06-01 against the canonical MFP library. `★` = one of the 6 highest-leverage additions.

---

## MODELS — the data structures and mental models this skill uses

- **M-22 ★ — GEO/AEO/LLMO Framework.** The governing model: optimise for **citation, not ranking**.
  Generative engines assemble one answer and attribute it to a few sources, so the unit of victory
  is being cited, not placed. This is the model the whole skill operationalises. *Source:* Aggarwal
  et al., "GEO: Generative Engine Optimization," KDD 2024 (Princeton / IIT Delhi / Georgia Tech /
  Allen Institute for AI) — the peer-reviewed primary source.
- **M-23 ★ — Kalicube Entity Home Model.** A single canonical point of reference that Google and the
  LLMs cross-check to understand and trust an entity. This is why the skill builds one dedicated
  Entity Home (not the scattered homepage) with identical naming everywhere — fragmentation stops
  the engines consolidating the entity, and an unidentified entity isn't cited. *Source:* Jason
  Barnard, Kalicube (Entity Home + Corroboration + Signposting).
- **M-24 ★ — E-E-A-T Four-Pillar Trust Model.** Experience, Expertise, Authoritativeness, and —
  at the centre — Trust. Citeability in a YMYL niche depends on it: cited sources, named
  credentials, and verifiable facts are what make an engine willing to attribute a high-stakes
  answer to you. *Source:* Google Search Quality Rater Guidelines, rev. 11 Sept 2025.

*Also used:* **M-30** Algorithmic Trinity (Index + Knowledge Graph + LLM — the three systems an
entity must satisfy) · **M-31** YMYL Topic Classification (pet import is health/safety/financial —
maximum proof bar). *Sources:* Jason Barnard / 3stepsdigital; Google QRG.

## FRAMEWORKS — the decision systems and processes

- **F-21 — RAG / Open-World Citation Loop.** The operating loop behind monitoring: generative
  engines retrieve and cite open-web sources, so the process is publish → observe what's cited →
  strengthen the answer → re-check. It is why the weekly monitor has an *action loop*, not just a
  scoreboard. *Source:* Mersel.ai GEO 2026 Guide (vendor — directional).
- **F-28 — sameAs / Wikidata / Wikipedia Linked-Data Stack.** The framework for corroborating the
  entity: the `sameAs` array ties the Entity Home to its verified profiles so Google and the LLMs
  confirm one identity across the web. *Source:* Schema.org; WordLift.
- **F-31 — "Who / How / Why" Self-Assessment Loop.** Google's people-first content test — who made
  it, how, and why — applied to every optimised page so the citeable answer is also a trustworthy
  one (the E-E-A-T check in practice). *Source:* Google Search Central, "Creating Helpful,
  Reliable, People-First Content."

*Also used:* the answer-box + FAQ + entity pattern is this skill's internal method, governed by
F-21 (the loop) + F-28 (the entity corroboration) and the two on-page principles below.

## PRINCIPLES — the non-negotiable rules

- **P-17 — Direct-Answer-First Structure.** A quotable answer to the query in the opening (first
  100 words) — what an engine can lift. Burying the answer hands the citation to whoever answered
  first. *Source:* Coseom 2026; Aggarwal et al. KDD 2024 (~27% higher AI citation for
  direct-answer structure).
- **P-18 — Statistics + Source Citations + Structured Formatting → up to 40% AI-visibility lift.**
  The research-backed trifecta every page must carry: a named statistic, a cited source, and
  machine-readable structure (FAQ schema). It is the measurable core of the Functional Quality
  Threshold. *Source:* Aggarwal et al., KDD 2024 (Princeton GEO paper).
- **P-29 — Designate a Single Entity Home (not the homepage).** One dedicated, stable page is the
  canonical reference; pointing the engines at a scattered homepage fragments the identity.
  *Source:* Kalicube Knowledge Panel Course.
- **P-30 — Consistency of Naming/Description Across Platforms.** The same canonical name and
  one-line description everywhere (pages, schema, `sameAs` profiles, NAP) so the engines consolidate
  rather than split the entity. *Source:* Kalicube / WordLift consensus.
- **P-48 — Track Citation Frequency Across ChatGPT / Perplexity / Gemini Weekly.** The monitoring
  rule: a weekly check of the target queries across the engines, with the action loop. *Source:*
  AI-Magicx 2026 GEO guide.

*Also used:* **P-47** Validate Schema with the Rich Results Test (before publishing) · **P-32**
Author bio + credentials on every YMYL page (the E-E-A-T signal that supports citation).

---
*Skill-map row (MFP-LIBRARY.md):* M-22★, M-23★ · F-21 · P-17, P-18 — extended to the
≥3-per-section house standard with the START-prompt codes M-24★, F-28, P-29, P-30, P-48 (all
genuinely used). The three components — entity definition (M-23/F-28/P-29/P-30), direct-answer
structure (P-17/P-18), and citation monitoring (P-48/F-21) — are governed by the GEO model (M-22)
and the YMYL trust bar (M-24/M-31). Full citations in `MFP-LIBRARY.md`.
