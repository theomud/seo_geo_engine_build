# Engine — Content Structure for Trust
## Spec for the page-structure / brief-generation engine (read files/04-automation-spec.md first)

This engine implements the automation specified in `files/04-automation-spec.md`. It drafts trust-first pages from fear + Source Bank data; it does not publish.

## What it does (per keyword)
1. Read intent (Column J) + fear (Column K) from the fear-mapped keyword spreadsheet.
2. Select the page type from the Intent × Fear matrix (9 types) and the depth level (1–4).
3. Gather the relevant **Verified** Source Bank rows (and any Unverifiable rows to hedge), plus the matching official-source screenshot.
4. Anthropic API drafts all 5 layers (fear acknowledgement → verified answer → process/evidence → related fears → help-first CTA), citing each claim inline (Proof Interstitial).
5. Write a brief row to `data/content-structure-briefs.md` and a first-draft page to `data/content-structure-templates/<page-type>/<slug>.md`.

## Inputs / outputs / guardrails
- **Inputs:** fear-mapped keyword spreadsheet (intent J + fear K), Verified Source Bank rows, official-source screenshots, `ANTHROPIC_API_KEY`.
- **Outputs:** `data/content-structure-briefs.md`, draft pages under `data/content-structure-templates/`, a saved skeleton per page type.
- **Automation level:** ~60% — Layer 1 (fear acknowledgement) and Layer 5 (CTA) always get human judgement.
- **Test phase:** draft the 4 universal-gap pages, PAUSE, human-check against File 03 before scaling.
- **Hand back to human:** no Verified row for a required claim; ambiguous page type; generic fear quote; depth off by >25%; any Emergency / Case Study / Trust page.
- **Audit:** 20% blind re-check against the File 03 gates; 90% pass threshold.

## Status
**NOT YET BUILT.** This is the spec; the Python engine and its real output depend on the manual proof run (Phase 3 — building the first 4 universal-gap pages by hand).

## Library codes
M-07 Five-Layer Page · M-08 Nine-Page-Type · F-08 Proof Interstitial · F-16 Content Architecture Hierarchy · P-03 Proof Over Promise · P-05 One Fear Per Page. Full citations in `MFP-LIBRARY.md`.
