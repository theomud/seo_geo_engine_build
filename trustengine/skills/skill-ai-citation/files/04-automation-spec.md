---
Status: draft — built 2026-06-01
Area: skill-ai-citation
Depends on: skill-ai-citation/files/02-how-to-do-it-manually.md, skill-ai-citation/files/03-how-to-verify-it.md
Feeds into: skill-ai-citation/engines/engine-ai-citation.md
---

# Skill · File 04 — Automation Spec
## What the GEO engine checks, validates and monitors — and what stays human

---

## Automation target

**~60% of the work can be automated** (Automation 4/5). The on-page GEO gates and the schema are
machine-checkable, and the weekly citation monitor — querying the AI engines for the target
queries and recording who's cited — is fully automatable. What stays human is the part that makes
a page citeable in the first place: **writing the direct-answer copy and judging citeability.** An
AI that writes the answer regresses to the generic, unsourced mush the skill exists to beat. So the
engine **checks, validates, and monitors only.** *(Library: M-22 GEO/AEO/LLMO; P-17; P-18.)*

What gets automated:
- **GEO gate-check** — per page: answer box ≤100 words, ≥1 statistic AND ≥1 C-ID inside it,
  FAQPage schema with ≥5 Q&A, an Entity-Home link with the exact name; flag any failing gate.
- **Schema validation** — parse and validate the FAQPage and Organization/LocalBusiness JSON-LD;
  confirm `sameAs`/NAP present and consistent (mirrors Google's Rich Results Test — P-47).
- **Weekly citation monitor** — query Perplexity/ChatGPT/Gemini APIs for the 10 target queries,
  record cited/not + which source, emit the action loop. *(P-48; F-21.)*

What stays manual:
- **Writing the answer boxes and FAQ answers** — verified, sourced, specific. Always human.
- **Judging citeability** — is this genuinely the most quotable, trustworthy answer? Human.
- **The entity's canonical name/credentials** — a human decides; the engine checks consistency.
- **Confirming a cited fact is true** — the engine sees a citation, not its correctness.
- **Google AI Overview monitoring** — no official API; checked manually in the checklist.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| The page drafts (answer box + FAQ JSON-LD) | Markdown + JSON-LD | the human writer |
| The verified facts (C-IDs) | list | the verified-source store |
| The entity facts (name, URL, credentials, profiles) | record | the business |
| The 10 target queries | list | the keyword/fear data |
| AI-engine API keys (optional, for the monitor) | env | `.env` |

The engine is **forbidden** from writing or rewriting the direct-answer copy — it only checks,
validates, and monitors.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Per-page GEO gate results (4 gates, pass/flag) | build report |
| Schema-validation results (FAQPage + Organization) | build report |
| Weekly citation report (cited y/n per query per engine + action loop) | monitoring log |

The engine never declares a page "will be cited" — it reports the gate results, the schema
validity, and what the engines actually cite.

---

## Engine flow

```
for each page:
    1. extract the first-100-words answer box -> check word count <= 100, query answered
    2. regex the answer box: >=1 statistic AND >=1 C-ID  (else flag)
    3. parse FAQPage JSON-LD -> valid + >=5 Q&A           (else flag)
    4. check Entity-Home link present with exact canonical name (else flag)
validate the Organization/LocalBusiness JSON-LD (+ sameAs/NAP consistency)
weekly:
    for each of the 10 target queries, for each engine API:
        query -> record cited(brand/page)? + which source cited
    emit action loop: queries lost where our answer is stronger -> strengthen + re-check
```

## The GEO gate-check core (deterministic)
```python
import re
CID = re.compile(r'\bC-\d{3}\b')
STAT = re.compile(r'\b\d[\d,]*\s?(AED|USD|%|days?|hours?|minutes?)\b', re.I)
def geo_gates(answer_box, faq_qa_count, has_entity_link):
    w = len(answer_box.split())
    return {"g1": 0 < w <= 100,
            "g2": bool(STAT.search(answer_box)) and bool(CID.search(answer_box)),
            "g3": faq_qa_count >= 5,
            "g4": bool(has_entity_link)}   # all four True => page passes
```

---

## Worked example (the four gap pages)

Fed the four optimised pages, the engine: counts the confiscation answer box at 71 words (≤100 ✔),
finds "500 AED"/"90 days" + C-003/C-010 inside it (g2 ✔), parses 5 FAQ Q&A (g3 ✔), finds the
Entity-Home link with the exact name (g4 ✔) → page passes. It repeats for titer cost (86w),
airport (84w), summer (88w) → **4/4**. It validates the Organization JSON-LD + `sameAs`. The
weekly monitor (once live) queries the 10 target questions and records that, pre-publication, the
engines cite generic/competitor sources — the baseline gap.

---

## Test phase (the 4 pages, then PAUSE)

Run the gate-check + schema validation on the four pages; confirm 4/4 and valid schema. Then run
one monitoring pass against the live APIs for the 10 queries to confirm the monitor records
citations correctly. Only after the pages are published does the monitor produce meaningful
citation data; pre-publication it records the baseline.

---

## Audit (after a build)

A sub-agent re-runs the GEO gate-check (4/4), re-validates the schema, and confirms the entity doc
and 10-query monitor exist. A missing/buried answer box, an invalid schema, a floating figure in an
answer box, or an inconsistently-named entity is a **hard fail** regardless of the others.
*(Library: P-07 Independent Verification.)*

---

## When automation must hand back to humans

- **Writing the answer boxes / FAQ answers** — always human; the engine never authors copy.
- **Judging citeability and the canonical entity name** — human.
- **Confirming a cited fact is true** — the engine sees a citation, not correctness.
- **The live-citation verdict** — the monitor reports what's cited; a human reads the trend and
  decides the action loop.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| GEO gate-check + schema validation | milliseconds per page (local regex/parse) |
| Weekly citation monitor | a few AI-API calls per query × 10 queries × 3 engines — cents/week |
| Human cost | one-time answer-writing; weekly read of the monitor + action loop |

---

## Files in this skill (created by the build)

```
skill-ai-citation/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   └── ai-citation-optimisation-output.md   ← 4 optimised pages + entity def + monitor (real output)
└── engines/
    └── engine-ai-citation.md
```
