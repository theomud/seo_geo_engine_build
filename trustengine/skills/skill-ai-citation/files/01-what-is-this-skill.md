---
Status: draft — built 2026-06-01
Area: skill-ai-citation
Depends on: skill-ai-citation/README.md
Feeds into: skill-ai-citation/files/02-how-to-do-it-manually.md, skill-ai-citation/files/04-automation-spec.md
---

# Skill · File 01 — What This Skill Is
## Niche-agnostic definition of AI Citation & Generative Engine Optimisation

---

## The problem this skill solves

A growing share of buyers never see your page. They ask ChatGPT, Perplexity, or Gemini a
question — or read Google's AI Overview at the top of the results — and they read the synthesised
answer, which names a few sources and silently discards the rest. In that world, ranking #1 is no
longer enough: if the engine summarises the facts from your page but cites the page above you (or
no one), you did the work and a competitor got the credit. Worse, in a high-fear market the AI may
answer with generic, unsourced reassurance that helps no one and builds no trust in anyone.

AI Citation & Generative Engine Optimisation solves it by making a page **the thing the engine
quotes**: a direct, quotable answer first; a statistic and a named source beside every claim;
machine-readable structure (FAQ schema) so the answer lifts cleanly; and one consistent entity the
engine can identify and trust. It is the difference between being *indexed* and being *cited*.

---

## What this skill produces

| Output | What it is |
|--------|-----------|
| AI-optimised pages | A direct-answer box (first 100 words) + FAQ schema (≥5 Q&A) per page |
| Entity definition document | The single Entity Home + Organization/LocalBusiness + `sameAs` schema |
| Weekly citation monitoring checklist | 10 target queries × 4 AI engines, with an action loop |

The rule that makes it scorable: **every optimised page has a direct-answer box in the first 100
words that contains a statistic and a verified citation, valid FAQ schema with ≥5 Q&A, and a link
to one consistent Entity Home.**

---

## The core idea — optimise for citation, not ranking

*(Library: M-22 GEO/AEO/LLMO.)* Generative engines don't rank ten links; they assemble one answer
and attribute it to a few sources. So the unit of victory changes from *position* to *citation*.
The peer-reviewed GEO study (Aggarwal et al., KDD 2024) measured what gets cited and found a clear,
repeatable pattern: content with **statistics + source citations + structured formatting** is
cited up to **40% more often** *(Library: P-18)*. This skill is that finding operationalised —
every page is built to carry the trifecta, and to answer first *(Library: P-17 direct-answer-first
— a quotable answer in the opening is what an engine can lift)*.

---

## The three components

1. **Entity definition** *(Library: M-23 Kalicube Entity Home; P-29, P-30.)* The engines must know
   *who* they're citing. That requires one canonical Entity Home (a dedicated About/entity page,
   not the scattered homepage), one identical name and description used everywhere, and a `sameAs`
   web of verified profiles, all tied together with Organization/LocalBusiness schema so Google and
   the LLMs corroborate a single, trustworthy entity.
2. **Direct-answer structure** *(Library: P-17, P-18.)* Every page opens with a quotable answer in
   the first 100 words that contains a statistic and a cited source, and carries FAQ schema (≥5
   Q&A) so engines can extract clean question–answer pairs.
3. **Citation monitoring** *(Library: P-48; F-21.)* A weekly check of 10 target questions across
   ChatGPT, Perplexity, Google AI Overview and Gemini, recording who gets cited, with an action
   loop to strengthen the pages that lose.

---

## A worked example (the proof niche)

The four universal HIGH-priority gap pages — confiscation, titer cost, which airport, summer
embargo (missing on 9/9 scored competitors) — are each given a first-100-words answer box. The
confiscation answer leads with *"a pet is held when its paperwork is incomplete… release fee 500
AED per dog (C-003), permit valid 90 days (C-010)"* — a quotable, statistic-bearing, cited answer
an engine can lift verbatim. The titer-cost answer leads with the **honest "no official price"**
(C-001) — which is itself a citation advantage, because an engine prefers a source that names what
is and isn't official over one asserting an unsupportable number. All four carry FAQ schema (5 Q&A
each) and link to one Entity Home. Result: **4/4** pages on all four GEO gates.

---

## How it differs from neighbouring skills

| Skill | Owns |
|-------|------|
| Content Architecture | where pages live and how they're found (sitemap, ≤3 clicks) |
| Conversion Copy | the words that convert the human reader on the page |
| **AI Citation & GEO** | making the page the **machine** quotes — answer-first, schema, entity |

Conversion Copy persuades the person; AI Citation persuades the *engine* to surface and credit the
page in the first place. One wins the click-through visitor; this one wins the cited answer that
decides whether a visitor ever appears.

---

## Why this is a standalone skill

1. **It targets a surface the others don't.** Ranking and conversion optimise the blue-link world;
   this optimises the synthesised-answer world that is taking its place. *(Market uniqueness 5/5.)*
2. **It's research-backed and measurable.** The 40%-lift trifecta and the on-page gates make
   "citeable" objective, not a guess.
3. **It's portable and teachable.** Every market has AI-answered questions and an entity that
   should be credited; the method (answer first, stats + sources, FAQ schema, one entity, monitor
   weekly) transfers cleanly.

---

## In scope / out of scope

**In scope.** Writing direct-answer boxes, FAQ schema, and the entity definition; designating the
single Entity Home and enforcing naming/`sameAs` consistency; the weekly citation-monitoring
process and action loop.

**Out of scope.** Originating the verified facts (cited from upstream), the page architecture and
internal linking, the conversion copy of the page body, and confirming a cited fact is still true
(the source-research re-verify cycle).

---

## What "good" looks like

- **A direct-answer box in the first 100 words** of every page that answers the target query.
- **A statistic and a verified citation inside that answer** (the stats + sources half of the
  40%-lift trifecta).
- **Valid FAQ schema, ≥5 Q&A** per page (the structured-formatting half).
- **One consistent Entity Home**, named identically everywhere, with Organization/`sameAs` schema.
- **Weekly monitoring** of 10 target queries across the four engines, with an action loop.

This skill is complete when the four gap pages are optimised to **4/4** on the on-page GEO gates,
the entity definition and 10-query monitor exist, and the audit passes. Live-citation confirmation
is the post-publication step the monitor runs once the pages are live.
