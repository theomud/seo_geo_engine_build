# SKILL AUDITOR ENGINE
## Claude Code prompt — run after every skill build

---

## WHAT THIS DOES

Runs an independent 4-layer audit on a completed skill folder.
Produces SKILL-AUDIT-REPORT.md with scores, status, and fix list.
Must be run by a sub-agent — not the agent that built the skill.

Audit version: 2.0 (47 checks) — upgraded 2026-05-30 from v1.0 (45 checks).
Layer 4 (Functional Quality + Independence) added per MASTER-SYSTEM build plan.

---

## USAGE

```
Run the Skill Auditor on: skill-[name]/
Do not skip any checks. Do not assume anything passes unless verified.
Produce SKILL-AUDIT-REPORT.md in the skill folder when complete.
```

---

## THE AUDIT PROMPT

Paste this as the sub-agent instruction:

```
You are an independent skill auditor. You did not build this skill.
Your job is to verify whether it meets the minimum standard.

Read the skill folder at: [skill folder path]

Run all 47 checks across 4 layers exactly as specified.
Score each check 0 or 1. Do not give partial credit.
If you cannot verify a check — it scores 0.

LAYER 1 — SKILL COMPLETENESS (20 checks)

STRUCTURE (5):
1. All required folders exist: README, .env.example, customer-profile/, 
   files/, guides/, data/, engines/
2. README describes the skill without referencing any other skill by name
3. README has a completed Skill Value Score with all 5 dimensions scored
4. .env.example only contains variables this skill actually needs
5. Customer profile snapshot contains only relevant excerpts, not the 
   full master profile

SPEC FILES (5):
6. File 01 exists and defines the skill in niche-agnostic terms
7. File 02 exists with a step-by-step manual process — not just theory
8. File 03 exists with a verification standard
9. File 04 exists with an automation specification
10. File 06 exists with models, frameworks, and principles clearly 
    separated into 3 distinct sections

PROOF (5):
11. data/ folder contains at least one real output file
12. Output file contains real data from a real niche — not empty, 
    not a template
13. README proof section has a date, a niche name, and a real result
14. Skill Value Score is confirmed — not marked "estimated"
15. At least one screenshot of real output exists in the skill folder

QUALITY (5):
16. Skill passes standalone test: someone unfamiliar can use it without 
    reading any other skill
17. Skill passes niche-agnostic test: methodology works for markets 
    other than Dubai pet relocation
18. Manual process (File 02) is detailed enough to follow without 
    asking questions
19. Automation spec (File 04) defines what Claude Code needs to build 
    the engine
20. Models, frameworks, and principles in File 06 are distinct — not 
    merged into one block of text

LAYER 1 THRESHOLD: 16/20 = PASS, 12-15 = NEEDS WORK, below 12 = INCOMPLETE

---

LAYER 2 — LEARNER GUIDE (15 checks)

STRUCTURE AND NAVIGATION (4):
21. Fixed sidebar navigation with all major sections listed
22. Progress bar visible at top of page
23. Active state on nav links updates as user scrolls
24. All section headings in the page match navigation labels exactly

CONTENT QUALITY (4):
25. Every major concept has a real example from the Dubai proof niche
26. Every framework has a before/after comparison shown
27. Real community quotes or real data appears at least once per 
    major section
28. Guide answers all 4 questions: what is it, why it matters, 
    how to do it, what good looks like

PROOF AND EVIDENCE (3):
29. Real scores from the Dubai proof run appear — not theoretical examples
30. At least one real failure or surprise from the proof niche is 
    documented in the guide
31. Community quotes sourced from actual research are used as examples

USER EXPERIENCE (4):
32. Readable without horizontal scrolling at 390px viewport width
33. Interactive elements work correctly (progress bar, nav, any quiz)
34. Typography matches the standard: Crimson Pro body, Bebas Neue 
    headings, JetBrains Mono for code/data
35. Colour coding applied: gold for key points, red for warnings, 
    green for correct examples

LAYER 2 THRESHOLD: 12/15 = PASS, 9-11 = NEEDS WORK, below 9 = INCOMPLETE

---

LAYER 3 — CHEATSHEET (10 checks)

PHONE USABILITY (4):
36. Renders correctly at 390px width with no horizontal scroll
37. All text readable without zooming — minimum 12px font size
38. Nothing requires a click to expand — all content visible immediately
39. Total content scrollable in under 30 seconds at normal reading speed

CONTENT COMPLETENESS (3):
40. Contains the single most important decision framework from the skill
41. Contains the most common mistakes or failure points
42. Contains the key numbers, thresholds, or benchmarks a practitioner 
    needs in the field

PROOF AND REAL DATA (3):
43. Includes at least one real result from the Dubai proof run
44. All numbers shown are from real work — not estimates
45. Dark theme with gold accents matches standard cheatsheet style

LAYER 3 THRESHOLD: 8/10 = PASS, 6-7 = NEEDS WORK, below 6 = INCOMPLETE

---

LAYER 4 — FUNCTIONAL QUALITY + INDEPENDENCE (2 checks)

This layer asks the question the first 45 checks do not: does the real
output actually work, and can anyone but the builder reproduce it.

CHECK 46 — FUNCTIONAL OUTPUT QUALITY
Every skill must define its own quality threshold in the README
(a "Functional Quality Threshold" section). The real output in data/
is scored against that threshold.
Score 1 if: a threshold is defined in the README AND the real output
  in data/ meets it.
Score 0 if: no threshold is defined OR the output does not meet it.

Examples of functional quality thresholds:
- Prompt Engineering: 70%+ of generated drafts usable without rewriting
- Editorial Judgment: 4 gap pages average 40+/50 on scoring rubric
- Conversion Copy: rewritten CTAs score higher on the help-first test
- Content Architecture: every page findable within 3 clicks
- Authority Assets: Hormozi test passes (AI cannot replicate it)
- Email Nurture: every email opens with a named fear from Column K
- AI Citation: at least one page cited by Perplexity for target query
- Monitoring: weekly report generated with at least 3 RICE-scored items

CHECK 47 — INDEPENDENCE TEST FLAG
The skill documentation must be clear enough for independent replication.
This is a STATUS FLAG, not pass/fail — but it must be addressed (the flag
must be explicitly set) for the skill to be marked PROVEN.
Flag TESTED if: a second person has followed the documentation
  independently and produced output meeting the quality threshold.
Flag NOT YET TESTED if: only the original builder has used it.
A skill cannot be marked COMMERCIALLY READY until the flag is TESTED.

LAYER 4 RULE:
- Check 46 scores 0 or 1 like every other check.
- Check 47 is a flag (TESTED / NOT YET TESTED). It counts as "addressed"
  for a 47/47 PROVEN score as long as the flag is explicitly set —
  NOT YET TESTED is an acceptable addressed state for PROVEN.
- Both checks must be addressed before COMMERCIALLY READY status.
- COMMERCIALLY READY additionally requires check 47 = TESTED.

---

AFTER RUNNING ALL 47 CHECKS:

Generate SKILL-AUDIT-REPORT.md in the skill folder with:

1. SUMMARY TABLE
   | Layer | Score | Status |
   | Layer 1 — Skill Completeness | X/20 | ✅/⚠️/❌ |
   | Layer 2 — Learner Guide | X/15 | ✅/⚠️/❌ |
   | Layer 3 — Cheatsheet | X/10 | ✅/⚠️/❌ |
   | Layer 4 — Functional Quality | Check 46 | Check 47 |
   | Output quality threshold met | ✅/❌ | Status |
   | Independence test | N/A for 46 | TESTED/NOT YET TESTED |
   | OVERALL | X/47 | ✅/⚠️/❌ |

2. OVERALL STATUS
   PASS (Layers 1-3 pass + check 46 = 1 + check 47 flag set):
     ✅ Skill may be marked PROVEN (47/47 — check 47 may be NOT YET TESTED)
   NEEDS WORK (1-2 layers fail OR check 46 = 0):
     ⚠️ Skill may be committed but not marked PROVEN
   INCOMPLETE (all layers fail): ❌ Do not commit — rebuild required
   COMMERCIALLY READY: PROVEN + check 47 = TESTED (independent replication
     confirmed). Until then the skill is PROVEN but not commercially ready.

3. FIX LIST
   For every failed check, one line:
   "Check [N]: [what failed] → [exact fix required]"

4. COMPARISON TO BENCHMARK
   Show how this skill compares to the 3 proven skills:
   Customer Fear Intelligence: 14/20 + 11/15 + 8/10 = 33/45 (pre-Layer-4)
   Trust Gap Analysis: 13/20 + 15/15 + 9/10 = 37/45 (pre-Layer-4)
   Official Source Research: 16/20 + TBD + TBD
   The 6 proven skills now require Layer 4 added (check 46 scored,
   check 47 flagged) to reach the new 47/47 standard — re-audit on drift.

   New skill must score at or above 33/45 on Layers 1-3 AND meet its
   functional threshold (check 46) to be considered passing.

5. SIGN-OFF
   Audited by: Sub-agent (independent)
   Date: [today's date]
   Skill folder: [path]
   Audit version: 2.0 (47 checks)
```

---

## HOW TO RUN IN CLAUDE CODE

After completing a skill build, type:

```
Spawn a sub-agent to audit skill-[name]/ using the 47-check 
framework in skill-skill-auditor/engines/engine-skill-auditor.md.
The sub-agent must be independent — do not share context from 
the build session. Generate SKILL-AUDIT-REPORT.md in the skill 
folder. Report the overall score and status when complete.
```

---

## AUDIT SCHEDULE

Run the audit at these points:
1. After README + customer profile are built — Layer 1 partial (checks 1-10)
2. After all spec files are built — Layer 1 full
3. After learner guide is built — Layer 2
4. After cheatsheet is built — Layer 3
5. After real output exists in data/ — Full 47-check audit (Layers 1-4)
6. Every 90 days — re-audit all proven skills for drift
