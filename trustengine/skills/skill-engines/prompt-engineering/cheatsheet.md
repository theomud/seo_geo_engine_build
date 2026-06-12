# Prompt Engineering (output clarity) — Cheatsheet

*Does the page read like a clear, well-briefed output — structured, specific, machine-readable?*

| # | Measurement | What to do | Example (don't &rarr; do) |
|---|---|---|---|
| 1 | Answer-first output | Open with the direct answer (re-prompt for answer-first). | DON'T: A long preamble before the point. &rarr; DO: The direct answer in the first sentence. |
| 2 | Clear structure | Break the output into clear H2/H3 sections. | DON'T: One block of text. &rarr; DO: H2 sections for each part. |
| 3 | Scannable formats | Add lists/tables for key points. | DON'T: Prose only. &rarr; DO: A bulleted list of the steps. |
| 4 | Specific, not generic | Re-prompt with required facts so the output is specific, not generic. | DON'T: Generic advice. &rarr; DO: Specific figures and named examples. |
| 5 | Right length / focused | Tighten scope in the prompt — cut padding or thicken thin content. | DON'T: 3,000 words of padding. &rarr; DO: ~800 focused words. |
| – | Prompt/brief quality (the 9 elements) (human-judged) | reviewed by a person | — |
| – | Revision-loop discipline (human-judged) | reviewed by a person | — |

**Run:** `python skill-engines/prompt-engineering/engine.py --url <URL>` or `--serve 8100` (web checker).
