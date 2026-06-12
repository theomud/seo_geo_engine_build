# CUSTOMER FEAR INTELLIGENCE
## Turning keywords into the fears behind them — the intelligence layer for high-stakes content

---

## What This Skill Is

Most keyword research tells you *what* people search and how often. This skill tells you *what they are afraid of* behind the search — and routes every keyword to the right page on that basis.

In regulated, high-stakes service markets, customers do not arrive curious. They arrive afraid: of getting it wrong, of the consequence, of being misled. A keyword like "pet relocation to country X" is not an information request — it is *"I'm afraid the paperwork has a mistake that gets my pet rejected at the border."* Customer Fear Intelligence converts a flat keyword list into a structured intelligence asset: every keyword classified by **intent** and mapped to a verbatim, visceral **fear statement** in the customer's own language.

This is the upstream layer that makes downstream content convert: the fear is what a page must open with.

**Skill Value Score: 21/25**
- Difficulty: 3/5
- Automation Potential: 4/5
- Market Uniqueness: 5/5
- Commercial Value: 5/5
- Teachability: 4/5

**Status:** ✅ PROVEN
**Proven on:** Dubai pet relocation — 598 keywords classified, May 2026
**Niche-agnostic:** Yes — every regulated market has fears behind its keywords

---

## What Goes In

| Input | Format | Required |
|-------|--------|----------|
| Seed keywords | seeds.txt | Yes |
| Multi-source collection (Autocomplete + PAA + Related Searches) | API | Yes |
| Community language (Reddit + Facebook groups) | screenshots / API | Yes |
| Search-volume validation | API / manual | Optional |

## What Comes Out

| Output | Format | Contains |
|--------|--------|----------|
| Keyword intelligence spreadsheet | .xlsx | Every keyword with Column J (intent) + Column K (fear statement) |
| Fear database | .md | The fear categories + verbatim community quotes per fear |
| Intent + fear distribution | summary | Counts that drive the content calendar |

---

## The Core Method

### The 8 Intent Types (Column J)
Not the standard 4 buckets — adapted for high-stakes markets where the nuance decides the page:
**Informational · Problem · Fear · Urgency · Emergency · Commercial · Transactional · Research/Navigational.**

### The Fear Formula (Column K)
For every keyword, complete one sentence: **"I'm afraid that…"** — specific, visceral, tied to a real outcome, written in the customer's exact words (drawn from community research, never invented).

### Multi-Source Keyword Collection
Collect from five sources, not one: **Google Autocomplete + People Also Ask + Related Searches + Reddit + Facebook groups.** Community sources surface the language and worries keyword tools never show.

### The Five-Phase Methodology
1. **Market research** — how the published market already does keyword/intent work, and the gap this fills.
2. **Community research** — collect verbatim fear language from forums and groups.
3. **Manual verification** — classify a sample by hand to calibrate the rubric.
4. **Automation** — classify the full set (intent + fear) at scale; human reviews the highest-priority clusters.
5. **Audit** — a sub-agent re-checks a sample of classifications.

---

## Files In This Skill

```
skill-customer-fear-intelligence/
├── README.md                              ← this file
├── .env.example
├── customer-profile/
│   └── customer-profile-snapshot.md
├── files/
│   ├── 01-google-search-discovery.md      ← multi-source collection
│   ├── 02-intent-classification.md        ← the 8 intent types + decision process
│   ├── 03-fear-formula.md                 ← the "I'm afraid that…" mapping
│   ├── 04-sorting-funnel.md               ← keyword → page priority
│   ├── 05-volume-validation.md            ← search-volume validation
│   ├── 06-competitor-research.md          ← competitor/gap input
│   └── 06-models-frameworks-principles.md ← models / frameworks / principles
├── guides/                                ← study manuals + cheatsheets (intent, fear, funnel, volume)
├── data/
│   └── skill-01-keyword-collection.xlsx   ← 598 keywords, Columns J + K populated
└── engines/
    ├── keyword_engine.py                  ← multi-source collection engine
    ├── fear_classification_engine.py      ← intent + fear classification engine
    ├── engine-keyword-collection.md       ← collection engine spec
    └── fear-classification-prompt.md      ← classification prompt
```

---

## Functional Quality Threshold

This skill's real output — `data/skill-01-keyword-collection.xlsx` — meets the standard when: **≥500 keywords are collected from ≥5 distinct sources, 100% are classified by intent (Column J) AND mapped to a fear (Column K), every fear statement opens with "I'm afraid" and is ≤30 words, and every fear traces to documented community language (no invented fears).** Measured on the Dubai pet-relocation proof run: **598 keywords from 38 source tags across 6 method families; Column J 100% classified; Column K 100% populated; 100% of fears open with "I'm afraid" (14–29 words); 77.9% unique; all grounded in the 12-fear database sourced from 69 community screenshots.** A screenshot of the populated Columns J + K is in `data/screenshots/`. **Threshold MET.**

**Independence Test (Check 47): NOT YET TESTED** — only the original builder has produced the collection; no second person has independently reproduced a passing dataset. Acceptable addressed state for PROVEN; blocks COMMERCIALLY READY until TESTED.

---

## Proof

**Status:** PROVEN — Dubai pet relocation, May 2026
**Real output:** 598 keywords classified (Column J intent + Column K fear), 0 errors; 8-tab spreadsheet in data/.
**Audit:** fear-classification audit PASS (100% of fears start with "I'm afraid", all ≤30 words, distinct intent types present, 78% unique).
**Fear source:** a 12-fear database sourced from 69 community screenshots — fears matched to documented community language, never invented.
**Skill Value Score (confirmed):** 21/25.

---

## Applying To A New Market

**What changes per niche:**
- The seed keywords and the communities searched
- The fear database (that market's verbatim community language)
- The intent/fear distribution

**What stays the same:**
- Multi-source collection, the 8 intent types, the "I'm afraid that…" Fear Formula
- The classify-then-fear-map order, the sorting funnel, the 15% manual audit
- The engines (point them at new seeds)
