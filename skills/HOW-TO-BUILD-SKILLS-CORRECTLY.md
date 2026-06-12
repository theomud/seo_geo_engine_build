---
name: how-to-build-skills-correctly
description: >
  The canonical standard for building every Claude skill in this repo — the
  "Anatomy of a Claude Skill" (Face · Brain · Memory · Spine · Pulse). Read this
  BEFORE creating a new skill or editing an existing one, and audit every skill
  against the self-check below. A prompt is rented; a skill is owned.
  Triggers: "build a skill", "new skill", "fix this skill", "is this skill built right",
  "audit the skills", "skill anatomy".
metadata:
  type: reference
  status: active — canonical standard
  last_updated: 2026-06-12
  source: "AI Founders — 'Anatomy of a Claude Skill' (5-step framework)"
---

# How to Build Skills Correctly — the Anatomy of a Claude Skill

> **North Star.** A skill turns a one-off prompt into owned infrastructure. The goal of
> every skill in this repo is to **trigger reliably, execute consistently, and stay alive**
> over time — never to drift, never to bloat the context window, never to do two jobs at once.
> **A prompt is rented; a skill is owned.** Build each one as a software component, not a
> copy-pasted block of text.

## How to use this file

When you create a new skill OR touch an existing one, walk the **5 anatomical parts** below
in order, then run the **Self-check**. Every skill in `skills/` must pass it. If a skill
fails, fix it or log the gap in its own *Known gaps* section. This file is itself built to the
standard it describes (Face → North Star → Core sections → Anti-patterns → Real examples →
Self-check → Known gaps) — copy its shape.

---

## Part 1 — The Face (routing logic) · the `description:` field

The Face is the skill's `description:` in the YAML frontmatter. It is **routing logic, not a
label.** Claude **under-triggers by default** — it won't load a skill unless the description
makes the match obvious — so the Face must be slightly *pushy*.

**The 3 elements every Face needs:**
1. **What** the skill does (one clause).
2. **When** to use it — and, where useful, when NOT to (point to the sibling skill instead).
3. **Trigger phrases** — the exact words you'd actually type in normal conversation.

**Constraint:** keep the Face **under 1,000 characters.**

```yaml
# WRONG — a label. Will never trigger.
description: "Reviews contracts"

# RIGHT — routing logic.
description: >
  Reviews contracts and flags risky clauses before you sign. Always load when
  checking an agreement. Triggers: "Review this MSA", "Check this brand agreement",
  "Is this safe to sign?". Not for drafting a new contract — use contract-draft.
```

---

## Part 2 — The Brain (instructions + the Freedom Dial)

The Brain is the body of core instructions. The biggest failure here is **matching the wrong
execution style to the task.** Set the **Freedom Dial** to match how many correct answers the
task has:

| Dial | Task type | What to write |
|------|-----------|---------------|
| **High freedom** (judgment work) | Many correct answers — copywriting, offers, strategy, naming | Give **principles, guardrails, and philosophy**, then let the model reason. Do **not** give rigid steps. |
| **Low freedom** (precision work) | One correct answer — formatting, file packaging, compliance checks, schema | Give an **uncompromising, mechanical, step-by-step checklist** where variance = failure. |

Pick the dial deliberately and state it. Most skills are one or the other; a few have a
high-freedom planning phase and a low-freedom output phase — say so explicitly and split them.

---

## Part 3 — The Memory (reference files)

Cramming examples, long datasets, or thousands of lines of voice rules into the Brain **burns
the context window**, slows the model, and degrades its logic.

**The rule:** keep instructions in the Brain; push **heavy, rarely-needed data** down into
sibling Markdown reference files (`long-form-examples.md`, `EVIDENCE.md`, `claim_bank.csv`,
etc.). The Brain points to Memory **only on condition**:

> "If writing a long-form post, reference `long-form-examples.md`."

If the condition isn't met, the Memory sits idle at **zero token cost.** A loaded reference
should be the exception, triggered by the task — not always-on ballast.

---

## Part 4 — The Spine (the addressable skeleton)

Every skill shares **one identical layout** so you and the model can locate any parameter
instantly. Use these sections, in this order:

1. **How to use the skill**
2. **North Star objective**
3. **Core sections** — one per concept
4. **Anti-patterns** — what NOT to do
5. **Real examples** — concrete inputs/outputs
6. **Self-check validation**
7. **Known gaps**

**Length rule:** keep the core skill file **under 500 lines** — ideally **under 350** for
high-frequency tools — so the whole thing is skimmable in ~30 seconds. Overflow goes to
Memory (Part 3), not into the Brain.

---

## Part 5 — The Pulse (long-term maintenance)

A skill **rots** without a pulse. Five rules keep it alive:

1. **Term consistency** — one term per concept. Don't swap "client" / "user" / "customer" in
   the same file. (In this repo: pick one and hold it.)
2. **No timestamp language** — avoid "as of 2025." Use structural headers — **Current method**
   vs **Old pattern** — so the file doesn't read as stale.
3. **Real-world examples** — concrete, exact inputs and outputs, not abstract description.
4. **Honest known gaps** — document what the skill *cannot* do yet, so the model doesn't
   confidently attempt work out of its depth.
5. **One skill, one job** — never bundle utilities. **Two sharply-triggered narrow skills beat
   one broad, unpredictable tool.**

---

## Anti-patterns (what NOT to do)

- **Label-as-Face** — `description: "Reviews contracts"`. Under-triggers; the skill never loads.
- **Wrong dial** — rigid 12-step checklist for copywriting (kills judgment), or vague
  "use your best judgment" for schema/formatting (causes variance failures).
- **Brain bloat** — pasting a 400-line example corpus or brand bible into the instructions.
- **Drifting terms** — "lead" in §2, "prospect" in §4, "customer" in §6.
- **Timestamp rot** — "the current 2025 best practice is…".
- **Swiss-army skill** — one skill that audits, writes, and packages. Split it.
- **>500-line Brain** — if it can't be skimmed in 30s, it's two skills or it needs Memory files.

---

## Real examples (from this repo)

**Strong Face** — `marketingskills/cro/SKILL.md`: names the job, the sibling skills to defer to,
and a dozen exact trigger phrases ("this page isn't converting", "my landing page sucks").

**Memory done right** — `copywriting/SKILL.md` keeps the Brain as the truth layer and pushes
full citations + the claim/benchmark bank to `EVIDENCE.md`, loaded only when needed.

**Length violation to fix** — `claude-blog/blog-write/SKILL.md` is **558 lines**; the heavy
template/example detail belongs in Memory files so the Brain drops under 500.

**Dial split** — a blog skill that *plans* the angle (high freedom: principles) then *formats*
the output to schema (low freedom: mechanical checklist) — state both phases.

---

## Self-check validation (run on every skill)

- [ ] **Face:** `description:` states what + when (+ when-not) + real trigger phrases, **<1,000 chars**.
- [ ] **Brain:** Freedom Dial is set deliberately (principles for judgment work; checklist for precision work).
- [ ] **Memory:** heavy/rare data is in sibling reference files, pointed to *conditionally* — not inlined.
- [ ] **Spine:** uses the 7-section skeleton, in order.
- [ ] **Length:** core file <500 lines (ideally <350 for high-frequency skills).
- [ ] **Pulse:** one term per concept · no timestamp language · concrete examples · honest *Known gaps* · one job only.

A skill that fails any box gets fixed or the gap is logged in its own *Known gaps* before merge.

---

## Known gaps

- Frontmatter conventions vary across the four imported skill packs (`metadata.version`,
  `when_to_use`, `argument-hint`, license fields). The standard above governs **content/shape**;
  it does not yet mandate a single frontmatter schema across packs — see the audit scorecard for
  per-skill deviations.
- "High-frequency" (the <350-line target) is a judgement call until usage is tracked; treat
  user-invokable, money-path skills as high-frequency.
