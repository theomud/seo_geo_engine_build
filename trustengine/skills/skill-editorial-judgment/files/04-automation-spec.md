---
Status: draft — built 2026-05-29
Area: skill-editorial-judgment
Depends on: skill-editorial-judgment/files/02-how-to-do-it-manually.md, skill-editorial-judgment/files/03-how-to-verify-it.md
Feeds into: skill-editorial-judgment/engines/engine-editorial-judgment.md
---

# Skill · File 04 — Automation Spec
## What the editorial engine flags and pre-scores, and what stays human

---

## Automation target

**~40% of the work can be automated** — deliberately the lowest ceiling of the writing skills, because the criteria that matter most are judgement calls. The engine flags the mechanical failures; the human owns the verdict. *(Library: F-06 Seven-Step Editorial Process; M-10 Ten-Criteria Quality Model.)*

What gets automated:
- **Flag the 7 weak patterns** with their location in the draft (Filler Opening, Laundry List, Unsupported Claim, Circular Definition, Vague Benefit, Fake Enthusiasm, Dead End).
- **Suggest a specific replacement** for each generic claim it finds.
- **Flag uncited claims** — any factual statement with no Source Bank citation or hedge (an A2 risk from File 03).
- **Pre-score the mechanical criteria** — 2 Specific, 4 Clear, 5 Commercial (structure/CTA present) — with reasons.
- **Run the SEO block** of the publishing checklist (title length, meta length, H1 keyword, keyword in first paragraph, internal links).
- **Check word count** against the page-type benchmark.

What stays manual (the 60%):
- **Criterion 1 True** — fact verification is human (the engine flags *uncited*; it cannot confirm *correct*).
- **Criterion 7 Better than competitors** — requires judgement against the live top pages.
- **Criterion 8 Brand-aligned** — does it sound like this business?
- **Criterion 10 Strong enough to publish** — the Hormozi name-on-it call. *(P-13.)*
- **The final /50 and the publish/hold decision** — always human.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| AI-generated draft | text | the writer / generation engine |
| Verified Source Bank (for the cited-claim cross-check) | `.xlsx` | `skill-official-source-research/data/skill-02-source-bank.xlsx` |
| The 10-criteria rubric + 7-pattern catalogue + publishing checklist | reference | files/01–03 |
| Brand guide (for human brand-alignment) | `.md` | the business |
| Anthropic API key | env | `ANTHROPIC_API_KEY` in `.env` |

---

## Outputs

| Output | Destination |
|--------|-------------|
| Flagged weak patterns + line locations + suggested fixes | `data/editorial-reports/` |
| Uncited-claim list (A2 risks) | same |
| Pre-score on the mechanical criteria (2,4,5) + SEO-block results | same |
| Draft edit notes (for the human to complete) | same |

The engine never writes the final /50 or the publish/hold decision — it hands the human a flagged draft and a pre-score.

---

## Engine flow per draft

```
for each AI draft:
    1. scan for the 7 weak patterns -> record pattern + location + suggested fix
    2. extract factual claims -> cross-check against Verified Source Bank
       -> flag any uncited / unhedged claim (A2 risk)
    3. pre-score criteria 2 (Specific), 4 (Clear), 5 (Commercial) with reasons
    4. run the SEO checklist block (title/meta/H1/keyword/links)
    5. write the editorial report; hand to a human for criteria 1,6,7,8,9,10 + final /50
    6. rate limit: 1s between API calls
```

---

## The evaluation system prompt

```
You are an editorial QC assistant. You FLAG and PRE-SCORE; you NEVER make the
publish decision and you NEVER confirm a fact is true (only whether it is cited).

Given DRAFT and SOURCE_BANK_CLAIMS, return ONLY JSON:
{
  "weak_patterns": [{"pattern":"<1-7>", "quote":"<the offending text>", "fix":"<specific replacement>"}],
  "uncited_claims": ["<factual statement with no citation/hedge>", ...],
  "prescore": {"specific":0-5, "clear":0-5, "commercial":0-5},
  "prescore_reasons": {"specific":"...", "clear":"...", "commercial":"..."},
  "seo": {"title_len_ok":bool, "meta_len_ok":bool, "h1_keyword":bool, "keyword_in_first_para":bool, "internal_links":bool},
  "for_human": ["True (verify facts)", "Better-than-competitors", "Brand-aligned", "Publishable", "final /50 + publish decision"]
}

RULES:
- Score "specific" low if any sentence could apply to any business.
- Flag every factual claim not matched to a SOURCE_BANK_CLAIMS row as uncited.
- Do NOT assert a fact is true; do NOT output a total or a publish verdict.
```

---

## Worked example (a competitor-style draft)

Fed a typical competitor draft, the engine should flag: Pattern 3 Unsupported Claim *"the leading pet relocation provider in Dubai"* (fix: "show it — 4.8★/283 reviews"); Pattern 7 Dead End *"contact us for a quote"* (fix: a help-first CTA); an **uncited claim** *"the titer test costs 700 AED"* (no Source Bank match → A2 risk, must hedge); pre-score Specific 2/5. It then hands the human criteria 1/7/8/10 and the final call — which, given those flags, is a **hold**.

---

## Test phase (the 4 universal-gap pages, then PAUSE)

The engine processes the four gap pages and stops. The human checks: did it catch every weak pattern? Did the uncited-claim flagging match the manual review? Are the suggested fixes specific, not generic? If it misses a pattern or mis-flags a cited claim across the four, fix the prompt before scaling.

---

## Audit (after a batch)

A sub-agent re-runs **20%** of drafts (minimum 3) blind and compares the engine's pattern flags + uncited-claim list to a manual pass. Pass threshold: **90%** agreement on patterns and uncited claims, with **no false "cited"** (an uncited claim the engine passed is a hard fail). Below 90% → fix the engine prompt. *(Same discipline as the proven skills.)*

---

## When automation must hand back to humans

- **Confirming a fact is true** — the engine only flags *uncited*; a human verifies *correct*.
- **Better-than-competitors / Brand-aligned** — judgement against the live market and brand guide.
- **The publish/hold decision and the final /50** — always human (the 40% ceiling).
- **Any draft scoring borderline (38–42)** — a human re-scores, never the engine alone.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| API-call pause | 1 second |
| Cost per draft | ≈ $0.02–0.06 |
| Drafts flagged per hour | ~400 |

---

## Files in this skill (created by the build)

```
skill-editorial-judgment/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   ├── editorial-scorecards.md          ← the 4 gap pages scored (real output)
│   └── editorial-reports/
└── engines/
    └── engine-editorial-judgment.md
```
