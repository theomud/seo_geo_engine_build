# Research Methodology — Pet Relocation Content Knowledge Base
# Numini / PawRoute | Version 1.0 | 2026-06-11

---

## Overview

This document describes the complete research methodology used to build the academic evidence
base for the PawRoute content engine. Every claim used to write content, set rules, or guide
copy decisions must pass this methodology before entering the active claim bank.

---

## Purpose

PawRoute is a pet relocation lead-generation website targeting Dubai expats relocating with
dogs and cats. The ICP ("Maya") is an emotionally high-stakes buyer whose deepest fear is
confiscation or quarantine. Poor content — vague, unverified, or misleading — breaks trust
in a niche where trust is the product.

This research exists to ensure every content rule, writing principle, image guideline, and
trust signal on PawRoute is traceable to peer-reviewed evidence, not opinion or convention.

---

## Source Rules — What We Accept

### ACCEPTED
| Source type | Examples | Tier |
|-------------|----------|------|
| Systematic review / meta-analysis | Cochrane, PubMed systematic reviews | Tier 1 |
| RCT or controlled experiment (replicated) | PubMed experimental studies | Tier 1 |
| Peer-reviewed observational study | Journal articles with DOI | Tier 1 |
| Landmark foundational study (pre-2015) | Kahneman 1974, Reber 2004, Nagasawa 2015 | Tier 1 (FOUNDATIONAL) |
| Practitioner consensus from primary-source org | NN/G, Baymard (where primary) | Tier 2 |

### REJECTED
| Source type | Why |
|-------------|-----|
| Marketing blogs | No peer review, often opinion dressed as fact |
| Industry surveys ("X% of marketers...") | Self-reported, sampling bias, not reproducible |
| LinkedIn posts / influencer claims | No methodology |
| AI-generated articles | No original evidence |
| Grey literature without methodology | Unverifiable |
| Vendor case studies | Context-specific, not reproducible |

---

## Search Databases

| Database | URL | What it covers |
|----------|-----|----------------|
| PubMed | pubmed.ncbi.nlm.nih.gov | Biomedical, psychology, behavioural science |
| OpenAlex | openalex.org | Broad academic, open access |
| CrossRef / DOI | doi.org | Paper verification, full-text links |
| PMC | ncbi.nlm.nih.gov/pmc | Free full-text papers |

---

## Date Filter

- **Primary:** 2015–2026
- **Foundational only:** Pre-2015 landmark studies that have been replicated and remain consensus

---

## The 10-Vote Adversarial Verification Framework

This is the core quality gate. Every extracted claim is independently reviewed by 10
adversarial agents, each instructed to REFUTE the claim if they can find valid grounds.

### What Adversarial Agents Check

1. **Methodological weakness** — small sample, no control group, uncontrolled confounds
2. **Replication failure** — has this finding failed to replicate in subsequent studies?
3. **Contradictory evidence** — do other peer-reviewed studies show the opposite or no effect?
4. **Effect size adequacy** — is the effect too small (d < 0.2) to be practically meaningful?
5. **Generalisability** — does this apply to web content / pet relocation, or only to the lab?
6. **Retraction / controversy** — has the paper been retracted or seriously challenged?

### Calibration Rules for Adversarial Agents

- **Default: refuted = false.** Only set refuted = true if there are SPECIFIC, ARTICULABLE grounds.
- Do NOT refute because evidence is imperfect. Imperfect evidence is normal.
- Do NOT refute foundational findings replicated hundreds of times.
- DO refute if: effect is small and contested, methodology is clearly weak, strong counter-evidence exists.

### Grading Thresholds

| Refutals / 10 | Grade | Admiralty Code | Outcome |
|---------------|-------|----------------|---------|
| 0–1 refutals | HIGH | A2 | Accepted — use confidently |
| 2–3 refutals | HIGH | B1 | Accepted — strong evidence |
| 4–5 refutals | MODERATE | B2 | Accepted with stated caveats |
| 6–7 refutals | CONTESTED | C1 | Quarantine — do not use in content |
| 8–10 refutals | KILLED | D1 | Quarantine — actively avoid claiming |

---

## The Claim Bank

All verified claims are stored in:
`Research/Web_Persuasion/claim_bank.csv`

All quarantined claims are stored in:
`Research/Web_Persuasion/claim_bank_quarantine.csv`

### Canonical Columns

| Column | Description |
|--------|-------------|
| claim_text | The specific, falsifiable claim |
| primary_domain | Research area (e.g. cognitive_fluency_trust) |
| subdomain | KB node (e.g. node_1) |
| source_title | Paper title |
| source_url | DOI URL or PubMed URL |
| source_year | Publication year |
| source_tier | 1=peer-reviewed, 2=practitioner, 3=other |
| admiralty_code | A2/B1/B2/C1/D1 |
| grade | HIGH / MODERATE / CONTESTED / KILLED |
| corroboration_count | Number of papers making same claim |
| contested | true if grade MODERATE or CONTESTED |
| still_valid_2026 | true if not superseded |
| verify_method | 10-vote-adversarial-2026-06-11 |

---

## The 8 Research Areas

| Area | Target Nodes | Key Topics |
|------|--------------|------------|
| 1. Cognitive Fluency & Trust | Nodes 1, 3 | Processing fluency, cognitive load, specificity, consistency |
| 2. Dual-Process Theory & Buying | Node 2 | System 1/2, affect heuristic, PMT fear appeals, loss aversion |
| 3. Trust Signals | Node 3 | Social proof, authority, testimonials, source credibility |
| 4. Persuasive Writing Styles | Nodes 3, 8 | Narrative vs statistical, curiosity gap, plain language |
| 5. Visual Persuasion & Images | Node 11 (NEW) | Face trust, Nagasawa gaze, Kindchenschema, eye tracking |
| 6. Pet Owner Psychology | Node 12 (NEW) | HAB, anthropomorphism, owner anxiety, vet trust |
| 7. Blog / Content Effectiveness | Nodes 4, 7 | Info-seeking, uncertainty reduction, FAQ/checklist |
| 8. Regulated-Service Content | Node 13 (NEW) | Disclaimers, citations, date recency, official source trust |

---

## Knowledge Base Node Structure

The Web Persuasion KB has 14 nodes (10 original + 4 new):

### Original Nodes (taxonomy.json)
| ID | Key | Name |
|----|-----|------|
| 1 | reading_attention_psychology | Reading & attention psychology |
| 2 | persuasion_behavioural_science | Persuasion & behavioural science |
| 3 | conversion_copywriting | Conversion copywriting |
| 4 | blogging_content_strategy | Blogging & content strategy |
| 5 | web_ux_design | Web/UX design |
| 6 | seo_2026 | SEO (2026) |
| 7 | geo | GEO — Generative Engine Optimization |
| 8 | ai_assisted_writing_editing | AI-assisted writing & editing |
| 9 | blog_purpose_business_model | Blog purpose & business model |
| 10 | lead_generation_content_system | Lead-generation content system & funnel |

### New Nodes Added (this research run, 2026-06-12)
| ID | Key | Name |
|----|-----|------|
| 11 | visual_persuasion | Visual persuasion — image design & photography science |
| 12 | pet_owner_psychology | Pet owner psychology — attachment, anthropomorphism, fear & trust |
| 13 | regulated_service_content | Writing for regulated/safety-critical services |
| 14 | ai_mode_geo_differentiation | AI Mode vs AI Overviews — GEO differentiation |

---

## Gap & Caveat Labels

Every piece of content using this evidence bank must respect these labels:

| Label | Meaning | How to handle in content |
|-------|---------|--------------------------|
| GAP — NO PEER-REVIEWED EVIDENCE | No academic evidence found | Do not assert as fact; present as best practice or omit |
| ONE STUDY — TREAT AS LEAD | Only one study supports this | Mention tentatively; do not build core rules on it |
| CONTESTED | 6-7 adversarial votes against | Do not use; may be flagged to watch |
| KILLED | 8-10 adversarial votes against | Never use; quarantined |
| FOUNDATIONAL | Pre-2015 landmark study | Use confidently; label as established |

---

## The AI Writer Connection

The claim bank feeds the AI Writer System Prompt at:
`Research/Web_Persuasion/AI_Writer_System_Prompt.md`

The AI writer is RAG-bound to the claim bank:
- It may ONLY cite claims present in `claim_bank.csv`
- It REFUSES to assert un-banked facts
- It flags gaps rather than inventing evidence
- It applies node-specific rules when writing each page type

---

## Research Run Log

| Run | Date | Method | Vectors | Papers | Claims | Bank Total |
|-----|------|--------|---------|--------|--------|------------|
| Batch 0-2 (Web Persuasion Engine) | 2026-06-08 | OpenAlex/Crossref harvest + SERP | n/a | ~5,450 | 30 banked | 30 |
| Deep Research (8 styles × 20 examples) | 2026-06-11 | 111-agent deep research | 8 areas | 26 primary | 7 confirmed | 37 |
| Pending Claims 10-Vote + Node 14 | 2026-06-11/12 | 61-agent 10-vote adversarial | 5 claims | 29 papers | 3 confirmed, 1 killed | 40 |
| 28-Framework Adversarial Verification | 2026-06-12 | 87-agent 3-vote adversarial | 28 frameworks | n/a | 0 new (framework grades only) | 40 |
| 28-Framework Profiles Recovery | 2026-06-12 | Read from workflow output | 28 frameworks | n/a | FRAMEWORKS-FULL-2026-06-12.md saved | 40 |
| Node 14 Chapter + Taxonomy Update | 2026-06-12 | Manual from workflow results | n/a | n/a | NODE-14-CHAPTER.md + taxonomy nodes 11-14 | 41 |
| KB Rebuild + Gate 3 | 2026-06-12 | build_knowledge_base.py + acceptance_gate.py | n/a | n/a | PASS — 14 pillars, 41 claims, T1=30 T2=11 | 41 |

---

## Files in This Research System

```
seo_geo_engine_build/skills/copywriting/
├── RESEARCH-METHODOLOGY.md          ← this file
├── MASTER-MODEL-COPYWRITING.md      ← Theo's synthesis framework (saved 2026-06-11)
├── NODE-MAPPING-PLAN.md             ← how research areas map to KB nodes
├── DEEP-RESEARCH-2026-06-11.md      ← 108-agent deep research (writing styles + GEO + images)
├── ACADEMIC-RESEARCH-2026-06-11.md  ← output of 3-vote deep-research run (superseded)
└── ACADEMIC-RESEARCH-10VOTE.md      ← output of 10-vote adversarial run (PRIMARY)

Research/Web_Persuasion/
├── claim_bank.csv                   ← active verified claims
├── claim_bank_quarantine.csv        ← contested/killed claims
├── AI_Writer_System_Prompt.md       ← RAG-bound writer
├── Web_Persuasion_Knowledge_Base.md ← full KB book
├── GEO_Checklist.md
├── SEO_EEAT_Checklist.md
├── Editing_Standards.md
├── AB_Test_Protocol.md
└── Lead_Gen_Playbook.md

Platform/numini-platform/research_elevator/web_persuasion/
├── taxonomy.json                    ← node definitions (will add nodes 11, 12, 13)
├── kb_chapters.json                 ← chapter content (will add/update chapters)
├── build_knowledge_base.py          ← rebuilds KB book from chapters
├── acceptance_gate.py               ← Gate 3 (must exit 0)
└── build_validation_report.py       ← validation report
```

---

## Post-Research Checklist

After every research run, complete these steps before publishing any content:

- [ ] Append verified claims to `claim_bank.csv`
- [ ] Append quarantined claims to `claim_bank_quarantine.csv`
- [ ] Update `taxonomy.json` with new nodes if any
- [ ] Update `kb_chapters.json` with new/updated chapters
- [ ] Run `py research_elevator/web_persuasion/build_knowledge_base.py`
- [ ] Run `py research_elevator/web_persuasion/acceptance_gate.py` — must exit 0
- [ ] Update this Research Run Log
- [ ] Commit all changes to git

---

*This methodology is the quality floor for PawRoute content. If a claim isn't in the bank, it doesn't go on the site.*
