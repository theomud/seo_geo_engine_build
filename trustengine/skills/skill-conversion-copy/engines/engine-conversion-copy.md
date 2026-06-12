# Engine — Conversion Copy
## Spec for the conversion-copy generation engine (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. It **drafts
and pre-scores** candidates; it never picks the winner, never declares copy final,
and never introduces a fact not passed to it (the ~70% automation ceiling — the
acknowledging-vs-exploiting verdict stays human).

## What it does (per page)
1. Draft **3 openings** — each must state the named fear in the customer's words **and**
   resolve it in the same passage, using only the supplied `VERIFIED_FACTS` (tag each
   with its C-ID, or mark `HEDGE`).
2. Draft **3 headlines** from the resolved fear + the target keyword.
3. Draft **3 help-first CTAs** (offer-before-ask; one primary CTA).
4. **Pre-score voice** /5 per opening, with a reason naming the real language used.
5. **Flag risks:** any CTA that is a bare ask (`bare_ask`); any opening that agitates
   without resolving (`p04_risk`); any figure not in `VERIFIED_FACTS` (`uncited_numbers`).
6. Write candidates + flags to `data/conversion-copy-output.md`; a human selects the
   winner, confirms voice 4+/5, and confirms acknowledging-not-exploiting.

## Inputs / outputs / guardrails
- **Inputs:** the named fear (a real quote or Column K category), `VERIFIED_FACTS`
  (each with a C-ID) from the Source Bank
  (`skill-official-source-research/data/skill-02-source-bank.xlsx`), the page intent +
  target keyword, the current page if rewriting, `ANTHROPIC_API_KEY`.
- **Outputs:** per page — 3 openings + 3 headlines + 3 CTAs with C-ID tags, a voice
  pre-score + reason per opening, a help-first flag per CTA, and P-04 / uncited-number
  flags, written to `data/conversion-copy-output.md`.
- **Never** introduces a fact, price, or figure not in `VERIFIED_FACTS` (an invented
  number is a hard audit fail); **never** sets the final voice score; **never** picks
  the winning candidate; **never** declares copy "done".
- **Hand back to human:** the acknowledging-vs-exploiting verdict (P-04); the final
  voice score and winner selection; brand voice; any opening flagged `p04_risk=true`.
- **Test phase:** draft the 4 universal-gap pages, PAUSE, human review before scaling.
- **Audit:** 20% blind re-run; 90% agreement on the P-04, bare-ask, and uncited-number
  flags, with **zero missed inventions** and **zero missed P-04 risks** (each a hard fail).

## The generation system prompt
See `files/04-automation-spec.md` ("The generation system prompt") for the full JSON
contract: `openings[]` (text, c_ids, hedges, voice, voice_reason, p04_risk),
`headlines[]`, `ctas[]` (text, bare_ask), and `uncited_numbers[]`.

## Status
**Spec complete; Python engine not yet built.** The skill is proven via the
hand-written conversion copy (`data/conversion-copy-output.md`) — the 4 gap pages
rewritten end-to-end and scored (avg 47.0/50, voice 5.0/5, 4/4 help-first CTAs). The
engine scales the drafting when built; the human keeps the fear-acknowledging call.

## Library codes
M-21 Cialdini · M-20 Protection Motivation Theory · M-02 Fear Hierarchy · M-01 Verified
Fact · F-19 PAS · F-18 AIDA · F-20 AICPBSAWN · P-04 Fear-Acknowledging Not
Fear-Exploiting · P-11 Real Examples · P-13 Hormozi Test · P-03 Proof Over Promise.
Full citations in `MFP-LIBRARY.md`.
