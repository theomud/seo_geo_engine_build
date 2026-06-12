# CONVERSION COPY
## The words on the page that turn a scared reader into an enquiry — without exploiting the fear

---

## What This Skill Is

A page can be true, well-structured, and still convert nobody. Conversion Copy
is the skill that writes the *actual words* — the headline, the opening line that
names the reader's fear in their own language, and the call-to-action that offers
help before it asks for anything.

It is not "salesy" copywriting. In a regulated, high-fear market (moving a pet
across a border, where a mistake means the animal is refused entry) the writing
that converts is the writing that **acknowledges the fear and resolves it with a
verified answer** — then offers something genuinely useful. Hype repels this buyer.
Honesty, specificity, and proof convert them.

This skill takes the fear database (named fears in customer language) and the
verified Source Bank (facts with sources) as raw material, and produces the
finished headlines, openings, and CTAs for each page.

**Skill Value Score: 21/25**
- Difficulty: 4/5
- Automation Potential: 4/5
- Market Uniqueness: 4/5
- Commercial Value: 5/5
- Teachability: 4/5

**Status:** 🔨 Building (Dubai pet relocation, 2026-05-30)
**Niche-agnostic:** Yes — fear-acknowledging copy works in any regulated, high-stakes service market

---

## What It Produces

| Output | What it is |
|--------|-----------|
| Headlines | The H1 and key sub-heads that name the fear and promise a verified answer |
| Fear-acknowledging openings | The first 1–3 sentences that say the fear out loud, in the customer's own words |
| Help-first CTAs | The closing offer — something useful given *before* asking for the enquiry |

Built for the four universal gap pages, scored against a 10-criteria editorial scoring rubric (/50).

---

## The Three Moves (what the skill actually does)

1. **Name the fear in their words, not yours.** Pull the exact phrasing from
   community language (Column K fears, real quotes). "What happens if my dog is
   taken at the airport and never given back" beats "Navigating import regulations."
2. **Resolve it with a verified answer, immediately.** Fear without a credible
   resolution produces avoidance, not action (P-04). Every opening pairs the fear
   with a Source-Bank-cited fact or an honest hedge.
3. **Close with help, not pressure.** The CTA offers the checklist, the calculator,
   the embargo calendar — value the scared owner wants — instead of "Get a quote."

---

## Functional Quality Threshold (Check 46)

This skill's real output is **proven** only when all three hold for the four gap pages:

1. **Editorial gate:** each page's rewritten copy scores **40+/50** on a
   10-criteria editorial scoring rubric (/50).
2. **In-the-trenches voice:** every fear-acknowledging opening scores **4+/5** on the
   voice criterion — it uses real customer language (traceable to a named quote or
   Column K fear), is specific, and could not be mistaken for generic AI filler.
3. **Help-first CTA test:** every CTA passes *"would you rather receive this or get a
   quote?"* — a scared pet owner would genuinely prefer the offered thing (a real
   checklist/tool/answer) over a sales quote. A CTA that fails this is rewritten.

Output that misses any of the three is not done. The score is recorded in
`data/conversion-copy-output.md`.

---

## Inputs and Outputs

| Input | Source | Required |
|-------|--------|----------|
| Named fears in customer language | Fear database / Column K | Yes |
| Verified facts with sources | Source Bank (by C-ID) | Yes |
| The draft / current page (if rewriting) | Existing site or brief | Optional |
| Target keyword + page intent | Keyword/intent map | Yes |

| Output | Format | Contains |
|--------|--------|----------|
| Rewritten copy per page | Markdown | Headline + opening + CTA, before/after |
| Score per page | /50 + voice + CTA test | The proof the threshold is met |
| Source map | C-ID list | Every claim traced to a verified row or hedged |

---

## Proof

**Status:** 🔨 Building — Dubai pet relocation
**Real output (target):** the four universal-gap pages rewritten — headline,
fear-acknowledging opening, and help-first CTA each — scored in
`data/conversion-copy-output.md`.
**Gold-standard source language:** the Muze Gu confiscation quote (Facebook,
"Dog Lovers In UAE") and the IrbisKat price-gouging quote (Reddit r/dubai, 24
upvotes — highest in the dataset) anchor the fear-acknowledging voice.
**Skill Value Score (confirmed on completion):** 21/25.

---

## Environment Variables

```
ANTHROPIC_API_KEY=     # For the draft-and-score automation loop
PROJECT_ROOT=
```

---

## Standalone Test

Someone in a different regulated market (immigration, medical travel, financial
licensing) can use this skill without any other skill: supply your own named fears
and your own verified facts, run the three moves, score against the threshold. The
method is portable; only the fears and facts are niche-specific.
