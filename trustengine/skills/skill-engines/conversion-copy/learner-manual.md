# Conversion Copy — Learner Manual

A page can be true, clean and well-structured and still convert nobody if it talks like a brochure to someone who arrived afraid. This engine scores the words that do the converting: a fear-acknowledging opening, a headline built from the resolved fear, social proof, answered objections, and a help-first call-to-action — never fear-exploiting.

## How to run the engine
- Score a page: `python skill-engines/conversion-copy/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/conversion-copy/engine.py --serve 8095`
- These docs: `python skill-engines/conversion-copy/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Fear-acknowledging opening

**How we measure it:** We read the first ~120 words for the reader's fear in their words.

**Why it works:** A scared buyer decides in seconds if you get them; naming the fear (then resolving it) earns the read.

**What to do:** Open with the customer's real fear in their words, then resolve it.

## Example (what NOT to do -> what to do)
- DON'T: Welcome to our company.
- DO: Worried your dog could be taken at the airport? Here's how to prevent it.

## 2. Headline from the resolved fear

**How we measure it:** We check the H1 for a question/benefit vs a generic 'Services/Welcome'.

**Why it works:** The headline is the ad for the page; a fear/benefit headline pulls the reader in, a brochure headline loses them.

**What to do:** Rewrite the H1 as the question they're asking or the answer they want.

## Example (what NOT to do -> what to do)
- DON'T: Pet Relocation Services in Dubai.
- DO: What happens if your dog is taken at Dubai airport — and the document that stops it.

## 3. Help-first CTA

**How we measure it:** We compare help offers (download/checklist/guide) vs pure asks (get a quote).

**Why it works:** Giving value before asking lowers the guard; 'Get a quote' asks the scared visitor to take a risk first.

**What to do:** Offer a useful free thing (checklist/guide) before asking for the enquiry.

## Example (what NOT to do -> what to do)
- DON'T: Get a Quote.
- DO: Download the airport checklist (free).

## 4. Social proof

**How we measure it:** We count reviews/ratings/testimonials and client-count signals.

**Why it works:** People follow others under uncertainty; visible proof others trusted you reduces the perceived risk.

**What to do:** Add real reviews/ratings or a specific client count.

## Example (what NOT to do -> what to do)
- DON'T: (no reviews shown)
- DO: Rated 4.8/5 across 283 reviews.

## 5. Objections answered

**How we measure it:** We look for FAQ/objection-handling language.

**Why it works:** An un-answered objection is a silent exit; answering it on-page removes the reason to leave.

**What to do:** Add an FAQ that answers the top objections directly.

## Example (what NOT to do -> what to do)
- DON'T: (no FAQ)
- DO: FAQ: "Can pets fly to Dubai in summer?"

## 6. Specific, not vague

**How we measure it:** We measure concrete-number density.

**Why it works:** Specifics convert; vague benefit-speak ('exceptional results') reads as empty and is ignored.

**What to do:** Replace vague claims with real numbers and specifics.

## Example (what NOT to do -> what to do)
- DON'T: Affordable, reliable service.
- DO: From 2,500 AED; realistic 3–6 month timeline.
