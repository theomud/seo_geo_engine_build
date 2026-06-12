# Engine — Prompt Engineering
## Spec for the prompt-evaluation engine (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. It **evaluates and improves** human-written prompts; it never writes the initial brief.

## What it does (per prompt)
1. Parse a human-written DRAFT_PROMPT; map its text to the 9 elements.
2. Anthropic API scores each element `present|weak|missing` with a one-line reason.
3. Flag Gate-set-A failures (File 03) — especially a missing hedge rule for an Unverifiable input, or untestable Quality Criteria.
4. Suggest a concrete fix per weak/missing element; output an improved prompt + 2–3 variations.
5. Write the evaluation to `data/prompt-evaluations/`; return to the human to approve a version.

## Inputs / outputs / guardrails
- **Inputs:** a human-written draft prompt, the content-type template from `data/prompt-template-library.md`, `ANTHROPIC_API_KEY`.
- **Outputs:** `data/prompt-evaluations/<name>.json` (element scores + gap flags + improved prompt + variations); prompts that pass Gate sets A+B promoted into `data/prompt-template-library.md`.
- **Never invents a brief** — returns an error if no draft is supplied.
- **Never removes a cited Source Bank C-ID** from Inputs.
- **Hand back to human:** no draft supplied; a business fact missing from Inputs; final Quality Criteria; choosing the winning variation; any output that would assert an Unverifiable claim.
- **Test phase:** evaluate the 4 hand-written gap-page prompts, PAUSE, human review before scaling.
- **Audit:** 20% blind re-evaluation; 90% agreement; B3 (no asserted Unverifiable claim) a hard pass.

## Status
**Spec complete; Python engine not yet built.** The skill is proven via the hand-built template library (`data/prompt-template-library.md`) tested on the 4 universal-gap pages; the evaluation engine scales that pattern when built.

## Library codes
M-09 Nine-Element Prompt · M-16 COSTAR · M-17 PICO/TCEPFT · F-09 Revision Loop · F-17 Agile Prompt Loop · P-14 Vague=Generic · P-16 Ban Generic Language. Full citations in `MFP-LIBRARY.md`.
