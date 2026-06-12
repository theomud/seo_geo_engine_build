---
Status: draft — built 2026-05-29
Area: skill-prompt-engineering
Depends on: skill-prompt-engineering/files/01-what-is-this-skill.md, skill-prompt-engineering/README.md
Feeds into: skill-prompt-engineering/files/03-how-to-verify-it.md, skill-prompt-engineering/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Writing a 9-element prompt by hand, then running the revision loop

---

## Why manual first

Automation can evaluate and improve a prompt, but it cannot decide what your business actually needs said. You write the brief; the model drafts from it. Build the first prompts by hand until filling the 9 elements is automatic — then the template library (File 04) makes every future prompt a fill-in-the-blanks job.

Time: **5–15 minutes per prompt** once you know the elements; ~2 weeks of daily practice to internalise them. Plan for **2–3 revision rounds** per draft — first prompts rarely produce final output.

---

## Step 1 — Identify the content type and open its template

Decide what you're producing (landing page, SEO article, service page, FAQ, location page, comparison, rewrite, meta tags, or a fear-resolution page). Open that template from the library (`data/prompt-template-library.md`). The template is the 9 elements pre-scoped for that content type — you fill the specifics.

---

## Step 2 — Fill all 9 elements with specifics (worked example)

Below, every element is filled for a real page from the proof niche: the **Cost Transparency page, "how much does the rabies titer test cost in Dubai."** *(Library: M-09 Nine-Element Prompt Model.)*

| # | Element | Filled for this page |
|---|---------|----------------------|
| 1 | **Context** | Dubai pet relocation — a maximum-risk regulated market; customers arrive afraid and distrustful, sure they are being overcharged. |
| 2 | **Role** | A pet-relocation specialist who has paid these fees and reads MOCCAE directly. |
| 3 | **Objective** | A 600–900-word Cost Transparency page answering "how much does the rabies titer test cost in Dubai," that helps the reader spot an unfair quote. |
| 4 | **Audience** | An owner mid-quote-comparison thinking *"I'm being quoted an insane amount and have no way to know if it's fair."* |
| 5 | **Inputs** | Verified: MOCCAE release fee 500 AED/dog (C-003). Unverifiable: titer cost — MOCCAE publishes no figure (C-001); community range 700–1,300 AED. Conflict: Etihad official USD 399 vs community USD 1,500 (C-015). Community quote: IrbisKat (24 upvotes). |
| 6 | **Constraints** | Open with the reader's price fear in their words. **Hedge every unpublished number** ("no official figure; community reports X") — never assert it. Lead the Etihad point with the official value, then name the discrepancy. No "Get a Quote." Ban generic phrases ("competitive pricing", "affordable"). |
| 7 | **Examples** | The 5-layer structure; the "silence-as-proof" device (embed the MOCCAE page to show it lists no titer price). |
| 8 | **Output Format** | The 5 layers in order, markdown; each factual line tagged with its Source Bank C-ID. |
| 9 | **Quality Criteria** | Every published number cites a Verified row; every unpublished number is hedged; a reader could use it to challenge an unfair quote; passes the Hormozi "would you put your name on it" test. |

The two elements people skip — **Constraints** and **Quality Criteria** — are the two that decide whether the draft is usable. *(Library: P-16 Ban Generic Language; P-11 Real Examples Mandatory.)*

---

## Step 3 — Generate the first draft

Paste the assembled 9-element prompt into the model. Expect a strong-but-imperfect first draft — that is normal and is what the revision loop is for.

## Step 4 — Evaluate against the Quality Criteria (element 9)

Read the draft against *your own* Quality Criteria, not a vague "is this good." For the page above: did every number get cited or hedged? Did it open with the fear? Did any banned generic phrase slip in? Mark exactly what misses.

## Step 5 — Run the revision loop (2–3 rounds)

State **what to change AND what to keep** — never only what's wrong. *(Library: F-09 Nine-Element Prompt Revision Loop.)*

> "Good start. Revise: (1) hedge the 700–1,300 AED line — it currently reads as the official price; (2) move the Etihad USD 399 fact up and name the USD 1,500 discrepancy. **Keep:** the opening fear sentence and the MOCCAE-silence paragraph — those are working."

Saying only what's wrong lets the model fix the problem while breaking what already worked.

## Step 6 — Save what works

When a prompt produces a 70%+-usable draft, save it to the personal archive (`data/prompt-template-library.md` for reusable types; an archive note for one-offs). The library compounds — next time this page type starts from a working prompt, not a blank box.

---

## The Minimum Viable Prompt

For quick tasks, the floor is **Context + Role + Objective + Output Format**. Example: *"Dubai pet relocation, maximum-risk niche (context). You are a relocation specialist (role). Write 3 FAQ answers about the summer heat embargo, hedging anything MOCCAE doesn't publish (objective). Markdown Q&A (format)."* Never go below these four.

---

## The 10 common mistakes (pre-flight checklist)

1. Vague objective → generic output · 2. No audience → generic reader · 3. Information overload → confused priorities · 4. Conflicting constraints ("be brief" + "be comprehensive") · 5. No quality criteria → no standard · 6. One-shot expectation → no revision plan · 7. Not saving good prompts · 8. Ignoring output format → wall of text · 9. Wrong role for the task · 10. Not comparing models. *(Library: P-14 Vague Prompt = Generic Output.)*

---

## What you must not do

- **Do not send a question and hope.** Send a brief.
- **Do not omit Quality Criteria.** Without a standard the model has nothing to aim for and you nothing to judge against.
- **Do not let the model assert an Unverifiable fact.** Put the hedge in Constraints.
- **Do not revise with only "what's wrong."** Always say what to keep.
- **Do not start from scratch** when a saved prompt exists.

---

## Output of this manual phase

A handful of 9-element prompts written by hand, each producing a 70%+-usable first draft of a real page, plus the first reusable templates saved to the library. That is what makes File 04's automation implementable — the engine evaluates and varies prompts you have already proven by hand.
