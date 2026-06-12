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
Variance equals failure — follow steps exactly.

## North Star
SINGLE_OUTCOME_WITH_ZERO_VARIANCE.

## Brain — Low Freedom

**Freedom Dial:** LOW — this task has exactly one correct answer. Follow steps exactly.
Do not interpret, adapt, or apply judgment to individual steps. Variance equals failure.

**Objective:** EXACT_OUTCOME

**Pre-conditions (check before starting):**
- [ ] PRE_CONDITION_1
- [ ] PRE_CONDITION_2

**Steps:**
1. DO_EXACTLY_THIS
2. DO_EXACTLY_THIS
3. IF CONDITION then DO_X; ELSE DO_Y
4. CHECK_THIS_EXACT_THING — if not present, STOP and alert user with: "ALERT_MESSAGE"
5. WRITE_OUTPUT_IN_THIS_EXACT_FORMAT
6. VERIFY_STEP — confirm output matches SPECIFICATION
7. DELIVER_OUTPUT

**Pass criteria:**
- CRITERION_1
- CRITERION_2

**Fail criteria (stop immediately and alert):**
- FAIL_CONDITION_1 → "ALERT: FAIL_MESSAGE"
- FAIL_CONDITION_2 → "ALERT: FAIL_MESSAGE"

## Memory

| Condition | File | Contents |
|---|---|---|
| CONDITION_1 | `memory/SKILL_NAME_reference.md` | WHAT_IT_HOLDS |

Load instruction: reference each file only when its condition is met.

## Anti-patterns
1. SKIPPING_STEP_N — why it causes failure
2. REORDERING_STEPS — why sequence matters
3. INTERPRETING_INSTEAD_OF_FOLLOWING — how it introduces variance

## Real examples

**Example 1 — success path**
Input: "EXACT_INPUT"
Steps executed: 1 → 2 → 3 (condition A, took X path) → 4 → 5
Output:
```
EXACT_OUTPUT_FORMAT
```

**Example 2 — failure path**
Input: "EXACT_INPUT_WITH_PROBLEM"
Step 4 check failed: PRE_CONDITION_NOT_MET
Alert issued: "ALERT: FAIL_MESSAGE"
Action required: USER_MUST_DO_THIS

## Self-check
Before returning output, verify:
- [ ] All steps were executed in order
- [ ] All pre-conditions were met
- [ ] Pass criteria are satisfied
- [ ] No fail conditions were triggered
- [ ] Output matches the exact format specification

## Known gaps
- GAP_1 — not handled by these steps
- GAP_2 — requires a different skill
- GAP_3 — manual verification needed

## Terminology
| Term used | Meaning | Never use |
|---|---|---|
| TERM_1 | DEFINITION | SYNONYMS_TO_AVOID |
| TERM_2 | DEFINITION | SYNONYMS_TO_AVOID |
