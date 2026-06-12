# Pet relocation blog content — for the website build

**16 blog content assets (JSON) + a UAE reference file.** Content + imagery only — **not live pages.**
De-branded (no brand name baked in — apply your own). Each file is self-explaining: it carries the
content *and* the reasoning (`method` block) and the provenance (`sourcing` block).

## What's here
- **8 outbound** (`dubai-to-uk.json`, `dubai-to-usa.json`, `dubai-to-australia.json`, `dubai-to-singapore.json`, `dubai-to-eu.json`, `dubai-to-canada.json`, `dubai-to-india.json`, `dubai-to-south-africa.json`)
- **8 inbound** (`uk-to-dubai.json`, `usa-to-dubai.json`, `australia-to-dubai.json`, `germany-to-dubai.json`, `canada-to-dubai.json`, `india-to-dubai.json`, `south-africa-to-dubai.json`, `pakistan-to-dubai.json`)
- **`uae-import-reference.json`** — the verified UAE import/export facts + banned-breed list shared by the inbound blogs.
- **`breeds-by-country.json`** — popular dog & cat breeds per route market (proxy for what relocates) + travel-suitability flags (snub-nosed/brachycephalic limits, banned-for-import). Sourced from national kennel clubs / cat registries where available; survey/market data flagged. Read its `_meta.honest_caveats`.
- Hero images render to an `images/` folder (low-res; paths are in each file's `images[]`).

## JSON shape (per file)
`_meta` · `seo` (title/meta/og/canonical) · `hero` · `byline` · `key_facts` · `takeaways` ·
`sections[]` (prose / table / flow / callout / compliance / case_study) · `story` · `faqs[]` ·
`sources[]` · `cta` · `images[]` · **`method`** · **`sourcing`**.

## The logic — why it's built this way (in every file's `method` block)
- **Structure:** answer-first opening → key takeaways → TOC → scannable sections → a visual →
  original insight/story → FAQ → official sources → one help-first CTA. Because readers scan
  (~20–28% of words, NN/G); a story is remembered where facts are forgotten; one page = one job + a
  single CTA converts. These patterns recurred across our whole research corpus.
- **GEO/SEO (what we found that might work):** GEO = answer-first self-contained chunks, cited stats,
  official-source citations, consistent entities, FAQ schema (citation is decoupled from ranking —
  ~66% of AI-Overview citations come from outside the top-20). SEO = intent-matched title+H1, topical
  depth, internal links into the money page, freshness, structured data. **Honest:** evidence-based
  best practice, **not** guaranteed — ranking also needs off-page authority/links/indexing, and GEO
  citation is unproven until measured live.
- **How + why we audit:** a 5-lens auditor (Website · SEO · GEO · Lead-gen/Trust · Quality) covering
  the 7-category QA (Helpful · Human · Original · Trustworthy · SEO · GEO · Conversion). Page-type
  profiles judge each page against *its* job; every check carries an evidence tier + verified/heuristic
  tag; not-measurable checks are excluded (coverage→confidence); risk caps catch stuffing/thin/fake
  schema. The score is an on-page **quality proxy**, not a measured outcome.

## How we verify — official sources only, with screenshots
- Every regulatory/factual claim is checked against an **official source only** — government, a
  standards body (IATA), or the **operator's own site** (the airline). **Never** blogs/forums/AI.
- Each verified claim is captured as a **full-page screenshot** and logged in a **regulatory register**
  with source · URL · date verified · version · reviewer · **re-verify-by** date (regs change).
- Anything not confirmable from an official source is **hedged / "confirm with [authority]"**, listed
  in each file's `sourcing.stated_but_unverified` — never asserted.
- **Facts are separated from advice** ("the authority requires X" vs "we recommend X").
- **AI never makes the final call** — a human reviews and signs off before publish.

## Read each file's `sourcing` block
- `verified_100pct` — facts screenshot-verified against an official source (with the evidence path + date).
- `stated_but_unverified` — what still needs an official-source confirmation before publish.
- `confidence` — the honest line: sure of the craft + verified facts; **not** sure of ranking/citation until measured.

## Before publish — what to add (don't fabricate)
1. **Brand** (name/logo/voice) and a **real named author + credentials** (the byline currently says "our relocation specialists").
2. **Real reviews/testimonials**, physical address, licence/membership numbers.
3. **Render the hero images** to your `images/` folder (prompts are in `images[]`).
4. **Close the open verifications** in each `sourcing.stated_but_unverified` (and the breed-list PDF screenshot) against the official sources.

Deeper docs (in the engine repo): `METHODOLOGY.md`, `SOURCING-METHOD.md`, `OPERATIONS-MANUAL.md`.
