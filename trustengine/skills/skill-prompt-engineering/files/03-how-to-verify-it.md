---
Status: draft — built 2026-05-29
Area: skill-prompt-engineering
Depends on: skill-prompt-engineering/files/02-how-to-do-it-manually.md
Feeds into: skill-prompt-engineering/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates a prompt and its output must pass before the prompt joins the library

---

## Why verification matters

A prompt is a multiplier. A weak prompt saved to the library scales weak output across every future page; a verified prompt scales 70%+-usable drafts. So a prompt is not "done" when it produces *something* — it is done when it passes the **prompt-completeness gates** and its output meets the **70%+-usable bar** measured against the prompt's own Quality Criteria. In a maximum-risk niche there is one more non-negotiable: **no Unverifiable claim may be asserted as fact** in the output.

---

## Gate set A — prompt completeness (check the brief, before generating)

| Gate | Passes when |
|------|-------------|
| A1 · All 9 elements (or deliberate MVP) | Context, Role, Objective, Audience, Inputs, Constraints, Examples, Output Format, Quality Criteria are all present — or a deliberate Minimum Viable Prompt (Context+Role+Objective+Format) for a quick task. *(M-09)* |
| A2 · Specifics, not placeholders | Every element is filled with real specifics — Inputs carry real facts (cited, e.g. by Source Bank C-ID) and a real style example. *(P-11)* |
| A3 · Constraints carry the hedge rules | For any Unverifiable input, Constraints explicitly instruct the model to hedge it, never assert it. |
| A4 · Quality Criteria are stated and testable | Element 9 is a standard you can actually check the output against — not "make it good". |
| A5 · No generic-language loophole | Constraints ban the niche's filler phrases ("competitive pricing", "world-class"). *(P-16)* |

A prompt failing A1–A5 is not run — it is completed first. A vague prompt produces generic output every time. *(P-14)*

---

## Gate set B — output quality (check the draft, after generating)

| Gate | Passes when |
|------|-------------|
| B1 · Meets its own Quality Criteria | The draft satisfies every line of element 9. |
| B2 · 70%+ usable on the first pass | See the usability measure below. |
| B3 · Every fact cited or hedged | Each factual claim traces to a Verified row (cited) or is hedged exactly per its Unverifiable status. **No asserted Unverifiable claim** — automatic block. |
| B4 · Output format honoured | The structure the prompt asked for (e.g. the 5 layers, markdown) is what came back. |
| B5 · No invented facts/sources/quotes | The model added nothing that wasn't in Inputs. |

---

## The 70%+-usable measure

"Usable" is measured, not felt. Take the first-pass draft and count the edits to publish-ready:

- **70%+ usable** = only light edits (tighten phrasing, reorder a sentence, swap one word). Ship after the revision loop.
- **Below 70%** = structural rewrites, missing/wrong facts, wrong angle. The *prompt* is the problem — fix an element (usually Constraints or Quality Criteria) and regenerate; do not hand-rewrite the output and call the prompt good.

The revision loop should close the remaining gap in **2–3 rounds**; if it takes more, the prompt is underspecified. *(F-09)*

---

## Worked check (the titer-cost prompt)

Running Gate set B on the titer-cost page draft: B3 is the live one — the 700–1,300 AED titer figure must appear **hedged** ("no official figure; community reports…", C-001), and the Etihad USD 399 must lead with the official value before naming the USD 1,500 discrepancy (C-015). A draft that states "the titer test costs 700 AED" fails B3 and is blocked, even if everything else reads well.

---

## The audit sub-agent — verifying the verifier

After a batch of prompts is built, a sub-agent independently re-runs **20%** of them (minimum 3) and scores the output against Gate set B, blind to the original draft. It also re-checks Gate set A on the prompts themselves. *(F-31 — who/how/why applied to the prompt's Quality Criteria.)*

Pass threshold: **90%** of sampled prompts produce a draft that passes all of Gate set B (with B3 a hard pass — any asserted Unverifiable claim fails the whole sample item). Below 90% → the library's prompts are underspecified; fix the failing templates' Constraints/Quality Criteria before reuse.

---

## What downgrades a prompt (do not save to the library)

- Missing Quality Criteria, or criteria too vague to test against.
- Inputs are placeholders, not real cited facts.
- Constraints omit the hedge rule for an Unverifiable input → output asserts it.
- Output needed structural rewrites (below 70% usable) — the prompt, not the output, is fixed.
- The prompt was never saved/named for reuse (a working prompt not archived is wasted capital).

---

## Output of the verification phase

A library of prompts each of which passes Gate set A and reliably produces Gate-set-B-passing drafts at 70%+ usable, with the audit logged at ≥90%. That verified library is the input to File 04's automation — the engine only varies and evaluates prompts that already clear these gates.
