# GEO Engine — Cheatsheet

*AI-citation readiness — Citation, Extractability, Entity corroboration (the AI-answer axis).*

| # | Measurement | What to do | Example (don't &rarr; do) |
|---|---|---|---|
| 1 | Citation Readiness · statistics | Add specific statistics (numbers, %, dated figures). | DON'T: 'Many pets travel.' &rarr; DO: '38,000 pets entered the UAE in 2025.' |
| 2 | Citation Readiness · source citations | Cite authoritative sources inline. | DON'T: Unsourced claims. &rarr; DO: Cited to MOCCAE / IATA inline. |
| 3 | Citation Readiness · quotations | Add direct quotes from named authorities. | DON'T: No quotes. &rarr; DO: A direct quote from a named authority. |
| 4 | Citation Readiness · quotable facts | Write self-contained factual sentences AI can lift verbatim. | DON'T: Facts tangled in prose. &rarr; DO: Self-contained sentences AI can lift verbatim. |
| 5 | Citation Readiness · freshness | Add a date and refresh facts on volatile topics. | DON'T: (no date) &rarr; DO: Updated June 2026, recent facts. |
| 6 | Extractability & Structure · passage self contained | Make each section stand alone as a complete answer. | DON'T: Sections depend on each other. &rarr; DO: Each section answers fully on its own. |
| 7 | Extractability & Structure · heading answer | Use question headings with the answer immediately under them. | DON'T: Vague heading. &rarr; DO: Question heading + answer right under it. |
| 8 | Extractability & Structure · answer first | Put the direct answer in the first ~200 words. | DON'T: Answer buried at the bottom. &rarr; DO: Answer in the first 200 words. |
| 9 | Extractability & Structure · scannable facts | Add lists/tables of the key facts. | DON'T: Wall of prose. &rarr; DO: A list/table of liftable data points. |
| 10 | Entity & Corroboration · entity coverage | Cover the related entities and sub-topics. | — |
| 11 | Entity & Corroboration · subquestion cover | Answer the related sub-questions on the page. | — |
| 12 | Entity & Corroboration · external corrob | (off-page — earn mentions on third-party sources) | — |
| 13 | Entity & Corroboration · entity schema | Add sameAs / Organization / Person schema. | DON'T: No entity markup. &rarr; DO: sameAs / Organization / Person schema. |
| – | G4 · cited in aio (human-judged) | reviewed by a person | — |
| – | G4 · citation breadth (human-judged) | reviewed by a person | — |
| – | G4 · ugc presence (human-judged) | reviewed by a person | — |
| – | G4 · decoupling diag (human-judged) | reviewed by a person | — |

**Run:** `python skill-engines/geo/engine.py --url <URL>` or `--serve 8111` (web checker).
