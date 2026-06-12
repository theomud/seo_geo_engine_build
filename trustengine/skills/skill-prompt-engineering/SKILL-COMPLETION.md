# SKILL COMPLETION DOCUMENT
## Prompt Engineering — proven on Dubai pet relocation

---

## SKILL IDENTITY

**Skill Name:** Prompt Engineering
**Folder:** skill-prompt-engineering/
**Date Started:** 2026-05-29
**Date Completed:** 2026-05-29 (template library built + tested on the 4 gap pages + 45-check audit PASS)
**Completed By:** Claude Code + human (David)
**Proof Niche:** Dubai pet relocation
**Skill Value Score (confirmed):** 23/25 (Difficulty 3 · Automation 4 · Uniqueness 5 · Commercial 5 · Teachability 5) — highest teachability in the collection

---

## PHASE 1 — MARKET RESEARCH ✅ DONE

**What was researched:** how people use AI (like a search engine → generic output); published prompt frameworks (Google's 4-element core, COSTAR, PICO/TCEPFT); the gap a 9-element system fills.
**Key findings:** the prompt is a **creative brief, not a question**. No published framework combines all 9 elements with content-type templates for a regulated market. The 9-element model is the superset; COSTAR (M-16) and PICO (M-17) are cousins; Google's canonical core is 4.
**Sources:** Google Prompt Engineering Guide 2nd ed.; Sheila Teo / GovTech Singapore (COSTAR); NIH PMC12058339 (PICO). *(Library: M-09, M-16, M-17.)*
**Verdict:** novel + most teachable (5/5).

---

## PHASE 2 — COMMUNITY RESEARCH ✅ DONE (consumed)

Prompt Engineering consumes the niche's fear research to fill the hardest prompt elements (Audience, Context, Inputs, Constraints). The customer-profile snapshot carries the real verbatim language used:
- "without it your dog will be taken away in airport and never give back… Still when I remember I crying" — Muze Gu (→ Audience + opening of the Fear-Resolution prompt)
- "relocation companies are shamelessly charging an insane amount of money" — IrbisKat, 24 upvotes (→ the Cost-Transparency prompt)

**Verdict:** the fears/personas needed to brief the model for this niche are documented and were used directly in the template library.

---

## PHASE 3 — MANUAL VERIFICATION ✅ DONE

**What was done manually:** built a complete **9-element prompt template for all 9 page types by hand** (`data/prompt-template-library.md`), and used the first four as the actual prompts that produced the four universal-gap pages in the proof run.

**Manual test date:** 2026-05-29 · **Time:** ~5–15 min per prompt · **Who:** human + Claude Code

**Real output produced:** `data/prompt-template-library.md` — 9 templates, each filled with real Dubai data, every Verified claim cited by Source Bank C-ID (C-019/010/007/003, C-024/026/028), every Unverifiable claim hedged (C-001), the Etihad conflict surfaced (C-015). Templates 1–4 produced the pages in `../skill-content-structure/data/content-structure-templates/`.

**What failed or surprised (in-the-trenches):** the first titer-cost draft **asserted "the titer test costs 700 AED" as fact.** The miss was in the *prompt*, not the output — Constraints lacked the hedge rule for the Unverifiable C-001. We added the hedge clause and **regenerated** (did not hand-edit the draft). This confirmed the skill's core discipline: below-70%-usable means fix the brief, not the page.

**Verdict:** the 9-element system produces 70%+-usable first drafts of real pages; Constraints + Quality Criteria are the decisive elements.

---

## PHASE 4 — AUTOMATION ⚠️ SPEC COMPLETE (engine not yet built)

**What is specified:** files/04-automation-spec.md + engines/engine-prompt-engineering.md fully define the prompt-evaluation engine (60% automation; evaluates and improves prompts, never writes the brief; refuses to invent; never drops a cited C-ID).
**Engine built:** the **template library was built by hand** (the proof); the **Python evaluation engine is not yet built** — by design, it scales the proven manual pattern.
**Automation level (planned):** 60% (writing the initial brief + final Quality Criteria stay human).

---

## PHASE 5 — AUDIT RESULTS ✅ PASS

**Audit date:** 2026-05-29 (re-audit after fixes) · **Audited by:** independent sub-agent · **Report:** SKILL-AUDIT-REPORT.md

| Layer | Score | Status |
|-------|-------|--------|
| Layer 1 — Skill Completeness | 20/20 | ✅ PASS |
| Layer 2 — Learner Guide | 15/15 | ✅ PASS |
| Layer 3 — Cheatsheet | 10/10 | ✅ PASS |
| **OVERALL** | **45/45** | ✅ PASS |

**Failed checks and fixes applied (first audit 39/45 → re-audit 45/45):**
| Check(s) | What failed | Fix applied |
|----------|-------------|-------------|
| 1 | No engines/ folder | Added engines/engine-prompt-engineering.md |
| 13, 14 | README proof had no real result; score "estimated" | README proof rewritten (PROVEN, date, real output); score confirmed 23/25 |
| 15 | No screenshot of real output | Rendered the template library → data/screenshots/ |
| 27 | Real data missing from some manual sections | Added real Dubai data to MVP / 10-mistakes / 70%-test sections |
| 30 | No real failure/surprise documented | Documented the "700 AED" assertion miss + fix |

---

## REAL OUTPUT EVIDENCE

**Output file:** data/prompt-template-library.md — 9 complete 9-element templates, real Dubai data, cited by C-ID.
**Screenshot:** data/screenshots/prompt-template-library-2026-05-29.png (574 KB rendered library).
**Date:** 2026-05-29 · **Niche:** Dubai pet relocation.

---

## WHAT THIS SKILL PROVED

**Core finding:** a vague prompt returns mush; a 9-element brief — with real cited Inputs and a hedge rule in Constraints — returns a 70%+-usable first draft of a real page. The library compounds: every future page starts from a working prompt.
**What changed from the spec:** the .xlsx-style brief output was realised as the .md template library; the engine consumes Verified-only inputs and is told to hedge Unverifiable ones.
**What others don't do:** no off-the-shelf prompting advice ties Inputs to a verified source bank by C-ID or bakes the hedge rule into Constraints for a regulated market.

---

## LEARNER GUIDE AND CHEATSHEET ✅ BUILT

**Study manual:** guides/prompt-engineering-study-manual.html — the 9 elements, MVP, the 9-element system applied to all 4 gap pages, the revision loop, the 10 mistakes, the 70%-usable test; sidebar nav + progress bar + scroll-spy; real Dubai data + the documented failure; 390px-clean.
**Cheatsheet:** guides/prompt-engineering-cheatsheet.html — 9 elements, MVP, real before/after, revision loop, 10 mistakes, 70%-rule; dark theme, ≥12px, no h-scroll at 390px.

---

## HOW TO APPLY TO A NEW NICHE

**What changes:** the Context/Audience (that market's customer + fears), the Inputs (that market's verified facts + sources), the Constraints (that market's hedge rules + banned phrases).
**What stays the same:** the 9 elements, the Minimum Viable Prompt, the revision loop, the 10 mistakes, the template library structure, the 70%-usable bar.
**Time:** ~5–15 min per prompt; ~2 weeks of practice to internalise.

---

## SKILL STATUS

**Status:** ✅ PROVEN — clean 45/45 on the 45-check Skill Auditor (all 3 layers pass)
**Ready to sell:** yes · **Ready to teach:** yes · **Next review:** 2026-08-27
**Optional follow-up (non-blocking):** build the Python prompt-evaluation engine to scale beyond the hand-built library.

---

## SIGN-OFF
Completed by: Claude Code + David · Date: 2026-05-29
GitHub commit: committed with this completion doc + the re-audit fixes.
