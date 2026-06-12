# Customer Fear Intelligence — Learner Manual

Customers in high-stakes markets search from fear and confusion. This engine scores whether a page reflects real customer fear-intelligence: it names the fears, answers the real questions people ask, covers objections, uses real customer language, and reassures — instead of talking about the company.

## How to run the engine
- Score a page: `python skill-engines/customer-fear-intelligence/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/customer-fear-intelligence/engine.py --serve 8099`
- These docs: `python skill-engines/customer-fear-intelligence/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Fear acknowledged first

**How we measure it:** We scan the first ~120 words for the customer's fear.

**Why it works:** A frightened customer needs to feel understood immediately, or they leave.

**What to do:** Open by naming the customer's real fear in their words.

## Example (what NOT to do -> what to do)
- DON'T: We are a pet relocation company.
- DO: Worried your dog won't be allowed in? Here's what actually happens.

## 2. Range of fears covered

**How we measure it:** We count distinct fear/concern terms across the page.

**Why it works:** Customers carry several fears; covering the cluster keeps them engaged and builds trust.

**What to do:** Address the other fears this customer has, not just one.

## Example (what NOT to do -> what to do)
- DON'T: Only mentions cost.
- DO: Covers confiscation, documents, timeline and the summer embargo.

## 3. Real questions answered

**How we measure it:** We count question-form content (the queries people actually type).

**Why it works:** Answering the real questions matches search intent and AI retrieval.

**What to do:** Turn the real questions people ask into on-page Q&A.

## Example (what NOT to do -> what to do)
- DON'T: (no questions)
- DO: How much does the titer test cost? Can pets fly in summer?

## 4. Objections / FAQ

**How we measure it:** We look for FAQ/objection-handling.

**Why it works:** An unanswered objection is a silent exit; addressing it removes the reason to leave.

**What to do:** Add an FAQ that answers the top objections.

## Example (what NOT to do -> what to do)
- DON'T: (no FAQ)
- DO: FAQ: "Is cargo safe for my dog?"

## 5. Real customer voice

**How we measure it:** We look for quotes / 'owners say' real language.

**Why it works:** Real customer words resonate; brochure language reads as out-of-touch.

**What to do:** Use a real customer quote / the words customers actually use.

## Example (what NOT to do -> what to do)
- DON'T: Brochure copy.
- DO: Owners say: "I was terrified it would be taken at the airport."

## 6. Reassurance

**How we measure it:** We look for reassurance phrasing.

**Why it works:** Naming a fear without reassurance creates avoidance; reassurance turns fear into action.

**What to do:** Add reassurance ('here's exactly what to do') alongside each fear.

## Example (what NOT to do -> what to do)
- DON'T: (none)
- DO: You're not alone — here's exactly what to do, step by step.
