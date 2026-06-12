# GEO Engine — Learner Manual

The GEO engine scores how an AI answer engine decides to CITE a page: citation readiness (stats, quotes, sources), extractability (self-contained, answer-first passages) and entity corroboration. It is deliberately SEPARATE from the SEO engine — being cited is a different game from ranking. Live AI Overview presence (G4) needs an API and is Not Measurable here.

## How to run the engine
- Score a page: `python skill-engines/geo/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/geo/engine.py --serve 8111`
- These docs: `python skill-engines/geo/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Citation Readiness · statistics

**How we measure it:** Specific numbers, %, dated figures

**Why it works:** Maps to GEO paper v3 levers: Cite +27.8%, Quote +25.9%, Stats +24.9% (T4)

**What to do:** Add specific statistics (numbers, %, dated figures).

## Example (what NOT to do -> what to do)
- DON'T: 'Many pets travel.'
- DO: '38,000 pets entered the UAE in 2025.'

## 2. Citation Readiness · source citations

**How we measure it:** Inline citations to authoritative sources

**Why it works:** Maps to GEO paper v3 levers: Cite +27.8%, Quote +25.9%, Stats +24.9% (T4)

**What to do:** Cite authoritative sources inline.

## Example (what NOT to do -> what to do)
- DON'T: Unsourced claims.
- DO: Cited to MOCCAE / IATA inline.

## 3. Citation Readiness · quotations

**How we measure it:** Direct quotes from named authorities

**Why it works:** Maps to GEO paper v3 levers: Cite +27.8%, Quote +25.9%, Stats +24.9% (T4)

**What to do:** Add direct quotes from named authorities.

## Example (what NOT to do -> what to do)
- DON'T: No quotes.
- DO: A direct quote from a named authority.

## 4. Citation Readiness · quotable facts

**How we measure it:** Self-contained standalone factual sentences

**Why it works:** Maps to GEO paper v3 levers: Cite +27.8%, Quote +25.9%, Stats +24.9% (T4)

**What to do:** Write self-contained factual sentences AI can lift verbatim.

## Example (what NOT to do -> what to do)
- DON'T: Facts tangled in prose.
- DO: Self-contained sentences AI can lift verbatim.

## 5. Citation Readiness · freshness

**How we measure it:** Dated / recently updated on volatile topics

**Why it works:** Maps to GEO paper v3 levers: Cite +27.8%, Quote +25.9%, Stats +24.9% (T4)

**What to do:** Add a date and refresh facts on volatile topics.

## Example (what NOT to do -> what to do)
- DON'T: (no date)
- DO: Updated June 2026, recent facts.

## 6. Extractability & Structure · passage self contained

**How we measure it:** Sections stand alone as extractable answers

**Why it works:** Maps to Chunk/passage extraction in RAG (T2)

**What to do:** Make each section stand alone as a complete answer.

## Example (what NOT to do -> what to do)
- DON'T: Sections depend on each other.
- DO: Each section answers fully on its own.

## 7. Extractability & Structure · heading answer

**How we measure it:** Clear H2/H3 questions with immediate answers

**Why it works:** Maps to Chunk/passage extraction in RAG (T2)

**What to do:** Use question headings with the answer immediately under them.

## Example (what NOT to do -> what to do)
- DON'T: Vague heading.
- DO: Question heading + answer right under it.

## 8. Extractability & Structure · answer first

**How we measure it:** Key answer in first 200-300 words

**Why it works:** Maps to Chunk/passage extraction in RAG (T2)

**What to do:** Put the direct answer in the first ~200 words.

## Example (what NOT to do -> what to do)
- DON'T: Answer buried at the bottom.
- DO: Answer in the first 200 words.

## 9. Extractability & Structure · scannable facts

**How we measure it:** Lists/tables of liftable data points

**Why it works:** Maps to Chunk/passage extraction in RAG (T2)

**What to do:** Add lists/tables of the key facts.

## Example (what NOT to do -> what to do)
- DON'T: Wall of prose.
- DO: A list/table of liftable data points.

## 10. Entity & Corroboration · entity coverage

**How we measure it:** Named entities/concepts a fan-out seeks

**Why it works:** Maps to Fan-out breadth + corroboration bias (T2/PRIMARY)

**What to do:** Cover the related entities and sub-topics.

## 11. Entity & Corroboration · subquestion cover

**How we measure it:** Answers the cluster of related sub-queries

**Why it works:** Maps to Fan-out breadth + corroboration bias (T2/PRIMARY)

**What to do:** Answer the related sub-questions on the page.

## 12. Entity & Corroboration · external corrob

**How we measure it:** Claim/brand corroborated across sources

**Why it works:** Maps to Fan-out breadth + corroboration bias (T2/PRIMARY)

**What to do:** (off-page — earn mentions on third-party sources)

## 13. Entity & Corroboration · entity schema

**How we measure it:** sameAs/Org/Person schema to verifiable profiles

**Why it works:** Maps to Fan-out breadth + corroboration bias (T2/PRIMARY)

**What to do:** Add sameAs / Organization / Person schema.

## Example (what NOT to do -> what to do)
- DON'T: No entity markup.
- DO: sameAs / Organization / Person schema.

## G4 · cited in aio (human-judged)

Live AI-Overview citation outcome — PRIMARY via SerpApi AIO.

## G4 · citation breadth (human-judged)

Live AI-Overview citation outcome — PRIMARY via SerpApi AIO.

## G4 · ugc presence (human-judged)

Live AI-Overview citation outcome — PRIMARY via SerpApi AIO.

## G4 · decoupling diag (human-judged)

Live AI-Overview citation outcome — PRIMARY via SerpApi AIO.
