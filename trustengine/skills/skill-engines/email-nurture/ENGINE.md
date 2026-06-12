# Email Nurture (capture readiness) — Engine Spec

Can the page even start a nurture relationship — capture the lead with a value-first offer?


---

# Models, Frameworks & Principles (that govern this engine)

> Each must FIT this engine. If one does not, research a fitting one from books + tier-one papers via `research/openalex.py` and tier it before use (see /department/mfp-fit-rule.md).

# 06 — Models, Frameworks & Principles
## Skill — Email Nurture Sequences
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES), each ≥3 entries. Codes reference **MFP-LIBRARY.md**.
## Built 2026-06-01 against the canonical MFP library. `★` = one of the 6 highest-leverage additions.

---

## MODELS — the data structures and mental models this skill uses

- **M-02 — Fear Hierarchy Model.** The customer's fears, ranked by depth/severity. This is what
  *orders* the sequence: deepest first (confiscation, the 3am fear), out to the practical
  (documents, timing, cost, airline), closing on trust. One fear per email maps one rung of the
  ladder to one email. *Source:* maps to Protection Motivation Theory's severity hierarchy
  (Rogers 1975).
- **M-20 ★ — Protection Motivation Theory.** The engine of every email: a fear appeal produces
  *action* only when the threat is paired with **response efficacy** (a step that works) and
  **self-efficacy** (a step the reader can take). So each email is a threat-then-coping pair —
  the named fear, then the verified, sourced answer that resolves it. Fear without a credible
  path produces avoidance, not booking. *Source:* Rogers 1975, *Journal of Psychology*; Tanner,
  Hunt & Eppright 1991, *Journal of Marketing* 55(3).
- **M-21 ★ — Cialdini's 7 Principles of Persuasion.** The sequence earns the booking with
  **Authority** (verified, cited facts), **Reciprocity** (six emails of genuine help before any
  ask), and **Commitment/Consistency** (each small reply — "checklist", "costs" — moves the
  reader toward the booking). Used as the ethical 6-principle spine, never as manipulation.
  *Source:* Cialdini, *Influence* (1984), *Pre-Suasion* (2016).

*Also used:* **M-32** Hierarchy of Effects (Awareness → Consideration → Conversion) — why the
booking ask comes only at Email 7, after trust is built. *Source:* Vakratsas & Ambler 1999,
*Journal of Marketing.*

## FRAMEWORKS — the decision systems and processes

- **F-22 — 7-Email Nurture Framework.** The spine of the deliverable: seven emails from first
  enquiry to booking — enough to resolve the real fear ladder without becoming noise. Defines
  the count, the one-fear-per-email rule, and the help-first balance. *Source:* Blogrator 2026;
  Smartlead playbook.
- **F-23 — AIM Welcome Sequence.** The arc: **A**wareness (Email 1 — name the deepest fear, set
  the tone), **I**nterest (Emails 2–6 — resolve each practical fear with a sourced answer),
  **M**ove (Email 7 — the help-first booking ask). It is why the deepest fear opens and the only
  sales ask closes. *Source:* Val Geisler / FixMyChurn.
- **F-18 — AIDA.** The scaffold *inside* each individual email — Attention (the named fear in
  real words), Interest/Desire (the verified answer that lowers it), Action (the one help-first
  CTA). A per-email writing scaffold, not a buyer-behaviour claim. *Source:* E. St. Elmo Lewis,
  1898.

*Also used:* **F-32** Funnel-Stage Copy Matching — fear-acknowledging openings early in the arc,
a clear (still help-first) ask at the conversion end. *Source:* LeadEnforce 2025.

## PRINCIPLES — the non-negotiable rules

- **P-19 — 80/20 Value-to-Pitch Rule.** The help-first contract: the sequence gives far more
  than it asks. Six emails hand over real value (checklist, timeline, cost sheet, airline map,
  embargo check) before Email 7 makes the only booking ask. *Source:* Sequenzy nurture playbook.
- **P-20 — Mid-Week Send Timing (Tue–Thu).** The cadence rule: Email 1 sends immediately (while
  the enquiry is warm), Emails 2–7 snap to the next Tue–Thu. This audience opens and reads
  mid-week. *Source:* Questline Digital.
- **P-21 — One Primary CTA Per Email.** Each email asks for exactly one thing — "reply
  'checklist'", "send your flight date". A second CTA splits the action and lowers response; the
  one CTA is always the help-first offer (only Email 7's is the booking ask). *Source:* HubSpot
  lead-nurture guide.

*Also used:* **P-04** Fear-Acknowledging Not Fear-Exploiting (name the fear, then resolve it —
never name it and push) · **P-05** One Fear Per Email (one threat-coping pair per email) · **P-15**
Deliver Then Document (every factual line is documented from a cited source — C-ID or honest
hedge).

---
*Skill-map row (MFP-LIBRARY.md):* — · F-22, F-23 · P-19, P-20, P-21 — extended to the
≥3-per-section house standard with the START-prompt codes M-20★, M-21★, M-02, F-18, P-04 (all
genuinely used). The map lists no Models for this skill; the three Models above (M-02 ordering,
M-20 the threat-coping engine, M-21 the ethical persuasion spine) are the mental models the
sequence actually runs on. Full citations in `MFP-LIBRARY.md`.
