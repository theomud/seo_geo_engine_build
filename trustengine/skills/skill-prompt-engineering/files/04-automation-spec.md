---
Status: draft — built 2026-05-29
Area: skill-prompt-engineering
Depends on: skill-prompt-engineering/files/02-how-to-do-it-manually.md, skill-prompt-engineering/files/03-how-to-verify-it.md
Feeds into: skill-prompt-engineering/engines/engine-prompt-engineering.md
---

# Skill · File 04 — Automation Spec
## What the prompt engine evaluates and improves, and what stays human

---

## Automation target

**~60% of the work can be automated.** The engine evaluates a prompt against the 9 elements, flags weak or missing ones, suggests fixes, and generates test variations of a strong prompt. What it **cannot** do is write the initial prompt: only a human knows what the business actually needs said. *(Library: M-09 Nine-Element Prompt Model; F-17 Agile Prompt Engineering Loop.)*

What gets automated:
- **Score a prompt** against the 9 elements (present / weak / missing), with a one-line reason per element.
- **Flag the gaps** against Gate set A (File 03) — including a missing hedge rule in Constraints, or untestable Quality Criteria.
- **Suggest improvements** to weak elements (a sharper Objective, a missing Audience).
- **Generate 2–3 variations** of a strong prompt for A/B testing.
- **Score the output** against Gate set B and run the iterate→evaluate→refine loop with relevance/usability scores.

What stays manual:
- **Writing the initial prompt** — always human (the business brief).
- **The final Quality Criteria** — what "good" means for this business.
- **Sign-off** that no Unverifiable claim is asserted in the output.
- **Choosing among variations** — the human picks the winner.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| A draft prompt (human-written) | text | the writer (File 02) |
| Content type + its 9-element template | `.md` | `data/prompt-template-library.md` |
| The 9-element rubric + Gate sets A/B | reference | files/01–03 |
| Anthropic API key | env | `ANTHROPIC_API_KEY` in `.env` |

The engine never invents the brief; it improves a human-written one. *(P-14 — a vague prompt produces generic output; the engine surfaces the vagueness, the human fixes it.)*

---

## Outputs

| Output | Destination |
|--------|-------------|
| 9-element completeness score + per-element notes | `data/prompt-evaluations/` |
| Flagged gaps (Gate set A failures) | same |
| Improved prompt + 2–3 test variations | same |
| Promoted templates (prompts that passed Gate sets A+B) | `data/prompt-template-library.md` |

---

## Engine flow per prompt

```
for each human-written prompt:
    1. parse the prompt; map text to the 9 elements
    2. Anthropic API: evaluation system prompt (below)
       - score each element present|weak|missing + one-line reason
       - flag Gate-set-A failures (esp. missing hedge rule, untestable criteria)
       - suggest a fix per weak/missing element
    3. (optional) generate 2-3 variations of the improved prompt
    4. write the evaluation; return to the human to approve a version
    5. rate limit: 1s between API calls
```

---

## The evaluation system prompt

```
You EVALUATE and IMPROVE a content prompt. You do NOT write a prompt from nothing —
if no draft is provided, return {"error":"no draft prompt supplied"}.

Given DRAFT_PROMPT and CONTENT_TYPE, return ONLY JSON:
{
  "elements": {"context":"present|weak|missing", "role":..., "objective":..., "audience":...,
               "inputs":..., "constraints":..., "examples":..., "output_format":..., "quality_criteria":...},
  "notes": {"<element>":"<one-line reason>", ...},
  "gate_A_failures": ["<which Gate-set-A check fails and why>", ...],
  "suggested_fixes": {"<element>":"<concrete improvement>", ...},
  "improved_prompt": "<the draft rewritten with the fixes applied>",
  "variations": ["<variation 1>", "<variation 2>"]
}

RULES:
- Score "missing" if an element is absent; "weak" if present but vague/placeholder.
- Flag a Gate-A failure if Constraints lack a hedge rule for any Unverifiable input,
  or if Quality Criteria are not testable.
- Do NOT invent business facts; improve structure and specificity only.
- Never remove a cited Source Bank C-ID from Inputs.
```

---

## Worked example (the titer-cost prompt)

Fed the human's draft titer-cost prompt, the engine should score Constraints "present" and Quality Criteria "present", and — if the writer forgot the hedge instruction — flag a Gate-A failure: *"Constraints omit the hedge rule for C-001 (titer cost is Unverifiable); output will likely assert the 700–1,300 AED figure as fact."* Its suggested fix adds the hedge clause. The human approves; the prompt is promoted to the library.

---

## Test phase (the 4 universal-gap prompts, then PAUSE)

Before any batch, the engine evaluates the **four hand-written gap-page prompts** and stops. The human checks: are the element scores right? Did it catch the missing hedge rule where one exists? Are the improved prompts actually better, not just longer? If the engine misjudges more than one element across the four, fix the evaluation prompt before scaling.

---

## Audit (after a batch)

A sub-agent re-evaluates **20%** of prompts (minimum 3) blind and compares element scores + Gate-A flags to the engine's. Pass threshold: **90%** agreement, with **B3 (no asserted Unverifiable claim in the resulting output)** a hard pass. Below 90% → the evaluation prompt is miscalibrated; fix it before trusting the engine. *(Same audit discipline as the proven skills.)*

---

## When automation must hand back to humans

- **No draft supplied** — the engine refuses to invent a brief.
- **A business fact is needed** that isn't in Inputs — a human supplies it (or commissions source research).
- **Final Quality Criteria** — the human defines the standard.
- **Choosing the winning variation** — human judgment.
- **Any output that would assert an Unverifiable claim** — hard stop to a human.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| API-call pause | 1 second |
| Cost per prompt evaluation | ≈ $0.01–0.03 |
| Prompts evaluated per hour | ~600 |

---

## Files in this skill (created by the build)

```
skill-prompt-engineering/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/
│   ├── 01-what-is-this-skill.md
│   ├── 02-how-to-do-it-manually.md
│   ├── 03-how-to-verify-it.md
│   ├── 04-automation-spec.md            ← this file
│   └── 06-models-frameworks-principles.md
├── guides/
│   ├── prompt-engineering-study-manual.html
│   └── prompt-engineering-cheatsheet.html
├── data/
│   ├── prompt-templates/                ← the 9-content-type template library (real output)
│   └── prompt-evaluations/
└── engines/
    └── engine-prompt-engineering.md
```
