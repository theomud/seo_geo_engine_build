# AI Citation — Source Verification Pass

A per-measurement check: does the auto-found candidate (`SOURCES.md`) actually support
the point? If not, what is the correct verified source + evidence tier?

## Headline result
**Auto-sources that actually fit: 0 / 10.** Every candidate in `SOURCES.md` is from an
unrelated field (medicine, deep learning, genomics, climate, crystallography). The
engine's *curated* basis, however, **does** hold up — the correct sources are listed
below. So: the engine is well-grounded; the **auto-research source layer is not usable
for this engine** and must be replaced with curated sources.

## Why it's like that (the real reason)
The auto-tool does keyword search **sorted by raw citation count**. For a niche, recent,
applied topic that fails three ways:
1. **Citation-rank bias.** Medicine/ML/genomics papers have 20k–60k citations; the
   relevant web/marketing papers have hundreds. The mega-fields always win.
2. **Token collision.** Query words are generic academic terms elsewhere: "answer" →
   PRISMA reporting; "table" → PRISMA/KEGG; "GEO" → *geo*science/genomics; "entity" →
   protein/UniProt; "freshness" → cardiology guidelines.
3. **Recency penalty.** The actual GEO paper (Aggarwal et al., 2024) is new and has far
   fewer citations than 2009–2018 classics, so it never surfaces above them.
Net: keyword + citation-rank returns the **biggest fields**, not the **right niche**.

## Per-measurement verdict + the correct verified source
| Measurement | Auto candidate (verdict) | Correct verified source | Tier | Status |
|---|---|---|---|---|
| Answer-first opening | PRISMA scoping reviews ❌ wrong field | Google Search Central — AI-features guidance (answer-first/extraction) + practitioner | T2/T6 | Verified mechanism |
| Statistics | ChatGPT opinion paper / PINNs ❌ | **Aggarwal et al., “GEO: Generative Engine Optimization”, KDD 2024 (arXiv:2311.09735)** — Statistics +24.9% | T4 | Verified |
| Cited sources | qualitative content analysis / CMIP6 climate ❌ | same GEO paper — Cite Sources **+27.8%** (top lever) | T4 | Verified |
| Direct quotations | focus-group methodology ❌ | same GEO paper — Quotation +25.9% | T4 | Verified |
| Quotable standalone facts | LeCun deep learning ❌ | Lewis et al. 2020, Retrieval-Augmented Generation (NeurIPS) — passage/chunk extraction; + Google AIO chunking | T4/T2 | Verified mechanism |
| Question-style headings | Pascal VOC vision ❌ | Google AIO (same index, query fan-out) + practitioner Q→A | T2/T6 | Verified (weaker) |
| Scannable lists & tables | PRISMA / KEGG ❌ | practitioner consensus (liftable lists/tables) — no strong paper | T6 | Weakly backed (honest) |
| FAQ structured data | DBpedia/knowledge-graph (adjacent) ❌ | Google structured-data docs — **caveat: Google states schema is NOT required for generative AI**; helps discoverability only | T2 (caveat) | Verified-with-caveat |
| Clear, consistent entity | protein structure / UniProt ❌ | Barnard/Kalicube Entity Home (practitioner) + Google entities/Knowledge Graph + schema.org sameAs | T2/T3/T6 | Verified mechanism |
| Freshness & dating | cardiology guidelines / Visual Genome ❌ | QDF (2024 leak / practitioner) + Google freshness | T2/T3 | Verified (weaker) |

## Honest conclusion
- **Strongly backed (T4):** statistics, cited sources, quotations — the GEO paper. These are the engine's real backbone.
- **Backed by official docs / practitioner (T2/T6):** answer-first, headings, FAQ (with caveat), entity, freshness.
- **Weak (T6 only):** scannable lists/tables — practitioner, not papered.
- **The auto `SOURCES.md` for this engine should be discarded** and replaced with the curated table above. The OpenAlex tool is useful for *broad* topics, not this niche.

## Fix
Curate the sources (above) into the engine, OR constrain the tool by concept-ID + venue
+ recency instead of raw-citation keyword search. Until verified, no source governs scoring (firewall).
