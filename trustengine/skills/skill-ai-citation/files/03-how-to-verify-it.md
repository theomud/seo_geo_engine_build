---
Status: draft — built 2026-06-01
Area: skill-ai-citation
Depends on: skill-ai-citation/files/02-how-to-do-it-manually.md
Feeds into: skill-ai-citation/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that prove a page is answer-first, sourced, schema-valid, and tied to one entity

---

## Why verification matters

AI-citation work fails in ways that look like success. A page can *feel* optimised — long, FAQ-ish,
confident — yet bury its answer below the fold (nothing for the engine to lift), assert numbers
with no source (nothing the engine will trust to cite), ship FAQ schema that doesn't validate
(the engine ignores it), or credit an entity named three different ways across the site (the
engine can't consolidate it). Each failure is invisible until you notice you're still not cited.
Verification proves the four things the research links to citation: **the answer comes first, it
carries a statistic and a source, the schema is valid, and the entity is one consistent thing.**

---

## Gate set A — per-page integrity (run on each page)

| Gate | Passes when |
|------|-------------|
| A1 · Answer-first | A direct answer to the target query sits in the first ~100 words (≤100), answering in sentence one. *(P-17)* |
| A2 · Stat + source in the answer | The answer box contains ≥1 named statistic AND ≥1 verified Source-Bank citation (C-ID), or an honestly-hedged absence anchored to a C-ID. No floating figure. *(P-18)* |
| A3 · Valid FAQ schema, ≥5 Q&A | FAQPage JSON-LD is present, parses/validates, and has ≥5 question–answer pairs. *(P-18; P-47)* |
| A4 · One consistent Entity Home | The page links to the single Entity Home using the exact canonical name. *(M-23, P-29, P-30)* |

A1 catches the buried answer; A2 catches both the unsourced assertion and the source-without-a-stat;
A3 catches schema that won't be machine-read; A4 catches a fragmented entity.

---

## Gate set B — the threshold check

The output clears the README's Functional Quality Threshold, counted across the 4 pages:

1. **Direct-answer box in first 100 words** — **4/4**.
2. **≥1 statistic AND ≥1 verified C-ID in the answer** — **4/4**.
3. **Valid FAQPage schema, ≥5 Q&A** — **4/4** (20 Q&A total).
4. **Entity-Home link, consistent naming** — **4/4**.
Plus: the entity definition document (Organization/LocalBusiness + `sameAs`) exists, and the
10-query monitoring checklist exists. Any gate unmet = the output is not done.

---

## The independent re-check (the core check)

A second person (a sub-agent or different human) verifies **blind to the builder's notes**:

- **Read only the first 100 words of each page** — is the target query actually answered there? If
  the answer is below, A1 fails.
- **Re-trace every figure in each answer box to a C-ID or an honest hedge** — a number with no
  citation and no hedge is a floating figure (A2 fail); a hedge not anchored to a verified C-ID
  also fails.
- **Validate each FAQPage and the Organization JSON-LD** (Rich Results Test or a parser) — invalid
  or <5 Q&A fails A3.
- **Check the entity name is byte-identical** on every page link and in the schema — any variant
  fails A4.

This is the gate polish can't fake: an engine either finds a quotable, sourced answer in the
opening and valid schema, or it doesn't.

---

## The audit sub-agent — verifying the verifier

After the build, a sub-agent re-runs A1–A4 on all 4 pages, re-validates the schema, and confirms
the entity doc and 10-query monitor exist. *(Library: P-07 Independent Verification.)* Pass
threshold: **4/4** on each gate, schema valid, entity consistent. A buried answer, a floating
figure in an answer box, invalid schema, or an inconsistently-named entity is a **hard fail** for
that page — fix and re-audit; a strong score elsewhere does not rescue it.

---

## The post-publication check (the live-citation step)

The on-page gates above are everything the skill *controls*. The outcome they're built for — an
actual AI citation — can only be verified **after publication**, via the weekly monitor: publish
and index the pages, then run the 10 target queries across the four engines and record citations.
*(Library: P-48; F-21.)* This is flagged **NOT YET CONFIRMED** until the pages are live — the GEO
equivalent of the independence test. The on-page threshold can fully pass before this step; this
step is what turns a citeable page into a confirmed citation.

---

## Worked check (the four gap pages)

A blind re-checker: A1 — reads the first 100 words of each and confirms the query is answered in
sentence one (confiscation, titer cost, airport, summer) ✔; A2 — re-traces 500 AED→C-003, 90
days→C-010, USD 399→C-015, and confirms the titer-price/embargo hedges are anchored (C-001; C-022)
✔; A3 — validates four FAQPage blocks, 5 Q&A each ✔; A4 — confirms each page links to one Entity
Home with the exact name ✔. Result: 4/4 on all gates → on-page threshold **passes**; live citation
**NOT YET CONFIRMED** pending publication.

---

## What downgrades / forces a rewrite

- The target query not answered in the first 100 words (buried answer).
- A statistic in an answer box with no C-ID and no honest hedge (a floating figure).
- FAQ schema that doesn't validate, or has fewer than 5 Q&A.
- The entity named inconsistently across pages, or pointing at the homepage instead of a dedicated
  Entity Home.
- An AI-written, generic answer with no verified specifics.

---

## Output of the verification phase

All 4 pages are answer-first with a stat + a verified citation, carry valid FAQ schema (≥5 Q&A),
and link to one consistently-named Entity Home; the entity definition and 10-query monitor exist;
an independent re-check reproduces 4/4. That verified discipline is what makes File 04's automation
safe — the engine validates schema and monitors citations, but it only ever checks human-written,
source-cited answers, and the live-citation outcome is tracked honestly post-publication.
