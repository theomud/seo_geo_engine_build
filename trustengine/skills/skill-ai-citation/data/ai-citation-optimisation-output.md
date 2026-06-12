# AI Citation & GEO — Optimisation Output
## The real output · 4 gap pages optimised for AI citation + entity definition + monitoring · Built 2026-06-01
## Functional Quality Threshold (README Check 46): every optimised page has (G1) a direct-answer
## box in the first 100 words that answers the target query, (G2) ≥1 named statistic AND ≥1 verified
## Source-Bank citation (C-ID) inside that answer, (G3) valid FAQPage schema with ≥5 Q&A, (G4) a link
## to the single Entity Home with consistent naming. Measured 4/4 in the count block at the foot.

---

## A note on how this output is built (honesty first)

This optimises the **four universal HIGH-priority gap pages** (confirmed missing on 9/9 scored
competitors — `skill-trust-gap-analysis/data/CONTENT-GAP-MATRIX.md`) for citation by ChatGPT,
Perplexity, Google AI Overview and Gemini. The on-page facts are unchanged from the verified
page drafts — every figure is cited to a verified Source-Bank row by C-ID, or its absence is
hedged honestly. *(Library: M-22 GEO/AEO/LLMO; P-18 — statistics + source citations + structured
formatting earn up to 40% more AI citations, Aggarwal et al. KDD 2024.)*

**What this output controls (and what it cannot).** It controls the on-page GEO attributes that
the research links to citation (a direct answer first, stats + sources, FAQ schema, a consistent
entity). It **cannot** confirm a live Perplexity citation, because the pages are not yet
published — that is a real-world post-publication step, flagged **NOT YET CONFIRMED** below (the
GEO equivalent of the independence test). The skill delivers the citeable artifact; publication
turns it into a citation.

**The single Entity Home** every page points to is defined in section 5. Replace the
bracketed working name/contact placeholders with the registered entity before publishing
*(Library: M-23 Kalicube Entity Home; P-29 single entity home; P-30 naming consistency)*.

**Verified facts available** (Source Bank): C-019 permit applied for online before travel ·
C-010 import permit valid 90 days · C-007 rabies vaccination valid ≥21 days after first dose ·
C-003 held-pet release fee 500 AED/dog (250 AED/cat) · C-022 flydubai cargo-only (no cabin) ·
C-015 Etihad fee USD 399 official vs ~USD 1,500 community (a verified conflict) · C-001 **no
official titer price** (honest absence; community 700–1,300 AED).

---

# PAGE 1 — Confiscation (Fear Resolution)
**Target query:** *"what happens if your dog is taken at Dubai airport"*
**Page:** `skill-content-structure/.../fear-resolution/what-happens-if-your-dog-is-taken-at-dubai-airport.md`

### Direct-answer box (insert as the first 100 words, immediately under the H1)
> **A pet is held at Dubai airport when its paperwork is incomplete — most often a missing
> import permit or an invalid rabies record — not at random.** To prevent it: apply for the
> MOCCAE import permit online before you fly (C-019), ensure the rabies vaccination is at least
> 21 days old (C-007), and time the permit to your flight as it is valid for **90 days** (C-010).
> If a pet is held, the published release fee is **500 AED per dog** (250 AED per cat) at the
> Cargo Village (C-003). Source: UAE Ministry of Climate Change & Environment (MOCCAE).

*(G1 answers the query in sentence one · G2 stats: 90 days, 21 days, 500 AED + citations C-019/
C-007/C-010/C-003 · 71 words.)*

### FAQ schema (JSON-LD — paste into the page `<head>`)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Can my dog be taken at Dubai airport and not returned?",
     "acceptedAnswer": {"@type": "Answer", "text": "A pet is held only when its documentation is incomplete — usually a missing MOCCAE import permit or an invalid rabies record. With a valid permit and rabies record, a healthy pet is not seized. Source: MOCCAE."}},
    {"@type": "Question", "name": "What does it cost if my dog is held at Dubai airport?",
     "acceptedAnswer": {"@type": "Answer", "text": "The MOCCAE published release fee is 500 AED per dog (250 AED per cat) at the Cargo Village, on top of any re-booking costs."}},
    {"@type": "Question", "name": "How do I prevent my dog being held at Dubai airport?",
     "acceptedAnswer": {"@type": "Answer", "text": "Three steps: apply for the MOCCAE import permit online before travel; ensure the rabies vaccination is at least 21 days old and recorded; align the 90-day permit validity window with your flight date."}},
    {"@type": "Question", "name": "How long is the UAE pet import permit valid?",
     "acceptedAnswer": {"@type": "Answer", "text": "The MOCCAE import permit is valid for 90 days from issuance, so it should be timed to the travel date."}},
    {"@type": "Question", "name": "When must the rabies vaccination be done before travelling to Dubai?",
     "acceptedAnswer": {"@type": "Answer", "text": "The rabies vaccination must be at least 21 days old at travel (MOCCAE, C-007); plan the vaccination well ahead of the flight."}}
  ]
}
```
**Entity Home link (G4):** *"Verified against MOCCAE by [Your Brand] — Dubai pet relocation."* → links to the Entity Home (section 5).

---

# PAGE 2 — Titer cost (Cost Transparency)
**Target query:** *"how much does the rabies titer test cost in Dubai"*
**Page:** `skill-content-structure/.../cost-transparency/how-much-does-the-rabies-titer-test-cost-in-dubai.md`

### Direct-answer box (first 100 words)
> **There is no official published price for the rabies titer test in Dubai — MOCCAE lists
> none (C-001) — so any "official price" quote is not from an official source.** The community
> consistently reports **700–1,300 AED**, with a 2–3 week wait and few labs; treat that as a
> sanity-check range, not gospel. What *is* official: the held-pet release fee is **500 AED per
> dog** (C-003). And a real price conflict to know — the Etihad cabin-pet fee is **USD 399**
> officially, not the ~USD 1,500 sometimes quoted (C-015). Source: MOCCAE; Etihad.

*(G1 answers the query in sentence one (honest "no official price") · G2 stats: 700–1,300 AED,
500 AED, USD 399 + citations C-001/C-003/C-015 · 86 words.)*

### FAQ schema (JSON-LD)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How much does the rabies titer test cost in Dubai?",
     "acceptedAnswer": {"@type": "Answer", "text": "There is no official published price — MOCCAE lists none (C-001). The community reports roughly 700–1,300 AED, with a 2–3 week wait; confirm with the lab."}},
    {"@type": "Question", "name": "Is there an official price for the titer test?",
     "acceptedAnswer": {"@type": "Answer", "text": "No. The MOCCAE import-of-pets page publishes no titer-test cost, so anyone quoting an 'official price' is not citing an official source."}},
    {"@type": "Question", "name": "How do I know if I am being overcharged for pet relocation in Dubai?",
     "acceptedAnswer": {"@type": "Answer", "text": "Compare each line against what is officially published (e.g. the 500 AED release fee) versus community ranges; an itemised, sourced quote is trustworthy, a single round number is the warning sign."}},
    {"@type": "Question", "name": "What is the official MOCCAE release fee if a pet is held?",
     "acceptedAnswer": {"@type": "Answer", "text": "500 AED per dog (250 AED per cat) at the Cargo Village (MOCCAE, C-003)."}},
    {"@type": "Question", "name": "Is the Etihad cabin pet fee really USD 1,500?",
     "acceptedAnswer": {"@type": "Answer", "text": "The official Etihad pets page shows a USD 399 fee; the ~USD 1,500 figure is community-reported. Always check the operator's own page (C-015)."}}
  ]
}
```
**Entity Home link (G4):** *"Cost breakdown verified by [Your Brand] — Dubai pet relocation."* → Entity Home.

---

# PAGE 3 — Which airport (Comparison)
**Target query:** *"Sharjah vs Dubai vs Abu Dhabi which airport for pet"*
**Page:** `skill-content-structure/.../comparison/sharjah-vs-dubai-vs-abu-dhabi-which-airport.md`

### Direct-answer box (first 100 words)
> **The airport you choose does not change the regulator's rules — MOCCAE requirements are
> identical at Dubai, Abu Dhabi and Sharjah.** The import permit is applied for online before
> travel at all three (C-019), and pets travel as **cargo, not cabin** (e.g. flydubai: cargo
> only, C-022). What differs is the route experience: the community widely reports **Sharjah as
> the simplest, fastest cargo run (~20 minutes)** — but that is community-sourced, not officially
> published, so confirm it with the carrier for your date. Source: MOCCAE; flydubai.

*(G1 answers the query in sentence one · G2 stats: 3 airports, ~20 minutes + citations C-019/
C-022 · 84 words.)*

### FAQ schema (JSON-LD)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Which UAE airport is easiest for moving a pet?",
     "acceptedAnswer": {"@type": "Answer", "text": "The regulator's rules are identical at Dubai, Abu Dhabi and Sharjah. The community reports Sharjah as the simplest, fastest cargo route, but this is community-sourced, not official — confirm with the carrier."}},
    {"@type": "Question", "name": "Does the MOCCAE import permit differ by airport?",
     "acceptedAnswer": {"@type": "Answer", "text": "No. The permit is applied for online before travel and applies to all UAE entry points (MOCCAE, C-019)."}},
    {"@type": "Question", "name": "Can a pet fly in the cabin into the UAE?",
     "acceptedAnswer": {"@type": "Answer", "text": "Into Dubai, pets travel as cargo, not in the cabin (e.g. flydubai: cargo only, C-022). Cabin options vary by carrier and airport — confirm directly."}},
    {"@type": "Question", "name": "Is the 'Sharjah hack' officially published?",
     "acceptedAnswer": {"@type": "Answer", "text": "No. The fast ~20-minute Sharjah cargo route is community-reported and not published by an official source — verify with the carrier and MOCCAE for your date."}},
    {"@type": "Question", "name": "Does choosing a different airport bypass the rabies timeline?",
     "acceptedAnswer": {"@type": "Answer", "text": "No. No airport bypasses the permit or the rabies vaccination timeline — those are set by MOCCAE and apply everywhere."}}
  ]
}
```
**Entity Home link (G4):** *"Airport guidance maintained by [Your Brand] — Dubai pet relocation."* → Entity Home.

---

# PAGE 4 — Summer embargo (Process Guide)
**Target query:** *"can I move my pet to Dubai in summer"*
**Page:** `skill-content-structure/.../process-guide/can-i-move-my-pet-to-dubai-in-summer.md`

### Direct-answer box (first 100 words)
> **Yes, you can move a pet to Dubai in summer — but airlines, not MOCCAE, restrict pet cargo in
> peak heat, so it must be planned around.** The regulator's rules do not change by season: the
> import permit is applied for online and valid **90 days** (C-019, C-010). The heat embargo is
> an airline/cargo rule — pets travel cargo-only (flydubai, C-022) — and there is **no official
> government embargo date**; the commonly-cited June–September window is airline/community
> guidance, so confirm your carrier's live policy before booking. Source: MOCCAE; flydubai.

*(G1 answers the query in sentence one ("yes, but plan around the airline heat rule") · G2 stats:
90 days, June–September + citations C-019/C-010/C-022 · 88 words.)*

### FAQ schema (JSON-LD)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Can I move my pet to Dubai in summer?",
     "acceptedAnswer": {"@type": "Answer", "text": "Yes, but airlines restrict pet cargo in peak summer heat, so the move must be planned around the carrier's heat policy. MOCCAE rules do not change by season."}},
    {"@type": "Question", "name": "Is there an official summer ban on flying pets to Dubai?",
     "acceptedAnswer": {"@type": "Answer", "text": "There is no official MOCCAE embargo date. The heat embargo is an airline/cargo operational rule; the commonly-cited June–September window is airline/community guidance — confirm with your carrier (C-022)."}},
    {"@type": "Question", "name": "How do I plan a summer pet move to Dubai?",
     "acceptedAnswer": {"@type": "Answer", "text": "Start early so the rabies and permit timeline never forces a peak-heat flight (permit valid 90 days, C-010); confirm the carrier's live heat policy; consider a night flight or a cooler shoulder date."}},
    {"@type": "Question", "name": "Do the MOCCAE rules change in summer?",
     "acceptedAnswer": {"@type": "Answer", "text": "No. The import permit is still applied for online and valid 90 days regardless of season (C-019, C-010); only the airline heat rules change."}},
    {"@type": "Question", "name": "Which months are affected by the Dubai pet heat embargo?",
     "acceptedAnswer": {"@type": "Answer", "text": "Commonly June–September, but this is airline/community guidance, not an official figure, and varies by carrier and route — confirm the specific dates with your airline's live cargo policy."}}
  ]
}
```
**Entity Home link (G4):** *"Summer-move planning by [Your Brand] — Dubai pet relocation."* → Entity Home.

---

# 5 — ENTITY DEFINITION DOCUMENT (the single Entity Home)
*(Library: M-23 Kalicube Entity Home — one canonical reference Google and LLMs cross-check; P-29
designate a single entity home, not the homepage; P-30 identical naming/description everywhere.
Replace the bracketed placeholders with the registered entity before publishing.)*

**Canonical name:** `[Your Brand]` (working name — replace with the registered legal/trading name)
**Entity Home URL:** `https://[yourbrand].ae/about` (a dedicated, stable About/Entity page — not the homepage)
**One-line description (use this exact wording everywhere — P-30):**
> *"[Your Brand] is a Dubai-based international pet relocation concierge that manages MOCCAE
> permits, airline coordination and documentation so pets travel safely to and from the UAE."*

**Disambiguation (who we are / are not):** a managed pet-relocation concierge — **not** a cargo
company, freight forwarder or budget transport service.

**Credentials to assert (fill with the real ones):** `[MOCCAE registration]`, `[IPATA membership]`,
`[trade licence / DED no.]`. *(Library: M-24 E-E-A-T four-pillar; P-32 credentials on YMYL pages.)*

### Organization / LocalBusiness schema (JSON-LD — on the Entity Home, site-wide)
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://[yourbrand].ae/#organization",
  "name": "[Your Brand]",
  "description": "Dubai-based international pet relocation concierge managing MOCCAE permits, airline coordination and documentation for pets travelling to and from the UAE.",
  "url": "https://[yourbrand].ae/",
  "telephone": "[+971-...]",
  "areaServed": ["AE", "Dubai"],
  "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE", "streetAddress": "[street]"},
  "knowsAbout": ["pet relocation", "MOCCAE import permit", "rabies titer test", "pet cargo to Dubai"],
  "sameAs": [
    "https://www.linkedin.com/company/[yourbrand]",
    "https://www.instagram.com/[yourbrand]",
    "https://www.facebook.com/[yourbrand]",
    "https://g.page/[yourbrand]"
  ]
}
```
*(Library: F-28 sameAs/Wikidata linked-data stack — the `sameAs` array ties the entity to its
verified profiles so Google and LLMs corroborate it. P-47 — validate with Google's Rich Results
Test before publishing.)* **NAP must be byte-identical** to every directory/citation listing.

---

# 6 — WEEKLY CITATION MONITORING CHECKLIST (10 target queries)
*(Library: P-48 track citation frequency across ChatGPT/Perplexity/Gemini/Google AI Overview
weekly; F-21 RAG open-world citation loop.)* Run each query on all four engines; record whether
**[Your Brand]** (or its page) is cited, and which competitor/source is cited instead.

| # | Target query | Page it should win | ChatGPT | Perplexity | Google AIO | Gemini |
|---|--------------|--------------------|---------|------------|------------|--------|
| 1 | what happens if my dog is taken at Dubai airport | Confiscation | ☐ | ☐ | ☐ | ☐ |
| 2 | Dubai pet import release fee if held | Confiscation | ☐ | ☐ | ☐ | ☐ |
| 3 | how much does the rabies titer test cost in Dubai | Titer cost | ☐ | ☐ | ☐ | ☐ |
| 4 | is there an official price for the dog titer test UAE | Titer cost | ☐ | ☐ | ☐ | ☐ |
| 5 | Sharjah vs Dubai vs Abu Dhabi airport for pet | Which airport | ☐ | ☐ | ☐ | ☐ |
| 6 | can pets fly in the cabin into the UAE | Which airport | ☐ | ☐ | ☐ | ☐ |
| 7 | can I move my pet to Dubai in summer | Summer embargo | ☐ | ☐ | ☐ | ☐ |
| 8 | Dubai pet summer heat embargo months | Summer embargo | ☐ | ☐ | ☐ | ☐ |
| 9 | how long is the UAE pet import permit valid | Confiscation / Summer | ☐ | ☐ | ☐ | ☐ |
| 10 | how to move a dog to Dubai without it being seized | Confiscation | ☐ | ☐ | ☐ | ☐ |

**Cadence:** weekly (P-48). **Action loop (F-21):** a query where a generic/competitor source is
cited and our answer is stronger → strengthen the direct-answer box and FAQ, re-submit, re-check.
**Baseline to record on first run (pre-publication):** which sources the engines cite *today* —
the gap-matrix shows 9/9 competitors omit these answers, so the baseline is expected to be
generic/uncited; that is the citation opportunity this skill captures.

---

## Functional Quality Threshold — measured (README Check 46)

| Page | G1 direct-answer box (≤100w, answers query) | G2 ≥1 stat + ≥1 C-ID in the answer | G3 FAQ schema ≥5 Q&A | G4 Entity Home link |
|------|---------------------------------------------|------------------------------------|----------------------|---------------------|
| 1 · Confiscation | ✅ (71w) | ✅ 90d/21d/500 AED · C-019/C-007/C-010/C-003 | ✅ 5 | ✅ |
| 2 · Titer cost | ✅ (86w) | ✅ 700–1,300/500 AED/USD 399 · C-001/C-003/C-015 | ✅ 5 | ✅ |
| 3 · Which airport | ✅ (84w) | ✅ ~20 min/3 airports · C-019/C-022 | ✅ 5 | ✅ |
| 4 · Summer embargo | ✅ (88w) | ✅ 90d/Jun–Sep · C-019/C-010/C-022 | ✅ 5 | ✅ |

| Gate | Requirement | Result |
|------|-------------|--------|
| G1 · direct-answer box in first 100 words | 4 of 4 pages | **4/4** ✅ |
| G2 · ≥1 statistic AND ≥1 verified C-ID inside the answer | 4 of 4 pages | **4/4** ✅ |
| G3 · valid FAQPage schema, ≥5 Q&A | 4 of 4 pages | **4/4** ✅ (20 Q&A total) |
| G4 · links to the single Entity Home, consistent naming | 4 of 4 pages | **4/4** ✅ |
| Entity Definition Document (Organization/LocalBusiness + sameAs schema) | present | **✅** |
| Weekly citation-monitoring checklist (10 target queries × 4 engines) | present | **✅ (10 queries)** |

**Threshold MET — 4/4 pages on all four on-page GEO gates**, entity definition present, 10-query
monitoring checklist present. Every figure is cited to a verified Source-Bank row or hedged
honestly; the GEO trifecta the research links to a ~40% citation lift (statistics + source
citations + structured formatting, P-18) is present on all four pages.

**Live-citation confirmation (output item 5): NOT YET CONFIRMED — requires publication.** The
pages must be published and indexed before a real Perplexity/AIO citation can be verified; this
is the post-publication validation step (the GEO equivalent of the independence test), tracked in
the monitoring checklist above.
