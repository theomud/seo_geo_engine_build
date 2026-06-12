# Engine — AI Citation & Generative Engine Optimisation
## Spec for the schema validator + GEO gate-checker + weekly citation monitor (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. It **checks, validates,
and monitors** — it never writes the direct-answer copy (the moment an AI writes the answer it
loses the verified, sourced specificity that makes it citeable). Automation 4/5: the on-page GEO
gates and schema are machine-checkable, and the weekly citation monitor is fully automatable; the
answer-writing and the citeability judgement stay human.

## What it does
1. **GEO gate-check (per page)** — confirm a direct-answer box exists in the first ~100 words,
   that it contains ≥1 statistic AND ≥1 verified C-ID, that FAQPage schema with ≥5 Q&A is present,
   and that an Entity Home link with the exact brand name is present. Flag any gate that fails.
2. **Schema validation** — parse the FAQPage and Organization/LocalBusiness JSON-LD; confirm it is
   valid and the `sameAs`/NAP are present and consistent. (Mirror Google's Rich Results Test — P-47.)
3. **Weekly citation monitor** — query each AI engine (Perplexity/OpenAI/Gemini APIs) for the 10
   target queries; record whether the brand/page is cited and which source is cited instead; emit
   the action loop (queries lost → strengthen + re-check). *(P-48; F-21.)*

## The GEO gate-check core (deterministic)
```python
import re
CID = re.compile(r'\bC-\d{3}\b')
STAT = re.compile(r'\b\d[\d,]*\s?(AED|USD|%|days?|hours?|minutes?)\b', re.I)
def geo_gates(answer_box_text, faq_qa_count, has_entity_link):
    return {
        "g1_answer_first_100w": 0 < len(answer_box_text.split()) <= 100,
        "g2_stat_and_cite": bool(STAT.search(answer_box_text)) and bool(CID.search(answer_box_text)),
        "g3_faq_schema_5plus": faq_qa_count >= 5,
        "g4_entity_home_link": bool(has_entity_link),
    }
# a page passes only when all four are True; a failed gate is flagged for a human.
```

## Inputs / outputs / guardrails
- **Inputs:** the page drafts (with their answer boxes + FAQ JSON-LD), the verified facts (C-IDs),
  the entity facts, the 10 target queries, `PROJECT_ROOT` (+ optional `PERPLEXITY_API_KEY`,
  `OPENAI_API_KEY`, `GEMINI_API_KEY` for the monitor).
- **Outputs:** per-page GEO gate results, schema-validation results, and the weekly citation
  report (cited y/n per query per engine + the action loop).
- **Never** writes or rewrites the direct-answer copy; **never** invents a fact or a figure (it
  checks that one is cited, not whether the citation is correct); **never** declares a page "will
  be cited" — it reports what the engines actually cite.
- **Hand back to human:** writing the answer boxes; judging citeability; confirming a cited fact
  is true; deciding the entity's canonical name/credentials.
- **Audit:** a sub-agent re-runs the GEO gate-check (4/4 pages), re-validates the schema, and
  confirms the monitoring checklist covers 10 queries × 4 engines. A missing answer box, an
  invalid schema, or a floating (uncited) figure in an answer box is a hard fail.

## Status
**Spec complete; the GEO gate-check was applied to the real output (the proof).** The four
optimised pages in `data/ai-citation-optimisation-output.md` pass all four gates (direct-answer
box ≤100 words, ≥1 stat + ≥1 C-ID, FAQPage ≥5 Q&A, Entity Home link), the entity definition
carries Organization/LocalBusiness + `sameAs` schema, and the 10-query monitoring checklist is
defined. Live-citation confirmation is the post-publication step the monitor runs after the pages
go live. The engine checks and monitors; the answers stay human-written and source-cited.

## Library codes
M-22 GEO/AEO/LLMO · M-23 Kalicube Entity Home · M-24 E-E-A-T Four-Pillar · M-30 Algorithmic
Trinity · M-31 YMYL · F-21 RAG/Open-World Citation Loop · F-28 sameAs/Wikidata Linked-Data Stack ·
F-31 Who/How/Why Self-Assessment · P-17 Direct-Answer-First · P-18 Stats+Sources+Structure=40% ·
P-29 Single Entity Home · P-30 Naming Consistency · P-48 Weekly AI Citation Tracking · P-47
Validate Schema. Full citations in `MFP-LIBRARY.md`.
