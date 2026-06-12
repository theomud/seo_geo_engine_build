# AUTHORITY ASSET CREATION
## The documented resource AI cannot replicate and competitors cannot match

---

## What This Skill Is

Anyone can prompt an AI for "a guide to pet relocation." Everyone has. The result is the
generic mush that fills page two and earns no trust, no links, and no AI citations.
Authority Asset Creation makes the opposite: a **documented resource built from real
work** — a real case, real failures, real evidence — that an AI cannot fabricate and a
competitor cannot copy, because they did not live it.

The governing principle is Hormozi's: **documentation over creation.** You do not invent
a guide; you document what actually happened — the customer who nearly had their dog
confiscated, the exact document that saved it, the thing that went wrong — with proof
beside every claim. Delivery becomes marketing. The asset earns the links and the
citations precisely because it could only have come from someone who did the work.

**Skill Value Score: 17/25**
- Difficulty: 4/5
- Automation Potential: 2/5
- Market Uniqueness: 3/5
- Commercial Value: 5/5
- Teachability: 3/5

**Status:** 🔨 Building (Dubai pet relocation, 2026-05-30)
**Niche-agnostic:** Yes — every market has real work to document that AI can't fake

---

## The Three Asset Types

1. **Documented Case Study** (1,500–3,000 words) — one real case, start to finish: the
   fear, what happened, the proof, the failure, the outcome.
2. **Verified Definitive Guide** (3,000–6,000 words) — the most complete, most cited
   resource on a topic, every claim sourced.
3. **Field Notes Series** (800–1,500 words, monthly) — ongoing documentation of real work
   as it happens — the compounding asset.

All three are built the same way: real work first, documented with proof, published. The
**free-public-work bootstrap** (do real work in public, document every step) generates the
asset library before paying clients exist.

---

## What It Produces

| Output | What it is |
|--------|-----------|
| One documented case study | A real case, start to finish, with proof beside every claim |
| The proof-density record | The count showing ≥1 verifiable proof item per 200 words |
| The Hormozi-test result | The check confirming a basic AI prompt cannot replicate it |

---

## Functional Quality Threshold (Check 46)

This skill's real output — the documented case study — is **proven** only when both hold:

1. **Proof density ≥ 1 item per 200 words.** Every ~200 words carries at least one
   **verifiable** proof item: a Source-Bank citation (C-ID), a named figure, a dated fact,
   or a documented real failure/surprise. Counted explicitly.
2. **The Hormozi test passes.** A basic AI prompt ("write a case study about a pet being
   held at Dubai airport") **cannot replicate** the asset — because it contains real
   documented specifics (a named failure, dated C-ID citations, exact figures) that an AI
   has no access to and would have to fabricate. Confirmed by an independent reviewer who
   attempts the generic prompt and shows what it cannot produce.

Output that misses either is not done. The case study and its proof-density count live in
`data/`.

---

## Inputs and Outputs

| Input | Source | Required |
|-------|--------|----------|
| The real case (what actually happened) | documented real work | Yes |
| Verified facts with sources (by C-ID) | the verified-source store | Yes |
| The named fear the case resolves | the fear database | Yes |
| At least one real failure/surprise | the documented work | Yes |

| Output | Format | Contains |
|--------|--------|----------|
| Documented case study | Markdown | the real case, proof beside every claim |
| Proof-density count | table | ≥1 proof item per 200 words, shown |
| Hormozi-test result | note | what a generic AI prompt cannot reproduce |

---

## Proof

**Status:** 🔨 Building — Dubai pet relocation
**Real output (target):** one complete documented case study — the airport-confiscation
case (a customer who nearly had their dog held at Dubai airport and what happened) — with
real MOCCAE documentation cited by C-ID, at least one documented failure/surprise, proof
density ≥1 item per 200 words, passing the Hormozi test.
**Anchor:** the Muze Gu confiscation fear (Facebook) and the MOCCAE titer/fee facts
(C-019, C-003) ground the case in real, citable specifics.
**Skill Value Score (confirmed on completion):** 17/25.

---

## Environment Variables

```
PROJECT_ROOT=          # absolute path to the project root on this machine
```

Manual-first skill (Automation 2/5) — documentation of real work is human; no API keys are
required. Automation later only checks proof density (a word/citation count), never writes
the case.

---

## Standalone Test

Someone in any market can use this skill alone: take a real piece of work they did, document
it start to finish with proof beside every claim, count the proof density, and run the
Hormozi test. The method is portable; only the case and the proofs are niche-specific.
