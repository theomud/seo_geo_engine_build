# Trust Gap Analysis — Learner Manual

In high-stakes markets (relocation, immigration, health, legal, finance) people don't buy on keywords or price — they buy on trust. This tool scores a page on 10 concrete trust signals. Each one is a point the page either earns or misses; the misses are your highest-leverage fixes, ranked by how much trust each one would add back.

## How to run the engine
- Score a page: `python skill-engines/trust-gap/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/trust-gap/engine.py --serve 8091`
- These docs: `python skill-engines/trust-gap/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Fear named in first 100 words

**How we measure it:** We read the first ~120 words and look for the visitor's actual concern in their language.

**Why it works:** A frightened buyer decides in seconds whether you 'get' them. Naming the fear first earns trust; opening with 'Welcome to our company' loses them.

**What to do:** Name the customer's real fear in the first 100 words.

## Example (what NOT to do -> what to do)
- DON'T: Welcome — your trusted pet partner.
- DO: Worried your dog could be taken at the airport? Here's what triggers it and how to prevent it.

## 2. Official source cited

**How we measure it:** We look for links to government/authority sites (.gov, .edu, regulators) and citation phrases.

**Why it works:** In high-stakes markets a claim with no official source is just an assertion. A cited regulation is the difference between 'trust me' and 'here's the proof'.

**What to do:** Link the official/government source for each claim.

## Example (what NOT to do -> what to do)
- DON'T: Dubai requires certain documents.
- DO: Dubai requires an import permit — see MOCCAE (moccae.gov.ae).

## 3. Specific route / variant named

**How we measure it:** We check whether the page names a specific route or variant ('Dubai to UK') vs. 'all routes'.

**Why it works:** Specificity signals real experience. 'We handle all international routes' reads as a brochure; a named route reads as someone who has actually done it.

**What to do:** Name the specific route/variant (e.g. 'Dubai to UK').

## Example (what NOT to do -> what to do)
- DON'T: We cover all international routes.
- DO: Dubai to UK: titer test, 4-month wait, DEFRA rules.

## 4. Step-by-step process

**How we measure it:** We detect numbered/ordered steps and sequence language (first, then, next…).

**Why it works:** A worried person wants to know exactly what happens. A clear numbered process removes uncertainty, which is the thing stopping them from acting.

**What to do:** Add a numbered step-by-step process with timings.

## Example (what NOT to do -> what to do)
- DON'T: We handle everything for you.
- DO: 1. Microchip 2. Rabies vaccine 3. Titer test 4. Import permit 5. Fly.

## 5. Timeline included

**How we measure it:** We look for specific durations — days, weeks, months, hours.

**Why it works:** Vagueness about time breeds anxiety. Concrete durations let the buyer plan, and planning is the step before buying.

**What to do:** State the real timeline in days/weeks/months.

## Example (what NOT to do -> what to do)
- DON'T: Quick and easy relocation.
- DO: Plan 3–6 months: titer results take 21–28 days; the permit is valid 90 days.

## 6. Cost ranges shown

**How we measure it:** We look for real figures (currency + numbers); 'contact us for a quote' with no numbers scores low.

**Why it works:** Hiding all pricing reads as 'we'll work out how much we can charge you'. Honest ranges (even with caveats) are one of the strongest trust signals there is.

**What to do:** Show real cost ranges (numbers), not 'contact us for a quote'.

## Example (what NOT to do -> what to do)
- DON'T: Contact us for a quote.
- DO: Titer test 700–1,300 AED (no official price); release fee 500 AED (MOCCAE).

## 7. Common-mistakes section

**How we measure it:** We check for a 'common mistakes / what to avoid / pitfalls' section.

**Why it works:** Telling people what goes wrong proves you've seen it go wrong — i.e. real expertise — and it's exactly the reassurance an anxious buyer is searching for.

**What to do:** Add a 'common mistakes to avoid' section.

## Example (what NOT to do -> what to do)
- DON'T: (no mistakes section)
- DO: Common mistake: booking the flight before the titer results are back.

## 8. Original visuals (not stock)

**How we measure it:** We count images and flag ones whose source looks like a stock library; we check alt text.

**Why it works:** Stock 'happy customer' photos are invisible — readers tune them out. A real photo of the actual work is proof; a stock photo is decoration.

**What to do:** Replace stock photos with real photos of the actual work.

## Example (what NOT to do -> what to do)
- DON'T: A stock photo of a smiling dog.
- DO: A real photo of the actual crate prep and airport handover.

## 9. CTA feels like help

**How we measure it:** We compare help-first offers (download, checklist, guide, estimate) against pure asks (get a quote, contact us).

**Why it works:** Offering something useful before asking for anything lowers the visitor's guard. 'Get a quote' asks them to take a risk; 'download the checklist' gives them value first.

**What to do:** Offer something useful (a checklist/guide) before asking for the enquiry.

## Example (what NOT to do -> what to do)
- DON'T: Get a Quote
- DO: Download the Dubai pet-import checklist (verified vs MOCCAE 2026).

## 10. Proof beside every claim

**How we measure it:** We measure how densely proof signals (figures, citations, images) are spread through the page, not just parked in a testimonials block.

**Why it works:** Trust is built claim-by-claim. Proof sitting beside each statement is believed; proof quarantined in one 'reviews' section at the bottom is not.

**What to do:** Put proof beside each claim, not only in a testimonials block.

## Example (what NOT to do -> what to do)
- DON'T: A testimonials block at the bottom only.
- DO: A MOCCAE screenshot beside the 500 AED fee claim.
