# 06 — Models, Frameworks & Principles
## Skill — Website Audit
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES). Codes reference **MFP-LIBRARY.md**.
## Built 2026-06-01 against the canonical MFP library. `★` = highest-leverage codes for this skill. Each entry is written for THIS skill, not the generic library definition.

---

## MODELS — the data structures and mental models this skill uses

- **M-04 — Risk Continuum Model.** Before a single dimension is scored, the auditor places the site on
  the risk continuum (Low → Maximum) — and that placement *is* the proof bar the whole audit applies.
  A maximum-risk site like DKC must cite an official source for every claim, so the same uncited fee
  that would be a minor note on a low-risk site is a scored failure on Dimension 3 here.
- **M-05 — Trust Score Model.** This is the engine of **Dimension 2**: the 10-point page trust score
  (fear-first, sourced, route, steps, timeline, cost, mistakes, visuals, help-CTA, proof) becomes a
  /10 audit dimension, one point per item. It turns "does this page feel trustworthy?" into ten
  yes/no checks the auditor can defend with a quote, and anchors the audit to the same scale DKC was
  benchmarked on (8.0/10).
- **M-10 — Ten-Criteria Quality Model.** This governs **Dimension 5 (Editorial Quality)**: the site's
  copy is scored against the ten editorial criteria and the seven weak-AI patterns. It lets the audit
  say *why* a page reads as thin or hyped — "criterion 4 fails: the opening is a 'in today's world'
  filler line" — rather than a vague "the writing could be better."
- **M-13 — Proof Density Model.** This is the lens for **Dimensions 3, 7 and 9**: proof must sit
  *beside* every claim, not in a testimonials ghetto. The auditor scores how densely the site backs
  claims with sources, real screenshots, and evidence imagery — a page asserting "trusted experts"
  with no proof beside it loses points wherever density is measured.
- **M-24 ★ — E-E-A-T Four-Pillar Trust Model.** This is the parent model the entire 13-dimension
  framework hangs on: every dimension is, ultimately, measuring Experience, Expertise,
  Authoritativeness, or Trust. It is also the direct lens for **Dimension 13 (Market Position)**,
  where the auditor judges whether the site demonstrates the four pillars better or worse than the
  market it competes in.
- **M-27 — RICE Prioritisation Model.** This governs the **action plan**: every gap the 13 dimensions
  surface is scored `(Reach × Impact × Confidence) ÷ Effort` so the report ends in one ordered queue,
  not thirteen separate to-do lists. It is what lets the audit name a *single* most-important action
  (for DKC, the airport-confiscation page) instead of overwhelming the owner with everything at once.

## FRAMEWORKS — the decision systems and processes

- **F-03 — Trust Score Competitor Scoring.** This is the operational process behind **Dimension 2**
  and the optional **competitor comparison**: the repeatable 10-point scoring procedure, applied to
  the audited site and to named rivals on the same scale. It is what makes "you score 8/13 where your
  competitor scores 5" a defensible, like-for-like claim rather than an assertion.
- **F-05 — Dashboard-to-Action Framework.** This governs the **shape of the action plan**: a dashboard
  of 13 scores is worthless unless it terminates in prioritised actions, so the audit always converts
  scores → ranked actions → a named next page. It is the rule that stops the report being a scorecard
  and makes it a plan a business can execute.
- **F-06 — Seven-Step Editorial Process.** This is the operational backbone of **Dimension 5**: the
  auditor runs the site's copy through the editorial process (the Who/How/Why self-assessment and the
  weak-pattern sweep) to score editorial quality with specifics. It keeps the editorial dimension a
  process, not a taste call.
- **F-08 — Proof Interstitial Framework.** This governs how **Dimensions 4, 7 and 9** are scored:
  proof should be interleaved through the page at the moment each claim is made, not bolted on at the
  end. The auditor scores whether proof appears *where the reader's doubt arises* — a claim about
  border safety should have its official-source proof right there, not three sections later.
- **F-11 — Forty-Five-Check Audit Framework.** This is the meta-framework the whole skill is built on:
  the same multi-layer, evidence-or-zero discipline that audits a *skill* is here pointed outward to
  audit a *website*. It is why every dimension demands quoted evidence and why an independent
  re-checker re-scores blind — the audit is itself audited.

## PRINCIPLES — the non-negotiable rules

- **P-02 — Wrong Information Causes Real Harm.** This makes **Dimension 3** non-negotiable: on a
  maximum-risk site, an uncited or wrong fact is not a style issue, it is the failure that gets a pet
  denied entry. The auditor scores a confident-but-unsourced regulation claim as a serious gap, not a
  rounding error.
- **P-03 — Proof Over Promise.** This governs how *every* dimension score is assigned: a score is only
  valid if it is backed by proof quoted from the live site. "Dimension 1: 3/10" is not a finding;
  "3/10 — the homepage opens 'Where family flies together' and never names a fear" is.
- **P-04 — Fear-Acknowledging Not Fear-Exploiting.** This governs **Dimensions 1 and 6**: the auditor
  scores not just *whether* the site addresses fear but *how* — acknowledging the fear and resolving
  it with verified help scores well; manufacturing urgency to push a sale scores badly. It is the line
  between a trustworthy page and a manipulative one.
- **P-07 — Independent Verification.** This governs the entire audit methodology: the auditor's claims
  about the site must themselves be verifiable, so every quote must be re-findable on the live page and
  a second party re-scores blind. An audit nobody can reproduce is just an opinion.
- **P-13 — The Hormozi Test.** This governs **Dimension 9 (Authority Assets)**: a case study or guide
  scores only if it passes the test — could an AI with no access to the business have written it? DKC's
  generic "expert team" copy fails; a documented, specific relocation case with real outcomes passes.
- **P-22 — Trust Is the Centre.** This confirms the **weighting and the verdict**: of E-E-A-T's four
  pillars, Trust is the one the others collapse without, so the trust-bearing dimensions (1, 2, 3, 6,
  9) carry the audit's verdict. A site can be fast, pretty, and well-architected and still fail the
  audit if it does not earn trust.

---
*Skill-map row (MFP-LIBRARY.md):* M-04, M-05, M-10, M-13, M-24★, M-27 · F-03, F-05, F-06, F-08, F-11 ·
P-02, P-03, P-04, P-07, P-13, P-22 — the 13 audit dimensions are each governed by one or more of these
(D2←M-05/F-03; D3←P-02/M-13/P-07; D4/7/9←F-08/M-13; D5←M-10/F-06; D1/6←P-04; D9←P-13; D13←M-24/P-22),
the proof bar is set by M-04, the action plan by M-27/F-05, and the whole instrument is F-11 pointed at
a live site, with P-03/P-07 keeping every score evidenced. Full citations in `MFP-LIBRARY.md`.
