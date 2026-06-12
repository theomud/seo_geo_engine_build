# Prompt Engineering (output clarity) — Learner Manual

Prompt engineering is a creation-process skill — but its result shows on the page: content that is structured, answer-first, specific and machine-readable instead of vague AI mush. This engine scores those observable signals. The prompt/brief quality itself is off-page and shown as Not Measurable.

## How to run the engine
- Score a page: `python skill-engines/prompt-engineering/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/prompt-engineering/engine.py --serve 8100`
- These docs: `python skill-engines/prompt-engineering/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Answer-first output

**How we measure it:** We check the opening for a direct answer.

**Why it works:** Good prompting produces an answer up front; vague prompting produces a warm-up.

**What to do:** Open with the direct answer (re-prompt for answer-first).

## Example (what NOT to do -> what to do)
- DON'T: A long preamble before the point.
- DO: The direct answer in the first sentence.

## 2. Clear structure

**How we measure it:** We count sectioning headings.

**Why it works:** Structured output is the hallmark of a well-briefed generation.

**What to do:** Break the output into clear H2/H3 sections.

## Example (what NOT to do -> what to do)
- DON'T: One block of text.
- DO: H2 sections for each part.

## 3. Scannable formats

**How we measure it:** We count lists and tables.

**Why it works:** Lists/tables show the content was shaped, not dumped.

**What to do:** Add lists/tables for key points.

## Example (what NOT to do -> what to do)
- DON'T: Prose only.
- DO: A bulleted list of the steps.

## 4. Specific, not generic

**How we measure it:** We measure concrete-figure density.

**Why it works:** Specifics are what a good brief forces; generic mush is what a lazy prompt returns.

**What to do:** Re-prompt with required facts so the output is specific, not generic.

## Example (what NOT to do -> what to do)
- DON'T: Generic advice.
- DO: Specific figures and named examples.

## 5. Right length / focused

**How we measure it:** We check word count against a focused range.

**Why it works:** Good prompting controls scope; bloat and thinness both signal a weak brief.

**What to do:** Tighten scope in the prompt — cut padding or thicken thin content.

## Example (what NOT to do -> what to do)
- DON'T: 3,000 words of padding.
- DO: ~800 focused words.

## Prompt/brief quality (the 9 elements) (human-judged)

Off-page — the prompt itself isn't on the page; review the brief against the 9-element model.

## Revision-loop discipline (human-judged)

Off-page — how the output was iterated isn't visible on the page.
