# GEO Checklist -- Generative Engine Optimization

> Getting cited by AI answer engines (Google AI Overviews, ChatGPT, Perplexity, Gemini).
> Backed by `claim_bank.csv` (pillar `geo`) and Numini's own AI-Overview measurements.

## Standing caveat

- **"Up to 40% visibility uplift" is a CEILING on the GEO-bench benchmark, domain-dependent --
  never a guarantee.** *(Aggarwal et al., KDD 2024; figure is in the full paper, not the abstract.)*
- **GEO does not replace SEO.** AI-Overview citations are drawn heavily from -- but not only
  from -- the classic top-10 organic results. *(Numini measurement, Jun 2026.)*

## The 9 GEO methods (apply the strongest, especially combined)

- [ ] **Cite Sources** -- reference authoritative sources inline.
- [ ] **Quotation Addition** -- include clear, quotable statements an engine can lift.
- [ ] **Statistics Addition** -- add relevant, verifiable statistics (from the claim bank).
- [ ] **Fluency Optimization** -- clean, fluent, well-structured prose.
- [ ] **Authoritative tone** -- confident, expert framing (without overclaiming).
- [ ] Plus: clear definitions, keyword/term coverage, technical accuracy, easy-to-understand
      phrasing.
  *(Cite Sources + Quotation + Statistics + Fluency were the strongest, especially combined.)*

## Retrievability

- [ ] Content is chunked into self-contained sections that each answer ONE question.
- [ ] Entities (brand, service, routes) are named unambiguously and consistently.
- [ ] Facts are consistent across the site and the wider web (no contradictions).
- [ ] Key answers appear near the top of their section (front-loaded).

## AI Mode & entity foundation (2026 additions)

> Six gaps surfaced by `DEEP-RESEARCH-2026-06-11.md` (Section C). The 9 methods above are tuned
> for **AI Overviews**; these add the parallel pass for **Google AI Mode**, which is ~4× longer
> and cites **3.3 entities on avg vs 1.3** for AI Overviews — so it over-indexes on entity
> density, community signals, and named-entity recognition.

- [ ] **AI Mode entity density** -- target **3+ named, disambiguated entities per self-contained
      chunk** (airlines, breeds, fees, authorities, documents, dates). Tighter than the generic S4
      target; AI Mode rewards it specifically. *(no stuffing — entities must be load-bearing.)*
- [ ] **Community signal** -- ensure core claims also appear in UAE/expat pet-owner community
      threads (Facebook groups, Reddit `r/dubai`, `r/expats`). AI Mode over-indexes on community
      citations; content the model can corroborate in a forum is likelier to be cited.
- [ ] **Video as a citation pathway** -- YouTube is a top citation source in AI Overviews. Embed a
      relevant video on key/money pages to open a citation pathway we don't currently have.
- [ ] **FAQ schema = REQUIRED** (upgraded from optional/"Ship" step) -- add FAQ schema to every
      blog post and HowTo schema to every route guide. Schema markup correlates with higher AI
      citation rates.
- [ ] **Brand entity disambiguation** -- get Google's Knowledge Graph to clearly associate our
      **brand name + location + service category**. This is the foundation for being cited *as a
      named entity*, and underpins brand-mention tracking on zero-click queries.
- [ ] **Visible update datestamp** -- show an explicit "Last updated: <date>" in the **visible page
      text** (not just meta/`<head>`). AI assistants read visible text; a fresh visible date is a
      recency signal they can lift.

## Measurement (this is the GEO ground-truth)

- [ ] For each priority head query, capture the AI Overview and record which domains/URLs are
      cited (`harvest_serp.py`).
- [ ] Track **AI-citation share** over time (AI Overviews are volatile -- re-measure regularly).
- [ ] Goal: BE one of the cited sources for the money queries (e.g. "pet relocation Dubai to
      UK"), then capture the click into a quote.

## Do NOT

- Quote the 40% figure as a promised result.
- Let entity facts drift between pages.
- Treat GEO as a replacement for ranking -- earn the top-10 organic too.
