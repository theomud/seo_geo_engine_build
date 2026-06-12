---
name: web_persuasion_brief
description: |
  Generates a grounded content brief for any PawRoute page or blog post,
  pulling verified claims from the Web Persuasion bank.
  Always load when: the user wants a content brief, writing plan, or blog post outline
  for any pet relocation topic.
  Triggers: "write a brief for", "content brief", "blog post plan", "what should I cover
  for", "brief for the page", "help me plan this article", "moving dog from dubai"
tags: [web_persuasion, pawroute, content_brief, seo, geo]
---

## How to use this skill
Run `py research_elevator/web_persuasion/generate_brief.py --slug SLUG` or pass
`--topic "free text"`. Returns a structured Markdown content brief saved to
`Research/Web_Persuasion/briefs/`. Requires ANTHROPIC_API_KEY (source keys.ps1 first).

## North Star
Produce a content brief that grounds every factual claim in the verified bank,
flags every un-banked regulatory fact as NEEDS VERIFICATION, and gives the writer
a zero-ambiguity blueprint for a single page or post.

## Brain — Mixed

**Freedom Dial:** MIXED
- Phase 1 (Low Freedom): claim retrieval, funnel stage detection, domain matching — follow the code
- Phase 2 (High Freedom): brief generation — Claude applies principles to structure the output

### Phase 1: Low Freedom — Claim Retrieval and Routing

Steps:
1. Detect funnel stage from slug/topic keywords:
   - BOFU if any of: quote, book, hire, apply, start, contact, pricing
   - MOFU if any of: best, compare, vs, cost, price, how much, review
   - TOFU otherwise (default)
2. Score domains by keyword match; always add +2 to pet_owner_psychology, +1 to persuasion
3. Load claims from claim_bank.csv filtered to top 6 scored domains
4. Sort: HIGH grade first, then MODERATE, then by domain rank
5. Pass to Phase 2 with: topic, stage, claims_block, AI system prompt excerpt

Fail criteria:
- claim_bank.csv does not exist → "FAIL: rebuild bank first with run_pipeline.py --from-step 4"
- ANTHROPIC_API_KEY not set → "FAIL: source keys.ps1 first"

### Phase 2: High Freedom — Brief Generation

Objective: a brief that would take any skilled writer from zero to published, without
them needing to do any additional research.

Principles:
- Front-load the intent: what is Maya trying to find out or do? State it in the first line.
- Every H2 must have a purpose, a tone note, and at least one bank claim assigned to it
- The GEO block must be self-contained (readable without the article), 40-60 words, and
  contain one named statistic from the bank
- NEEDS VERIFICATION must list every regulatory, timeline, cost, or outcome fact that
  the brief needs but the bank does not contain — leave none implicit
- CTA is always single, always specific, always links to the money page (never "contact us")
- Word count target matches funnel stage: TOFU 900-1400, MOFU 600-900, BOFU 300-500
- Maya note = one sentence on what fear or hope drives this exact search

Guardrails:
- Never invent statistics not in the bank — put them in NEEDS VERIFICATION
- Never recommend a CTA to a page that doesn't exist yet
- Never merge two different funnel stages in one brief

## Memory

| Condition | File | Contents |
|---|---|---|
| Writing a brief | `Research/Web_Persuasion/AI_Writer_System_Prompt.md` | AI writer system prompt (first 4000 chars used) |
| Need claim data | `Research/Web_Persuasion/claim_bank.csv` | 37 verified claims with grades and sources |
| Need GEO format | `Research/Web_Persuasion/GEO_Checklist.md` | GEO block format and entity consistency rules |
| Need lead-gen rules | `Research/Web_Persuasion/Lead_Gen_Playbook.md` | Maya ICP, funnel map, CTA rules |

Load instruction: all four files are referenced by generate_brief.py automatically.
When manually crafting a brief, reference AI_Writer_System_Prompt.md and claim_bank.csv.

## Anti-patterns

1. Writing the article instead of the brief — the output is a BLUEPRINT, not content
2. Inventing claims not in the bank — always flag as NEEDS VERIFICATION
3. Using vague CTAs ("learn more", "contact us") — always name the specific money page
4. Mixing TOFU and BOFU intent on one brief — one stage per brief, always
5. Omitting the Maya note — every brief must state which fear or hope is driving the search

## Real examples

**Example 1 — TOFU informational**
Input: `--slug "how-to-move-your-dog-from-dubai-to-uk"`
Stage detected: TOFU
Domains matched: pet_owner_psychology (+4), reading_attention_psychology (+2), seo_2026 (+1)
Output (abbreviated):
```markdown
## Brief: How to Move Your Dog from Dubai to the UK (2026 Complete Guide)

Slug: how-to-move-your-dog-from-dubai-to-uk
Title tag: Move Your Dog Dubai to UK 2026 — Complete Checklist
Funnel stage: TOFU | Word count: 1,100-1,400
Maya note: She's researching what's involved; fear = discovering she's done something
wrong too late to fix it.

H2: What documents does your dog actually need?
- Bank claim: E-E-A-T Trust is the most important component (seo_2026 / A1)
  → apply by citing official DEFRA source for every requirement listed
- NEEDS VERIFICATION: current DEFRA tapeworm treatment window, AHC validity period

H2: The realistic timeline from start to finish
- Tone: reassuring and specific — give a week-by-week breakdown
- NEEDS VERIFICATION: current rabies titer wait time post-vaccination

GEO block: "Moving a dog from Dubai to the UK requires four documents: a microchip,
a rabies vaccination, an Anti-Parasite Treatment certificate, and an Animal Health
Certificate (AHC) issued within 10 days of travel. The process typically takes 3-6
months from first vaccination. [NEEDS VERIFICATION: confirm current AHC window]"

CTA: "Get a personalised Dubai–UK relocation checklist → /services/dubai-to-uk"
```

**Example 2 — BOFU lead capture**
Input: `--slug "pet-relocation-dubai-quote"`
Stage detected: BOFU
Word count target: 300-500
Output:
```markdown
## Brief: Get a Dubai Pet Relocation Quote — What to Expect

Funnel stage: BOFU | Word count: 350-450
Maya note: She's ready to act; fear = choosing the wrong company and having no
recourse if something goes wrong.

H2: What the quote covers (and what it doesn't)
H2: What happens after you submit the form

CTA: "Get your free quote — responses within 2 hours → /quote"
Trust signal: "[X] relocations completed successfully. IATA-certified handlers."

NEEDS VERIFICATION: response time SLA, IATA certification status
```

## Self-check
Before returning output, verify:
- [ ] Every H2 has a bank claim assigned to it or is listed under NEEDS VERIFICATION
- [ ] GEO block is self-contained and 40-60 words
- [ ] NEEDS VERIFICATION lists every un-banked regulatory/cost/timeline fact
- [ ] CTA links to a specific money page slug (not generic "contact us")
- [ ] Word count target matches the funnel stage
- [ ] Maya note states the specific fear or hope

## Known gaps
- Does not handle non-pet-relocation topics (briefs for generic lifestyle content need a
  different domain configuration in generate_brief.py)
- Does not verify that the money page CTA target actually exists — writer must confirm
- Does not include image briefs — use the image strategy section of MASTER_FRAMEWORK.md
- Regulatory facts in NEEDS VERIFICATION must be sourced and added to claims_seed.json
  before the article goes live

## Terminology
| Term used | Meaning | Never use |
|---|---|---|
| brief | The planning document, not the article | outline, plan, spec, draft |
| bank claim | A row in claim_bank.csv (grade A1 or B2) | claim, fact, evidence, source |
| Maya | The ICP — Dubai expat, dog = family, fears confiscation | user, customer, client |
| money page | The primary conversion page this post links to | landing page, service page |
| NEEDS VERIFICATION | Un-banked fact that must be sourced before publish | TODO, TBD, check this |
