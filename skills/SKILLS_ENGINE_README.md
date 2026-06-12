# Skills Engine

The infrastructure for building, auditing, and maintaining all Claude skills on the Numini
platform. Every skill is a permanent software component — not a throwaway prompt.

> **Core principle:** A prompt is rented. A skill is owned.

---

## What this engine contains

| File / Folder | What it does |
|---|---|
| `ANATOMY_GUIDE.md` | The 5-part anatomy framework — Face, Brain, Memory, Spine, Pulse |
| `templates/HIGH_FREEDOM.md` | Blank skill for judgment work (writing, strategy, analysis) |
| `templates/LOW_FREEDOM.md` | Blank skill for precision work (formatting, compliance, file ops) |
| `templates/MIXED.md` | Blank skill combining both modes |
| `build_skill.py` | CLI: scaffold a new anatomy-compliant skill from a template |
| `audit_skills.py` | Check all skills in `.claude/skills/` against the anatomy standard |
| `examples/web_persuasion_brief.md` | Worked anatomy example — content brief generator |

Skills live in `.claude/skills/<name>/SKILL.md`. The engine builds and checks them.

---

## Quick start: build a new skill

```powershell
# Scaffold a high-freedom skill
py skills_engine/build_skill.py --name my_skill_name --freedom high

# Scaffold a low-freedom skill
py skills_engine/build_skill.py --name my_skill_name --freedom low

# Audit all existing skills
py skills_engine/audit_skills.py

# Audit a single skill
py skills_engine/audit_skills.py --skill e1_market_intelligence
```

---

## Current skills inventory (37 groups in `.claude/skills/`)

All 37 groups follow the legacy format (Purpose / Scripts / Invocation / Inputs / Outputs).
They are functional but not yet anatomy-compliant. New skills must use the anatomy format.
Existing skills are migrated when they are next edited.

### Engine 1 — Market Gap Profiling (6 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `e1_market_intelligence` | Core platform: 21+ data sources, scoring, reports | Mixed |
| `e1_consumer_voice` | Amazon/Etsy reviews, YouTube, pricing sentiment | Mixed |
| `e1_research_discovery` | PubMed, Europe PMC, literature discovery | Low |
| `e1_sector_intelligence` | Sector handlers, brand intel, SERP | Mixed |
| `e1_construction_modules` | Jadco: demand, distribution, trade shows, sourcing | Low |
| `e1_stage_pipeline` | 19 sequential stages from init to report export | Low |

### Engine 2 — Competitor Deep Dive (3 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `e2_competitive_landscape` | Competitor ID, signals, benchmarking | Mixed |
| `e2_market_entry` | Country entry playbooks, risk scoring, SWOT/PESTLE | High |
| `e2_deal_intelligence` | M&A research, exclusivity, private sector, institutional | High |

### Engine 3 — Industrial Feasibility (4 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `e3_feasibility_core` | DCF, Monte Carlo, financial modelling, preflight | Low |
| `e3_business_plan` | Business plan generator, DOCX reports, UNIDO sections | Mixed |
| `e3_environmental` | ESIA, CBAM, circular economy, EPD sustainability | Mixed |
| `e3_supply_chain` | Certification, shipping disruption, supplier discovery | Low |

### Engine 4 — Financial Foresight and M&A (3 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `e4_financial_modelling` | Business toolkit, build-vs-ship, landed cost | Low |
| `e4_investment_analysis` | IC reports, funding, tax treaty, TAM, M&A exit | High |
| `e4_capabilities` | 23 capability modules (risk, strategy, scoring) | Mixed |

### Engine 5 — BiRhythmia Evidence (2 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `e5_evidence_engine` | Funnel linker, cross-domain, enrichment pipeline | Low |
| `e5_safety_compliance` | Safe language checking, citation verification | Low |

### Shared / Orchestration (10 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `core_libraries` | gap_main, gap_engine, gap_math function libraries | Low |
| `reporting_export` | Word reports, PDF, marketing copy | Mixed |
| `validation_qa` | Evidence checks, QA gates, verification | Low |
| `regulatory` | Regulatory readiness scoring (FDA, EFSA, MHRA, FCA) | Low |
| `product_market` | Product classification, sector APIs, plan isolation | Low |
| `runners` | Master runners, preflight checks, stage orchestration | Low |
| `system_health` | System integrity, internal ops monitoring | Low |
| `orchestrator_query` | Query classification, decomposition, routing | Mixed |
| `orchestrator_sources_routing` | 136 sources, 8-tier routing, scraping | Low |
| `orchestrator_verification_ops` | Admiralty Code verification, audit, learning | Low |

### BiRhythmia (8 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `evidence_harvesting` | Citation foundry, full-text fetch, master audit | Low |
| `evidence_grading` | iCite, GRADE SoF, claim rewriter, RoB 2, PRISMA | Low |
| `domain_tagging_and_cleanup` | 21 domains/108 subdomains, topic extraction | Low |
| `hub_content_generation` | Hub gap analysis, PubMed gap-filling, injection | Mixed |
| `calculator_validation` | Formula-to-evidence mapping, gap analysis | Low |
| `client_report_orchestration` | Word reports, 12-phase master pipeline | Low |
| `research_elevator_new_features` | AI Coach, trajectory, inverse evidence | High |
| `birhythmia_specific_utilities` | Evidence decay, Tier 1 APIs, safe language | Mixed |

### Client / Website (3 groups)
| Skill | What it covers | Freedom |
|---|---|---|
| `client_workflows` | Greig: research briefs, follow-ups, pitches, updates | High |
| `client_tools` | Skill extractor, knowledge ingestion, voice triggers | Mixed |
| `website_builder` | React/TS website generation, deployment | Mixed |

---

## Anatomy compliance status

**37 legacy skills** — functional, not anatomy-compliant. Missing: Face routing triggers,
freedom dial classification, Memory pointers, Pulse maintenance rules.

**0 anatomy-compliant skills** — migration begins with next edit of each skill.

**Rule:** Any skill touched from today must be migrated to anatomy format before commit.

---

## The migration checklist (when editing a legacy skill)

- [ ] Add `## Face` section (under 1,000 chars, includes trigger phrases)
- [ ] Re-label the instructions block as `## Brain` and add Freedom Dial classification
- [ ] Extract any large reference blocks into separate `.md` files and add `## Memory` pointers
- [ ] Ensure the 7-section Spine order is followed
- [ ] Add `## Pulse` section with term glossary, known gaps, and one-skill-one-job statement

---

## Rules

1. One skill, one job — never bundle two utilities in one SKILL.md
2. Keep core skill files under 500 lines (under 350 for high-frequency skills)
3. Face section: under 1,000 characters
4. Brain: High Freedom = principles + guardrails. Low Freedom = mechanical steps.
5. Memory: never paste large data blocks directly into Brain — pointer to a .md file
6. No timestamp language ("as of 2025") — use structural headers (Current Method / Old Pattern)
7. Stick to one term per concept throughout the file
8. Always include Real Examples and Known Gaps sections
