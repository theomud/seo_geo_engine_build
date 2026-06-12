---
Status: draft — built 2026-05-29
Area: skill-content-structure
Depends on: skill-content-structure/files/02-how-to-do-it-manually.md
Feeds into: skill-content-structure/files/04-automation-spec.md
---

# Skill 03 · File 03 — How To Verify It
## The gates a page must pass before it is allowed to publish

---

## Why verification matters

A page built with this skill is a trust instrument. One broken layer breaks the whole instrument: an opening that talks about the company instead of the fear, a claim with no Verified source behind it, a Level-1 word count on a page that needed Level-4 depth — any of these and the reader's "I don't know who to trust" feeling wins. Verification is the discipline of catching that **before** publish, not after a customer acts on a weak page.

Every page is checked against three things: the **5-layer gates** (is the structure intact?), the **page-type fit** (is it the right type, built the right way?), and the **content-depth fit** (is it the right length for its job?). A page that fails any gate is downgraded to draft and rebuilt.

---

## The 5-layer gates

Walk every page through these, in order. Each is pass/fail — no "mostly".

| Gate | Layer | Passes when |
|------|-------|-------------|
| 1 · Fear-first | L1 | The first 100 words name the customer's actual fear in their language — not "Welcome", not the company, not the keyword. |
| 2 · Verified answer | L2 | Every factual claim links to a **Verified** Source Bank row (plain English + exact quote + URL + date). No Unverifiable/Pending claim is asserted as fact. |
| 3 · Real evidence | L3 | At least one screenshot of an official source (or named, real proof) is present. No stock images standing in for proof. |
| 4 · Related fears | L4 | 2–3 related fears are linked to real pages (or logged as required pages). The reader has somewhere to go next. |
| 5 · Help-first CTA | L5 | The CTA offers something useful that resolves a specific fear — not "Get a Quote / Contact Us". |
| 6 · One fear | whole page | The page resolves exactly **one** primary fear. A second primary fear = a second page. |
| 7 · Acknowledge, don't exploit | L1 | The opening makes the reader feel understood, not more anxious. Fear-acknowledging, never fear-exploiting. |

A page that fails Gate 2 (an unverified claim asserted as fact) is the most dangerous failure in a regulated market and is an automatic block — never a "fix later".

---

## Page-type fit — including the 3 newer types

The page must be the type the Intent × Fear matrix selected, and built to that type's structural variation. Spot-check the weighting:

| Page type | The layer that must carry the page | Type-specific check |
|-----------|-----------------------------------|---------------------|
| Fear Resolution | L1 + L2 | Fear named in the opening; answer cited |
| Process Guide | L3 (the steps) | Each regulated step cites its Verified row |
| Route/Variant | L2 | Destination authority's Verified rows used, not the origin's |
| Cost Transparency | L2 (+ honest L2 hedge) | Published costs cited; unpublished costs **hedged** as Unverifiable, never invented |
| Comparison | L3 (the table) | Criteria are objective; competitors not misrepresented |
| Urgency | L5 | One clear action path; deadline stated; decisive CTA |

**The 3 newer page types — verify specifically:**

- **Emergency Page.** Verify it is *short* (Level 1 depth, 300–500 words) and that the **immediate-contact CTA (call / WhatsApp) is above the fold**. Layer 1 is one line of acknowledgement — no long preamble. Fails if it reads like a guide; an in-crisis reader will not scroll.
- **Case Study Page.** Verify it documents **one real, completed** relocation end-to-end, with real names/dates/route and at least one real artefact (document, photo, screenshot). Fails if it is a generic "success story" with no verifiable specifics — that is fabricated proof, which is worse than no proof.
- **Trust Page.** Verify every credential, licence, accreditation, and guarantee is **real and checkable** (registration numbers, named team, linkable bodies). Fails the moment a single claimed credential cannot be verified — a Trust Page with one unverifiable badge destroys the trust it exists to build.

---

## Content-depth fit — the 4 levels

Verify the page's length matches its job. Depth is chosen at briefing; verification confirms it was honoured.

| Level | Word target | When to use it | Verify it is NOT |
|-------|-------------|----------------|------------------|
| 1 — Quick answer | 300–500 | Acute need, single fact, fast exit (Emergency; thin FAQ) | Padded — extra words bury the CTA |
| 2 — Focused | 500–1,000 | One specific fear or cost, fully resolved (Fear Resolution, Cost Transparency) | So thin the fear is left half-answered |
| 3 — Comprehensive | 1,000–2,000 | A full process or head-to-head (Process Guide, Comparison, Route/Variant) | Bloated past 2,000 with filler, or too thin to be the definitive answer |
| 4 — Pillar / authority | 2,000–5,000 | Top-of-hierarchy hub linking the cluster (service pillar, Trust Page, deep Case Study) | Under-built — a pillar under 2,000 words can neither rank nor anchor its cluster |

The two failure directions: **over-writing** a Level-1 Emergency page (the contact CTA gets buried under prose an in-crisis reader will never reach) and **under-writing** a Level-4 pillar (it cannot rank or hold the cluster together). Check the word count against the level before publish; mismatch = downgrade.

---

## The audit sub-agent — verifying the verifier

After a batch of pages is built (manually or by the File 04 engine), a sub-agent independently samples **20%** of the pages (minimum 3) and re-checks them. It reads only the keyword, intent, and fear — never the existing copy — and re-derives: which page type *should* this be? does each L2 claim trace to a Verified row? is the depth right? is the CTA help-first?

Pass threshold: **90%** of sampled pages pass all gates. Below 90% → halt publishing on that batch's page types until the failures are rebuilt and re-audited. (Same audit discipline as Official Source Research; no skill is complete without the audit step.)

---

## What downgrades a page to draft

- Opening talks about the company, the brand, or the keyword instead of the fear.
- Any claim asserted as fact without a Verified Source Bank row behind it.
- An Unverifiable cost/figure stated as if confirmed (it must be hedged).
- Stock imagery used in place of real Layer-3 proof.
- Two primary fears competing on one page.
- A CTA that asks before it gives ("Get a Quote").
- Wrong page type for the intent, or right type built with the wrong layer carrying it.
- Word count in the wrong depth band for the page's intent and hierarchy position.
- (Newer types) Emergency page too long / contact below the fold; Case Study with no verifiable specifics; Trust page with an uncheckable credential.

---

## Output of the verification phase

When a batch passes, you have: every page traced to Verified sources, every page the correct type at the correct depth, the audit sample logged at ≥90%, and a list of any related-fear pages still required (from Layer 4). That list feeds the next build cycle — and the clean, audited batch is what makes the File 04 automation trustworthy to run at scale.
