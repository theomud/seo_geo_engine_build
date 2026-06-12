---
Status: draft — built 2026-05-29
Area: skill-content-structure
Depends on: skill-content-structure/files/02-how-to-do-it-manually.md, skill-content-structure/files/03-how-to-verify-it.md
Feeds into: skill-content-structure/engines/engine-content-structure.md, skill-content-structure/data/content-structure-briefs.md
---

# Skill 03 · File 04 — Automation Spec
## What the page-structure engine drafts, and what stays human

---

## Automation target

**~60% of the work can be automated** once the first four pages are built by hand (File 02) and the verification gates exist (File 03). The engine drafts; the human shapes and approves. The 60% ceiling is deliberate — Layer 1 (fear acknowledgement) and Layer 5 (CTA) are exactly where formulaic AI output reads as insincere, and insincerity in a fear-first market is fatal.

What gets automated:
- Selecting the page type from the Intent × Fear matrix (intent Col J + fear Col K).
- Setting the content-depth level (1–4) from intent + hierarchy position.
- Pulling the relevant **Verified** Source Bank rows for the claims the page must make.
- Drafting all five layers, with citations placed beside each claim (the Proof Interstitial — proof next to the claim, not only at the end).
- Hedging any Unverifiable claim in the exact language the Source Bank status dictates.
- Proposing 2–3 related-fear internal links from the fear hierarchy.
- Writing a complete brief row + a first-draft page to the outputs.

What stays manual:
- Judging whether the Layer 1 opening reads as genuinely understanding vs formulaic.
- Final CTA wording (the engine proposes; the human chooses).
- Final internal-link selection (the engine suggests neighbours; the human confirms targets exist and fit).
- Page-type calls on genuinely ambiguous keywords.
- Sign-off that no Unverifiable claim slipped through as fact.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| Fear-mapped keyword row (intent J + fear K) | `.xlsx` | `skill-customer-fear-intelligence` keyword spreadsheet |
| Verified Source Bank rows | `.xlsx` | `skill-official-source-research/data/skill-02-source-bank.xlsx` (**Verified only**) |
| Community language (verbatim fear quotes) | `.md` | `skill-content-structure/customer-profile/customer-profile-snapshot.md` |
| Official-source screenshots | `.png` | `skill-official-source-research/data/source-screenshots/` |
| Anthropic API key | env | `ANTHROPIC_API_KEY` in `.env` |

The engine reads **only Verified rows** from the Source Bank. Unverifiable/Pending rows are passed in solely so the engine knows to *hedge* the claim, never to assert it.

---

## Outputs

| Output | Destination |
|--------|-------------|
| One brief row per keyword (intent, fear, page type, depth level, 5-layer content, Source Bank IDs cited, screenshots used, related-fear links) | `data/content-structure-briefs.md` |
| First-draft page (5 layers) | `data/content-structure-templates/<page-type>/<keyword-slug>.md` |
| Saved page-type skeleton (first time a type is built) | `data/content-structure-templates/<page-type>/_template.md` |
| Required-page list (unbuilt Layer-4 targets) | brief column → next build cycle |

The engine never publishes. Every output is a draft for human review against File 03's gates.

---

## Engine flow per keyword

```
for each keyword row:
    1. read intent (Col J), fear (Col K)
    2. select page type via Intent x Fear matrix (9 types)
    3. select depth level (1-4) from intent + hierarchy position
    4. gather Verified Source Bank rows whose claim matches the page's topic
       - also gather any Unverifiable rows on the topic (to hedge, not assert)
       - pick the matching official-source screenshot(s) for Layer 3
    5. Anthropic API: generation system prompt (below) + the gathered inputs
       - parse JSON: { layer1..layer5, page_type, depth_level, cited_ids,
                        hedged_ids, related_fears, cta_options }
    6. write brief row + draft page; flag for human review
    7. rate limit: 1s between API calls
```

---

## The generation system prompt

```
You draft a trust-first page for a regulated service market using a fixed
5-layer structure. You are given: PAGE_TYPE, DEPTH_LEVEL (target word range),
PRIMARY_FEAR (verbatim community quote), VERIFIED_FACTS (rows: plain_english +
exact_quote + url + date), UNVERIFIABLE_FACTS (claims with no official source),
RELATED_FEARS (candidate neighbours).

Return ONLY JSON:
{
  "layer1_fear_ack": "<opens with the customer's fear in their language; <100 words>",
  "layer2_verified_answer": "<answers the fear; every fact cited inline to a VERIFIED_FACTS row>",
  "layer3_evidence": "<process steps or proof; references the provided screenshot>",
  "layer4_related_fears": ["<related fear + internal link target>", ...],
  "layer5_cta_options": ["<help-first CTA>", "<alt>", "<alt>"],
  "cited_ids": [...], "hedged_ids": [...], "depth_level": 1-4
}

RULES:
- Layer 1 must use PRIMARY_FEAR's language. Acknowledge to resolve; never
  amplify to sell. If it would make the reader more anxious, rewrite.
- Every factual claim in Layer 2/3 must cite a VERIFIED_FACTS row inline
  (Proof Interstitial). Do NOT state any UNVERIFIABLE_FACTS claim as fact —
  hedge it exactly: "commonly reported as X; no official figure is published."
- Exactly ONE primary fear. Extra fears go to layer4_related_fears only.
- CTAs must be help-first (offer a useful resource), never "Get a Quote".
- Stay within DEPTH_LEVEL's word range. Do not invent facts, sources, or quotes.
```

---

## Test phase (the 4 universal-gap pages, then PAUSE)

Before any batch run, the engine drafts the **four universal-gap pages** (confiscation / summer embargo / titer cost / airport comparison) and stops. The human checks each against File 03:

- Does Layer 1 read as genuine, or formulaic?
- Does every Layer 2 claim trace to a Verified row? Any Unverifiable claim asserted as fact?
- Is the depth level right for the page type?
- Is the CTA help-first?

If any of the four fail, fix the prompt or the inputs before running more. Never scale a flawed generator in a fear-first market.

---

## Audit (after a batch run)

A sub-agent samples **20%** of drafted pages (minimum 3) and re-checks them blind against File 03's gates — re-deriving page type, tracing every claim to a Verified row, checking depth and CTA. Pass threshold: **90%**. Below 90% → halt the batch's page types and rebuild the failures. (Same audit discipline as Official Source Research.)

---

## When automation must hand back to humans

The engine flags a draft `Human review required` (never auto-approves) whenever:

- A required claim has **no Verified row** — the page cannot make the claim; a human decides to hedge, cut, or commission new source research.
- The page type is ambiguous (two intents tie in the matrix).
- The fear quote is generic — Layer 1 needs a human to sharpen it against the fear hierarchy.
- The draft exceeds or falls short of its depth band by >25%.
- An Emergency/Case Study/Trust page is drafted — these three carry the highest trust risk and always get human eyes before publish.

Regulated-market content has no acceptable "auto-published" path. The engine accelerates the draft; the human owns the publish decision.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| API-call pause | 1 second |
| Cost per page draft | ≈ $0.05–0.15 |
| Pages drafted per hour | ~300 |
| Cost of drafting the 4 universal-gap pages | <$0.60 |

---

## Files in this skill (created by the build)

```
skill-content-structure/
├── README.md
├── .env.example
├── customer-profile/
│   └── customer-profile-snapshot.md
├── files/
│   ├── 01-what-is-this-skill.md
│   ├── 02-how-to-do-it-manually.md
│   ├── 03-how-to-verify-it.md
│   ├── 04-automation-spec.md            ← this file
│   └── 06-models-frameworks-principles.md   ← standard (no File 05; architecture → Skill 31)
├── guides/
│   ├── content-structure-study-manual.html  ← built after the engine is proven
│   └── content-structure-cheatsheet.html
├── data/
│   ├── content-structure-briefs.md
│   ├── content-brief-template.md            ← standalone brief template (output)
│   └── content-structure-templates/
└── engines/
    └── engine-content-structure.md
```
