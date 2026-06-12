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

## North Star
SINGLE_OUTCOME_THIS_SKILL_EXISTS_TO_ACHIEVE.

## Brain — High Freedom

**Freedom Dial:** HIGH — this task has many correct answers. Do not follow rigid steps.
Reason your way to the best output using the principles and guardrails below.

**Objective:** WHAT_A_GREAT_OUTPUT_ACHIEVES

**Principles:**
- PRINCIPLE_1
- PRINCIPLE_2
- PRINCIPLE_3
- PRINCIPLE_4
- PRINCIPLE_5

**Guardrails (never do):**
- ANTI_PATTERN_1
- ANTI_PATTERN_2
- ANTI_PATTERN_3

**Output format:**
- Length: TARGET_LENGTH
- Sections: SECTION_LIST
- Tone: TONE_DESCRIPTION
- Start with: OPENING_FORMAT
- End with: CLOSING_FORMAT

## Memory

| Condition | File | Contents |
|---|---|---|
| CONDITION_1 | `memory/SKILL_NAME_examples.md` | WHAT_IT_HOLDS |
| CONDITION_2 | `memory/SKILL_NAME_reference.md` | WHAT_IT_HOLDS |

Load instruction: reference each file only when its condition is met. If the condition
is not triggered by the current task, ignore the file entirely.

## Anti-patterns
1. ANTI_PATTERN_DESCRIPTION — why it fails
2. ANTI_PATTERN_DESCRIPTION — why it fails
3. ANTI_PATTERN_DESCRIPTION — why it fails

## Real examples

**Example 1**
Input: "EXACT_INPUT_STRING"
Output:
```
EXACT_OR_STRUCTURED_OUTPUT
```

**Example 2**
Input: "EXACT_INPUT_STRING"
Output:
```
EXACT_OR_STRUCTURED_OUTPUT
```

## Self-check
Before returning output, verify:
- [ ] The output achieves the North Star objective
- [ ] No anti-patterns were used
- [ ] Output format matches the specification
- [ ] SKILL_SPECIFIC_CHECK_1
- [ ] SKILL_SPECIFIC_CHECK_2

## Known gaps
- GAP_1 — manual step required
- GAP_2 — out of scope for this skill
- GAP_3 — requires human judgment

## Terminology
| Term used | Meaning | Never use |
|---|---|---|
| TERM_1 | DEFINITION | SYNONYMS_TO_AVOID |
| TERM_2 | DEFINITION | SYNONYMS_TO_AVOID |
