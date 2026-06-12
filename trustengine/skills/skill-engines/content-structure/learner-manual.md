# Content Structure for Trust — Learner Manual

In high-stakes markets people arrive afraid. A page that opens with 'Welcome to our company' loses them in the first sentence. This skill checks the 5-layer fear-first structure: (1) acknowledge the fear in the first 100 words, (2) give the verified answer immediately, (3) show the process/proof, (4) link the related fears, (5) end with a help-first call-to-action — with clear layered headings throughout. It measures structure, not prose.

## How to run the engine
- Score a page: `python skill-engines/content-structure/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/content-structure/engine.py --serve 8093`
- These docs: `python skill-engines/content-structure/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Layer 1 — fear acknowledged first

**How we measure it:** We scan the first ~120 words for the visitor's fear in their language.

**Why it works:** A frightened visitor decides in seconds whether you understand them. Naming the fear first earns the read.

**What to do:** Open the first 100 words on the customer's fear, in their words.

## Example (what NOT to do -> what to do)
- DON'T: About our company.
- DO: If you've been told your dog could be taken at Dubai airport — that fear is real. Here's how to prevent it.

## 2. Layer 2 — direct answer in the opening

**How we measure it:** We check the opening for a direct answer (a number, a definition, a yes/no).

**Why it works:** After the fear, the page must resolve it immediately. A buried answer loses the anxious reader.

**What to do:** Give the direct answer immediately after naming the fear.

## Example (what NOT to do -> what to do)
- DON'T: A long company intro before any answer.
- DO: Yes, pets can enter Dubai year-round, but airlines suspend cargo in summer heat.

## 3. Layer 2 — verified fact early

**How we measure it:** We look for a number AND a citation/source within the first ~250 words.

**Why it works:** The reassurance only works if it's backed. A cited fact near the top is what turns fear into trust.

**What to do:** Add a verified, cited fact near the top.

## Example (what NOT to do -> what to do)
- DON'T: It costs a lot.
- DO: The release fee is 500 AED per dog (MOCCAE, verified 2026).

## 4. Layer 3 — process / steps

**How we measure it:** We detect ordered lists and step language.

**Why it works:** Uncertainty is what blocks action. A clear step-by-step removes it.

**What to do:** Add the step-by-step process.

## Example (what NOT to do -> what to do)
- DON'T: We take care of the whole process.
- DO: Step 1 microchip … Step 5 fly.

## 5. Layer 3 — proof / evidence

**How we measure it:** We count images and proof references (official sources).

**Why it works:** Proof beside the claim is believed; an unbacked claim is not — especially in high-stakes niches.

**What to do:** Add proof (official-source screenshot / real images) beside claims.

## Example (what NOT to do -> what to do)
- DON'T: A stock image.
- DO: A MOCCAE screenshot beside the rule it proves.

## 6. Layer 4 — related fears linked

**How we measure it:** We count internal links to other pages.

**Why it works:** A worried visitor has several fears. Linking the related ones keeps them on-site and builds the cluster.

**What to do:** Link 2–3 related-fear pages internally.

## Example (what NOT to do -> what to do)
- DON'T: A dead-end page with no links.
- DO: Links to the 'summer embargo' and 'documentation mistakes' pages.

## 7. Layer 5 — help-first CTA

**How we measure it:** We compare help-first offers (download/checklist/guide) against pure asks (get a quote).

**Why it works:** Offering value before asking lowers the guard; 'Get a quote' asks the scared visitor to take a risk first.

**What to do:** End with a help-first CTA (checklist/guide), not 'get a quote'.

## Example (what NOT to do -> what to do)
- DON'T: Request a consultation.
- DO: Get the one-page airport checklist.

## 8. Layered heading structure

**How we measure it:** We count H2/H3 sectioning headings.

**Why it works:** The 5 layers need visible structure; a wall of text hides the answer and the path.

**What to do:** Add H2/H3 headings to segment the page into the 5 layers.

## Example (what NOT to do -> what to do)
- DON'T: A wall of text.
- DO: H2: 'What triggers confiscation' → 'The 3 steps that prevent it'.
