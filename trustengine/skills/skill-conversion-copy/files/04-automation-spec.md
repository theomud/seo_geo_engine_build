---
Status: draft — built 2026-05-30
Area: skill-conversion-copy
Depends on: skill-conversion-copy/files/02-how-to-do-it-manually.md, skill-conversion-copy/files/03-how-to-verify-it.md
Feeds into: skill-conversion-copy/engines/engine-conversion-copy.md
---

# Skill · File 04 — Automation Spec
## What the conversion-copy engine drafts and pre-scores, and what stays human

---

## Automation target

**~70% of the work can be automated** — higher than Editorial Judgment's 40%,
because drafting *candidate* headlines, openings, and CTAs from a named fear plus a
verified fact is exactly what an LLM does well. What stays human is the one thing the
machine cannot be trusted with in a high-fear market: the final call on whether the
copy *acknowledges* the fear or *exploits* it. *(Library: F-19 PAS; M-21 Cialdini;
P-04 Fear-Acknowledging Not Fear-Exploiting.)*

What gets automated:
- **Draft the three moves** from inputs: 3 candidate openings, 3 headlines, 3
  help-first CTAs per page — each built from the supplied named fear + C-ID facts.
- **Bind every claim to a source** — the engine may only use facts passed to it from
  the Source Bank; it tags each with its C-ID or marks it `HEDGE`.
- **Pre-score voice** — rate each candidate opening /5 on the in-the-trenches rubric,
  with a reason naming the real language used.
- **Run the help-first CTA heuristic** — flag any CTA that is a bare ask ("contact
  us", "get a quote", "request a callback") as a likely fail.
- **Flag P-04 risk** — flag any opening that raises a fear without resolving it in
  the same passage (the dangerous failure from File 03, gate A2).
- **Flag uncited numbers** — any figure with no C-ID and no hedge.

What stays manual (the 30%):
- **The acknowledging-vs-exploiting verdict** — does this resolve the fear or just
  frighten? The load-bearing human call. *(P-04.)*
- **The final voice score** — the engine pre-scores; a human confirms the 4+/5.
- **Brand voice** — does it sound like this specific business?
- **Selecting the winning candidate** and the final CTA — human pick from the three.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| Named fear for the page | text | Column K / fear database (a real quote or fear category) |
| Verified facts (with C-IDs) | list | `skill-official-source-research/data/skill-02-source-bank.xlsx` |
| Page intent + target keyword | text | keyword/intent map |
| Current page/draft (if rewriting) | text | existing site |
| Anthropic API key | env | `ANTHROPIC_API_KEY` in `.env` |

The engine is **forbidden** from introducing any fact or figure not passed in the
verified-facts list. A number it invents is a hard audit fail.

---

## Outputs

| Output | Destination |
|--------|-------------|
| 3 candidate openings + 3 headlines + 3 CTAs per page, each with C-ID tags | `data/conversion-copy-output.md` |
| Voice pre-score /5 + reason per opening | same |
| Help-first CTA flag (pass/likely-fail) per CTA | same |
| P-04 risk flags + uncited-number flags | same |

The engine never sets the final voice score, never picks the winner, and never
declares the copy "done" — it hands a human three sourced candidates and the flags.

---

## Engine flow per page

```
for each page (named_fear, verified_facts, intent, keyword):
    1. draft 3 openings -> each must state the fear (from named_fear) AND resolve it
       using only verified_facts (tag each fact with C-ID, or mark HEDGE)
    2. draft 3 headlines from the resolved fear + keyword
    3. draft 3 help-first CTAs (offer-before-ask; one primary CTA)
    4. pre-score each opening /5 on the voice rubric, with a reason
    5. flag: any CTA that is a bare ask; any opening that agitates without
       resolving (P-04 risk); any number not in verified_facts (uncited)
    6. write candidates + flags to data/conversion-copy-output.md
    7. human selects, confirms voice 4+/5, confirms acknowledging-not-exploiting
    8. rate limit: 1s between API calls
```

---

## The generation system prompt

```
You are a conversion-copy assistant for a regulated, high-fear service market.
You DRAFT candidates and PRE-SCORE them. You NEVER pick the winner and you NEVER
declare copy final. You may ONLY use facts from VERIFIED_FACTS — never invent a
number, a figure, or a claim.

Given NAMED_FEAR (a real customer quote or fear category), VERIFIED_FACTS (each
with a C-ID), INTENT and KEYWORD, return ONLY JSON:
{
  "openings": [
    {"text":"<1-3 sentences: name the fear in their words, then resolve it>",
     "c_ids":["C-019", ...], "hedges":["<honest hedge text if any>"],
     "voice":0-5, "voice_reason":"<names the real language used>",
     "p04_risk":bool}    // true if it agitates without resolving — a failure
  ],
  "headlines": ["<names the fear + promises the verified answer>", ...],
  "ctas": [{"text":"<offer-before-ask>", "bare_ask":bool}],   // bare_ask=true likely fails help-first
  "uncited_numbers": ["<any figure not in VERIFIED_FACTS>", ...]
}

RULES:
- Every opening MUST resolve the fear it raises, in the same passage (P-04).
- Score voice high ONLY when the text uses language traceable to NAMED_FEAR and is
  specific enough that it could not front any other company's page.
- Mark bare_ask=true for "contact us", "get a quote", "request a callback", etc.
- NEVER output a fact, price, or figure that is not in VERIFIED_FACTS.
```

---

## Worked example (the titer-cost page)

Inputs: NAMED_FEAR = 7Ssisi's *"being quoted endless amount"*; VERIFIED_FACTS =
{titer cost: no official figure, community range 700–1,300 AED — HEDGE}. The engine
should return an opening that names the price-gouging fear and resolves it with the
honest hedge ("there is no official price, so here's the real range and how to stop
being overcharged"), voice ~5/5; a headline promising the sourced range; a
help-first CTA ("get the cost breakdown") with bare_ask=false; and **zero**
uncited_numbers — because it was given no fake single price to use. If it had emitted
"the test costs 700 AED" as fact, that is an uncited-number hard fail.

---

## Test phase (the 4 universal-gap pages, then PAUSE)

The engine drafts candidates for the four gap pages and stops. The human checks:
did every opening resolve the fear (no P-04 risk slipping through)? Did it stay
inside the verified facts (no invented numbers)? Are the voice pre-scores honest?
Did it correctly flag bare-ask CTAs? If it invents a fact or lets a P-04 risk pass
across the four, fix the prompt before scaling.

---

## Audit (after a batch)

A sub-agent re-runs **20%** of pages (minimum 3 — here all 4) blind and compares the
engine's P-04 flags, uncited-number flags, and bare-ask flags to a manual pass. Pass
threshold: **90%** agreement, with **zero missed inventions** (an invented number the
engine emitted as fact is a hard fail) and **zero missed P-04 risks** (an
agitate-without-resolve opening the engine scored as clean is a hard fail). Below
that → fix the engine prompt before any copy ships. *(Library: P-07 Independent
Verification.)*

---

## When automation must hand back to humans

- **The acknowledging-vs-exploiting verdict** — always human (P-04).
- **The final voice score and the winning candidate** — human pick from the three.
- **Brand voice** — does it sound like this business?
- **Any opening the engine flags p04_risk=true** — human rewrites; the engine does
  not self-clear a fear it raised.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| API-call pause | 1 second |
| Cost per page (3× each move) | ≈ $0.04–0.10 |
| Pages drafted per hour | ~250 |

---

## Files in this skill (created by the build)

```
skill-conversion-copy/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   └── conversion-copy-output.md        ← the 4 gap pages rewritten + scored (real output)
└── engines/
    └── engine-conversion-copy.md
```
