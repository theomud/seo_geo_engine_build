# AI Citation Readiness — Cheatsheet

*How likely AI answer engines are to quote this page — and exactly what to fix.*

| # | Measurement | What to do | Example (don't &rarr; do) |
|---|---|---|---|
| 1 | Answer-first opening | Put a direct answer (a number or definition) in the first 100 words. | DON'T: Welcome to our pet relocation company. &rarr; DO: A dog is held at Dubai airport when its rabies titer paperwork is incomplete; the release fee is 500 AED. |
| 2 | Statistics & specific numbers | Add specific numbers, %, prices and dated figures to the page. | DON'T: We move many pets safely. &rarr; DO: 256,114 pets were transported in 2021, with an incident rate below 1 in 10,000. |
| 3 | Cited sources | Cite authoritative sources (link .gov/.edu/official pages; use 'according to…'). | DON'T: Pets need vaccinations. &rarr; DO: Per MOCCAE, pets need a microchip, rabies vaccination and import permit (moccae.gov.ae). |
| 4 | Direct quotations | Add a direct quote from a named authority. | DON'T: Our service is trusted. &rarr; DO: “The route is the product,” says a relocation specialist quoted by Reuters (2025). |
| 5 | Quotable standalone facts | Write short, self-contained factual sentences that can be lifted verbatim. | DON'T: There are many requirements to consider. &rarr; DO: The export health certificate is valid for 10 days from the date of issue. |
| 6 | Question-style headings | Use question-style H2/H3 headings (How…/What…) with the answer underneath. | DON'T: Our Services &rarr; DO: How much does the rabies titer test cost in Dubai? |
| 7 | Scannable lists & tables | Add lists and a comparison table for the key facts. | DON'T: We cover the EU, Australia and more. &rarr; DO: A table: EU — 30 days | Australia — 180 days. |
| 8 | FAQ structured data | Add 5+ FAQ Q&A as FAQPage JSON-LD (validate with Rich Results Test). | DON'T: (no FAQ on the page) &rarr; DO: Add FAQPage schema with 5 Q&A, e.g. “Can pets fly to Dubai in summer?” |
| 9 | Clear, consistent entity | Add Organization/Person schema with a sameAs to your verified profiles. | DON'T: Names vary: PetCo / Pet Co. / petco dubai &rarr; DO: One Organization schema, one name, sameAs linking LinkedIn + IPATA profile. |
| 10 | Freshness & dating | Add a visible published/updated date and a recent year. | DON'T: © 2019 (or no date) &rarr; DO: Updated June 2026 — verified against current MOCCAE rules. |


**Run:** `python skill-engines/ai-citation/engine.py --url <URL>` or `--serve 8090` (web checker).
