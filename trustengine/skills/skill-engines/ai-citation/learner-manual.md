# AI Citation Readiness — Learner Manual

When someone asks ChatGPT, Google's AI Overview, Perplexity or Gemini a question, the engine writes one answer and quotes a few sources. Being one of those quoted sources is the whole game — research shows pages with statistics, cited sources and clean structure get cited up to 40% more. This tool measures the on-page signals that decide whether you are the page it quotes, or the page it ignores.

## How to run the engine
- Score a page: `python skill-engines/ai-citation/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/ai-citation/engine.py --serve 8090`
- These docs: `python skill-engines/ai-citation/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Answer-first opening

**How we measure it:** We read the first ~120 words and check whether the page answers the question immediately (a definition, a number, a direct statement) instead of warming up with an intro.

**Why it works:** AI engines lift the opening of a page. If your answer is buried under 'Welcome to our company', the engine lifts a competitor's answer instead. Answer-first = liftable.

**What to do:** Put a direct answer (a number or definition) in the first 100 words.

## Example (what NOT to do -> what to do)
- DON'T: Welcome to our pet relocation company.
- DO: A dog is held at Dubai airport when its rabies titer paperwork is incomplete; the release fee is 500 AED.

## 2. Statistics & specific numbers

**How we measure it:** We count the specific quantified facts on the page — percentages, prices, dates, counts, durations.

**Why it works:** Adding statistics is one of the strongest citation levers measured (~+24.9%). A concrete number ('500 AED', '90 days', '66%') is exactly the kind of fact an engine quotes verbatim.

**What to do:** Add specific numbers, %, prices and dated figures to the page.

## Example (what NOT to do -> what to do)
- DON'T: We move many pets safely.
- DO: 256,114 pets were transported in 2021, with an incident rate below 1 in 10,000.

## 3. Cited sources

**How we measure it:** We look for citation phrases ('according to', 'source:', 'per …') and outbound links to authoritative domains (.gov, .edu, .org).

**Why it works:** Citing sources is the single biggest citation lever (~+27.8%). Engines prefer claims that are backed by an authority over claims that just assert themselves.

**What to do:** Cite authoritative sources (link .gov/.edu/official pages; use 'according to…').

## Example (what NOT to do -> what to do)
- DON'T: Pets need vaccinations.
- DO: Per MOCCAE, pets need a microchip, rabies vaccination and import permit (moccae.gov.ae).

## 4. Direct quotations

**How we measure it:** We detect quoted passages — direct quotes from named people or authorities.

**Why it works:** Quotation is a top lever (~+25.9%). A self-contained quote is easy for an engine to attribute and reuse, so quote-rich pages get pulled into answers more often.

**What to do:** Add a direct quote from a named authority.

## Example (what NOT to do -> what to do)
- DON'T: Our service is trusted.
- DO: “The route is the product,” says a relocation specialist quoted by Reuters (2025).

## 5. Quotable standalone facts

**How we measure it:** We count short, self-contained factual sentences (a fact with a number or named entity, under ~30 words) that would still make sense lifted out of the page.

**Why it works:** Engines extract sentence-level chunks, not whole pages. A standalone, accurate sentence can be quoted as-is; a long marketing sentence cannot.

**What to do:** Write short, self-contained factual sentences that can be lifted verbatim.

## Example (what NOT to do -> what to do)
- DON'T: There are many requirements to consider.
- DO: The export health certificate is valid for 10 days from the date of issue.

## 6. Question-style headings

**How we measure it:** We scan H2/H3 subheadings for question words (how, what, why, when, can, is …) followed by an answer.

**Why it works:** Question headings mirror how people prompt AI. A page structured as Q→A maps directly onto the engine's retrieval, so each section becomes a candidate answer.

**What to do:** Use question-style H2/H3 headings (How…/What…) with the answer underneath.

## Example (what NOT to do -> what to do)
- DON'T: Our Services
- DO: How much does the rabies titer test cost in Dubai?

## 7. Scannable lists & tables

**How we measure it:** We count lists and tables — structured data points an engine can lift cleanly.

**Why it works:** Lists and tables are the most extractable format on the web; a comparison table or step list is often quoted wholesale into an AI answer.

**What to do:** Add lists and a comparison table for the key facts.

## Example (what NOT to do -> what to do)
- DON'T: We cover the EU, Australia and more.
- DO: A table: EU — 30 days | Australia — 180 days.

## 8. FAQ structured data

**How we measure it:** We check the page's machine-readable code for FAQPage / Question schema (the data engines read directly), and count the Q&A pairs.

**Why it works:** FAQ schema hands the engine clean question→answer pairs in a format it parses natively — the easiest possible thing to cite.

**What to do:** Add 5+ FAQ Q&A as FAQPage JSON-LD (validate with Rich Results Test).

## Example (what NOT to do -> what to do)
- DON'T: (no FAQ on the page)
- DO: Add FAQPage schema with 5 Q&A, e.g. “Can pets fly to Dubai in summer?”

## 9. Clear, consistent entity

**How we measure it:** We look for Organization/Person schema and a 'sameAs' identity (links to verified profiles) that tell engines exactly who you are.

**Why it works:** Engines only cite sources they can identify and trust. One consistent identity lets them build a profile of you; a fragmented identity gets skipped.

**What to do:** Add Organization/Person schema with a sameAs to your verified profiles.

## Example (what NOT to do -> what to do)
- DON'T: Names vary: PetCo / Pet Co. / petco dubai
- DO: One Organization schema, one name, sameAs linking LinkedIn + IPATA profile.

## 10. Freshness & dating

**How we measure it:** We check for recent years and dating language ('updated', 'published', a visible date).

**Why it works:** On topics that change, engines favour current sources. A visible recent date signals the fact is still good; an undated page reads as possibly stale.

**What to do:** Add a visible published/updated date and a recent year.

## Example (what NOT to do -> what to do)
- DON'T: © 2019 (or no date)
- DO: Updated June 2026 — verified against current MOCCAE rules.
