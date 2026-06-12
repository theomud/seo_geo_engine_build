# Editing Standards (structural -> line -> copy -> plain language)

> Backed by `claim_bank.csv` (pillar `ai_assisted_writing_editing`). Edit in order; do not
> jump to grammar before structure is right. New facts introduced during editing must clear
> the AI-writer grounding rules.

## 1. Structural (developmental) edit -- fix the shape first

- [ ] The single goal of the page is clear (inform, compare, or convert).
- [ ] The conclusion/answer is front-loaded (inverted pyramid).
- [ ] Sections are ordered logically; each has a descriptive heading.
- [ ] Funnel stage is correct and there is a link to the money page + one primary CTA.
- [ ] Nothing essential is missing; nothing off-goal is padding the piece.

## 2. Line edit -- improve flow and clarity

- [ ] One idea per sentence where possible; vary sentence length for rhythm.
- [ ] Benefit before feature; concrete and specific over vague superlatives.
- [ ] Transitions guide the skimmer; bullets used for parallel items.
- [ ] Cut hedging and filler; active voice by default.

## 3. Copy edit -- correctness

- [ ] Grammar, spelling, punctuation (British English).
- [ ] Consistent terminology and entity names (matters for GEO).
- [ ] Every figure traces to a `numeric_verified` bank row; no un-banked facts.
- [ ] Links work and point to the right money/pillar page.

## 4. Plain-language pass -- readability as a guide, not a target

- [ ] Replace jargon with plain words; define unavoidable terms.
- [ ] Short paragraphs; scannable structure.
- [ ] Check a readability score for a sanity signal -- **do NOT game it.** Readability
      formulas are heuristics and weak predictors of true reading ease.
      *(emerging evidence; arXiv:2502.11150.)*

## Editor's refusal rule

If an edit would require asserting something the claim bank does not support, stop and flag
"NEEDS VERIFICATION" with the relevant `verify_method` -- do not invent to smooth the prose.
