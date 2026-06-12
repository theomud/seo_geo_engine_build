# Web Persuasion -- Validation Report

Validation summary for the Numini Web Persuasion knowledge base (Research Elevator domain module). Internal document.

## Headline counts

- Accepted (load-bearing) claims: **31**
- Quarantined claims: **7**
- Tier mix (accepted): Tier 1 = 22, Tier 2 = 9, Tier 3 = 0
- Tier-1 outnumbers Tier-3 in load-bearing claims: **PASS**

## Grade distribution (accepted)

- HIGH: 17
- MODERATE: 14
- LOW: 0
- VERY_LOW: 0

## Coverage by pillar x grade (accepted)

| Pillar | HIGH | MODERATE | LOW | VERY_LOW | TOTAL |
|---|---:|---:|---:|---:|---:|
| ai_assisted_writing_editing | 2 | 2 | 0 | 0 | 4 |
| blog_purpose_business_model | 0 | 1 | 0 | 0 | 1 |
| blogging_content_strategy | 1 | 1 | 0 | 0 | 2 |
| conversion_copywriting | 2 | 2 | 0 | 0 | 4 |
| geo | 1 | 2 | 0 | 0 | 3 |
| lead_generation_content_system | 1 | 2 | 0 | 0 | 3 |
| persuasion_behavioural_science | 3 | 0 | 0 | 0 | 3 |
| reading_attention_psychology | 2 | 2 | 0 | 0 | 4 |
| seo_2026 | 2 | 2 | 0 | 0 | 4 |
| web_ux_design | 3 | 0 | 0 | 0 | 3 |

## Contested claims (caveats preserved, not laundered)

- The F-shaped scanning pattern is ONE of several gaze patterns, not a design goal; it is a sign of skimming that good layout (front-loading, headings, bullets) can prevent or reshape. -- *Often mis-cited as a universal law; NN/G stress it is one of several patterns and is preventable with good design.*
- Working memory is sharply limited (classically about 7 plus or minus 2 items, with later estimates near 4 chunks), so interfaces should chunk information rather than present long undifferentiated lists. -- *The exact capacity is debated; modern estimates often cite ~4 chunks. Use as a chunking heuristic, not a hard limit.*
- E-E-A-T (Experience, Expertise, Authoritativeness, Trust) is a quality framework used in Google's Search Quality Rater Guidelines, NOT a direct ranking factor; Trust is described as the most important component. -- *Widely mis-stated as a direct ranking signal; Google states raters do not directly affect ranking and E-E-A-T is a concept, not a metric.*
- Generative Engine Optimization (Aggarwal et al., KDD 2024) defines methods to raise a source's visibility in generative-engine answers; Cite Sources, Quotation Addition, and Statistics Addition were among the strongest, especially combined, with up to ~40% visibility uplift on GEO-bench. -- *The 'up to 40%' is a CEILING and is domain-dependent ('the efficacy of these strategies varies across domains') -- NOT a guaranteed uplift. Figure confirmed verbatim in the full paper (Numini fetched the full text, 9 Jun 2026): 'GEO can boost visibility by up to 40% in GE responses.'*
- Readability formulas (Flesch Reading Ease, Flesch-Kincaid Grade Level) are heuristics, not ground truth; recent work shows formulas and even LLMs are weak predictors of true reading ease, so they should guide, not be gamed. -- *Treat readability scores as a guide, never a target to optimise blindly.*

## Dated tactics (still_valid_2026 = false)

- Classic ad/affiliate blogging tactics aimed at raw traffic (and 2000s-era channels like Digg, Del.icio.us, trackbacks, blog carnivals) do not transfer to a lead-gen service blog; the durable, transferable lesson is to build an email list for nurture. -- *Traffic-source specifics are obsolete; the list-building principle still holds. Tier-3, illustrative only.*

## Prior-report reconciliation

- The prior SEO/GEO report (`Research/SEO_GEO/*_2026-06-02.*`) is **superseded** for the claims it overlaps: its SEO/GEO findings are now represented as graded, source-confirmed rows in `claim_bank.csv` (pillars `seo_2026`, `geo`). The new work adds live AI-Overview citation measurement and confirms figures against fetched primaries. See `web_persuasion_supersedes_2026-06-02.md`.
- The two uploaded practitioner PDFs are reconciled as Tier-3: durable principles kept (build the email list), dated tactics flagged `still_valid_2026 = false` and quarantined.

## Gaps / next harvest

- Confirm the GEO 'up to 40%' figure against the FULL GEO paper PDF (currently quarantined -- not on the abstract page).
- Expand Tier-2 corroboration for CRO/landing-page claims (currently MODERATE).
- Re-measure AI-Overview citation share periodically (volatile).
- Optional: extract additional atomic claims from the academic harvest (noisy; needs relevance filtering before promotion).
