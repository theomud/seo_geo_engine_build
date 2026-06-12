# AI-citation synthesis — do the incumbents appear in AI answers? (2026-06-09)

Synthesis of 3 GEO-citation probes (UAE · strict+EU · Americas+India).

## ⚠️ Method caveat (read first)
**Google AI Overviews were NOT programmatically retrievable** in this environment — WebSearch does
not expose the live AIO surface. All three agents correctly refused to fabricate citations and instead
**inferred** citation-likelihood from observable page structure (answer-first text, schema, official-source
links, entity density, freshness) using `GEO/geo-scoring-rubric.md`. **Organic results are observed;
AI-Overview citation is inferred.** True measurement still requires a manual browser check or API run,
logged to `TRACKING/geo_visibility.csv`.

## What we can say (inferred)

1. **On government-owned regulatory queries, AI most likely cites the regulator first** — CDC, USDA-APHIS,
   CFIA, DAFF, AVS, EC, gov.uk. You don't get cited by restating the rules; the regulator wins that.
2. **The aggregators likely to be AI-cited are the dated, schema'd ones** — pettravel.com (dated + JSON-LD +
   answer-first) and petrelocation.com (high authority). **The UAE locals (CarryMyPet, Pawsome, DKC) are
   unlikely to be cited** — no datelines, no deep MOCCAE links, no FAQ/HowTo schema.
3. **Several queries have NO authoritative citation at all — wide open:**
   - **Cost** ("cost to relocate a pet from Dubai") — nobody prices it; widest open field.
   - **Dubai → USA** — *zero regulators cited*; all relocators + PR wire.
   - **India-returnee NOC** — the real issuer (AQCS) ranks below relocators.

## 🔥 The goldmine: AI is currently citing WRONG information

Two places where the AI's grounding corpus is factually wrong, which a dated, sourced page can correct —
**becoming the corrective citation is the single clearest GEO win:**

- **MOCCAE permit validity:** the web consensus says **30 days**; the regulator (MOCCAE, screenshot-verified)
  says **90 days**. An AI synthesising the web gets it **wrong**. (This is our claim-audit item CQ-01, now
  doubly important — it's not just our accuracy, it's a citation opportunity.)
- **Dubai → USA:** the synthesised answer repeats a **non-existent "CDC dog import permit, apply 6 weeks
  before."** No such permit exists under the current (Aug-2024) rules — it's the free CDC Dog Import Form.
  The commercial corpus is propagating **outdated CDC rules**, and AI is grounding on it.

**Implication:** where the SEO lane is closed (gov owns the rules), the GEO lane is open precisely because
the incumbents are stale, unschema'd, and uncited. The play isn't to out-rank — it's to be the **accurate,
dated, officially-cited source that corrects what the AI currently gets wrong.**

## New bets this generated (filed in ledger)
- **G06** — a dated, official-source-cited page that *corrects* a fact AI currently gets wrong (90-day
  permit; no CDC "permit") gets AI-cited for that query.
- **G07** — on queries where no authority is cited (cost, Dubai→USA), a sourced answer-first page earns
  AI citation faster than on gov-contested queries.

## The real measurement (next)
To turn "inferred" into "observed": run the query set through actual AI engines (AI Overviews in-browser,
ChatGPT, Perplexity, Gemini), record who's cited, log to `TRACKING/geo_visibility.csv`. That's the
instrument; this pass is the hypothesis.

---

## MEASURED BASELINE — 2026-06-09 (WebSearch-grounded surface)

Ran the 15-query set through the **WebSearch grounded-answer surface** (a real AI-retrieval proxy — NOT
Google's proprietary AIO, which is still browser/API-only). 15/15 returned grounded summaries. Logged to
`TRACKING/geo_visibility.csv`. **PawRoute absent from all 15** — the honest zero baseline we re-measure
against post-launch.

### Did our inferences call it right? (the same loop, on ourselves)

| Inference (from the inferred pass) | Measured result | Verdict |
|---|---|---|
| Government owns the "rules" queries | DAFF, AVS, EC, CDC (6×), CFIA all cited #1 on their rules queries | ✅ **Confirmed** |
| gov.uk / DAFF absent on certain phrasings | "Australia quarantine" = no gov; "UK from non-EU" = no gov.uk | ✅ **Confirmed (strong)** |
| Cost query is wide open, no authority | All aggregators, zero gov | ✅ **Confirmed** |
| Dubai→USA propagates WRONG CDC info | opsmatters.com #1 repeats the defunct "CDC import permit"; no CDC.gov; APHIS buried #7 | ✅ **Confirmed — with the actual source** |
| UAE locals unlikely to be cited | **carrymypet.ae appears in 4/5 UAE-area queries**; furry.ae, sandypaws.ae, petfirst.ae also surface | ❌ **Refuted** |
| pettravel/petrelocation dominate aggregators | They appear, but the field is fragmented (jamescargo, moveconnector, opsmatters, worldcarepet, petsabroaduk all rank #1 somewhere) | ◐ **Partial** |

**Score: 4 confirmed (one a bullseye), 1 partial, 1 refuted.** Honest result for an inference engine.

### Two findings the measurement added that inference missed
1. **CarryMyPet.ae is the rival to watch** — it's already surfacing in AI-grounded answers across UAE
   routes *despite* its schema/citation gaps, on tenure + keyword-match alone. Our most direct threat.
2. **USDA APHIS is the single most-cited domain across ALL geographies** (UAE, Australia, India, even
   non-US routes) because it publishes a US-export page for every destination. The AI leans on it as a
   universal pet-travel reference — a structural quirk worth exploiting (it's US-origin-blind, so an
   origin-agnostic UAE source fills the gap it can't).

### Impact on the ledger
- **G06 (corrective-citation bet) just got real supporting evidence** — the Dubai→USA misinformation is
  now *observed*, not hypothesised. The premise is sound; the bet still resolves only when our dated,
  CDC-cited page is live and measured as the citation that replaces it.
- This baseline becomes the **before** snapshot for resolving B07 / G-series post-launch.
