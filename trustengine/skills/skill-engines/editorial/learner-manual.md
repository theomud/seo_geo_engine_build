# Editorial Quality — Learner Manual

AI writes content at about 60% quality — competent, complete, and forgettable. This skill is the gate that decides whether a page is strong enough to publish. It rewards the things that make content rank and convert (specificity, clarity, proof, a real call-to-action) and flags the 7 weak patterns that mark generic filler. Some judgements (is it true? is it on-brand? is it better than competitors?) need a human or your sources — those are shown as Not Measurable, never guessed.

## How to run the engine
- Score a page: `python skill-engines/editorial/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/editorial/engine.py --serve 8092`
- These docs: `python skill-engines/editorial/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Specific (real numbers & names)

**How we measure it:** We count concrete numbers and named entities per 500 words.

**Why it works:** Specifics are what make content credible and un-generic. 'We deliver results' applies to anyone; '256,114 pets moved in 2021' could only come from someone who did the work.

**What to do:** Add real numbers and named examples; cut generic claims.

## Example (what NOT to do -> what to do)
- DON'T: We deliver exceptional results.
- DO: We completed 450 moves in 2025 with a 99.6% on-time rate.

## 2. Clear & scannable

**How we measure it:** We count subheadings, lists and tables, and flag over-long paragraphs.

**Why it works:** A reader decides in ~10 seconds. Structure lets them find the answer; a wall of text loses them.

**What to do:** Break into subheadings and lists; shorten over-long paragraphs.

## Example (what NOT to do -> what to do)
- DON'T: One 400-word paragraph.
- DO: Three H2 sections + a 5-step list.

## 3. Proof / trustworthy

**How we measure it:** We count proof phrases and links to authoritative sources.

**Why it works:** Every claim needs backing. Show, don't tell — proof beside a claim is believed; a bare assertion isn't.

**What to do:** Back each claim with a number, source, or citation.

## Example (what NOT to do -> what to do)
- DON'T: We are the best provider.
- DO: Rated 4.8/5 across 283 reviews.

## 4. Clear call-to-action

**How we measure it:** We check for a clear next step / call-to-action.

**Why it works:** Content with no next step is a dead end. One clear action turns a reader into a lead.

**What to do:** Add one clear call-to-action.

## Example (what NOT to do -> what to do)
- DON'T: (no call-to-action)
- DO: Download the checklist.

## 5. No filler opening

**How we measure it:** We scan the first 60 words for stock openers ('In today's fast-paced world…').

**Why it works:** Filler openings signal AI-generated boilerplate and waste the most valuable real estate on the page.

**What to do:** Delete the filler opening; start with the reader's problem or a fact.

## Example (what NOT to do -> what to do)
- DON'T: In today's fast-paced world, pet travel is complex.
- DO: Moving a pet to Dubai takes 3–6 months. Here's the timeline.

## 6. No unsupported superlatives

**How we measure it:** We look for 'leading / best / #1 / world-class' without nearby proof.

**Why it works:** An unbacked 'the leading provider' reads as empty marketing and erodes trust. Prove it or cut it.

**What to do:** Replace 'leading/best' superlatives with a proof point, or cut them.

## Example (what NOT to do -> what to do)
- DON'T: The leading pet relocation company.
- DO: IPATA-accredited since 2018 (member #1234).

## 7. No vague jargon

**How we measure it:** We detect generic buzzwords ('innovative solutions', 'synergy', 'seamless', 'leverage').

**Why it works:** Jargon is the language of pages that have nothing specific to say — it's the opposite of credibility.

**What to do:** Cut buzzwords (innovative solutions, synergy, leverage, seamless).

## Example (what NOT to do -> what to do)
- DON'T: We leverage innovative solutions for seamless relocations.
- DO: We handle the permit, the titer test and the flight booking.

## 8. No fake enthusiasm

**How we measure it:** We flag hype words ('passionate', 'amazing', 'exceptional') and exclamation-mark overuse.

**Why it works:** Manufactured excitement reads as insincere. Show passion through specifics, not adjectives.

**What to do:** Remove hype words and excess exclamation marks; show, don't gush.

## Example (what NOT to do -> what to do)
- DON'T: We are absolutely passionate about amazing results!!!
- DO: We've moved 450 pets; here's how the process works.

## 9. Strong ending (no dead end)

**How we measure it:** We check the last 60 words for a real next step vs. a dead-end ('thanks for visiting!').

**Why it works:** The ending is where conversion happens. 'Thanks for reading' wastes it; a clear action captures it.

**What to do:** End with a clear next step, not 'thanks for visiting'.

## Example (what NOT to do -> what to do)
- DON'T: Thanks for visiting!
- DO: Next step: download the checklist and send us your flight date.

## Factually true (human-judged)

Needs source verification against official sources (the Source Bank).

## On-brand voice (human-judged)

Needs the brand's own voice/style to compare against.

## Speaks to the right buyer (human-judged)

Needs the customer persona to judge fit.

## Better than competitors (human-judged)

Needs a competitor comparison for the same query.
