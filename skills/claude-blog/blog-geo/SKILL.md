---
name: blog-geo
description: >
  Audits a blog post for AI citation readiness and scores it 0-100, with
  per-platform fixes for ChatGPT, Perplexity, Claude, Gemini, and Google AI
  Overviews. Evaluates passage citability, Q&A formatting, entity clarity,
  structure, and AI-crawler access, then generates citation capsules. Load
  whenever the user wants content to be cited by AI assistants. Triggers:
  "geo", "ai citation", "ai optimization", "citation audit", "aeo",
  "perplexity optimization", "chatgpt citation", "rank in ChatGPT". NOT for
  Google organic rankings or combined Google+AI work — use blog-rewrite.
user-invokable: true
argument-hint: "<file-path>"
license: MIT
---

# Blog GEO: AI Citation Optimization Audit

Scores blog posts for AI citation readiness across ChatGPT, Perplexity, and
Google AI Overviews. Generates citation capsules and a 0-100 AI Citation
Readiness score with platform-specific recommendations.

## How to use this skill

Invoke with a file path: `/blog geo <file-path>` (for example, a pet-relocation
post like `sites/pawroute/content/exporting-a-dog-from-dubai.md`). The skill
reads the post, runs the 10-step audit below in order, and emits the report in
Step 10. It audits AI-assistant citability only — it does not change Google
organic rankings.

## North Star objective

Make the post the passage an AI assistant quotes when a user asks Maya's
question ("how do I export my dog from Dubai?"). Every check below serves one
goal: self-contained, attributable passages an LLM can lift verbatim and cite.

## Freedom dial: LOW (precision work)

This is a scoring rubric, not a judgment call. The point thresholds, weights,
and the 0-100 mapping are fixed — follow them mechanically so two runs on the
same post produce the same score. Variance here is failure. The ONE high-freedom
part is writing the citation capsules (Step 8): there the wording is yours, but
the 40-60 word length and claim+data+source structure are still mandatory.

## Cross-reference

This skill covers FLOW surface 3 (AI assistant citations: ChatGPT, Perplexity, Claude, Gemini, Copilot, You.com) and contributes to surface 2 (SERP plus AI Overviews). Surface mapping: `skills/blog/references/flow-alignment.md`.

For directly relevant AI-citation prompts (AI-supporting-pages-rewrite-prompt, ai-detector-test, ChatGPT discovery, visibility prompts), see `/blog flow optimize`.

## Key Research Data

Reference these benchmarks throughout the audit:

- Only 11% of domains cited by both ChatGPT and Perplexity (Digital Bloom, domain-level)
- 80% of LLM citations don't rank in Google's top 100 (Ahrefs)
- Brands 6.5x more likely cited through third-party sources (AirOps)
- 120-180 word sections get 70% more ChatGPT citations (SE Ranking, Nov 2025)
- Comparison tables with `<thead>` achieve 47% higher AI citation rates (directional)
- Content freshness: 76.4% of top citations updated within 30 days (Ahrefs, ~17M citations)

## Audit Process

### Step 1: Read Content

Extract from the blog post:
- Full content text and word count
- Heading structure (H1, H2, H3 hierarchy)
- Individual paragraphs and their word counts
- FAQ sections (if present)
- Schema markup (JSON-LD, microdata, RDFa)
- robots.txt mentions or meta robots directives
- Any TL;DR or summary boxes
- Comparison tables and their HTML structure
- Numbered/ordered lists
- Definition-style formatting

### Step 2: Passage-Level Citability (4 pts)

Check each section between headings for AI-extractable passages:

| Check | Criteria |
|-------|----------|
| Word count | Each section contains 120-180 word self-contained passages |
| Context independence | Each passage makes sense extracted from surrounding context |
| Claim structure | Passages contain: specific claim + supporting evidence + source attribution |
| Completeness | Passage answers a question without requiring reader to read adjacent sections |

**Scoring:** Count passages meeting all criteria vs total sections.
- 4 pts: 80%+ sections have citable passages
- 3 pts: 60-79%
- 2 pts: 40-59%
- 1 pt: 20-39%
- 0 pts: <20%

### Step 3: Q&A Formatting (3 pts)

Check heading format and answer structure:

| Check | Criteria |
|-------|----------|
| Question headings | 60-70% of H2s are phrased as questions |
| Answer-first format | Opening paragraph under each H2 provides a direct answer |
| FAQ section | Dedicated FAQ section with structured question-answer pairs |

**Scoring:**
- 3 pts: All three criteria met
- 2 pts: Two criteria met
- 1 pt: One criterion met
- 0 pts: None met

### Step 4: Entity Clarity (3 pts)

Check topic consistency and disambiguation:

| Check | Criteria |
|-------|----------|
| Canonical topic | One unambiguous primary topic per page |
| Consistent naming | Same entity name used throughout (no confusing synonyms) |
| Intro statement | Clear topic statement in the introduction paragraph |
| Title-content match | Title accurately reflects the content focus |

**Scoring:**
- 3 pts: All four criteria met
- 2 pts: Three criteria met
- 1 pt: One or two criteria met
- 0 pts: None met

### Step 5: Content Structure for Extraction (3 pts)

Check for AI-extractable content patterns:

| Check | Criteria |
|-------|----------|
| TL;DR box | 40-60 word standalone summary present at top |
| Comparison tables | Tables with proper HTML `<thead>` (47% higher citation rate) |
| Ordered lists | Numbered lists for processes and step-by-step instructions |
| Definition formatting | Key terms formatted with clear definition patterns |
| Citation capsules | 40-60 word definitive statements in each major section |

**Scoring:**
- 3 pts: 4-5 elements present
- 2 pts: 3 elements present
- 1 pt: 1-2 elements present
- 0 pts: None present

### Step 6: AI Crawler Accessibility (2 pts)

Check technical requirements for AI crawler indexing:

| Check | Criteria |
|-------|----------|
| Static HTML | Content rendered in static HTML, not behind JavaScript |
| robots.txt | Allows AI crawlers: GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot |
| Schema in HTML | Schema markup in static HTML, not JS-injected |
| Page size | Reasonable page size within AI crawler limits |

**Scoring:**
- 2 pts: All criteria met
- 1 pt: Most criteria met but one issue
- 0 pts: Multiple issues blocking AI crawlers

### Step 7: Platform-Specific Analysis

Evaluate the post for each AI platform's citation preferences:

#### ChatGPT
- Favors "Best X" listicles (43.8% of citations)
- Prefers well-cited, authoritative content
- Recency matters: recent updates get priority
- Domain authority influences citation likelihood

#### Perplexity
- Favors Reddit sources (6.6% of all citations)
- Rapid content decay: 2-3 day citation window
- Freshness is the most critical factor
- Community-validated content preferred

#### Google AI Overviews
- Favors Google properties (23% of citations)
- High Domain Rating strongly correlated with citation
- Present in 49% of SERPs
- Prefers content that already ranks well organically

For each platform, provide:
- Current citability rating (High / Medium / Low)
- Specific improvements to increase citation likelihood
- Content format recommendations

### Step 8: Generate Citation Capsules

For each H2 section in the post, write a citation capsule:

- **Length**: 40-60 words, self-contained
- **Structure**: Specific claim + data point + source attribution
- **Purpose**: A passage AI could directly quote as a citation
- **Format**: Present as a suggested addition the author can embed

Example:
```
According to [Source], [specific claim with number]. This represents
[context/comparison], making it [significance]. [Supporting detail
that reinforces the claim].
```

Generate one capsule per H2 section. Label each with the section heading
it belongs under.

### Step 9: Calculate AI Citation Readiness Score (0-100)

Map the 15-point subcategory scores to a 0-100 display score:

| Category | Raw Points | Display Weight | Max Display Score |
|----------|-----------|----------------|-------------------|
| Passage-Level Citability | /4 | x6.75 | 27 |
| Q&A Formatting | /3 | x6.67 | 20 |
| Entity Clarity | /3 | x6.67 | 20 |
| Content Structure | /3 | x6.67 | 20 |
| AI Crawler Accessibility | /2 | x6.5 | 13 |
| **Total** | **/15** | | **100** |

Rating thresholds:
- 90-100: Excellent: highly citable by AI systems
- 70-89: Good: citable with minor improvements
- 50-69: Needs Work: significant gaps in citability
- Below 50: Poor: major restructuring needed

### Step 10: Generate Report

Output the following report:

```
## AI Citation Readiness Report: [Title]

**AI Citation Readiness Score: [X]/100**: [Rating]

### Score Breakdown
| Category | Raw | Display | Max |
|----------|-----|---------|-----|
| Passage-Level Citability | X/4 | X | 27 |
| Q&A Formatting | X/3 | X | 20 |
| Entity Clarity | X/3 | X | 20 |
| Content Structure | X/3 | X | 20 |
| AI Crawler Accessibility | X/2 | X | 13 |
| **Total** | **X/15** | **X** | **100** |

### Per-Section Citability Analysis
| Section (H2) | Word Count | Self-Contained | Claim+Evidence | Citable |
|---------------|-----------|----------------|----------------|---------|
| [heading] | [N] | Yes/No | Yes/No | Yes/No |

### Platform-Specific Optimization
#### ChatGPT
- [specific recommendations]

#### Perplexity
- [specific recommendations]

#### Google AI Overviews
- [specific recommendations]

### Generated Citation Capsules

#### [H2 Section 1]
> [40-60 word citation capsule]

#### [H2 Section 2]
> [40-60 word citation capsule]

### Technical Recommendations
- [ ] [Technical fix with specifics]

### Priority Action Items
1. [Most impactful improvement]
2. [Second most impactful]
3. [Third most impactful]

Run `/blog analyze <file>` for full content quality scoring.
```

### Optional: Search Performance Context (blog-google)

If blog-google credentials include Tier 1 (GSC) and the post has a published URL:

1. Query GSC: `python3 skills/blog-google/scripts/run.py gsc_query --property <property> --filter-page <url> --json`
2. Add to platform-specific analysis:
   - Current impressions, clicks, CTR, average position
   - Search queries driving traffic to this URL
3. Check indexation: `python3 skills/blog-google/scripts/run.py gsc_inspect <url> --json`
4. Report indexation status, canonical selection, mobile usability.
5. Falls back silently if not configured.

## Anti-patterns

- **Inventing the score.** Do not eyeball a 0-100 number. Score each subcategory
  on its point scale, then apply the Step 9 weights. The display score is derived,
  never guessed.
- **Optimizing for Google rankings.** This skill is AI-citation only. If the user
  wants organic SERP work or combined Google+AI, defer to blog-rewrite — do not
  start tweaking title tags and internal links here.
- **Capsules that aren't self-contained.** A citation capsule that says "as noted
  above" or omits the source attribution can't be lifted by an LLM. Each capsule
  must stand alone with claim + data + source.
- **Padding passages to hit word count.** 120-180 words means *self-contained*,
  not *bloated*. Filler to reach the count lowers citability, not raises it.

## Real examples

Input: `sites/pawroute/content/exporting-a-dog-from-dubai.md` — a 1,400-word
post with eight H2s, no TL;DR box, two of eight H2s phrased as questions, one
comparison table without `<thead>`.

Output (abridged):
- Passage-Level Citability: 2/4 (only ~45% of sections self-contained).
- Q&A Formatting: 1/3 (question headings present but no answer-first opening,
  no FAQ block).
- Score: 58/100 — "Needs Work."
- Top action item: add a 40-60 word TL;DR and rephrase four H2s as the questions
  Maya actually types ("How long is dog export from Dubai to the UK?").
- Sample capsule under "Export timeline": "Exporting a dog from Dubai to the UK
  takes 4-7 months end to end, per the UK's pet travel rules, driven mainly by
  the rabies-titre wait. Most of that time is the mandatory 3-month gap between
  the blood test and travel."

## Self-check validation

- [ ] Each of the 5 scored subcategories has a raw point value on its own scale.
- [ ] The 0-100 display score is computed via the Step 9 weight table, not estimated.
- [ ] One citation capsule generated per H2, each 40-60 words and self-contained.
- [ ] Platform section gives High/Medium/Low plus concrete fixes for all three platforms.
- [ ] Report follows the Step 10 template exactly (headings and tables in order).
- [ ] No Google organic-ranking advice leaked in (that belongs to blog-rewrite).

## Known gaps

- **No live crawler check.** Step 6 (AI Crawler Accessibility) reasons from the
  content/markup it can see; it does not fetch the live robots.txt or test GPTBot
  reachability. Verify those out of band.
- **Benchmarks are directional.** The citation-rate percentages (e.g. "47% higher
  with `<thead>`") are cited research, not guarantees for a given post.
- **Capsule freshness.** Capsules embed claims and numbers; if the underlying fact
  changes, the capsule must be re-audited. The skill does not track expiry.
- **GSC step is optional and silent.** The blog-google integration only runs when
  credentials exist; absence of search-performance data is not flagged as an error.
