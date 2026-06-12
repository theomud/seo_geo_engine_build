# Gold-standard auditor — Website · SEO · GEO · Lead-gen/Trust

A unified, evidence-tiered, on-page auditor. Built from the best of the Trust Engine's
`seo-geo-audit-tool` (kept its honesty discipline) with the gaps fixed and a scored
**Lead-gen/Trust lens** that no generic SEO tool has.

## Run it (stdlib only — no API keys, no installs)
```bash
py audit/audit.py https://example.com/page              # a live URL
py audit/audit.py dist/pawroute/destinations/uae-to-uk/index.html   # a local file
py audit/audit.py dist/pawroute --site                  # every page, rolled up + ranked
#   --json out.json   --html report.html
```

## The 5 lenses (39 checks) — the full 7-category QA + the 15 Principles + Human Writing System
Default weights (page-type profiles re-weight these per the page's job):
| Lens | Weight | What it scores |
|---|---|---|
| 🌐 **Website** | 15% | title/meta/H1, heading hierarchy, scannability, alt text, viewport, canonical, internal links, JSON-LD, page weight |
| 🔍 **SEO** | 25% | intent match, topical depth/info-density, descriptive anchors, named-author E-E-A-T, authoritative outbound links, visible freshness, FAQ |
| 🤖 **GEO** | 25% | answer-first opening, statistics, cited sources, quotable facts, entity coverage, definition block, FAQ schema |
| 💛 **Lead-gen / Trust** | 20% | **fear-first**, **cost transparency**, help-first CTA/lead-magnet, single primary CTA, social proof, objection handling, original (non-stock) visuals |
| ✨ **Quality** | 15% | **human voice** (no AI clichés), **original insight**, **helpful & actionable**, **outcome focus** (Principle 12), **reader focus** ("you" not "we" — Principle 15), **storytelling** (narrative, not just facts — Human Writing System L4), **headline hook** (curiosity/promise) |

The five lenses map to the Content-Intelligence-Engine **7-category QA**: Helpful + Human + Original (Quality) · Trustworthy (Trust/sources) · SEO · GEO · Conversion (Trust). Blog-type pages weight Quality at 25% and make *human voice* + *original insight* critical.

## What makes it gold-standard (kept from the Trust Engine, gaps fixed)
- **Evidence tier on every check** (`T1` sworn testimony → `T6` practitioner, `PRIMARY` own data, `T4` paper).
- **Verified vs heuristic** tag per check + a **verified-coverage %** — you see which points are machine-checked vs inferred.
- **Coverage → confidence label** (High/Moderate/Limited/Low). **Not-measurable checks are excluded, never zeroed** — a score on 55% of the rubric is not the same as 95%.
- **SEO ≠ GEO decoupling** — separate axes, because citation is decoupled from ranking (66% of AI-Overview citations come from outside the top-20).
- **Risk caps** — thin content, keyword stuffing, fake schema, no-conversion-path each cap the final score.
- **Lead-gen/Trust promoted to a *scored* lens** (the Trust Engine left it advisory) — fear-first + cost-transparency are the niche-beating moves we proved competitors all skip.
- **On-page-first**: runs fully offline. (Live SERP / AI-Overview / backlink checks are a future optional add behind keys; the tool reports lower coverage rather than faking those points.)

## Scoring
```
lens%   = Σ(check_score × weight) / Σ(weight)   over MEASURABLE checks only
overall = Σ(lens_weight × lens%) / Σ(lens_weight measured)
final   = min(overall, lowest triggered risk cap)
grade   = A≥90 B≥80 C≥70 D≥60 E≥40 F<40
```

## Honesty note
Scores are **structured judgments from on-page signals**, evidence-tiered — not measured
conversion/ranking outcomes. The HTML report shows every check, its tier, verified/heuristic
type, the measured detail, and a prioritized ✗→✓ fix list (highest leverage first).

## Roadmap to "true 100" (optional, behind keys)
Live SERP rank + AI-Overview citation testing (multi-engine: ChatGPT/Perplexity/Gemini),
real Core Web Vitals (PSI/CrUX), backlink authority, and an optional Claude-judge for the
subjective checks (run **advisory until calibrated against human labels**, never scored uncalibrated).
