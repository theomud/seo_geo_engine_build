# The Anatomy of a Claude Skill

Five structural parts that turn a temporary prompt into permanent business infrastructure.
Every skill in `.claude/skills/` must follow this anatomy.

> Source: AI Founders channel — "Anatomy of a Claude Skill" framework

---

## Why anatomy matters

A raw prompt is context-dependent, forgets itself between sessions, and drifts as the model
updates. A skill with anatomy is a software component: it routes itself, knows its own
constraints, references external memory without bloating context, and tells you exactly when
it is failing.

**The 400-line prompt problem.** Cramming everything into one massive prompt:
- Burns context tokens on every call, even for simple requests
- Causes model drift — behaviour changes as context fills up
- Is impossible to audit, update, or reason about
- Breaks when you add a new piece because everything is tangled

**The anatomy solution.** Split each skill into exactly 5 parts. Each part has one job.

---

## Part 1: The Face (Routing Logic)

**What it is:** The description field. It is the skill's front door. Claude reads this to
decide whether to trigger the skill. Because Claude under-triggers by default (it will not
run a skill unless it recognises the signal), the Face must be slightly pushy — it routes
Claude in, not just describes what the skill is.

**The 3 elements:**
1. What the skill does (one sentence, concrete)
2. When to use it (specific conditions, not generic ones)
3. Exact trigger phrases the user will actually type

**Character limit:** Under 1,000 characters. The Face is not the manual — it is the label
on the door.

**Bad Face example:**
```
Reviews contracts.
```

**Good Face example (Red Line — contract review skill):**
```
Reviews legal agreements for unfavourable clauses, missing terms, and risk flags.
Always load when the user is checking a contract or agreement of any kind.
Triggers: "Review this MSA", "Check this brand agreement", "Is this safe to sign?",
"What am I agreeing to?", "Can you look at this contract?", "Red line this for me."
```

**Why the Face must include trigger phrases:**
Claude maps natural language to skill descriptions at runtime. If the description uses
abstract terms ("contract review") but the user says "is this safe to sign?", the skill
may not trigger. Exact trigger phrases close the gap.

**Face template (frontmatter + first section):**
```markdown
---
name: skill_name
description: |
  One sentence on what this skill does.
  Always load when: [specific condition].
  Triggers: "phrase 1", "phrase 2", "phrase 3", "phrase 4"
tags: [tag1, tag2, tag3]
---
```

---

## Part 2: The Brain (Instructions + Freedom Dial)

**What it is:** The core instruction set. Everything Claude needs to execute the skill.
The biggest mistake here is using the wrong instruction style for the task type.

**The Freedom Dial — two modes:**

### High Freedom (Judgment Work)
Use when there are many correct answers.
- Creative writing, copywriting, strategy, analysis, restructuring, research synthesis
- Give: principles, guardrails, your philosophy, desired outcomes, what to avoid
- Do NOT give rigid steps — rigid steps kill judgment work
- The model reasons its way to the answer; you constrain the direction, not the method

```markdown
## Brain — High Freedom

**Objective:** [What a great output achieves]

**Principles:**
- [Principle 1 — a guardrail or philosophy, not a step]
- [Principle 2]
- [Principle 3]

**Guardrails (never do):**
- [Anti-pattern 1]
- [Anti-pattern 2]

**Output format:** [What the output should look like — sections, length, tone]
```

### Low Freedom (Precision Work)
Use when there is exactly one correct answer.
- File formatting, technical compliance, document packaging, data extraction, gate checks
- Give: numbered steps, exact formats, specific conditions, unambiguous pass/fail criteria
- Variance equals failure — do not leave room for interpretation
- Every step is an instruction, not a principle

```markdown
## Brain — Low Freedom

**Objective:** [Exact outcome with zero variance]

**Steps:**
1. [Do exactly this]
2. [Do exactly this]
3. [If condition X, do Y; else do Z]
4. [Check this exact thing]
5. [Write output in this exact format]

**Pass criteria:** [What counts as success]
**Fail criteria:** [What counts as failure — stop and alert]
```

### Mismatching the dial — the failure mode

| Task type | Wrong dial | Result |
|---|---|---|
| Write a brand voice audit | Low Freedom | Rigid steps produce mechanical, identical outputs every time — no judgment |
| Package a DOCX report with exact headers | High Freedom | Model interprets formatting guidelines loosely — headers shift, sections vanish |
| Generate a competitor analysis | Low Freedom | Over-specified steps ignore context; model ignores instructions that don't apply |
| Extract specific fields from a legal doc | High Freedom | Fields are missed; extraction is inconsistent |

---

## Part 3: The Memory (Reference Files)

**What it is:** Pointers to external Markdown files that hold heavy, rarely-needed data.

**The rule:** Never paste reference data into the Brain. If a piece of information is:
- More than ~50 lines long
- Only needed for some task variants (not all)
- Slow to change (style guides, example libraries, regulatory tables)

...it goes into a separate `.md` file. The Brain points to it conditionally.

**Why this matters:** Every token in the skill body is loaded into context on every call.
A 500-line example library pasted directly into Brain burns context tokens even when
the task doesn't need examples. The model's reasoning degrades as context fills.

**How to write Memory pointers:**

```markdown
## Memory

Reference files loaded on demand — not preloaded unless the condition is met.

| Condition | File | What it contains |
|---|---|---|
| Writing a long-form post | `memory/long_form_examples.md` | 8 full-length post examples with annotations |
| Running a regulatory check | `memory/regulatory_tables.md` | FDA/EFSA/MHRA requirement tables |
| Citing an academic source | `memory/source_format_guide.md` | Citation format by database and jurisdiction |

**Loading instruction:** "If the task requires [condition], reference [file] before
proceeding. If the condition is not met, ignore this section."
```

**Memory file naming convention:**
- `memory/<skill_name>_examples.md` — worked examples
- `memory/<skill_name>_reference.md` — static data tables
- `memory/<skill_name>_style.md` — tone/voice/brand guidelines

---

## Part 4: The Spine (Addressable Skeleton)

**What it is:** A standard 7-section layout that every skill file follows. The Spine exists
so both you and Claude can locate any piece of information instantly. When you are debugging
a skill at 11pm, you should not have to read the whole file — you jump to the section you
need.

**The standard 7-section layout:**

```markdown
## How to use this skill
[Two sentences. When to invoke, what to pass in, what comes out.]

## North Star
[One sentence. The single outcome this skill exists to achieve.]

## [Core section 1 — one concept]
[...]

## [Core section 2 — one concept]
[...]

## Anti-patterns
[Numbered list of things NOT to do and why.]

## Real examples
[Concrete input → output pairs. Not abstract descriptions.]

## Self-check
[Questions the model asks itself before returning output.]

## Known gaps
[What this skill cannot do yet. Honest, specific.]
```

**Length rules:**
- Core skill files: under 500 lines
- High-frequency tools (used daily): under 350 lines
- The file must be skimmable in 30 seconds

**Why the Spine enables compounding:**
When all skills share the same skeleton, you can build workflows where Skill A passes output
to Skill B without custom glue code. Skill B knows exactly where to look for Skill A's output
format because both follow the same structure. This is how skills compound into a platform.

---

## Part 5: The Pulse (Long-Term Maintenance)

**What it is:** Five rules that keep a skill alive and accurate over time. Without a Pulse,
skills rot: terms drift, examples go stale, gaps are forgotten, and the skill quietly starts
failing in ways that are hard to notice.

**The 5 Pulse rules:**

### Rule 1: Term Consistency
Pick one term per concept. Use it everywhere in the file. Never swap.

| Concept | Pick one | Never mix with |
|---|---|---|
| The person using the system | `user` | client, customer, operator, caller |
| The output document | `report` | output, deliverable, result, document |
| The evidence standard | `peer-reviewed` | academic, scholarly, research-backed, cited |

Put your term choices in the Known Gaps or a `## Terminology` section.

### Rule 2: No Timestamp Language
Never write "as of 2025" or "updated March 2026." These phrases become lies silently.

Use structural headers instead:
- `## Current Method` / `## Old Pattern`
- `## Active Rules` / `## Deprecated Rules`
- `## Version 2 Behaviour` / `## Legacy Behaviour`

Structural headers age gracefully. Timestamps become noise.

### Rule 3: Real Examples
Always include concrete input/output pairs. Abstract descriptions fail.

**Bad example entry:**
```
The skill takes a contract and returns a risk assessment.
```

**Good example entry:**
```
Input: "Review this SaaS MSA — we're the vendor, 12-month term, auto-renew clause."
Output:
  - RISK: Auto-renew clause (Section 7.2) gives the customer 30-day exit window
    but vendor needs 90 days. Asymmetric.
  - MISSING: No indemnification cap. Standard is 12 months of fees.
  - SAFE: IP assignment (Section 4) is standard.
```

### Rule 4: Known Gaps
Explicitly document what the skill cannot do. This prevents Claude from confidently
attempting tasks out of depth, and tells the user exactly when to escalate.

```markdown
## Known gaps
- Does not validate regulatory citations against primary official sources (manual check required)
- Cannot process scanned PDFs — text extraction must be provided by the user
- Does not handle non-English contracts without a translation layer
- Jurisdiction: defaults to UK law; US/UAE law requires the user to flag the jurisdiction
```

### Rule 5: One Skill, One Job
Never bundle two utilities in one SKILL.md. The moment a skill tries to do two things,
its Face description becomes ambiguous and routing degrades.

**Wrong:** One skill that both generates a brief AND formats the output document.
**Right:** `brief_generator` (generates the brief) + `brief_formatter` (formats it).

Two narrow, sharply triggered skills always outperform one broad, unpredictable one.

---

## The complete anatomy template

```markdown
---
name: skill_name
description: |
  [What this skill does — one sentence]
  Always load when: [specific condition]
  Triggers: "phrase 1", "phrase 2", "phrase 3"
tags: [tag1, tag2]
---

## How to use this skill
[One sentence invocation guide. One sentence on what to pass in and what comes out.]

## North Star
[One sentence. The single outcome this skill exists to achieve.]

## Brain — [High Freedom / Low Freedom / Mixed]

**Freedom Dial:** [HIGH / LOW / MIXED — and one sentence on why]

**Objective:** [Exact outcome]

[For High Freedom:]
**Principles:**
- [...]

**Guardrails:**
- [...]

[For Low Freedom:]
**Steps:**
1. [...]

## Memory

| Condition | File | Contents |
|---|---|---|
| [condition] | `memory/[file].md` | [what it holds] |

Load instruction: reference [file] only when [condition] is met.

## Anti-patterns
- [What NOT to do — numbered, specific]

## Real examples

**Input:** [exact input]
**Output:** [exact output or output structure]

## Self-check
Before returning output, verify:
- [ ] [Check 1]
- [ ] [Check 2]

## Known gaps
- [What this skill cannot do — specific, honest]

## Terminology
| Term used | Meaning | Never use |
|---|---|---|
| [term] | [definition] | [synonyms to avoid] |
```

---

## Quick reference card

| Part | Job | Limit | Failure mode |
|---|---|---|---|
| Face | Routing trigger | < 1,000 chars | Under-triggers (skill never loads) |
| Brain | Core instructions | Dominant section | Wrong freedom dial (rigid creative / loose precision) |
| Memory | External data pointers | Pointer only, not data | Data pasted in Brain bloats context |
| Spine | Standard 7-section layout | < 500 lines total | Custom layouts break compounding |
| Pulse | Maintenance rules | Living section | Skill rots — stale terms, dead examples, hidden gaps |
