---
Status: draft — built 2026-05-29
Area: skill-content-structure
Depends on: skill-content-structure/customer-profile/customer-profile-snapshot.md
Feeds into: skill-content-structure/files/02-how-to-do-it-manually.md, skill-content-structure/files/04-automation-spec.md
---

# Skill 03 · File 01 — What This Skill Is
## Niche-agnostic definition of Content Structure for Trust

---

## The problem this skill solves

Most content frameworks are built around a *topic*. This skill is built around the *fear behind the topic*.

In regulated service markets — pet relocation, immigration, medical travel, legal, financial, animal welfare — customers do not arrive at a page curious. They arrive **afraid**: afraid of getting it wrong, afraid of the consequence, afraid that nobody will tell them the truth. A page that opens with a company introduction, a keyword-stuffed heading, or a generic "Welcome" speaks past that fear and loses the reader in the first sentence.

Content Structure for Trust is the architectural framework that meets the fear head-on. It is **not a writing style** — it is a structural system. It determines what appears in the first 100 words, what the subheadings say, where the official sources appear, where the social proof sits, and what the call to action asks for. The structure is the same on every page; the content inside it changes per niche, persona, and route.

---

## What this skill produces

| Output | Format | Contains |
|--------|--------|----------|
| Page structure templates | .md + .html | One template per intent/page type |
| Content briefs | .xlsx | One brief per priority keyword |
| Page opening library | .md | Fear-acknowledging openings by fear category |
| CTA library | .md | Help-first CTAs by intent type |

The skill turns the upstream research assets into pages that convert: it consumes the fear-mapped keywords, the verified facts, and the competitor gaps, and outputs a brief a writer (or an engine) can fill in without re-deciding the structure each time.

---

## The core structure — every page, five layers

```
LAYER 1 — FEAR ACKNOWLEDGEMENT (first 100 words)
   The exact fear the customer arrived with, in their language, not the company's.
LAYER 2 — VERIFIED ANSWER
   The direct answer, cited against an official Source Bank entry
   (plain English + exact quote + URL + date verified).
LAYER 3 — PROCESS OR EVIDENCE
   The step-by-step, or the proof — screenshots of official documents,
   named sources. Not stock images, not generic assurances.
LAYER 4 — RELATED FEARS
   Two or three related fears, each internally linked to the page that resolves it.
LAYER 5 — HELP-FIRST CTA
   Not "Get a Quote." A useful resource that resolves a specific fear.
```

Trust is built in sequence, not all at once: Layer 1 earns emotional trust, Layer 2 informational trust, Layer 3 credibility, Layer 4 completeness, Layer 5 relational trust.

---

## The 9 page types — chosen by the Intent × Fear matrix

Every page in a regulated market fits one of nine types, selected in seconds from the keyword's intent (Column J of Customer Fear Intelligence — now 8 intent types) and its fear (Column K):

| Page type | Intent | Fear addressed |
|-----------|--------|----------------|
| Fear Resolution Page | Fear | A specific worst-case fear (e.g. confiscation) |
| Process Guide | Informational | Overwhelm — don't know where to start |
| Route/Variant Page | Commercial | Route-specific documentation mistake |
| Cost Transparency Page | Commercial | Price gouging — no way to know if fair |
| Comparison Page | Research | Choosing the wrong provider |
| Urgency Page | Urgency | Timeline — a deadline is approaching |
| Emergency Page | Emergency | Acute crisis happening now (pet stuck, flight imminent) |
| Case Study Page | Problem | "Will this actually work for someone like me?" |
| Trust Page | Research | "Can I trust this company/provider at all?" |

The three additions extend the framework to the full search-intent surface: **Emergency** pages serve the acute, happening-now crisis (distinct from a planned deadline — see the Urgency/Emergency intent split); **Case Study** pages document a real, completed relocation as proof; **Trust** pages concentrate credentials, licences, named team, and guarantees for the visitor whose fear is the provider itself.

The full matrix, openings formula, and per-type structural variations live in `files/02-how-to-do-it-manually.md` and `files/06-models-frameworks-principles.md`. How these page types connect into a journey — conversion-path design, sitemap and URL structure, navigation logic — is the domain of **Skill 31 — Content Architecture** (`skill-content-architecture/`); this skill structures the individual page, that skill structures the site.

---

## Why this is a standalone skill — not a step inside writing

1. **It outlives any single page.** The 5-layer structure and 9 page types are fixed assets; only the fear/fact/gap inputs change per market.
2. **It produces a defensible commercial asset.** The template + brief library is reusable across every page and licensable to anyone publishing in the same niche.
3. **It changes the brand position.** Pages that acknowledge the real fear and cite verified sources read fundamentally differently from pages that open with marketing copy.

---

## How it differs from a generic content framework

| Generic content framework | Content Structure for Trust |
|---------------------------|------------------------------|
| Organised around topic/keyword | Organised around the primary fear behind the keyword |
| Opening sets up the company/topic | Opening names the customer's exact fear in their own words |
| Facts asserted in the writer's voice | Every fact cited to a Verified Source Bank row |
| One fear/angle per article optional | Exactly one primary fear per page — related fears get their own pages |
| CTA = "Get a Quote / Contact Us" | CTA = a useful resource that resolves a specific fear |

---

## What this skill depends on (inputs from other skills)

| Input | Source skill | Required |
|-------|--------------|----------|
| Fear-mapped keywords (intent Col J + fear Col K) | `skill-customer-fear-intelligence` | Yes |
| Verified facts (Verified-only Source Bank rows) | `skill-official-source-research` | Yes |
| Community language (12 fear categories, verbatim quotes) | `skill-customer-fear-intelligence` | Yes |
| Competitor gap matrix (the 4 universal gaps) | `skill-trust-gap-analysis` | Yes |

**Verified before published:** no factual claim appears on a page without a Source Bank entry whose status is **Verified** — not Unverifiable, not Pending.

---

## In scope / out of scope

**In scope.** Page architecture, opening structure, layer sequencing, page-type selection, internal-link planning between related-fear pages, and CTA design.

**Out of scope.** The fear research itself (`skill-customer-fear-intelligence`), source verification (`skill-official-source-research`), competitor gap scoring (`skill-trust-gap-analysis`), and conversion-copy micro-wording (`skill-conversion-copy`). This skill assembles their outputs into a page; it does not produce them.

---

## What "good" looks like

A page built with this skill is good when:

- The first sentence names the customer's real fear in community language, not the company's voice.
- Every factual claim links to a Verified Source Bank row (plain English + quote + URL + date).
- At least one screenshot of an official source document appears as proof — not decoration.
- The page resolves **one** primary fear completely, with 2–3 related fears linked out.
- The CTA offers something immediately useful, not a sales ask.

Skill 03 is complete when the template + brief libraries exist for the proof niche, the first four pages (the four universal competitor gaps) are structured against all five layers, and each page passes the verification gates in `files/03-how-to-verify-it.md`.
