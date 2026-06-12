---
name: blog-rewrite
description: >
  Rewrite and optimize existing blog posts for Google rankings (December 2025
  Core Update, E-E-A-T) and AI citations (GEO/AEO). Full rewrite for both
  Google rankings AND AI citations. For AI-citation-only audit (no Google
  work), use blog-geo instead. Replaces fabricated statistics with sourced
  data, applies answer-first formatting, adds Pixabay/Unsplash images,
  generates built-in SVG charts, injects FAQ schema, performs AI content
  detection, adds citation capsules and information gain markers, and
  updates freshness signals. Works with any blog format (MDX, markdown,
  HTML). Use when user says "rewrite blog", "optimize blog", "update blog",
  "improve blog", "fix blog", "refresh blog post", "blog optimization".
user-invokable: true
argument-hint: "<file-path>"
license: MIT
---

# Blog Rewriter: Optimize Existing Posts

Rewrites and optimizes existing blog posts for dual ranking: Google search
and AI citation platforms. Preserves the author's voice while applying the
6 pillars of optimization.

## How to use this skill

Invoke as `/blog rewrite <file-path>` (or `/blog update <file-path>` for the
freshness-only mode at the end). Walk Phases 1-6 in order. Audit is read-only;
stop and wait for user approval after Phase 1 before changing any file.

## North Star objective

Take an existing post and raise its score across all 5 categories without
losing the author's voice or first-hand insight. The user is never the first
reviewer of the rewrite (Phase 5.5 delivery contract). A rewrite that scores
lower than the original is a failure, not a deliverable.

## Freedom Dial — MIXED (plan high · output low)

This is a two-phase skill. State both phases explicitly when you run it:

- **Phases 1-2 (Audit + Research) = HIGH freedom.** Judge what's weak, which
  statistics to replace, what the post's real angle is. Use the checklists as
  diagnostics, not as a script — reason about the post in front of you.
- **Phases 3-6 (Generate + Rewrite + Verify + Deliver) = LOW freedom.** The
  formatting rules, gate thresholds, delivery contract, and summary template
  are mechanical. Variance here = failure. Follow them exactly.

**Key references:**
- `references/quality-scoring.md` - 5-category scoring (Content 30, SEO 25, E-E-A-T 15, Technical 15, AI Citation 15)
- `references/eeat-signals.md` - Experience, expertise, authority, trust markers
- `references/internal-linking.md` - Linking strategy and anchor text rules
- `references/visual-media.md` - Image sourcing and chart styling
- `skills/blog/references/synthesis-contract.md` - 6 LAWs for re-citation hygiene during rewrite (v1.8.0; cross-skill ref lives in the orchestrator's references dir)
- `skills/blog/references/research-quality.md` - cross-source clustering for replacement-statistic research (v1.8.0)

## Cross-reference

For 21 evidence-led optimization prompts (AI-detector test, CTR audit, schema, PAA rewording, technical audit, ChatGPT visibility) directly applicable to rewrite work, see `/blog flow optimize`.

## Workflow

### Phase 1: Audit (Read-Only)

1. **Read the blog post** - Detect format (MDX, markdown, HTML)
2. **Run the quality checklist** against `references/quality-scoring.md`:
   - Count fabricated vs sourced statistics
   - Check answer-first formatting (H2 -> stat in first sentence?)
   - Count images and charts (type diversity?)
   - Measure paragraph lengths (any > 150 words?)
   - Check heading hierarchy (H1 -> H2 -> H3, no skips?)
   - Look for FAQ schema
   - Check freshness signals (lastUpdated, dateModified)
   - Assess self-promotion level
   - Evaluate citation tier quality
3. **AI content detection scan**:
   - **Burstiness score** - Measure sentence length variance across the post. Low
     variance (most sentences within 3-5 words of each other) is a strong AI signal.
     Calculate: standard deviation of sentence word counts. Target SD > 6.
   - **Known AI phrase scan** - Check for these high-frequency AI phrases:
     - "in today's digital landscape", "it's important to note", "dive into"
     - "game-changer", "navigate the landscape", "revolutionize", "seamlessly"
     - "cutting-edge", "harness the power of", "leverage" (as verb)
     - "delve", "crucial", "elevate", "foster", "landscape" (overused)
     - "multifaceted", "robust", "tapestry", "embark"
     - Full list in `agents/blog-writer.md`
   - **Vocabulary diversity** - Calculate Type-Token Ratio (TTR): unique words /
     total words. Low TTR (< 0.40) suggests AI-generated repetitive phrasing.
     Target TTR > 0.50 for natural prose.
   - **AI content percentage estimate** - Based on burstiness, phrase density, and
     TTR, estimate what percentage of the content reads as AI-generated (0-100%).
     Report as: "AI content estimate: ~X%"
   - **Second-order structural reflex scan** (v1.8.0) - The first-order checks above
     are vocabulary-level. The second-order pass catches what survives them: structural
     and rhythmic tics LLMs default to after the obvious words are replaced. Run against
     `skills/blog/references/ai-slop-detection.md`. Flag at minimum:
     - Question-cadence H2s above 70% of headings
     - Three or more "Here..." paragraph openers
     - Three-clause sentence rhythm above 50% in any 200-word window
     - More than 2 hedge words ("may," "often," "typically," "generally") in any 20-word span
     - Symmetric-list bloat (list-item word-count SD below 5)
     - More than 2 wrap-up rhetorical questions ("What does this mean for...?")
     - More than half of H2 openers starting with a transition word
     - "The key insight is..." or "What's important here is..." as sentence openers
     - Listicle pre-list intro above 250 words
     - Opening-word repetition: top three first-words above 25% share
     - Paragraph-shape SD below 25 (visual monotony)
     A draft is only "AI-detection clean" when both passes are clean. The two-namespace
     terminology (first-order/second-order for slop-detection vs Tier 1/2/3 for source
     authority) is intentional: see `skills/blog/references/ai-slop-detection.md` for
     why the labels diverged in v1.8.1.
4. **Video embed check**:
   - Count existing YouTube embeds in the post
   - If 0 embeds, flag: "No video embeds. YouTube has the strongest AI visibility correlation (0.737)"
   - If present, check: lazy loading? aria-labels? noscript fallback? VideoObject schema?
5. **Cannibalization check**:
   - Identify the post's primary keyword from title, H1, and first paragraph
   - Search the blog directory for other posts targeting the same keyword:
     - Grep headings and meta descriptions across all blog posts
     - Flag any posts with significant keyword overlap
   - If cannibalization found, report:
     - Which posts compete for the same keyword
     - Recommend: **merge** (combine into one stronger post) or **differentiate**
       (shift one post to a related but distinct keyword)
6. **Calculate current score** across 5 categories:
   - Score across 5 categories (Content Quality 30, SEO Optimization 25, E-E-A-T Signals 15, Technical Elements 15, AI Citation Readiness 15)
   - Total: 0-100
7. **Present audit summary** with specific findings, AI detection results, video status, cannibalization status, and score
8. **Enter plan mode** - Present section-by-section optimization plan

Wait for user approval before proceeding.

### Phase 2: Research

1. **Identify the blog's core topic** from existing content
2. **Find replacement statistics** for any fabricated/unsourced data:
   - Search: `[topic] study 2025 2026 data statistics`
   - Target tier 1-3 sources only
3. **Find images** if post has fewer than 3:
   - Pixabay: `site:pixabay.com [topic keywords]`
   - Unsplash: `site:unsplash.com [topic keywords]`
   - Verify each URL returns HTTP 200
   - If nanobanana-mcp is configured, offer AI generation for missing/insufficient images via `blog-image`
4. **Plan charts** if post has fewer than 2:
   - Identify data suitable for visualization
   - Select diverse chart types

### Phase 3: Chart Generation (Built-In)

When the post needs more visual elements, invoke the `blog-chart` sub-skill:

1. Select chart type using the diversity rule (no repeated types per post)
2. Pass: chart type, title, data values, source, platform format
3. Embed the returned SVG directly within a `<figure>` wrapper
4. Target 2-4 charts per 2,000-word post

See `references/visual-media.md` for chart type selection and styling rules.

### Phase 4: Content Rewrite

Apply changes in this order:

#### 4a. Preserve What Works
- Keep the author's voice and unique perspective
- Preserve original insights and first-hand experience
- Keep existing quality images and charts
- Maintain internal links

#### 4b. Fix Frontmatter
- Add `lastUpdated: "YYYY-MM-DD"` (today's date)
- Keep original `date` unchanged
- Fix meta description: fact-dense, 150-160 chars, includes 1 statistic
- Add `coverImage` + `coverImageAlt` + `ogImage` if missing
  - Search Pixabay/Unsplash/Pexels for wide hero image (1200x630)
  - Or generate custom SVG cover via `blog-chart` (text-on-gradient with key stat)
  - Or generate custom AI image via `blog-image` sub-skill (if nanobanana-mcp configured)
- Verify tags/categories are appropriate

#### 4c. Apply Answer-First Formatting
Every H2 section MUST open with a 40-60 word paragraph containing:
- At least one specific statistic with source attribution
- A direct answer to the heading's implicit question

#### 4d. Replace Fabricated Statistics
- Search for patterns: "X% of...", "X out of Y...", unsourced claims
- Replace with real data from tier 1-3 sources
- Always include inline attribution: `([Source Name](url), year)`

#### 4e. Improve Headings
- Convert statement headings to questions where natural (60-70% target)
- Keep 2-3 statement headings for variety
- Ensure keyword appears in 2-3 headings naturally

#### 4f. Fix Paragraph Length
- Split any paragraph > 150 words
- Target 40-80 words per paragraph
- Ensure each paragraph starts with its most important sentence

#### 4g. Add Visual Elements
- Embed new images after H2 headings, spaced evenly
- Embed charts within relevant sections
- If nanobanana-mcp configured: generate custom images for sections lacking good stock matches (invoke `blog-image` sub-skill via Task)
- Adapt embed format to detected platform (MDX vs markdown vs HTML)

#### 4h. Add Video Embeds
If the post lacks YouTube video embeds:
- Search 2-3 relevant videos using quality criteria from `references/video-embeds.md`
- Embed using platform-appropriate format (srcdoc lazy loading)
- Place: 1 after introduction, 1-2 in mid-article sections
- Include noscript fallback for AI crawlers

#### 4i. Add/Improve FAQ
- If no FAQ exists, add one (3-5 questions)
- If FAQ exists, ensure answers are 40-60 words with statistics
- Add FAQ schema markup appropriate to platform

#### 4j. Reduce Self-Promotion
- Max 1 brand mention (author bio context only)
- Remove "At [Company], we..." patterns
- Convert promotional sections to educational content

#### 4k. Citation Capsule Injection
For each H2 section, generate (or improve existing) a citation capsule:
- 40-60 word self-contained passage per H2
- Contains: one specific claim + one data point + source attribution
- Written in a declarative style so an AI system could extract and quote it directly
- Placed naturally within the section body, not as a separate callout

Example:
```markdown
According to a 2026 Gartner study, 58% of enterprise buyers now consult AI
assistants before contacting a vendor ([Gartner](https://www.gartner.com), 2026).
This shift means B2B content must answer specific questions concisely enough
for AI systems to extract and cite in their responses.
```

Capsules map to the "AI Citation Readiness" category (15 points) in
`references/quality-scoring.md`.

#### 4l. Anti-AI-Detection Patterns
Apply these transformations to reduce AI-detectable writing patterns:
- **Eliminate em dashes** - Replace every em dash (-) with a comma, hyphen (-),
  colon, or period. Split sentences if needed. Em dashes are an AI writing tell.
- **Replace flagged phrases** - Swap every detected AI phrase (from the scan in
  Phase 1 step 3) with a natural alternative. Examples:
  - "it's important to note" -> "worth noting" or "keep in mind"
  - "in today's digital landscape" -> "right now" or "in [specific year]"
  - "leverage" -> "use", "apply", "take advantage of"
  - "delve" -> "look at", "explore", "dig into"
  - "robust" -> "strong", "solid", "reliable"
  - "crucial" -> "key", "essential", "critical" (or restructure the sentence)
- **Vary sentence length deliberately** - After rewriting, scan each paragraph.
  Inject short punchy sentences (5-10 words) between longer ones (18-25 words).
  Target: no more than 3 consecutive sentences within 5 words of each other's length.
- **Inject rhetorical questions** - Add at least one rhetorical question every
  200-300 words to break up declarative monotony.
- **Use contractions naturally** - Replace formal constructions with contractions
  where they sound natural: "it is" -> "it's", "we have" -> "we've",
  "do not" -> "don't", "is not" -> "isn't".
- **Include hedging language** - Sprinkle first-person hedges that signal real
  experience: "in our experience", "we've found that", "from what we've seen",
  "this tends to", "it depends on".

#### 4m. Summary Box (Key Takeaways)
If the post lacks a summary box, add one immediately after the introduction:
```markdown
> **Key Takeaways**
> - [Core finding with statistic and source]
> - [Second key insight or recommendation]
> - [Third actionable takeaway]
> (3-5 bullets, 40-60 words combined. Self-contained - reader gets
> the core value without reading the full article.)
```
Default label is "Key Takeaways", but this is configurable per persona or
brand voice (e.g., "The Bottom Line", "Quick Summary", "What You Need to Know").

If an existing TL;DR box is present, convert it to the bullet-point Key
Takeaways format. Verify it meets the 40-60 word requirement and contains
at least one statistic with source attribution.

#### 4n. Information Gain Marker Injection
Review the post for original value and tag it:
- `[ORIGINAL DATA]` - Any proprietary data, survey results, experiments, or
  case study metrics the author collected first-hand
- `[PERSONAL EXPERIENCE]` - First-hand observations, lessons learned
- `[UNIQUE INSIGHT]` - Novel analysis, contrarian perspectives backed by data

If the post lacks original value markers:
- Ask the author for first-hand data or experience to include
- At minimum, add analytical insights that connect existing research in new ways
- Target: at least 2-3 markers per post

Use HTML comments (`<!-- [ORIGINAL DATA] -->`) or visible callouts depending
on the post's style.

### Phase 5: Verification

After rewriting, verify all quality gates pass:

#### Core Quality Gates
1. Every H2 opens with a statistic + source
2. No paragraph exceeds 150 words
3. Zero fabricated statistics
4. Heading hierarchy is clean
5. FAQ section present with schema
6. Images have descriptive alt text
7. Cover image present in frontmatter (coverImage + ogImage)
8. If MDX: build the project to verify no compilation errors

#### New Element Verification
9. TL;DR box present after introduction (40-60 words, contains statistic)
10. At least 2-3 information gain markers present
11. Citation capsules in major H2 sections (40-60 words, self-contained)
12. Internal linking zones marked or actual links present (5-10 per 2,000 words)
13. No AI-detectable phrases remain from banned list

#### Burstiness and Naturalness Check
14. Sentence length variance: SD > 6 (mix of short and long sentences)
15. Contractions used naturally throughout
16. Rhetorical questions present (1 per 200-300 words)
17. AI content estimate reduced from audit baseline
18. Score improved across all 5 categories vs Phase 1 audit
19. YouTube video embeds present with lazy loading, aria-labels, and noscript fallback

### Phase 6: Summary

```
## Blog Optimization Complete: [Title]

### Score Change
- Before: [X]/100 ([Rating])
  - Content Quality: [X]/30
  - SEO Optimization: [X]/25
  - E-E-A-T Signals: [X]/15
  - Technical Elements: [X]/15
  - AI Citation Readiness: [X]/15
- After: [Y]/100 ([Rating])
  - Content Quality: [Y]/30
  - SEO Optimization: [Y]/25
  - E-E-A-T Signals: [Y]/15
  - Technical Elements: [Y]/15
  - AI Citation Readiness: [Y]/15

### AI Detection
- Before: ~[X]% AI-detected content
- After: ~[Y]% AI-detected content
- Phrases replaced: [N]
- Burstiness improved: [before SD] -> [after SD]

### Cannibalization
- [Status: none found / flagged N posts / resolved]

### Changes Made
- [X] statistics replaced with sourced data
- [X] SVG charts added (types: ...)
- [X] images added from Pixabay/Unsplash
- Answer-first formatting applied to [N] H2 sections
- FAQ schema injected with [N] questions
- TL;DR box: [added/updated]
- Information gain markers: [N] ([types])
- Citation capsules: [N] across H2 sections
- AI phrases replaced: [N]
- lastUpdated set to [date]
- Self-promotion reduced to [N] mentions

### Visual Elements
- Charts: [count] ([types])
- Images: [count]
- YouTube videos: [count] ([titles])

### Ready for
- `/blog analyze <file>` to verify final score
- Publishing / deploying
```

## Phase 5.5: Delivery Contract Enforcement (v1.9.0)

Before presenting the rewritten draft, run the 5-gate delivery contract per `skills/blog/references/blog-delivery-contract.md`. The contract applies to rewrites the same way it applies to new posts: the user is never the first reviewer.

Steps:

1. **Hero check**: if the existing post already has a hero image referenced and still on disk, keep it. If the rewrite changed the topic substantially OR the hero is missing, regenerate via `python scripts/generate_hero.py --topic "<new title>" --tags "<tags>" --out <folder>`.
2. **Re-render**: run `python scripts/blog_render.py --md <slug>.md --out-dir <folder>` to refresh the `.html` and `.pdf` from the updated `.md`.
3. **Reviewer dispatch**: dispatch the `blog-reviewer` agent against the rendered `.html`. Threshold: score 90/100 or higher AND zero P0 issues.
4. **Preflight**: run `python scripts/blog_preflight.py --draft <folder> --strict`. Exit 0 = ship; exit 1 = block.
5. **Iterate on failure**: maximum 3 iterations. After the 3rd failure, STOP and present the diagnostic from `<folder>/preflight-report.json`.

Rewrites have a higher implicit threshold because the existing draft was presumably already published. Re-presenting something worse than the original is not acceptable. If the rewritten score is lower than the original score, that itself is a P0 condition.

## Update Mode

When invoked as `/blog update <file>`, focus on freshness:
1. Update statistics to latest available data (2025-2026)
2. Add new developments since last update
3. Refresh images if older than 1 year
4. Update `lastUpdated` in frontmatter
5. Preserve the existing structure - minimize rewrites
6. Target: at least 30% content change to register as "fresh" for AI crawlers

## Anti-patterns (what NOT to do)

- **Skipping the audit gate.** Never edit the file before presenting the Phase 1
  audit and getting user approval. The audit is read-only by contract.
- **Voice erasure.** Do not flatten the author's voice or delete first-hand
  experience to hit a formatting rule. Preserve > rewrite (Phase 4a).
- **Inventing replacement statistics.** Fabricated data is the exact problem the
  rewrite removes — replace only with tier 1-3 sourced figures, never with a
  plausible-sounding number.
- **First-order-clean ≠ done.** Passing the AI-phrase scan but ignoring the
  second-order structural reflex scan ships detectable slop. Both passes must
  be clean.
- **Shipping a worse post.** If the rewritten score is below the original, that
  is a P0 — stop, do not present it.
- **Confusing this with blog-geo.** If the user wants an AI-citation-only audit
  with no Google ranking work, defer to `blog-geo`.

## Real examples

**Input (PawRoute pet-relocation post, fabricated stat + AI phrasing):**
```markdown
## Why pet relocation matters
In today's digital landscape, it's crucial to leverage proper planning. Studies
show 87% of pet owners worry about confiscation when relocating from Dubai.
```

**Output after rewrite (sourced stat, answer-first, em-dash removed, voice intact):**
```markdown
## What goes wrong when expats relocate a pet from Dubai?
Most delays trace back to one missing document: the import permit. The UAE
Ministry of Climate Change requires it before arrival, and a 2025 review of
clinic intake records found incomplete paperwork was the top cause of holds
([MOCCAE](https://www.moccae.gov.ae), 2025). In our experience moving dogs out
of Dubai, the permit is where families lose the most time.
```
The fabricated "87%" is gone, the H2 became a question, the opening paragraph
answers it with a sourced statistic, the AI phrases ("digital landscape",
"crucial", "leverage") are replaced, and a first-person hedge signals real
experience.

## Self-check validation (for this skill file)

- [ ] **Face:** `description:` states what + when + when-not (defer to blog-geo) + trigger phrases, <1,000 chars.
- [ ] **Brain:** Freedom Dial set explicitly as MIXED (plan high / output low).
- [ ] **Memory:** heavy data (scoring rubric, E-E-A-T markers, visual rules) lives in `references/*` and the cross-skill `skills/blog/references/*`, pointed to conditionally — not inlined.
- [ ] **Spine:** How to use · North Star · Core (Phases) · Anti-patterns · Real examples · Self-check · Known gaps, in order.
- [ ] **Length:** core file <500 lines.
- [ ] **Pulse:** one term per concept ("post", "statistic", "source"); no "as of 2025" timestamp language; concrete PawRoute example; honest Known gaps.

(For the per-post quality gates the rewrite must hit, see Phase 5 above and
`references/quality-scoring.md`.)

## Known gaps

- **Reference files are pointers, not present.** `references/quality-scoring.md`,
  `references/eeat-signals.md`, `references/internal-linking.md`,
  `references/visual-media.md`, `references/video-embeds.md`, and the cross-skill
  `skills/blog/references/*` are expected to be supplied by the blog orchestrator
  pack. They are not vendored in this skill folder; if absent, the audit falls
  back to the inline thresholds in this file.
- **Score is model-judged, not measured.** The 0-100 score and the AI-content
  percentage are LLM estimates, not validated against a live ranking or a trained
  detector. Treat them as relative (before vs after), not absolute.
- **MDX build check assumes a buildable project.** Phase 5 gate 8 only runs if the
  repo has a build command; for loose markdown/HTML it is skipped.
- **Two namespaces by design.** first-order/second-order (slop detection) vs
  Tier 1/2/3 (source authority) are deliberately separate; see
  `skills/blog/references/ai-slop-detection.md`.
- **Residual scope note:** this skill both *audits* and *rewrites*. That is one
  job (optimize an existing post) split across phases, not two skills — the audit
  exists only to drive the rewrite and is not independently invokable.
