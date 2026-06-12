---
name: content-refresher
description: 'Use when the user asks to "update outdated content" or "fix traffic/ranking decay"; scores decay, prioritizes refresh work, and produces an update plan with GEO and republishing guidance. Not for net-new content — use seo-content-writer. 内容更新/排名恢复'
version: "9.9.10"
license: Apache-2.0
compatibility: "Claude Code and compatible agent-skill hosts"
homepage: "https://github.com/aaron-he-zhu/seo-geo-claude-skills"
when_to_use: "Use when updating outdated content, refreshing old articles, improving declining pages, or adding new information to existing content."
argument-hint: "<URL of outdated content>"
metadata:
  author: aaron-he-zhu
  version: "9.9.10"
  geo-relevance: "medium"
  tags:
    - seo
    - geo
    - content-refresh
    - content-update
    - content-decay
    - ranking-recovery
    - evergreen-content
    - content-lifecycle
    - 内容更新
    - コンテンツ更新
    - 콘텐츠갱신
    - actualizar-contenido
  triggers:
    - "refresh content"
    - "content refresh strategy"
    - "this post is outdated"
    - "my old content needs updating"
    - "which posts have lost the most traffic"
    - "how often should I update content"
    - "Clearscope content refresh"
    - "文章过时了"
    - "内容刷新"
---

# Content Refresher

Identifies outdated content, scores decay/freshness, prioritizes refresh work, and produces update plans with GEO and republishing guidance.

## How to use

Invoke when the user wants to recover an *existing* page that has lost traffic/rankings (not to write a new page). Give it a URL or pasted content; it scores decay, then walks Steps 1-9 below. One term throughout: the page being recovered is the **page**; the requester is the **user**. Quick-start phrasings:

```text
Find content on [domain] that needs refreshing
Which of my blog posts have lost the most traffic?
Refresh this article for [current year]: [URL/content]
Update this content to outrank [competitor URL]: [your URL]
Create a content refresh strategy for [domain/topic]
```

## North Star objective

Recover lost traffic and rankings on existing pages by diagnosing *why* a page decayed (with evidence, not guesses) and shipping a prioritized refresh plan that an editor can execute and republish. Success = the page earns back rankings/citations; never a cosmetic date bump.

**Freedom Dial: mixed.** Diagnosis and prioritization are **high-freedom judgment** — weigh decay signals, intent shifts, and ROI with the principles below rather than a rigid rubric. The republish/packaging phase is **low-freedom precision** — the Step 8 date thresholds, schema/sitemap/cache updates, and the labeling rule (Measured / User-provided / Estimated) are mechanical; follow them exactly, variance = failure.

## Skill Contract

**Expected output**: a scored diagnosis, prioritized repair plan, and a short handoff summary ready for `memory/audits/`.

- **Reads**: candidate URLs/content, traffic and ranking history, publish/update dates, and competitor examples.
- **Writes**: a user-facing refresh plan (and optional refreshed content) plus a reusable summary that can be stored under `memory/audits/`.
- **Promotes**: blocking defects, repeated weaknesses, fix priorities, and pending decisions to `memory/open-loops.md`.
- **Done when**: decay drivers are identified with evidence; a refresh plan lists specific updates with a republish-date strategy; a Changes Made block and handoff summary are produced.
- **Primary next skill**: use the `Next Best Skill` below when the repair path is clear.

### Handoff Summary

> Emit the standard shape from [skill-contract.md §Handoff Summary Format](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md).

## Data Sources

Use ~~analytics, ~~search console, and ~~SEO tool when connected; otherwise ask for traffic data, ranking history, publish dates, candidate URLs, and competitor examples. See [CONNECTORS.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/CONNECTORS.md).

## Instructions

Label every metric **Measured** (tool/export), **User-provided**, or **Estimated** (model inference); never present an estimate as measured; if a required metric is unavailable, mark it N/A — do not invent it.

When a user requests content refresh help:

1. **CORE-EEAT Quick Score** — Estimate all 8 dimensions, prioritize red/yellow areas, and hand off to [content-quality-auditor](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/cross-cutting/content-quality-auditor/SKILL.md) for full scoring when needed.
2. **Identify Refresh Candidates** — Use age, dated claims, declining traffic, lost rankings, broken links, SERP shifts, and missing topics.
3. **Analyze Page-Level Decay** — Compare 6-month-old vs current performance, keyword deltas, SERP intent, competitor updates, and the why-refresh rationale.
4. **Define Updates Needed** — Capture outdated elements, competitor/PAA gaps, SEO updates, GEO updates, links, images, sources, and dates.
5. **Create Refresh Plan** — Specify title, structure, new sections, refreshed statistics, internal/external links, images, and validation requirements.
6. **Write Refresh Content** — Draft updated intro, replacement sections, refreshed facts, FAQ answers, and Changes Made notes.
7. **Optimize for GEO** — Add 40-60 word definitions, quotable statements, Q&A, dated citations, and standalone factual statements.
8. **Set Republishing Strategy** — Use published-date update for 50%+ new content, last-updated date for 20-50%, original date for <20%; update schema, sitemap `lastmod`, cache, Search Console, and 4-6 week monitoring.
9. **Create Refresh Report** — Summarize completed changes, expected outcomes, owners, next review date, and open loops.

> **Reference**: [references/refresh-templates.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/optimize/content-refresher/references/refresh-templates.md) has compact templates for steps 2-9.

## Decision Gates

**Stop and ask the user when:**
- A page is decayed enough that a rewrite may beat a refresh (e.g., outdated premise, intent shift, or >50% of content stale) — state the finding and ask: (1) refresh in place, or (2) rewrite as new content via [seo-content-writer](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/SKILL.md).

**Continue silently (never stop for):**
- Missing analytics/ranking history — score decay from on-page signals (dated claims, broken links, stale stats), label findings Estimated, and proceed.
- A request to "refresh" content that is actually net-new (no existing URL) — note the mismatch once and route to [seo-content-writer](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/SKILL.md) rather than fabricating a prior version.
- Which republish-date treatment to apply — follow the Step 8 thresholds without asking.

## Tips for Success

Prioritize by ROI/search demand, make substantive improvements instead of date-only edits, add stronger evidence than competitors, track post-publish rankings/traffic, and treat every refresh as a GEO citation opportunity.

## Anti-patterns

- **Date-only refresh** — bumping the published date or "last updated" without substantive content change. Search engines and readers both see through it; this is the single most common failure mode.
- **Presenting an estimate as measured** — never report decay or traffic loss as fact when it was inferred from on-page signals; label it Estimated.
- **Refreshing net-new content** — if there is no existing URL/version, this is not a refresh. Route to [seo-content-writer](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/build/seo-content-writer/SKILL.md) instead of fabricating a prior version.
- **Refreshing a page that should be rewritten** — when premise is outdated or intent has shifted (>50% stale), do not patch it; stop and offer the rewrite path (see Decision Gates).
- **Skipping the republish mechanics** — a content edit with no schema/sitemap `lastmod`/cache/Search Console update leaves the refresh invisible to crawlers.
- **Ignoring GEO** — treating a refresh as classic-SEO only and skipping 40-60 word definitions, quotable statements, and dated citations that earn AI-answer citations.

> **Reference data**: [references/content-decay-signals.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/optimize/content-refresher/references/content-decay-signals.md) covers decay signals, lifecycle stages, refresh-vs-rewrite decisions, and content-type strategy.

## Real examples

**User**: "Refresh my blog post about 'best cloud hosting providers'"

**Output**: CORE-EEAT quick score flags weak Referenceability, Experience, and Trust; recommends pricing refresh, broken-link fixes, author credential additions, affiliate disclosure, and a Changes Made block ready for republish.

**User (pet-relocation)**: "Update our 'Cost to relocate a dog from Dubai to the UK' page — traffic's been sliding for 6 months."

**Output**: flags stale 2024 airline cargo rates and a dead DEFRA link as **Estimated** decay drivers (no GSC connected); plan replaces the fare table with current figures, adds a 40-60 word "What does it cost to fly a dog from Dubai to the UK?" definition for GEO, refreshes the IATA crate-size citation with a date, and sets last-updated date treatment (30% of content changed) with sitemap `lastmod` + cache bust. Changes Made block emitted; gate to content-quality-auditor recommended.

> **Reference**: See [references/refresh-example.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/optimize/content-refresher/references/refresh-example.md) for the full worked example and checklist.

### Save Results

Ask to save results; if yes, write a dated summary to `memory/audits/content-refresher/YYYY-MM-DD-<topic>.md`. Hand off veto-level risks to the auditor gate before any hot-cache marker.

**Gate check recommended**: Run content-quality-auditor on refreshed content before republishing.

## Reference Materials

- [Content Decay Signals](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/optimize/content-refresher/references/content-decay-signals.md) — Decay indicators, lifecycle stages, and refresh triggers by content type
- [Refresh Templates](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/optimize/content-refresher/references/refresh-templates.md) — Compact templates for steps 2-9
- [Refresh Example & Checklist](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/optimize/content-refresher/references/refresh-example.md) — Full worked example and pre/post-refresh checklist

## Self-check validation

Before handing off a refresh plan, confirm:

- [ ] Decay drivers are named **with evidence** (dated claims, broken links, keyword/ranking deltas, SERP shift) — not asserted.
- [ ] Every metric is labeled **Measured**, **User-provided**, or **Estimated**; nothing missing is invented (N/A used instead).
- [ ] The plan lists **specific updates** per section, not "improve the content".
- [ ] Refresh-vs-rewrite was judged; if >50% stale or intent shifted, the rewrite gate was offered.
- [ ] Republish-date treatment follows the Step 8 thresholds (50%+ → published date; 20-50% → last-updated; <20% → original).
- [ ] Republish mechanics are covered: schema, sitemap `lastmod`, cache, Search Console, 4-6 week monitoring.
- [ ] GEO additions present: 40-60 word definitions, quotable statements, Q&A, dated citations.
- [ ] A **Changes Made** block and handoff summary are produced; gate check to content-quality-auditor recommended before republish.

## Known gaps

- **No live measurement.** This skill cannot pull analytics/Search Console data itself; without a connected `~~analytics`/`~~search console` source or user-provided exports, all decay scoring is **Estimated** from on-page signals only.
- **No post-publish tracking loop.** It produces a monitoring plan (4-6 weeks) but does not execute or revisit it — the user must re-invoke to evaluate whether the refresh recovered rankings.
- **Refresh only, not rewrite.** Full ground-up rewrites of decayed pages are out of scope; this skill detects the case and hands off to seo-content-writer rather than performing the rewrite.
- **CORE-EEAT is a quick score, not a full audit.** Deep scoring belongs to content-quality-auditor; this skill estimates 8 dimensions to triage, then defers.
- **Pet-relocation tuning is not baked in.** Examples here are generic SEO; for PawRoute pages, apply the engine's ICP ("Maya") and pet-image rules manually — this skill does not encode them.

## Next Best Skill

Primary: [content-quality-auditor](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/cross-cutting/content-quality-auditor/SKILL.md) — re-score refreshed content before shipping.
