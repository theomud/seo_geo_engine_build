---
name: geo-content-optimizer
description: 'Use when the user asks to "optimize for AI citations"; improves citation readiness for ChatGPT, Perplexity, AI Overviews, Gemini, and Claude. Not for structural on-page SEO — use on-page-seo-auditor; not for net-new drafting — use seo-content-writer. AI引用优化/GEO优化/AI搜索'
version: "9.9.10"
license: Apache-2.0
compatibility: "Claude Code and compatible agent-skill hosts"
homepage: "https://github.com/aaron-he-zhu/seo-geo-claude-skills"
when_to_use: "Use when optimizing content for AI engines like ChatGPT, Perplexity, AI Overviews, Gemini, Claude, or Copilot. Also for AI citation optimization, generative engine visibility, AI引用优化, AI搜索优化, GEO优化, or 让AI引用我."
argument-hint: "<content URL or text> [target AI engine]"
metadata:
  author: aaron-he-zhu
  version: "9.9.10"
  geo-relevance: "high"
  tags:
    - geo
    - ai-seo
    - ai-citations
    - chatgpt-optimization
    - perplexity-optimization
    - google-ai-overview
    - gemini
    - generative-engine-optimization
    - llm-citations
    - quotable-content
    - AI引用优化
    - GEO优化
    - AI最適化
    - AI최적화
    - optimizacion-ia
  triggers:
    - "get cited by ChatGPT"
    - "get cited by AI"
    - "show up in ChatGPT answers"
    - "how to appear in AI answers"
    - "Perplexity optimization"
    - "AI Overview is eating my clicks"
    - "让AI引用我"
    - "AI不提我的品牌"
---

# GEO Content Optimizer

Optimizes content for AI-generated answers and citation surfaces such as ChatGPT, Perplexity, Gemini, Claude, and AI Overviews. It improves structure, authority signals, factual density, quotable statements, source attribution, and overall GEO readiness — on *existing* content (not net-new drafting, not page restructuring).

## How to use this skill

Trigger it with a content URL or paste, plus an optional target engine. Typical invocations:

```text
Optimize this content for GEO/AI citations: [content or URL]
Make this article more likely to be cited by AI systems
Write content about [topic] optimized for both SEO and GEO
Audit this content for GEO readiness and suggest improvements
AI Overview is eating clicks on 12 head queries — build a recovery plan
```

Then walk the body in order: read the **North Star**, honour the **Freedom Dial**, run the 5-step **Instructions**, and clear the **Self-check** before handoff. See [AI Overview Recovery](references/ai-overview-recovery.md) for the 4-phase playbook (measure → diagnose → rewrite → monitor) tailored to recovery scenarios (as opposed to generic GEO optimization).

## North Star objective

Make each target AI query answerable by a single standalone, quotable block in the content, so generative engines cite *this* page (not a competitor) — without degrading the human read. Success = every target query has a 25-50 word answer block, a before/after GEO score and AI Query Coverage are reported, and the CORE-EEAT GEO self-check shows no unaddressed Fail.

## Freedom Dial — MIXED (plan high / output low)

- **Diagnosis & rewrite phase = HIGH freedom.** Choosing which facts to surface, how to phrase a quotable claim, and which authority signals to add is judgment work — use the principles in *Tips for Success*, do not follow rigid steps.
- **Scoring & self-check phase = LOW freedom.** The CORE-EEAT GEO self-check, the metric-labelling rule, and the before/after report are mechanical: run every required check, label every metric, never skip or invent. Variance here = failure.

## Skill Contract

**Expected output**: a ready-to-use asset or implementation-ready transformation plus a short handoff summary ready for `memory/content/`.

- **Reads**: the brief, target keywords, entity inputs, and quality constraints. **Canonical entity profiles**: if the content mentions a brand / person / product, this skill MUST consult `memory/entities/<slug>.md` (per the [entity-geo handoff schema](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/entity-geo-handoff-schema.md)) to populate `display_name`, `description_short`, `ai_resolution_status` and decide whether disambiguation boilerplate is needed. If the profile is missing or stale (>90 days), declare `DONE_WITH_CONCERNS` and recommend `entity-optimizer` as an open loop.
- **Writes**: a user-facing content, metadata, or schema deliverable plus a reusable summary that can be stored under `memory/content/`.
- **Promotes**: approved angles, messaging choices, missing evidence, and publish blockers to `memory/hot-cache.md` and `memory/open-loops.md`; propose durable decisions as pending-decision items.
- **Done when**: each target AI query has a standalone, quotable answer block; a before/after GEO score and AI Query Coverage are reported; and the CORE-EEAT GEO self-check (C02, O03, O05, E01) has no unaddressed Fail.
- **Primary next skill**: use the `Next Best Skill` below when the asset is ready for review or deployment.

### Handoff Summary

> Emit the standard shape from [skill-contract.md §Handoff Summary Format](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md).

## Data Sources

Use `~~AI monitor` and `~~SEO tool` when connected; otherwise ask for target queries, content, engines, competitor examples, and known AI-citation gaps. See [CONNECTORS.md](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/CONNECTORS.md).

## Instructions

When a user requests GEO optimization, run these five steps:

1. **Load CORE-EEAT GEO-First Targets** — prioritize C02, C09, O03, O05, E01, O02 plus engine-specific preferences.
2. **Analyze Current Content** — score clear definitions, quotable statements, factual density, source citations, Q&A format, authority signals, freshness, and structure clarity.
3. **Apply GEO Techniques** — add standalone 25-50 word definitions, sourced quotable statements, expert/source signals, Q&A/tables/lists, specific data, and visible-content-matching FAQ schema.
4. **Generate GEO Output** — report Changes Made, before/after GEO score, and AI Query Coverage.
5. **CORE-EEAT GEO Self-Check** — verify C02, C04, C09, O02, O03, O05, O06, R01, R02, R04, R07, E01, Exp10, Ept08 with Pass/Warn/Fail.

Label every metric **Measured** (tool/export), **User-provided**, or **Estimated** (model inference); never present an estimate as measured; if a required metric is unavailable, mark it N/A — do not invent it.

> **Reference**: See [Instructions Detail](references/instructions-detail.md) for the full CORE-EEAT GEO target tables, AI engine preferences, analysis templates, optimization report template, self-check matrix, and examples.

## GEO Optimization Checklist

> **Reference**: See the GEO Readiness Checklist in [GEO Optimization Techniques](references/geo-optimization-techniques.md) for the full checklist covering definitions, quotable content, authority, structure, and technical elements.

## Tips for Success

Answer first, be specific, cite dated sources, stay current, match query format, and build authority. Full list in [Instructions Detail — Tips for Success](references/instructions-detail.md#tips-for-success).

### Save Results

On user confirmation, save to `memory/content/YYYY-MM-DD-<topic>.md` — see [Skill Contract](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/references/skill-contract.md) §Save Results Template.

## Reference Materials

- [Instructions Detail](references/instructions-detail.md) - Full 5-step workflow, CORE-EEAT GEO targets, self-check matrix, worked example, tips
- [GEO Optimization Techniques](references/geo-optimization-techniques.md) - Detailed before/after examples, templates, and checklists for each technique
- [AI Citation Patterns](references/ai-citation-patterns.md) - How Google AI Overviews, ChatGPT, Perplexity, and Claude select and cite sources
- [Quotable Content Examples](references/quotable-content-examples.md) - Before/after examples of content optimized for AI citation

## Anti-patterns (what NOT to do)

- **Restructuring the page instead of optimizing for citation** — moving H2s and fixing internal links is on-page SEO; hand that to `on-page-seo-auditor`, not here.
- **Drafting net-new copy from a blank page** — that is `seo-content-writer`'s job; this skill transforms existing content.
- **Presenting an estimate as a measured metric** — every figure must be labelled Measured, User-provided, or Estimated; an unbacked "GEO score: 82" is a failure.
- **Inventing a citation or a date to look authoritative** — if a sourced fact is unavailable, mark it N/A and flag it as an open loop.
- **Keyword-stuffing the answer block** — the 25-50 word definition must read cleanly to a human; AI engines down-rank obviously templated filler.
- **Skipping the entity profile** — if the content names a brand/person/product (e.g. a pet-relocation operator), consult `memory/entities/<slug>.md` first; do not guess `display_name` or resolution status.

## Example

**User**: "Optimize this paragraph for GEO: 'Email marketing is a good way to reach customers. It's been around for a while and many businesses use it.'"

**Output** adds a clear definition, dated/source-backed facts, structured list, quotable statements, and a before/after GEO score. See the full pattern in [Instructions Detail — Example](references/instructions-detail.md#example).

## Self-check validation (run before handoff)

- [ ] Every target AI query has one standalone, quotable 25-50 word answer block.
- [ ] Before/after GEO score and AI Query Coverage are both reported.
- [ ] CORE-EEAT GEO self-check run (C02, C04, C09, O02, O03, O05, O06, R01, R02, R04, R07, E01, Exp10, Ept08) with no unaddressed **Fail**.
- [ ] Every metric labelled **Measured / User-provided / Estimated**; nothing invented; unavailable metrics marked **N/A**.
- [ ] If content names an entity, `memory/entities/<slug>.md` was consulted; missing/stale (>90 days) profile flagged and `entity-optimizer` recommended.
- [ ] Stayed in lane — no on-page structural rework (defer to `on-page-seo-auditor`) and no net-new drafting (defer to `seo-content-writer`).
- [ ] Handoff summary emitted; results offered for `memory/content/YYYY-MM-DD-<topic>.md`.

## Known gaps

- **No live citation measurement.** Without `~~AI monitor` connected, before/after "GEO score" is a model estimate, not a measured citation rate across ChatGPT/Perplexity/Gemini — it must be labelled Estimated.
- **Engine behaviour drifts.** AI Overview and ChatGPT citation selection change without notice; the patterns in `references/ai-citation-patterns.md` are best-known, not guaranteed-current.
- **English/Chinese first.** Triggers and examples cover EN + 中文; other-language nuance (JA/KO/ES tags exist) is under-tested.
- **Does not verify the underlying claims.** This skill makes facts *quotable*, not *true* — factual accuracy is out of scope; pair with `content-quality-auditor`.
- **Entity profile dependency is advisory.** The skill recommends `entity-optimizer` when a profile is missing but cannot create or refresh it itself.

## Next Best Skill

- **Primary**: [content-quality-auditor](https://github.com/aaron-he-zhu/seo-geo-claude-skills/blob/main/cross-cutting/content-quality-auditor/SKILL.md) — verify the optimized content is strong enough to ship and cite.
