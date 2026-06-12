---
name: SKILL_NAME
description: |
  WHAT_IT_DOES_ONE_SENTENCE.
  Always load when: SPECIFIC_CONDITION.
  Triggers: "TRIGGER_PHRASE_1", "TRIGGER_PHRASE_2", "TRIGGER_PHRASE_3", "TRIGGER_PHRASE_4"
tags: [TAG1, TAG2, TAG3]
---

## How to use this skill
Invoke when CONDITION. Pass in INPUT_DESCRIPTION. Returns OUTPUT_DESCRIPTION.
This skill has both a precision phase (follow exactly) and a judgment phase (apply principles).

## North Star
SINGLE_OUTCOME_THIS_SKILL_EXISTS_TO_ACHIEVE.

## Brain — Mixed

**Freedom Dial:** MIXED — this skill has two phases:
- Phase 1 (Low Freedom): PRECISION_TASK_DESCRIPTION — follow steps exactly
- Phase 2 (High Freedom): JUDGMENT_TASK_DESCRIPTION — apply principles

### Phase 1: Low Freedom — PRECISION_PHASE_NAME

Steps (follow exactly, variance equals failure):
1. DO_EXACTLY_THIS
2. DO_EXACTLY_THIS
3. IF CONDITION then DO_X; ELSE DO_Y
4. Pass criteria: EXACT_CONDITION
5. Fail criteria: EXACT_CONDITION → stop and alert: "ALERT: MESSAGE"

### Phase 2: High Freedom — JUDGMENT_PHASE_NAME

Objective: WHAT_A_GREAT_OUTPUT_ACHIEVES

Principles:
- PRINCIPLE_1
- PRINCIPLE_2
- PRINCIPLE_3

Guardrails (never do):
- ANTI_PATTERN_1
- ANTI_PATTERN_2

Output format:
- Length: TARGET_LENGTH
- Sections: SECTION_LIST
- Tone: TONE_DESCRIPTION

## Memory

| Condition | File | Contents |
|---|---|---|
| CONDITION_1 | `memory/SKILL_NAME_reference.md` | WHAT_IT_HOLDS |
| CONDITION_2 | `memory/SKILL_NAME_examples.md` | WHAT_IT_HOLDS |

Load instruction: reference each file only when its condition is met.

## Anti-patterns
1. MIXING_THE_TWO_PHASES — apply judgment in Phase 1 (precise phase) or follow rigid steps in Phase 2 (judgment phase)
2. ANTI_PATTERN_2 — why it fails
3. ANTI_PATTERN_3 — why it fails

## Real examples

**Example 1 — full flow**
Input: "EXACT_INPUT_STRING"
Phase 1 output: INTERMEDIATE_RESULT
Phase 2 output:
```
FINAL_OUTPUT
```

**Example 2 — Phase 1 failure**
Input: "EXACT_INPUT_WITH_PROBLEM"
Phase 1 fail: PRE_CONDITION_NOT_MET
Alert: "ALERT: MESSAGE"
Action: USER_MUST_DO_THIS

## Self-check
Before returning output, verify:
- [ ] Phase 1 steps were completed in order and all pass criteria met
- [ ] Phase 2 principles were applied (not rigid steps)
- [ ] Output format matches specification
- [ ] SKILL_SPECIFIC_CHECK

## Known gaps
- GAP_1 — Phase 1 only handles [scope]; outside this requires manual step
- GAP_2 — Phase 2 judgment is constrained by [limitation]
- GAP_3 — does not handle [edge case]

## Terminology
| Term used | Meaning | Never use |
|---|---|---|
| TERM_1 | DEFINITION | SYNONYMS_TO_AVOID |
| TERM_2 | DEFINITION | SYNONYMS_TO_AVOID |
