# Engine — Editorial Judgment & Quality Control
## Spec for the editorial QC engine (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. It **flags and pre-scores**; it never confirms a fact is true and never makes the publish decision (the 40% automation ceiling).

## What it does (per draft)
1. Scan for the **7 weak patterns** → record pattern + location + a specific suggested fix.
2. Extract factual claims → cross-check against the Verified Source Bank → **flag any uncited/unhedged claim** (an A2 risk from File 03).
3. **Pre-score the mechanical criteria** — 2 Specific, 4 Clear, 5 Commercial — with a reason each.
4. Run the **SEO block** of the publishing checklist (title/meta length, H1 keyword, keyword in first paragraph, internal links).
5. Write the editorial report; hand to a human for criteria 1, 6, 7, 8, 9, 10 + the final /50 and the publish/hold decision.

## Inputs / outputs / guardrails
- **Inputs:** an AI-generated draft, the Verified Source Bank (`skill-official-source-research/data/skill-02-source-bank.xlsx`) for the cited-claim cross-check, the brand guide, `ANTHROPIC_API_KEY`.
- **Outputs:** `data/editorial-reports/<name>.json` (weak-pattern flags + uncited-claim list + mechanical pre-score + SEO results + draft edit notes).
- **Never** asserts a fact is true (only whether it is cited); **never** outputs a total /50 or a publish verdict.
- **Hand back to human:** confirming a fact true; Better-than-competitors; Brand-aligned; Strong-enough-to-publish; the final /50 + publish/hold; any borderline 38–42 draft.
- **Test phase:** run the 4 universal-gap pages, PAUSE, human review before scaling.
- **Audit:** 20% blind re-run; 90% agreement on patterns + uncited claims; a false "cited" (uncited claim the engine passed) is a hard fail.

## Status
**Spec complete; Python engine not yet built.** The skill is proven via the hand-scored editorial scorecards (`data/editorial-scorecards.md`) — the 4 gap pages scored end-to-end, one real defect caught and fixed. The engine scales the flagging when built.

## Library codes
M-10 Ten-Criteria Quality · M-11 Content Depth · M-01 Verified Fact · F-06 Seven-Step Editorial · F-11 Forty-Five-Check Audit · F-31 Who/How/Why · P-13 Hormozi Test · P-11 Real Examples · P-03 Proof Over Promise. Full citations in `MFP-LIBRARY.md`.
