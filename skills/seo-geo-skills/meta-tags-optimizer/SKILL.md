---
name: meta-tags-optimizer
description: 'Optimizes a page''s title tag, meta description, Open Graph, Twitter Card, and CTR test variants. Load whenever a page needs its SERP/social snippet written or improved. Triggers: "optimize meta tags", "write a title tag", "my title tag needs work", "low click-through rate", "OG tags not showing", "improve this meta description", "title for the Dubai pet relocation page". NOT for JSON-LD/structured data — use schema-markup-generator; NOT for body/page copy — use seo-content-writer. 标题优化/元描述/CTR'
version: "9.9.10"
license: Apache-2.0
compatibility: "Claude Code and compatible agent-skill hosts"
homepage: "https://github.com/aaron-he-zhu/seo-geo-claude-skills"
when_to_use: "Use when optimizing title tags, meta descriptions, Open Graph tags, or Twitter Cards for a page."
argument-hint: "<page URL or content>"
metadata:
  author: aaron-he-zhu
  version: "9.9.10"
  geo-relevance: "low"
  tags:
    - seo
    - meta-tags
    - title-tag
    - meta-description
    - open-graph
    - twitter-card
    - ctr-optimization
    - social-sharing
    - 标题优化
    - 元描述
    - メタタグ
    - 메타태그
    - meta-tags-seo
  triggers:
    - "my title tag needs work"
    - "low click-through rate"
    - "OG tags not showing"
    - "how to write a good title tag"
    - "Yoast SEO title tool"
    - "RankMath title optimizer"
    - "TDK优化"
    - "点击率太低"
---

# Meta Tags Optimizer

Creates title tags, meta descriptions, and social meta tags that improve CTR and sharing quality.

## How to use the skill

Invoke it when a page needs its SERP/social snippet written or improved. Give the page topic and target keyword (and current tags, if rewriting). The skill returns three title options, three description options, and a complete OG/Twitter/canonical tag block. Quick starts:

```
Create meta tags for a page about [topic] targeting [keyword]
```

```
Improve these meta tags for better CTR: [current tags]
```

For JSON-LD/structured data, use schema-markup-generator instead; for body/page copy, use seo-content-writer.

## North Star objective

Ship a metadata package that wins the click in the SERP and renders cleanly when shared: keyword front-loaded, intent matched, inside the character limits, with a complete OG/Twitter/canonical block. The win condition is a higher click-through rate on the live page, not a prettier tag.

## Freedom Dial — MIXED (plan high · output low)

- **Wording the title and description is HIGH freedom (judgment work).** There are many winning angles. Use the formulas as a palette, not a cage; pick what matches searcher intent and the page's promise. Do not mechanically fill a template.
- **The tag block and the limits are LOW freedom (precision work).** Character ranges, required tags (OG, Twitter, canonical, robots, viewport), the metric-labeling rule, and the C01/C02 checks are mechanical. Variance here = failure: follow the steps exactly.

## Skill Contract

**Expected output**: a ready-to-use metadata package plus the standard handoff summary for `memory/content/`.

- **Reads**: the brief, target keywords, entity inputs, and quality constraints.
- **Writes**: a user-facing metadata deliverable and reusable summary.
- **Promotes**: approved angles, messaging choices, missing evidence, and publish blockers to `memory/hot-cache.md` and `memory/open-loops.md`; propose durable decisions as pending-decision items.
- **Done when**: three title and three description options are provided within the character limits with the keyword front-loaded; a complete OG/Twitter tag block is included; and C01 (Intent Alignment) and C02 (Direct Answer) pass.
- **Primary next skill**: [schema-markup-generator](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/schema-markup-generator/SKILL.md) when the metadata package is ready for structured-data support.

### Handoff Summary

> Emit the standard shape from [skill-contract.md §Handoff Summary Format](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md).

## Data Sources

Optional search console and SEO tool integrations pull CTR data and competitor patterns automatically; otherwise ask for current tags, keywords, and competitors. See [CONNECTORS.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/CONNECTORS.md).

## Instructions

When a user requests meta-tag optimization, run these six steps:

1. **Gather Page Information** — URL, page type, primary and secondary keywords, audience, CTA, and value proposition.
2. **Create Optimized Title Tag** — keep it near 50-60 characters, front-load the keyword, and generate three options using the supported title formulas.
3. **Write Meta Description** — target 150-160 characters, include the keyword and CTA, and generate three options.
4. **Create Open Graph, Twitter Card, and Additional Meta Tags** — include OG, Twitter, canonical, robots, viewport, author, and article tags as needed.
5. **CORE-EEAT Alignment Check** — verify C01 (Intent Alignment) and C02 (Direct Answer).
6. **Provide CTR Optimization Tips** — explain the winning elements, tradeoffs, and A/B test options.

Label every metric **Measured** (tool/export), **User-provided**, or **Estimated** (model inference); never present an estimate as measured; if a required metric is unavailable, mark it N/A — do not invent it.

> **Reference**: See [Instructions Detail](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/meta-tags-optimizer/references/instructions-detail.md) for the compact workflow, formulas, alignment matrix, CTR analysis, and example. See [Meta Tag Code Templates](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/meta-tags-optimizer/references/meta-tag-code-templates.md) for HTML blocks.

## Real example

**Input:** page about relocating a dog from Dubai to the UK; target keyword `pet relocation Dubai to UK`; audience = leaving-Dubai expat; CTA = get a quote.

**Output (one of three title/description options):**

- **Title (57 chars):** `Pet Relocation Dubai to UK: Costs, Rules & Quote 2026`
- **Meta description (156 chars):** `Moving your dog from Dubai to the UK? See exact costs, the DEFRA rules that avoid quarantine, and a step-by-step timeline. Get a no-obligation quote today.`
- **Tag block:** OG (`og:title`, `og:description`, `og:image`, `og:type=article`, `og:url`), Twitter Card (`summary_large_image`), `<link rel="canonical">`, `robots`, `viewport`.

Keyword is front-loaded once, intent matches the page (C01 pass), the description answers the searcher's question directly (C02 pass), and both tags sit inside the character limits. See the full worked sample in [Instructions Detail — Example](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/meta-tags-optimizer/references/instructions-detail.md#example).

## Tips for Success

Front-load keywords, match intent, be specific, test variations, and refresh tags when the SERP changes.

### Save Results

On user confirmation, save to `memory/content/YYYY-MM-DD-<topic>.md` — see [Skill Contract](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md) §Save Results Template.

## Reference Materials

- [Instructions Detail](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/meta-tags-optimizer/references/instructions-detail.md) — Workflow, formulas, alignment matrix, example
- [Meta Tag Formulas](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/meta-tags-optimizer/references/meta-tag-formulas.md) — Title and description formulas
- [Meta Tag Code Templates](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/meta-tags-optimizer/references/meta-tag-code-templates.md) — HTML templates
- [CTR and Social Reference](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/meta-tags-optimizer/references/ctr-and-social-reference.md) — CTR patterns and social guidance

## Anti-patterns (what NOT to do)

- **Keyword stuffing the title** — repeating the keyword or chaining "| Brand | City | Service". Front-load once, then sell the click.
- **Truncated tags** — a 75-character title or a 200-character description that the SERP cuts mid-word. Stay inside the limits in Step 2/3.
- **Description that doesn't match the page** — promising "free quote" when the page has none. Mismatched intent fails C01 and tanks CTR.
- **Inventing metrics** — presenting an Estimated CTR as Measured. Label every metric, or mark it N/A.
- **Doing the neighbors' jobs** — emitting JSON-LD (that's schema-markup-generator) or rewriting body copy (that's seo-content-writer).
- **One option only** — shipping a single title/description instead of the required three each.

## Self-check validation

- [ ] Three title options, each ~50-60 characters, keyword front-loaded.
- [ ] Three meta-description options, each ~150-160 characters, with keyword + CTA.
- [ ] Complete tag block: OG, Twitter Card, canonical, robots, viewport (+ author/article as needed).
- [ ] C01 (Intent Alignment) and C02 (Direct Answer) both pass.
- [ ] Every metric labeled Measured / User-provided / Estimated; nothing invented.
- [ ] Handoff summary emitted; results saved to `memory/content/` on user confirmation.

## Known gaps

- **No live SERP/CTR data without a connector.** Absent Search Console or an SEO-tool integration, CTR figures are Estimated, not Measured — flag them as such.
- **Character counts are guidance, not pixel-perfect.** Google truncates by pixel width, not character count; long-glyph titles can still clip inside the 60-char target.
- **No structured data and no body copy.** This skill stops at the snippet — JSON-LD and on-page copy belong to the sibling skills.
- **Reference files are linked, not local.** Formulas, code templates, and the worked example live in `references/`; deep workflow detail still points to the upstream repo URLs.

## Next Best Skill

- **Primary**: [schema-markup-generator](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/schema-markup-generator/SKILL.md) — complete the SERP package with structured data.
