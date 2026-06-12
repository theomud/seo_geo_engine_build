---
Status: draft — built 2026-06-01
Area: skill-ai-citation
Depends on: skill-ai-citation/files/01-what-is-this-skill.md, skill-ai-citation/README.md
Feeds into: skill-ai-citation/files/03-how-to-verify-it.md, skill-ai-citation/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Optimising a page for AI citation by hand — answer first, stats + sources, schema, one entity

---

## Why manual first

The citeable answer is a human act of verified specificity — the exact figure, the exact source,
the honest "no official figure." An AI can format schema, but if an AI *writes* the answer it
regresses to the generic, unsourced mush the skill exists to beat. So write the answer boxes and
the entity definition by hand; automation validates the schema and monitors citations afterwards.
*(Library: P-01 Manual Before Automated; P-17 Direct-Answer-First; P-18.)*

Three things on the desk before you start:
1. **The target queries** — the AI-answered questions you want to be cited for (from the keyword/
   fear data; the four universal gap questions for the proof niche).
2. **The verified facts** — the C-IDs that answer each query, plus the honest hedges where no
   official source exists.
3. **The entity facts** — the canonical name, the Entity-Home URL, the credentials, and the
   verified profile links for the `sameAs` array.

---

## Step 1 — Write the direct-answer box (first 100 words)

For each page, write a **quotable answer to the target query as the opening**, in ~40–100 words.
*(Library: P-17.)* Sentence one must answer the question directly — "a pet is held when its
paperwork is incomplete", "there is no official published price", "yes, but airlines restrict
summer cargo". An engine lifts the opening; bury the answer and it lifts a competitor's instead.

---

## Step 2 — Put a statistic and a citation inside that answer

The answer box must contain **≥1 named statistic AND ≥1 cited source** *(Library: P-18 — stats +
sources + structure = up to 40% more citations)*. "500 AED per dog (C-003)", "valid 90 days
(C-010)", "USD 399 official vs ~USD 1,500 community (C-015)". Where no official figure exists, the
honest hedge is *itself* citeable: "no official price (C-001); community 700–1,300 AED." A number
without a source, or a source without a number, leaves citation lift on the table.

---

## Step 3 — Add FAQ schema (≥5 Q&A)

Below the answer, write **5+ question–answer pairs** as FAQPage JSON-LD *(Library: P-18 structured
formatting; M-22 AEO surface)*. Use the real questions people ask (the target query and its
variants) and answer each in 1–3 sentences carrying the same verified facts. Valid schema lets the
engine extract clean Q&A and surfaces the page for featured snippets and AI answers. Validate it
with Google's Rich Results Test *(Library: P-47)* before publishing.

---

## Step 4 — Point the page at one Entity Home

Add a link/byline tying the page to the **single Entity Home**, using the **exact** canonical brand
name *(Library: M-23 Kalicube Entity Home; P-30 naming consistency)*. Every page crediting the same
consistently-named entity is what lets the engines build and trust a single identity — scattered or
inconsistent naming fragments it and the citation goes elsewhere.

---

## Step 5 — Build the entity definition document (once)

Create the canonical Entity Home: one name, one description used **identically everywhere**, the
disambiguation (what you are and are *not*), the real credentials (MOCCAE / IPATA / licence), and
the `sameAs` array of verified profiles, all in Organization/LocalBusiness JSON-LD with a stable
`@id`. *(Library: P-29 single entity home — a dedicated page, not the homepage; F-28 sameAs/Wikidata
linked-data stack.)* NAP (name, address, phone) must be byte-identical to every directory listing.

---

## Step 6 — Set up weekly citation monitoring (10 queries × 4 engines)

List **10 target queries** and, weekly, run each on ChatGPT, Perplexity, Google AI Overview and
Gemini; record whether your brand/page is cited and who is cited instead. *(Library: P-48; F-21.)*
Record a **pre-publication baseline** first — for the proof niche, 9/9 competitors omit these
answers, so the baseline is generic/uncited, which *is* the citation opportunity. The action loop:
a query you lose → strengthen the answer box and FAQ → re-submit → re-check.

---

## Worked example — the four gap pages

| Page | Direct-answer opening (stat + cite) | FAQ | Entity link |
|------|-------------------------------------|-----|-------------|
| Confiscation | "held when paperwork incomplete… 500 AED/dog (C-003), permit 90 days (C-010)" | 5 Q&A | ✓ |
| Titer cost | "no official price (C-001); community 700–1,300 AED; 500 AED release fee (C-003)" | 5 Q&A | ✓ |
| Which airport | "rules identical at all 3; cargo-only (C-022); permit online (C-019); Sharjah ~20 min (hedged)" | 5 Q&A | ✓ |
| Summer embargo | "yes, but airline heat rule; permit 90 days (C-010, C-019); no official embargo date (hedged)" | 5 Q&A | ✓ |

Result: 4/4 pages carry an answer-first box with a stat + a citation, 5 FAQ Q&A, and an Entity-Home
link → all four GEO gates met.

---

## What you must not do

- **Do not bury the answer.** If the first 100 words don't answer the query, the engine lifts
  someone else's.
- **Do not let a figure float.** Every statistic in an answer box carries a C-ID or an honest
  hedge, or it is cut.
- **Do not assert an unverified number.** "No official price — here's the community range" is more
  citeable than a confident guess.
- **Do not let an AI write the answer.** It regresses to generic, unsourced mush; the engine
  formats schema, the human writes the verified answer.
- **Do not fragment the entity.** One canonical name, one Entity Home, identical everywhere.
- **Do not ship invalid schema.** Validate FAQPage and Organization JSON-LD before publishing.

---

## Output of this manual phase

The four pages each have a first-100-words answer box (statistic + verified citation), FAQPage
schema (≥5 Q&A), and an Entity-Home link; the entity definition document exists with
Organization/`sameAs` schema; and a 10-query weekly monitoring checklist is set up. That output is
the real deliverable (`data/ai-citation-optimisation-output.md`) and the input to File 04 —
automation validates the schema and runs the monitor; the answer-writing stays human.
