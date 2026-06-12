---
name: blog-write
description: >
  Write new blog articles from scratch optimized for Google rankings and AI
  citations. Generates full articles with template selection, answer-first
  formatting, Key Takeaways summary box, information gain markers, citation capsules, sourced
  statistics, Pixabay/Unsplash images, built-in SVG chart generation, FAQ schema,
  internal linking zones, and proper heading hierarchy. Supports MDX, markdown,
  and HTML output.
  Use when user says "write blog", "new blog post", "create article",
  "write about", "draft blog", "generate blog post".
user-invokable: true
argument-hint: "<topic>"
license: MIT
---

# Blog Writer: New Article Generation

Writes complete blog articles from a topic, brief, or outline. Every article
follows the 6 pillars of dual optimization (Google rankings + AI citations).

## How to use this skill

Invoke with a topic (e.g. `/blog-write UAE pet relocation costs 2026`). Walk the
phases in order: target the surface, research, outline (get approval), then write,
chart, and run the delivery gates before presenting. Each phase points to the
heavy detail it needs; load reference files only when that phase is active.

## North Star objective

One article that wins on BOTH surfaces at once: it ranks in organic Google AND
gets quoted verbatim by AI assistants — because every claim is answer-first,
sourced, and extractable. Drafting discipline (the FLOW evidence triple) plus the
5-gate delivery contract mean the user is never the first reviewer.

## Freedom Dial: MIXED (plan high, output low)

- **High freedom — Phases 0-3 (surface choice, research, angle, outline).** This is
  judgment work: pick the template, the angle, the statistics, the narrative. Use
  the principles below; do not treat them as a rigid script.
- **Low freedom — Phases 4-7 (chart embed, content format, delivery gates).** This is
  precision work: the frontmatter schema, evidence triple, citation format, and the
  5-gate contract are mechanical. Variance here = failure. Follow them exactly.

**Key references** (paths relative to repo root; references live in the
main `blog` skill's references directory, not in `blog-write/`):

- `skills/blog/references/synthesis-contract.md`: 6 LAWs for synthesis output (v1.8.0; applies whenever the article embeds research-synthesis prose)
- `skills/blog/references/content-templates.md`: Template selection guide and usage
- `skills/blog/references/quality-scoring.md`: 5-category scoring (Content 30, SEO 25, E-E-A-T 15, Technical 15, AI Citation 15)
- `skills/blog/references/eeat-signals.md`: Experience, expertise, authority, trust markers
- `skills/blog/references/internal-linking.md`: Linking strategy and anchor text rules
- `skills/blog/references/visual-media.md`: Image sourcing and chart styling

## Workflow

### Phase 0: Surface Targeting (do this BEFORE research)

Decide which of the FLOW 5 surfaces this post is meant to win. The choice
shapes structure, length, citation density, and call-to-action. The 5 surfaces
in 2026:

1. Owned site (organic Google ranking)
2. SERP including AI Overviews
3. AI assistant citations (ChatGPT, Perplexity, Claude, Gemini, Copilot, You.com)
4. Local pack (out of scope for blog content; use claude-seo for local)
5. Communities and video (Reddit, YouTube, LinkedIn, Quora, niche forums)

Most posts target surfaces 1, 2, and 3 by default. If the same query also
surfaces in a community (Reddit thread, YouTube comment), apply dual-surface
thinking: optimize the post for extraction AND plan a community echo (covered
in `/blog repurpose`).

For a deeper surface-by-surface workflow, see
`skills/blog/references/flow-alignment.md` and `/blog flow find`.

### Phase 1: Topic Understanding

1. **Clarify the topic** - If the user provides just a topic, ask:
   - Target audience (who is this for?)
   - Primary keyword / search intent
   - Desired word count (default: 2,000-2,500 words)
   - Platform/format (MDX, markdown, HTML - auto-detect if in a project)
2. **If a brief exists** - Load it and skip to Phase 1.5

### Phase 1.5: Template Selection

Select the appropriate content template from the 12 templates in
`skills/blog/templates/` (the main `blog` skill owns the templates directory).

1. **Auto-detect content type** from the topic and search intent:
   | Signal | Template |
   |--------|----------|
   | "How to...", process, steps | `how-to-guide` |
   | "Best X", "Top N", list format | `listicle` |
   | Client result, before/after, metrics | `case-study` |
   | "X vs Y", comparison, alternatives | `comparison` |
   | Broad topic, comprehensive guide | `pillar-page` |
   | "Is X worth it", product evaluation | `product-review` |
   | Opinion, prediction, industry take | `thought-leadership` |
   | Expert quotes, multi-source collection | `roundup` |
   | Code walkthrough, tool demo, technical | `tutorial` |
   | Breaking news, algorithm update, event | `news-analysis` |
   | Survey results, experiment, original data | `data-research` |
   | Q&A, knowledge base, "What is X" | `faq-knowledge` |

2. **Load the matching template**: Read from `skills/blog/templates/<type>.md`
3. **Adapt the outline** - Use the template's section structure, heading patterns,
   and word count guidance to shape Phase 3's outline
4. **Fallback** - If no template clearly fits, use the generic outline structure
   in Phase 3 below. Inform the user which template was selected (or that none matched).

See `skills/blog/references/content-templates.md` for detailed selection criteria and intent mapping.

### Phase 2: Research

Spawn a `blog-researcher` agent (or do inline research with WebSearch):

1. **Find 8-12 current statistics** (2025-2026 data preferred)
   - Search: `[topic] study 2025 2026 data statistics`
   - Prioritize tier 1-3 sources (see `skills/blog/references/quality-scoring.md`)
   - Record: statistic, source name, URL, date, methodology
2. **Find a cover image** (wide, high-quality, topic-relevant):
   - Search: `site:pixabay.com [topic] wide banner` (preferred)
   - Alternative: `site:unsplash.com [topic] wide`
   - Fallback: `site:pexels.com [topic] wide banner`
   - Target dimensions: 1200x630 (OG-compatible) or 1920x1080
   - Or generate a custom SVG cover via `blog-chart` (text-on-gradient with key stat)
   - Or generate a custom AI image via `blog-image` sub-skill (if nanobanana-mcp configured)
   - See `skills/blog/references/visual-media.md` for cover image sizing details
3. **Find 3-5 inline images** from open-source platforms:
   - **Pixabay** (preferred): Search `site:pixabay.com [topic keywords]`
     - Extract image URL from page
     - Direct URLs: `https://cdn.pixabay.com/photo/YYYY/MM/DD/HH/MM/filename.jpg`
     - Verify with `curl -sI "<url>" | head -1` returns HTTP 200
   - **Unsplash** (alternative): Search `site:unsplash.com [topic keywords]`
     - Build URL: `https://images.unsplash.com/photo-<id>?w=1200&h=630&fit=crop&q=80`
   - **Pexels** (fallback): Search `site:pexels.com [topic keywords]`
4. **Plan 2-4 data visualizations** from researched statistics
   - Select diverse chart types (see `skills/blog/references/visual-media.md`)
   - Map data points to chart formats
5. **AI image generation** (optional, if nanobanana-mcp configured):
   - If stock photo results are insufficient (< 3 good matches) or topic is too niche
   - Generate custom hero image and/or inline illustrations via `blog-image` sub-skill
   - Stock photos remain default - AI generation supplements, never replaces
6. **NotebookLM research** (optional, if user has relevant notebooks):
   - If the user mentions a NotebookLM notebook or the topic aligns with a configured notebook
   - Query via `blog-notebooklm` for source-grounded data from user-uploaded documents
   - Treat NotebookLM responses as Tier 1 sources (user's own primary documents)
   - Falls back silently if not configured or not authenticated
7. **Find relevant YouTube videos** (2-3 per post):
   - Use `blog-google` youtube command or WebSearch `site:youtube.com [topic] [year]`
   - Apply quality criteria from `skills/blog/references/video-embeds.md` (min score 50/100)
   - Select 2-3 best videos. Falls back silently if none found.

### Phase 3: Outline Generation

Create a structured outline before writing. If a template was loaded in Phase 1.5,
adapt the skeleton to match the template's section structure.

**For the full outline skeleton** (Intro → Key Takeaways box → 4-5 H2 sections →
CTA → FAQ → Conclusion, with per-section word counts and placeholder markers),
see `references/writing-mechanics.md` ("Full outline skeleton"). The shape, in brief:

- Introduction (100-150w) with a surprising stat, then a Key Takeaways box (3-5 bullets)
- 4-5 H2 sections (300-400w each), each answer-first with a citation capsule and an internal-link zone
- CTA placed after value delivery (single focused CTA per post)
- FAQ (3-5 Q&A) and Conclusion (100-150w)

Present the outline to the user for approval before writing.

**Visual element pacing**: Insert `[IMAGE]`, `[CHART]`, `[VIDEO]`, or `[CALLOUT]` markers
every 300-500 words. Alternate types (no consecutive same-type). See
`skills/blog/references/content-rules.md` Visual Rhythm section and
`skills/blog/references/cta-placement.md` for CTA positioning.

### Phase 4: Chart Generation (Built-In)

When the researcher identifies chart-worthy data (3+ comparable metrics, trend data,
before/after comparisons):

1. Select chart type using the diversity rule (no repeated types per post)
2. Invoke `blog-chart` sub-skill with: chart type, title, data values, source, platform format
3. Embed the returned SVG directly in the post within a `<figure>` wrapper
4. Target 2-4 charts per 2,000-word post
5. Distribute charts evenly - never cluster them

See `skills/blog/references/visual-media.md` for chart type selection and styling rules.

### Phase 5: Content Writing

Write the full article following these rules. **This phase is LOW freedom** — the
syntax below is mechanical. **For the full embed/format reference** (frontmatter
schema, summary box, image/chart/video/FAQ syntax, internal-link zones), see
`references/writing-mechanics.md` sections 5a-5n. The load-bearing rules:

#### 5a. Frontmatter
Emit a YAML block with `title`, `description` (150-160 chars, 1 stat), `coverImage`,
`coverImageAlt`, `ogImage`, `date`, `lastUpdated`, `author`, `tags`. If the platform
uses a different field name (`image`, `hero`, `thumbnail`), match the project's
existing convention. Exact template: `references/writing-mechanics.md` §5a.

#### 5b. Summary Box (Key Takeaways)
Immediately after the introduction, add a Key Takeaways box: 3-5 bullets, 40-60
words combined, self-contained, with 1 specific statistic + source. Default label
"Key Takeaways" (use the persona's `summary_label` if a persona is active). Accept
existing TL;DR boxes during rewrites. Template: §5b.

#### 5c. Answer-First Formatting (Critical)
Every H2 MUST open with a 40-60 word paragraph that contains one specific statistic
with source AND directly answers the heading's implicit question.

**FLOW evidence triple (drafting requirement, not just audit).** Every public
statistic carries three components AT DRAFTING TIME:

1. **Year anchor in prose** — "In 2026," BEFORE the stat, in the sentence body
   (not buried in parentheses).
2. **Inline citation with publisher AND title** — "Ahrefs, AI Overviews CTR update,
   December 2025", not just "Ahrefs reported...".
3. **URL + retrieval date** in the source block at the bottom: "[Publisher],
   [Title], retrieved YYYY-MM-DD, [full URL]".

**Quality bar (drop or replace):** public claims use verified sources OR stay
qualitative. If a stat can't be verified, drop it; if contradicted by a newer
source, replace it. Never soften vague language to keep an unsourceable number.
Worked GOOD/WEAK examples: `references/writing-mechanics.md` §5c. For evidence-led
optimization prompts, see `/blog flow optimize`.

#### 5d. Information Gain Markers
Distribute at least 2-3 markers (target 3) that signal original value: `[ORIGINAL
DATA]`, `[PERSONAL EXPERIENCE]`, `[UNIQUE INSIGHT]`. Weave naturally or use as
HTML comments / `> **Our finding:**` callouts. Maps to the "Originality" criterion
in `skills/blog/references/quality-scoring.md`. Detail: §5d.

#### 5e. Citation Capsules
Per major H2, write a 40-60 word self-contained, quotable passage with one claim +
one data point + source, placed in the section body (not a separate block). Maps to
"AI Citation Readiness" (15 pts) in quality-scoring.md. Example: §5e.

#### 5f. Internal Linking Zones
Mark opportunities with `[INTERNAL-LINK: anchor text → target description]` in the
intro, each H2, the FAQ, and the conclusion. Target 5-10 zones per 2,000-word post;
descriptive anchor text only (never "click here"). See
`skills/blog/references/internal-linking.md` and §5f.

#### 5g. Paragraph & Heading Rules
- Paragraphs 40-80 words (never exceed 150); sentences max 15-20 words; lead with
  the most important info; Flesch 60-70.
- One H1 (title); H2s for main sections (60-70% as questions); H3s for subsections,
  never skip levels; primary keyword in 2-3 headings.

#### 5h. Image / Chart / Video / FAQ / Citation embedding
Exact syntax (markdown vs MDX) for images, `<figure>`-wrapped SVG charts,
srcdoc-lazy-loaded YouTube embeds, FAQSchema vs plain markdown FAQ, and inline
citation format lives in `references/writing-mechanics.md` §5i-5n. Defaults:
images after H2 before body and evenly spaced; charts in `<figure>` with source
caption; videos 500+ words apart with aria-label + noscript fallback; FAQ answers
40-60 words each with a statistic; inline citations always name source + year.

### Phase 6: Quality Check

Before delivering, verify:

#### Structure and Content
1. Every H2 opens with a statistic + source
2. No paragraph exceeds 150 words
3. All statistics have named tier 1-3 sources
4. 2-4 charts with type diversity
5. 3-5 inline images with descriptive alt text
6. Cover image present in frontmatter (coverImage + ogImage)
7. FAQ section present with 3-5 items
8. Heading hierarchy is clean (H1 -> H2 -> H3)
9. Meta description is 150-160 chars with a stat

#### New Element Verification
10. TL;DR box present after introduction (40-60 words, contains statistic + source)
11. At least 2-3 information gain markers (`[ORIGINAL DATA]`, `[PERSONAL EXPERIENCE]`, or `[UNIQUE INSIGHT]`)
12. Citation capsules present in major H2 sections (40-60 words, self-contained, quotable)
13. Internal linking zones marked in introduction, H2 sections, FAQ, and conclusion
14. No AI-detectable phrases from banned list (see `agents/blog-writer.md`)

#### Burstiness and Naturalness Check
15. **Sentence length variance** - Verify a mix of short (8-word) and long (25-word) sentences. Uniform sentence length signals AI authorship.
16. **Banned AI phrase scan** - Check for and remove:
    - "in today's digital landscape", "it's important to note", "dive into"
    - "game-changer", "navigate the landscape", "revolutionize", "seamlessly"
    - "cutting-edge", "harness the power of", "leverage" (as verb)
    - "delve", "crucial", "elevate", "foster", "landscape" (overused)
    - "multifaceted", "robust", "tapestry", "embark"
    - Full list in `agents/blog-writer.md`
17. **Contractions** - Verify natural use of contractions ("it's", "we've", "don't", "isn't"). Formal AI prose avoids contractions; natural writing uses them.
18. **Rhetorical questions** - Verify at least one rhetorical question every 200-300 words to break up declarative patterns.
19. **YouTube videos** - 2-3 embeds with lazy loading, aria-labels, and noscript fallback (see `skills/blog/references/video-embeds.md`)

### Phase 6.5: Delivery Contract Enforcement (v1.9.0)

Before Phase 7, run the 5-gate delivery contract per `skills/blog/references/blog-delivery-contract.md`. The user is never the first reviewer; the gates are.

Steps:

1. **Capability discovery + hero**: run `python scripts/blog_preflight.py --draft <folder> --gate 1` to enumerate available paths. If `nanobanana-mcp` is loaded, generate the hero via the MCP tool. Otherwise run `python scripts/generate_hero.py --topic "<title>" --tags "<tags>" --out <folder>` (uses the Gemini, Unsplash, Pexels, Pixabay, Openverse ladder).

2. **Format completeness**: render the canonical `.md` to `.html` and `.pdf` via `python scripts/blog_render.py --md <slug>.md --out-dir <folder>`. All three artifacts plus `hero.<ext>` must end up in the draft folder.

3. **Content review (blocking)**: dispatch the `blog-reviewer` agent (Task tool) against the rendered `.html`. The agent emits its scorecard to `<folder>/review.md` ending with `BLOCKING: true|false (reason)`. Threshold: overall score 90/100 or higher AND zero P0 issues per `editorial-heuristics.md`.

4. **Visual + asset gates**: run `python scripts/blog_preflight.py --draft <folder> --strict`. This runs Gate 3 (visual verification via patchright at 3 viewport widths), Gate 4 (reads review.md BLOCKING line), and Gate 5 (asset + link integrity). Exit 0 = ship; exit 1 = block.

5. **Iteration**: on any block, capture the failure diagnostic from `<folder>/preflight-report.json`, re-dispatch the blog-writer agent with the diagnostic as input, and re-run from step 1. Maximum 3 iterations. On the 3rd failure, STOP and present the failure diagnostic instead of the draft.

The orchestrator holds the loop counter; this sub-skill never loops itself.

### Phase 7: Delivery

Present the completed article ONLY after Phase 6.5 returns all gates passing. Include the screenshots from `<folder>/preview/*.png` in the summary so the user can see what they are getting before reading the prose.

Summary template:

```
## Blog Post Complete: [Title]

### Template Used
- [Template name] (or "generic outline - no template matched")

### Statistics
- [N] sourced statistics from tier 1-3 sources
- [N] unique sources cited

### Visual Elements
- Cover image: [source - Pixabay/Unsplash/Pexels or generated SVG]
- [N] inline images (Pixabay/Unsplash/Pexels)
- [N] SVG charts (types: bar, lollipop, donut, line)
- [N] YouTube video embeds (titles: ...)

### Dual-Optimization Elements
- TL;DR box: present (N words)
- Information gain markers: [N] ([types used])
- Citation capsules: [N] across H2 sections
- Internal linking zones: [N] marked

### Structure
- [N] H2 sections with answer-first formatting
- [N] FAQ items with schema
- Word count: ~[N] words
- Estimated reading time: [N] min

### Naturalness
- Sentence length variance: [pass/fail]
- AI phrase scan: [pass/fail]
- Contractions used: [yes/no]
- Rhetorical questions: [N] (target: 1 per 200-300 words)

### Next Steps
- Review and customize for your brand voice
- Resolve [INTERNAL-LINK] placeholders with actual URLs
- Add internal links to your existing content
- Run `/blog analyze <file>` to verify quality score
- Generate VideoObject schema: `/blog schema <file>` (includes video markup)
- Generate audio narration: `/blog audio generate <file>` (optional)
```

## Anti-patterns (what NOT to do)

- **Writing before approval.** Never skip the Phase 3 outline sign-off and jump
  straight to prose — the user approves the angle first.
- **Year in parentheses.** "(Ahrefs, 2026)" alone fails the evidence triple; the
  year anchor must be in the sentence body.
- **Keeping an unsourceable stat.** Do not soften a number into vague language to
  avoid dropping it. Verified-or-qualitative, no middle ground.
- **Clustered visuals.** Two charts (or two images) back-to-back. Alternate types
  and space them every 300-500 words.
- **Banned AI phrases.** "dive into", "leverage", "in today's digital landscape",
  "game-changer", "robust", "tapestry" — scan and strip (full list in `agents/blog-writer.md`).
- **Uniform sentence length.** All sentences ~18 words reads as AI. Mix 8-word and
  25-word sentences; use contractions and a rhetorical question every 200-300 words.
- **Presenting before the gates pass.** The user is never the first reviewer — Phase
  6.5's 5-gate contract is.
- **Inlining the embed templates here.** The frontmatter/chart/FAQ syntax belongs in
  `references/writing-mechanics.md`, loaded only while drafting.

## Real examples

**Input:** `/blog-write Cost to relocate a dog from Dubai to the UK in 2026`

**Phase 1.5 → template:** "Cost to..." signals a data/comparison structure; loads
`cost-breakdown`-style sections from the `how-to-guide` template.

**Phase 5c answer-first H2 (GOOD):**
> ## How Much Does It Cost to Fly a Dog from Dubai to the UK in 2026?
>
> In 2026, a Dubai-to-London relocation for a 20 kg dog runs AED 14,000-22,000
> all-in (Dubai Pet Travel, 2026 rate sheet). The spread depends on crate size,
> whether you use IATA-approved cargo or excess baggage, and the UK's mandatory
> rabies titre wait.

**WEAK version (rejected):** "Relocating a dog can be expensive (sources vary)."
No year anchor, no named source, no figure — fails the evidence triple, gets dropped.

**Phase 6.5 outcome:** `blog_preflight.py --strict` exits 1 because the hero image
is missing; orchestrator re-runs `generate_hero.py`, gate passes on iteration 2,
article is presented with the three viewport screenshots.

## Self-check validation

- [ ] **Face:** `description:` states what + when + trigger phrases, under 1,000 chars.
- [ ] **Brain:** Freedom Dial is stated (MIXED: high Phases 0-3, low Phases 4-7) and the
      instruction style matches.
- [ ] **Memory:** heavy embed templates and the full outline live in
      `references/writing-mechanics.md`, pointed to conditionally — not inlined.
- [ ] **Spine:** How to use · North Star · Core (phases) · Anti-patterns · Real examples ·
      Self-check · Known gaps, in order.
- [ ] **Length:** core file under 500 lines.
- [ ] **Pulse:** one term per concept ("user", "statistic", "H2"); no "as of 2025"
      timestamp language; concrete pet-relocation example; honest Known gaps.
- [ ] Every H2 opens answer-first with a year-anchored, sourced statistic.
- [ ] All 5 delivery gates (Phase 6.5) pass before Phase 7 delivery.

## Known gaps

- **Internal links ship unresolved.** `[INTERNAL-LINK: ...]` zones are placeholders;
  this skill marks them but does not resolve them to real URLs (a follow-up pass does).
- **Stat verification is best-effort.** The evidence triple enforces *format*, not
  ground truth. A confidently-cited but stale number can pass drafting; the
  `blog-reviewer` gate and `/blog flow optimize` are the deeper check.
- **References live in two folders.** Most reference files sit under the main `blog`
  skill (`skills/blog/references/`); only `writing-mechanics.md` is local to
  `blog-write/`. Paths must be followed exactly — they are not interchangeable.
- **Image sourcing assumes external tools.** Pixabay/Unsplash/Pexels search, hero
  generation, and chart rendering depend on `blog-chart`, `blog-image`, and the
  preflight scripts being present; degrades to stock-only or text covers otherwise.
- **No multilingual support.** Templates, banned-phrase list, and readability targets
  (Flesch 60-70) assume English output.
