# AI CITATION & GENERATIVE ENGINE OPTIMISATION
## Make every page the one ChatGPT, Perplexity, Google AI Overview and Gemini cite

---

## What This Skill Is

Search is splitting in two. Half your buyers still click a blue link; the other half ask an AI
a question and read the answer it synthesises — and that answer cites a handful of sources and
drops the rest. Ranking #1 is worth nothing if the AI summarises the page above you and never
names you. AI Citation & Generative Engine Optimisation makes a page **citeable**: it leads with
a direct, quotable answer, backs every claim with a statistic and a named source, marks it up so
machines can lift it cleanly, and ties it to a single, consistent entity the AI can trust.

The method is research-backed, not folklore. The peer-reviewed GEO study (Aggarwal et al., KDD
2024 — Princeton / IIT Delhi / Georgia Tech / Allen Institute for AI) found that content with
**statistics + source citations + structured formatting** is cited up to **40% more often** by
generative engines. This skill turns that finding into three repeatable components: an **entity
definition** so the engines know who you are, a **direct-answer structure** so every page has a
citeable answer in the first 100 words, and **weekly citation monitoring** across the four major
AI platforms.

**Skill Value Score: 21/25**
- Difficulty: 3/5
- Automation Potential: 4/5
- Market Uniqueness: 5/5
- Commercial Value: 5/5
- Teachability: 4/5

**Status:** 🔨 Building (Dubai pet relocation, 2026-06-01)
**Niche-agnostic:** Yes — every market has questions AI answers and an entity that should be cited

---

## The Three Components

1. **Entity definition** — one canonical Entity Home (not the homepage) with an identical name,
   description and `sameAs` profiles everywhere, plus Organization/LocalBusiness schema, so Google
   and the LLMs cross-check and trust who you are. *(M-23 Kalicube Entity Home; P-29, P-30.)*
2. **Direct-answer structure** — every page opens with a quotable answer in the first 100 words
   that contains a statistic and a cited source, and carries FAQ schema (≥5 Q&A) so engines can
   lift it cleanly. *(P-17 direct-answer-first; P-18 stats + sources + structure = 40% lift.)*
3. **Citation monitoring** — a weekly check of 10 target questions across ChatGPT, Perplexity,
   Google AI Overview and Gemini, with an action loop to strengthen pages that lose. *(P-48; F-21.)*

---

## What It Produces

| Output | What it is |
|--------|-----------|
| 4 AI-optimised gap pages | Direct-answer box (first 100 words) + FAQ schema (≥5 Q&A) per page |
| Entity definition document | The single Entity Home + Organization/LocalBusiness + `sameAs` schema |
| Weekly citation monitoring checklist | 10 target queries × 4 AI engines, with an action loop |

---

## Functional Quality Threshold (Check 46)

This skill's real output is **proven** only when **every optimised page** meets all four on-page
GEO gates:

1. **A direct-answer box in the first 100 words** that directly answers the page's target query
   (P-17).
2. **At least one named statistic AND at least one verified Source-Bank citation (C-ID) inside
   that answer** — the stats-plus-sources half of the research-backed 40%-lift trifecta (P-18).
3. **Valid FAQPage schema with ≥5 Q&A pairs** (the structured-formatting half; the AEO/featured
   surface).
4. **A link to the single Entity Home with consistent naming** (M-23, P-29, P-30).

Measured **4/4** pages on all four gates in `data/ai-citation-optimisation-output.md`, with the
entity definition document and the 10-query monitoring checklist present. A page missing any gate
is not done.

**Live-citation confirmation is NOT YET CONFIRMED** — a real Perplexity/AI-Overview citation can
only be verified after the pages are published and indexed. That is the post-publication
validation step (the GEO equivalent of the independence test, Check 47), tracked in the
monitoring checklist — it does not block the on-page threshold above.

---

## Inputs and Outputs

| Input | Source | Required |
|-------|--------|----------|
| The pages to optimise (the 4 universal gap pages) | the content templates | Yes |
| Verified facts with sources (by C-ID) | the verified-source store | Yes |
| The entity facts (name, URL, credentials, profiles) | the business | Yes |
| The target queries to monitor | the keyword/fear data | Yes |

| Output | Format | Contains |
|--------|--------|----------|
| AI-optimised pages | Markdown + JSON-LD | direct-answer box + FAQPage schema per page |
| Entity definition | Markdown + JSON-LD | Entity Home + Organization/LocalBusiness + `sameAs` |
| Monitoring checklist | table | 10 queries × ChatGPT/Perplexity/AIO/Gemini + action loop |

---

## Proof

**Status:** 🔨 Building — Dubai pet relocation
**Real output:** the four universal HIGH-priority gap pages (confiscation, titer cost, which
airport, summer embargo — missing on 9/9 scored competitors) optimised for AI citation, plus the
entity definition and the 10-query monitoring checklist (`data/ai-citation-optimisation-output.md`).
**Threshold result:** **4/4** pages on all four on-page GEO gates; 20 FAQ Q&A total; every figure
cited to a verified C-ID (C-019, C-010, C-007, C-003, C-022, C-015) or honestly hedged (C-001).
**Anchor:** the GEO trifecta (statistics + source citations + structured formatting → ~40%
citation lift, Aggarwal et al. KDD 2024) is present on all four pages.
**Skill Value Score (confirmed on completion):** 21/25.

---

## Environment Variables

```
PROJECT_ROOT=          # absolute path to the project root on this machine

# Optional — only for the automated weekly citation monitor (querying the AI engines).
# The on-page optimisation (answer boxes, FAQ/entity schema) needs NO keys.
PERPLEXITY_API_KEY=    # query Perplexity for the 10 target queries
OPENAI_API_KEY=        # query ChatGPT for the same set
GEMINI_API_KEY=        # query Gemini for the same set
```

Automation 4/5: schema validation and the weekly citation monitor are automatable; writing the
direct-answer copy and judging citeability stay human. See `files/04-automation-spec.md`.

---

## Standalone Test

Someone in any market can use this skill alone: take a page, add a first-100-words answer box
with a statistic and a cited source, add FAQPage schema, point it at one consistent Entity Home,
and monitor 10 target queries weekly across the AI engines. The method is portable; only the
queries, the entity, and the verified facts are niche-specific.
