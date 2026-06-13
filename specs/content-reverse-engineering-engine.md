# Content Reverse-Engineering Engine — Spec

> **Status: SPEC — build later.** Saved 2026-06-13. This is the design for a content-intelligence
> capability that studies *other people's* content + entire source ecosystems and extracts the
> repeatable mechanisms that create rankings, citations, trust, leads, and authority.
>
> Cross-references in the vault (`SKILL_MASTERY_OS`):
> `07-SEARCH-SCIENCE/content-os.md` (the build-output blueprint) ·
> `10-EXAMPLES-LIBRARY/` (where breakdowns land) ·
> `03-CUSTOMER-INTELLIGENCE/` (VOC / forums tier) ·
> `12-EVIDENCE/` (the source-tier discipline) ·
> `18-QUALITY-STANDARDS/` (the scoring rubric reused here).

---

## Primary objective

**Do not summarize content. Reverse-engineer it.** For any winning piece, discover:
- Why the content exists · why it ranks · why it converts · why AI systems cite it
- What psychological mechanisms it uses
- What patterns repeat across winning content

**Final objective: extract *systems*, not article summaries.** The output is reusable frameworks —
repeatable mechanisms — stored in a structured database, never copied articles.

---

## Analysis order (never skip a layer)

1. Business Context → 2. Audience → 3. Search Intent → 4. Information Architecture →
5. Writing Structure → 6. Psychology → 7. SEO → 8. GEO → 9. Trust → 10. Conversion → 11. Information Gain

---

## The 11 analysis layers (capture fields)

### 1. Business analysis
Why was this created? (traffic / leads / sell software / build authority / acquire backlinks /
support sales / educate / reduce support tickets / build audience.)
**Store:** `business_objective`, `confidence_score`.

### 2. Audience analysis
**Store:** `persona_name`, `experience_level`, `industry`, `pain_points`, `desires`, `objections`,
`fears`, `awareness_stage`.

### 3. Search intent
**Store:** `intent_type` (Informational / Commercial / Transactional / Navigational), `primary_query`,
`secondary_queries`, `question_variations`, `search_journey_stage`.

### 4. Information architecture
**Store the hierarchy:** H1, all H2s/H3s/H4s, content sections, lists, tables, images, videos,
downloads, tools, calculators, checklists, FAQs, CTA locations.

### 5. Writing analysis
**Store:** `headline_type`, `introduction_type`, `opening_hook`, `paragraph_length`,
`sentence_length`, `tone`, `voice`, `reading_level`, `transition_patterns`, `storytelling_usage`,
`analogy_usage`, `example_usage`, `question_usage`.

### 6. Psychology analysis
Identify and **store frequency** of: trust, authority, fear, curiosity, identity, belonging, status,
progress, certainty, safety triggers.

### 7. SEO analysis
**Store:** `primary_keyword`, `secondary_keywords`, `entities`, `internal_links`, `external_links`,
`anchor_text_patterns`, `schema_usage`, `faq_usage`, `title_structure`, `meta_structure`,
`topical_coverage`, `content_depth`, `word_count`.

### 8. GEO analysis
**Store:** `direct_answers`, `definitions`, `faq_count`, `answer_density`, `citation_opportunities`,
`entity_density`, `source_count`, `evidence_count`, `retrieval_friendly_sections`,
`semantic_chunk_count`, `machine_readability_score`, `AI_extractability_score`.

### 9. Trust analysis
Identify: experience signals, expertise signals, authority signals, trust signals, author profile,
sources, references, statistics, case studies, official citations.

### 10. Conversion analysis
Capture: CTA type, CTA location, lead-magnet usage, form usage, trust badges, testimonials,
guarantees, risk reversal, conversion pathway.

### 11. Information gain analysis
What is unique? Original research / data / framework / expert insight / case study / opinion /
novel conclusion. **Store:** `information_gain_score`.

---

## Screenshot collection procedure (per article)

`01-full-page.png` · `02-hero-section.png` · `03-introduction.png` · `04-h2-sections.png` ·
`05-faq-section.png` · `06-cta-section.png` · `07-author-section.png` · `08-sidebar.png` ·
`09-footer.png`. Store all. *(Engine already has a Playwright capture path — reuse it.)*

---

## Article database schema

`article_id` · `url` · `author` · `brand` · `publish_date` · `topic` · `intent` · `persona` ·
`business_objective` · `headline_type` · `intro_type` · `word_count` · `entity_count` · `faq_count` ·
`source_count` · `internal_link_count` · `external_link_count` · `trust_score` · `seo_score` ·
`geo_score` · `conversion_score` · `information_gain_score` · `overall_score`.

---

## Pattern discovery (after 100+ articles)

Identify and store recurring patterns: most common headline types, introductions, CTA placements,
FAQ structures, GEO structures, trust signals, citation patterns, information-gain patterns.

## Competitor cluster analysis

Group content by: brand · topic · industry · search intent · persona · journey stage · country ·
language. Compare patterns across clusters.

---

## Page-type analysis variants (not all pages analyzed the same)

| Page type | Capture |
|---|---|
| **Blog** | headline, intro, structure, FAQ, CTA, GEO elements |
| **Service page** | offer, trust signals, objections, CTA flow, proof |
| **Landing page** | headline, promise, benefits, proof, CTA |
| **Knowledge base** | definitions, relationships, internal linking, retrieval structure |
| **Homepage** | positioning, messaging, navigation, trust |
| **Comparison page** | differentiators, decision criteria, buyer intent |

### Website intelligence database (per page)
website · brand · url · page_type · intent · audience · funnel_stage · geo_score · seo_score ·
trust_score · conversion_score · information_gain_score.

---

## The Content Intelligence Source Hierarchy

The engine analyzes **every place knowledge exists**, not just competitor blogs. Elite teams study
ecosystems. Weighted tiers (pet-relocation examples):

| Tier | Source class | Purpose | Key questions | Weight |
|---|---|---|---|---|
| 1 | **Official sources** (govt depts, customs, vet authorities, airline policies, intl orgs) | Truth & accuracy | What are the actual rules? What changed? | 10/10 |
| 2 | **Research** (academic papers, industry research, white papers, surveys, market reports) | Evidence | What does the evidence say? What patterns exist? | 10/10 |
| 3 | **Industry leaders** (Ahrefs, HubSpot, CXL, Animalz, Backlinko) | Best practices | How do they structure / explain / convert? | 9/10 |
| 4 | **Subject-matter experts** (consultants, practitioners, specialists) | Experience | What do they know others don't? What mistakes recur? | 9/10 |
| 5 | **Competitors** | Market understanding | What's covered / missing / ranking? | 8/10 |
| 6 | **Forums & communities** (Reddit, Quora, FB groups, forums) | Customer language | What do people actually ask? What words/fears? | 8/10 |
| 7 | **Reviews** (Google, Trustpilot, product) | Pain points | Why happy? Why angry? | 8/10 |
| 8 | **YouTube** | Explanations | What topics/examples resonate? | 7/10 |
| 9 | **Podcasts** | Deep expertise | What stories/frameworks emerge? | 7/10 |
| 10 | **Conferences** | Future trends | What will matter next year? | 7/10 |

> Reconciles with the vault's evidence doctrine: own-research-first → official sources (Tier 1–2 =
> the A1/T1 grades) → named experts (Tier 3–4 = NAMED-EXPERT/CONSENSUS) → forums/reviews mined for
> VOC (Tier 6–7, feeds `03-CUSTOMER-INTELLIGENCE` the Fear Formula). Never grade a forum claim as truth.

---

## The elite level: multi-layer research per topic

For a topic (e.g. "Move dog from Dubai to UK"), gather across tiers — official regulations,
competitor guides, forum questions, review complaints, YouTube demonstrations, recent news, expert
advice, supporting research — then combine into **one knowledge graph**.

### Knowledge graph model

Replace `Keyword → Article` with:

```
Question → Entities → Relationships → Sources → Evidence → Insights → Content
```

The content is the *final output* of a much larger research-and-intelligence process. The mindset
shift: not "what keyword should we target?" but "what does the customer need to know, what do
authoritative sources say, what's being asked, what mistakes happen, what's missing — and how do we
become the best source on the internet for this topic?"

---

## Build notes — model strategy (Sonnet vs Opus)

Default to **Sonnet** for ~90% of this engine: research extraction, website/blog/SEO/GEO/competitor
analysis, content briefs, knowledge-graph population, vault maintenance, database population, pattern
extraction, QA scoring, markdown/doc/file generation.

Reserve **Opus** for ~10%: designing the multi-agent architecture, building major frameworks,
reconciling conflicting evidence, novel methodology design, and final synthesis across hundreds of
documents — the partner-level reasoning, not the analyst-level throughput.

**Hybrid orchestration:** when this runs as a multi-agent workflow, an Opus *orchestrator* can design
the run while **Sonnet sub-agents** do the parallel fan-out extraction/scoring (cheap, sufficient).
The Workflow tool supports per-agent model override for exactly this.

> The quality of this engine depends far more on the source hierarchy, research process, knowledge
> architecture, scoring system, QA process, reverse-engineering framework, and content database than
> on the model choice. A well-structured Sonnet system beats a poorly-structured Opus one almost every time.

---

## Final objective

**Do not copy articles. Extract systems.** The purpose of every analysis is to discover the
**repeatable mechanisms** that reliably create:

- **Rankings** · **Citations** · **Trust** · **Leads** · **Authority**

The output is always **reusable frameworks, not article summaries.** A breakdown that ends with "here
is what this article says" has failed; a breakdown that ends with "here is the transferable mechanism,
and here is how to deploy it on our content" has succeeded. The article is disposable; the system is
the asset.

---

## How this connects to what already exists

- **Output side** is already built: `content-os.md` (the universal content formula + DNA blend),
  the 21 validated page specs (`08-PAGE-WRITING-SYSTEM`), the 7-dimension scorer (`18-QUALITY-STANDARDS`).
- **This engine is the input side** — the research/intelligence that feeds the output side.
- **Existing engine skills to reuse:** `skill-website-audit`, `skill-content-architecture`,
  `competitors`, `skill-official-source-research`, `skill-editorial-judgment`, the Playwright
  screenshot path, and `graphify` (already produces a knowledge graph of the codebase — the same
  pattern applied to external content).
- **Examples Library** (`10-EXAMPLES-LIBRARY`) is the human-readable destination for the breakdowns;
  this engine is the systematic, database-backed version of what that library does by hand.

*Saved as a spec to build later. Faithful capture of the Content Reverse-Engineering Engine +
Source Hierarchy brief (Theo, 2026-06-13).*
