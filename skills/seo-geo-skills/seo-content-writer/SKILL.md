---
name: seo-content-writer
description: 'Drafts NEW SEO posts, articles, and landing pages with natural keyword placement, scannable headers, snippet-ready blocks, and cited-or-flagged evidence. Load whenever drafting fresh content for search. Triggers: "write an SEO article about X", "write me a blog post", "create a landing page for [keyword]", "write SEO content", "help me write about X", "SEO文章写作". Not for AI-citation/GEO readiness scoring — use geo-content-optimizer; not for updating decaying existing pages — use content-refresher.'
version: "9.9.10"
license: Apache-2.0
compatibility: "Claude Code and compatible agent-skill hosts"
homepage: "https://github.com/aaron-he-zhu/seo-geo-claude-skills"
when_to_use: "Use when writing SEO-optimized articles, blog posts, landing pages, or product descriptions. Also when the user asks to create content targeting a specific keyword."
argument-hint: "<topic> <target keyword>"
metadata:
  author: aaron-he-zhu
  version: "9.9.10"
  geo-relevance: "medium"
  tags:
    - seo
    - content-writing
    - blog-writing
    - seo-copywriting
    - content-creation
    - article-writing
    - landing-page
    - SEO文章
    - 博客写作
    - SEOライティング
    - SEO글쓰기
    - redaccion-seo
  triggers:
    - "create blog post"
    - "SEO copywriting"
    - "write me a blog post"
    - "help me write about"
    - "how to write SEO friendly content"
    - "SurferSEO alternative"
    - "SEO文章写作"
    - "帮我写文章"
---

# SEO Content Writer

Creates SEO content that aligns with search intent, integrates keywords naturally, and stays usable for readers.

## How to use (Quick Start)

```
Write an SEO-optimized article about [topic] targeting the keyword [keyword]
```

```
Here's my content brief: [brief]. Write SEO-optimized content following this outline.
```

## North Star objective

A reader who searched the target query gets their answer above the fold, the primary keyword reads naturally (never stuffed), the structure is scannable with at least one snippet-targetable block, and every source-needing claim is cited or flagged — never fabricated. Optimize for the human first, the SERP second.

**Freedom Dial: MIXED.** Plan high, output low.
- **Plan phase (HIGH freedom)** — research, angle, intent mapping, and voice are judgment work. Reason from the principles in *Tips for Success*; do not follow rigid steps.
- **Output phase (LOW freedom)** — the on-page mechanics (keyword placement points, H1/H2 structure, meta description, snippet block, evidence flagging, self-check) are precision work. Run the nine-step checklist and the quality bar exactly; variance here is failure.

## Skill Contract

**Expected output**: a ready-to-use draft plus the standard handoff summary for `memory/content/`.

- **Reads**: the brief, target keywords, entity inputs, and quality constraints.
- **Writes**: a user-facing content deliverable and reusable summary.
- **Promotes**: approved angles, messaging choices, missing evidence, and publish blockers to `memory/hot-cache.md` and `memory/open-loops.md`; propose durable decisions as pending-decision items.
- **Done when**: the draft satisfies the target intent with the primary keyword placed naturally; H1/H2 structure, meta description, and at least one snippet-targetable block are present; and every claim needing a source is either cited or flagged.
- **Primary next skill**: [content-quality-auditor](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/cross-cutting/content-quality-auditor/SKILL.md) when the draft is ready for gating.

### Handoff Summary

> Emit the standard shape from [skill-contract.md §Handoff Summary Format](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md).

## Data Sources

Use `~~SEO tool` and `~~search console` when connected; otherwise ask for keywords, intent, and competitors. See [CONNECTORS.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/CONNECTORS.md).

## Instructions

When a user requests SEO content, run these nine steps:

1. **Gather Requirements** — confirm primary and secondary keywords, word count, content type, audience, intent, tone, CTA, and competitors.
2. **Load CORE-EEAT Constraints** — apply the 16 high-weight items listed in the companion reference.
3. **Research and Plan** — analyze the SERP, map keywords, and choose the content angle.
4. **Create Optimized Title** — keep it concise, keyword-led, and aligned with intent.
5. **Write Meta Description** — include the keyword, value proposition, and CTA.
6. **Structure Content and Write** — use a clean H1 > intro > H2/H3 > FAQ > conclusion flow.
7. **Apply On-Page Best Practices** — manage keyword placement, readability, snippets, and supporting visuals.
8. **Add Internal / External Links** — include relevant internal and authoritative external links.
9. **Run Final SEO + CORE-EEAT Review** — score the draft, auto-fix small issues, and surface any decisions that still need the user.

Any factual claim, statistic, or quote that requires a source must be cited or explicitly flagged `[needs source]`; never invent figures, studies, dates, or attributions to fill a gap.

**Quality bar**: before handing off, confirm the draft passes — (1) intent match: a reader with the target query gets their answer above the fold; (2) keyword placement reads naturally (no stuffing) in title, H1, first 100 words, and one H2; (3) structure is scannable (H2/H3, lists, one snippet-ready block); (4) zero fabricated facts — every source-needing claim is cited or `[needs source]`. If any item fails, fix it or report it in the handoff, do not ship silently.

> **Reference**: See [Instructions Detail](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/references/instructions-detail.md) for the compact workflow, pre-write checklist, issue-classification rules, and self-check format.

## Example

Sample outcome: a keyword-led H1, optimized meta description, clear H2 structure, FAQ section, and a brief Changes Made block after the self-check. See [references/seo-writing-checklist.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/references/seo-writing-checklist.md) for the copy-start checklist and article template.

## Content Type Templates

Quick-start patterns for how-to guides, comparisons, listicles, pillar pages, reviews, and FAQ pages live in [references/content-structure-templates.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/references/content-structure-templates.md).

## Tips for Success

Match intent, front-load value, support claims with evidence, and write for humans before optimizing for the SERP.

## Anti-patterns

- **Keyword stuffing** — repeating the target keyword unnaturally instead of placing it once each in title, H1, first 100 words, and one H2.
- **Fabricated evidence** — inventing a statistic, study, date, or quote to fill a gap. Cite it or write `[needs source]` — never guess (acute for confiscation/import-rule claims an expat like Maya acts on).
- **Wall of text** — no H2/H3, no lists, no snippet-ready block; fails scannability.
- **Intent mismatch** — answering a different question than the query implies, or burying the answer below the fold.
- **Job creep** — scoring AI-citation/GEO readiness (use geo-content-optimizer) or refreshing decaying live pages (use content-refresher). This skill drafts new content only.

## Self-check validation

Before handoff, confirm every box; fix or report each failure in the handoff — do not ship silently:
- [ ] Intent match: a reader with the target query gets their answer above the fold.
- [ ] Keyword placement reads naturally in title, H1, first 100 words, and one H2 (no stuffing).
- [ ] Structure is scannable: H2/H3, lists, and at least one snippet-ready block.
- [ ] Meta description includes keyword + value proposition + CTA.
- [ ] Zero fabricated facts — every source-needing claim is cited or marked `[needs source]`.
- [ ] Handoff summary emitted; saved only on user confirmation.

## Known gaps

- **Reference links point to remote GitHub URLs**, but the same files also exist locally in `references/`. If offline or the repo is renamed, prefer the local sibling files (`references/instructions-detail.md`, `seo-writing-checklist.md`, `title-formulas.md`, `content-structure-templates.md`).
- **Does not score AI-citation/GEO readiness** — that is geo-content-optimizer's job; this skill stops at SEO + CORE-EEAT.
- **Does not refresh live/decaying pages** — that is content-refresher's job; this skill drafts new content only.
- **No live SERP access without a connector** — if `~~SEO tool`/`~~search console` is not connected, the SERP analysis in step 3 relies on user-supplied keywords and competitors and may be incomplete.

### Save Results

On user confirmation, save to `memory/content/YYYY-MM-DD-<topic>.md` — see [Skill Contract](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md) §Save Results Template.

## Reference Materials

- [Instructions Detail](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/references/instructions-detail.md) — Workflow, CORE-EEAT constraints, issue handling, self-check
- [SEO Writing Checklist](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/references/seo-writing-checklist.md) — On-page checklist, snippet patterns, and copy-start template
- [Title Formulas](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/references/title-formulas.md) — Headline formulas and CTR patterns
- [Content Structure Templates](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/references/content-structure-templates.md) — Compact content blueprints

## Next Best Skill

- **Primary**: [content-quality-auditor](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/cross-cutting/content-quality-auditor/SKILL.md) — gate the draft before publishing.
