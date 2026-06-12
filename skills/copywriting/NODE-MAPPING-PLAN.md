# Research-to-Node Mapping Plan
# Academic Research → Web Persuasion Knowledge Base

*Created 2026-06-11 — applies to ACADEMIC-RESEARCH-2026-06-11.md output*

---

## Purpose

The Web Persuasion KB has 10 pillar nodes (taxonomy.json + kb_chapters.json).
The academic research covers 8 areas. This document maps every research area to its
target node so the output can be ingested directly rather than stored as a flat report.

Each research finding lands in exactly one primary node (plus optional secondary).
New nodes are created only where no existing node covers the domain.

---

## Existing Node Registry (taxonomy.json pillars)

| ID | key | Name |
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

---

## Research Area → Node Mapping

### Research Area 1: Cognitive Fluency & Trust

**Primary node:** `1 — reading_attention_psychology`
**Secondary node:** `3 — conversion_copywriting`

What feeds Node 1:
- Processing fluency → perceived truth (Reber, Schwarz, Winkielman) — adds to mechanism
- Cognitive load theory — adds to practical_rules and pitfalls
- Sentence length and readability evidence — adds to checklist

What feeds Node 3:
- Specificity as credibility signal — adds to practical_rules (specificity → trust)
- Consistency effects on trust — adds to checklist

New sub-domains to add to Node 1:
- "processing fluency → perceived truth (Reber et al.)"
- "specificity as a credibility proxy"

---

### Research Area 2: Dual-Process Theory & Buying Decisions

**Primary node:** `2 — persuasion_behavioural_science`

What feeds Node 2:
- System 1 / System 2 (Kahneman) — foundational; already referenced; add academic citations
- Affect heuristic in decision-making — adds to mechanism
- Fear appeals + Protection Motivation Theory (Rogers) — adds to practical_rules with PMT framework
- Loss aversion in service purchases — adds to practical_rules (frame around loss, not gain)
- Emotional vs rational appeals + when each works — adds to pitfalls (don't use emotional only)

New sub-domains to add to Node 2:
- "Protection Motivation Theory (Rogers) — fear appeals in high-risk services"
- "affect heuristic — emotional state biases quality judgements"
- "loss aversion in service choice"

---

### Research Area 3: Trust Signals in Web Content

**Primary node:** `3 — conversion_copywriting`
**Secondary node:** `2 — persuasion_behavioural_science`

What feeds Node 3:
- Social proof academic evidence (review research) — adds citations to practical_rules
- Authority and expertise signals — adds citations to practical_rules
- Credibility and source attribution — adds to checklist
- Risk reduction language — adds to pitfalls (what NOT to say)

What feeds Node 2:
- Authority bias (Cialdini) — academic backing for existing claim

---

### Research Area 4: Persuasive Writing Styles

**Primary node:** `3 — conversion_copywriting`
**Secondary node:** `8 — ai_assisted_writing_editing`

What feeds Node 3:
- Narrative vs statistical evidence (Green & Brock; Slater & Rouner) — adds effect sizes
- Data-driven vs emotional appeals — adds to practical_rules (when to use each)
- Question-based headlines (curiosity gap) — adds to headline_frameworks subdomain
- Plain language and comprehension — adds to practical_rules

What feeds Node 8:
- Writing style matching — adds to brand-voice-control subdomain
- Evidence from readability research — adds to mechanism

New sub-domains to add to Node 3:
- "narrative vs statistical evidence — effect sizes and use cases"
- "curiosity gap headlines — academic basis"

---

### Research Area 5: Visual Persuasion & Images

**Primary node:** `NEW — visual_persuasion` (Node 11)
**Secondary node:** `5 — web_ux_design`

This research area does NOT fit cleanly into any existing node.
Node 5 (web_ux_design) covers layout/UX laws but not image psychology.

**→ CREATE NEW NODE 11: visual_persuasion**

Proposed node definition:
```json
{
  "id": 11,
  "key": "visual_persuasion",
  "name": "Visual persuasion & image psychology",
  "subdomains": [
    "human face processing — amygdala, attention, trust",
    "pet-human bond neuroscience (Nagasawa 2015 — dog-human mutual gaze)",
    "authentic vs stock photo trust differences",
    "Kindchenschema (baby schema) in animals — Lorenz + replications",
    "image-text congruence effects",
    "5 pet relocation image archetypes",
    "visual hierarchy and attention (F-pattern, Z-pattern, heat maps)",
    "image SEO and alt text",
    "before/during/after journey photography"
  ]
}
```

What feeds Node 11 from Research Area 5:
- Human face processing — mechanism
- Nagasawa 2015 (dog-human gaze → oxytocin) — practical_rules (show dog facing camera)
- Authentic vs stock photo trust — practical_rules (no generic stock)
- Kindchenschema — practical_rules (breed selection)
- Image-text congruence — checklist
- Visual hierarchy eye-tracking research — practical_rules

What feeds Node 5 (secondary):
- Visual hierarchy findings that overlap with layout

---

### Research Area 6: Pet Owner Psychology

**Primary node:** `NEW — pet_owner_psychology` (Node 12)
**Secondary node:** `10 — lead_generation_content_system`

This is the most specialised node and has NO equivalent in the existing taxonomy.

**→ CREATE NEW NODE 12: pet_owner_psychology**

Proposed node definition:
```json
{
  "id": 12,
  "key": "pet_owner_psychology",
  "name": "Pet owner psychology & the human-animal bond",
  "subdomains": [
    "human-animal bond (HAB) research — attachment and identity",
    "pet-as-family identity (anthropomorphism)",
    "pet owner anxiety and risk perception",
    "separation anxiety — owner perspective",
    "decision-making under high emotional stakes",
    "trust in veterinary and animal-care communication",
    "Maya ICP profile — leaving-Dubai expat, dog = family, fear = confiscation",
    "fear of quarantine, document failure, airline denial",
    "certainty as the core purchase driver (not price, not speed)"
  ]
}
```

What feeds Node 12 from Research Area 6:
- HAB literature — mechanism
- Anthropomorphism and pet-as-family identity — mechanism + practical_rules
- Pet owner anxiety and risk perception — practical_rules
- Separation anxiety research — practical_rules (language that reduces fear)
- Veterinary trust communication literature — practical_rules

What feeds Node 10 (secondary):
- "Certainty as the core purchase driver" — adds to lead_gen application

---

### Research Area 7: Blog / Content Effectiveness

**Primary node:** `4 — blogging_content_strategy`
**Secondary node:** `7 — geo`

What feeds Node 4:
- Information seeking behaviour for high-stakes decisions — adds to mechanism
- Uncertainty reduction theory (Berger & Calabrese) — adds to mechanism
- Content depth and perceived expertise — adds to practical_rules
- FAQ and checklist psychology — adds to content_types subdomain

What feeds Node 7:
- GEO content-depth evidence — adds to practical_rules
- Long-form vs short-form for trust — adds to checklist

---

### Research Area 8: Regulated-Service Content

**Primary node:** `NEW — regulated_service_content` (Node 13)
**Secondary node:** `6 — seo_2026`

This is a distinct domain not fully covered by any existing node.

**→ CREATE NEW NODE 13: regulated_service_content**

Proposed node definition:
```json
{
  "id": 13,
  "key": "regulated_service_content",
  "name": "Regulated-service content — accuracy, disclaimers, citations",
  "subdomains": [
    "health communication research — misinformation avoidance",
    "disclaimer and warning label effectiveness",
    "citation and source attribution effects on credibility",
    "last-updated date effects on trust",
    "official vs commercial source preferences",
    "separating official rules from company advice",
    "never-guess-import-requirements rule",
    "date-checking for airline and country rules",
    "liability language and legal risk",
    "how to write about changing regulations"
  ]
}
```

What feeds Node 13 from Research Area 8:
- Health communication misinformation research — mechanism
- Disclaimer effectiveness research — practical_rules
- Citation attribution effects — practical_rules (cite everything)
- "Last updated" date trust effects — checklist
- Official vs commercial source preference — practical_rules

What feeds Node 6 (secondary):
- E-E-A-T and trust for regulated content — reinforces existing Node 6 claims

---

## Summary: Node Changes Required

### Existing nodes — add new subdomains + citations:
- Node 1: +processing fluency, +specificity as credibility
- Node 2: +PMT fear appeals, +affect heuristic, +loss aversion
- Node 3: +narrative vs statistical evidence effect sizes, +curiosity gap headlines
- Node 4: +uncertainty reduction theory, +FAQ psychology
- Node 7: +content depth for GEO, +long-form trust evidence

### New nodes to create:
- Node 11: `visual_persuasion` — image psychology, Kindchenschema, Nagasawa, stock photo distrust
- Node 12: `pet_owner_psychology` — HAB, anthropomorphism, anxiety, certainty as purchase driver
- Node 13: `regulated_service_content` — disclaimers, citations, date-checking, official-source rules

---

## KB Chapter Template (for each new node)

Each new node should be added to kb_chapters.json in this format:

```json
{
  "pillar_key": "<key>",
  "definition": "<one sentence: what this pillar covers>",
  "mechanism": "<2-3 sentences: why this matters psychologically/behaviourally>",
  "practical_rules": [
    "<rule 1 — specific, actionable>",
    "<rule 2>",
    "<rule 3>",
    "<rule 4>",
    "<rule 5>"
  ],
  "pitfalls": [
    "<common mistake 1>",
    "<common mistake 2>",
    "<common mistake 3>"
  ],
  "checklist": [
    "<pre-publish check 1>",
    "<pre-publish check 2>",
    "<pre-publish check 3>",
    "<pre-publish check 4>"
  ],
  "lead_gen": "<how this node applies specifically to pet relocation lead generation>"
}
```

---

## Claim Bank Column Mapping

Each academic finding extracted by the workflow should be formatted as:

```csv
claim_text, primary_domain, subdomain, source_title, source_url, source_year,
source_tier, admiralty_code, grade, corroboration_count, contested,
still_valid_2026, verify_method
```

Grade mapping from academic evidence:
- Systematic review / meta-analysis → HIGH, Tier 1, A2
- RCT / experimental with replication → HIGH, Tier 1, B1
- Single peer-reviewed study (replicated elsewhere) → MODERATE, Tier 1, B2
- Single peer-reviewed study (not replicated) → LOW, Tier 2, C1 — ONE STUDY label
- No peer-reviewed evidence → VERY_LOW — GAP label

---

## Post-Workflow Action Plan

When ACADEMIC-RESEARCH-2026-06-11.md is complete:

1. **Extract claims** — format each confirmed finding into claim_bank.csv columns
2. **Kill quarantined claims** — any contradicted finding → claim_bank_quarantine.csv
3. **Write new KB chapters** — Node 11, 12, 13 in kb_chapters.json format
4. **Update existing chapters** — add new subdomains and citations to Nodes 1, 2, 3, 4, 7
5. **Update taxonomy.json** — add Node 11, 12, 13 to pillars array
6. **Run acceptance gate** — `py research_elevator/web_persuasion/acceptance_gate.py`
7. **Rebuild KB** — `py research_elevator/web_persuasion/build_knowledge_base.py`

---

*Node mapping is frozen before the workflow completes so findings slot in without ambiguity.*
