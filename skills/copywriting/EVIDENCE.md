# Evidence bank — sourced claims & benchmarks

The truth layer behind `SKILL.md`. Every load-bearing claim with its **tier**, **source**,
and a **contested note** where the popular version runs ahead of the evidence. Compiled
from 4 sources (validated persuasion corpus · SEO_GEO ranking report · deep-research web
pass · curated skills). **Tiered/primary evidence wins over vendor/practitioner claims.**

## Tiers
`T1` sworn DOJ testimony / primary regulator · `T2` official vendor/Google docs ·
`PRIMARY` own measurement · `T4` peer-reviewed paper · `CONSENSUS` practitioner consensus
(no RCT) · `VENDOR` vendor benchmark (selection bias) · `⚠️` weaker than popular claim.

---

## A. Persuasion & psychology
| Claim | Tier | Source | Note |
|---|---|---|---|
| Cialdini's 7 principles (Reciprocity, Commitment, Social Proof, Authority, Liking, Scarcity, **Unity**-2016) | T1 | Cialdini, *Influence* 1984 / *Pre-Suasion* 2016 (verified 3-0) | Widely replicated |
| Behaviour = Motivation + Ability + Prompt converging (**Fogg B=MAP**) | T1 | Fogg 2009 (doi:10.1145/1541948.1541999) | If it fails, cut friction / fix prompt before adding motivation |
| Fear-acknowledgement + high-efficacy solution = strongest trust mechanism | T4 | Tannenbaum et al. 2015 meta-analysis, 127 studies, n=27,372 | Acknowledge ≠ exploit |
| Ethical influence vs dark pattern: make the better choice easier, not the worse one harder to avoid | T1 | NN/G / Brignull deceptive patterns 2023 | The ethical line |
| Kahneman System 1/2 framing (most web decisions are System 1) | T1(framing) ⚠️ | Kahneman 2011 | Dual-process stands; some priming numbers replicate poorly — **quarantined as illustrative** |
| Berger STEPPS; high-arousal emotion drives sharing (arousal, not positivity) | T1 | Berger & Milkman 2012 JMR (doi:10.1509/jmr.10.0353) | |

## B. Conversion benchmarks (attribute, don't treat as law)
| Claim | Tier | Source | Note |
|---|---|---|---|
| Median landing-page conversion **6.6%**; range **3.8% SaaS – 12.3% entertainment**; Prof. Services **6.1%** | VENDOR | Unbounce 2024 Conversion Benchmark Report (41k pages, 464M visits) | Paid/optimized skew; neutral ~2.35% (WordStream) |
| Readability ↔ conversion: 5th–7th grade **11.1%**, 8th–9th **7.1%**, professional **5.3%** | VENDOR ⚠️ | Unbounce 2024 | Correlation, not causation (verified 2-1). Write ~7th grade |
| **~70%** cart/funnel abandonment; ~32 checkout fixes → **up to ~35%** lift | T1 | Baymard Institute checkout-usability | 35% is a ceiling, large-sample |
| **Fewer form fields** + trust signals near the form convert better | T1 | Baymard form research | Every non-essential field = drop-off |
| Single primary CTA beats competing CTAs | Tier-2/CONSENSUS | CXL / GoodUI / Unbounce | Graded expert consensus |
| Attention ratio ~1:1 (one page, one goal) | Tier-2 ⚠️ | Unbounce CCD (Oli Gardner) | Vendor uplift %s context-specific — **quarantined**; principle holds |
| "Best practices" frequently fail when tested | CONSENSUS | CXL conversion-myths | Test on your audience |

## C. Email benchmarks (2025)
| Claim | Tier | Source | Note |
|---|---|---|---|
| Mailchimp avg **35.63% open / 2.62% click / 0.22% unsub** | VENDOR | mailchimp.com/resources/email-marketing-benchmarks | Platform customers only |
| MailerLite avg **43.46% open / 2.09% click** | VENDOR | mailerlite.com benchmarks | |
| **Apple Mail Privacy Protection inflates opens ~10–15+ pts** → use click rate | T2/⚠️ | Apple MPP (Sept 2021+) | Prefer click / click-to-open |

## D. SEO ranking mechanics (SEO_GEO report)
| Claim | Tier | Source | Note |
|---|---|---|---|
| Ranking ≈ **T\*** (Anchors+Body+**Clicks**) + **Q\*** static site-wide authority + **P\*** popularity | T1 | US v. Google testimony (Kim, Nayak) | Reframes the public model |
| **Navboost** memorises which result satisfied a query over a **13-month window** | T1 | Nayak sworn testimony | Kills the old "we don't use clicks" denial |
| **Q\*/siteAuthority is site-wide & static** → topical depth lifts every page | T1+T3 | testimony + 2024 leak | Build clusters; stay focused (siteFocusScore) |
| PageRank demoted to **one input** to Q* | T4+T1 | Brin-Page 1998 + testimony | Editorial on-topic links only (Penguin zeroes spam) |
| Write for **meaning/entities, not exact keywords** | T1+T4 | RankEmbed(BERT), DPR | Stuffing is also the worst GEO method |
| **HCU/E-E-A-T**: people-first content; Trust most important; **E-E-A-T is NOT a direct ranking factor** | T2 | Google QRG + helpful-content docs (verified 3-0) | "Experience" added Dec 2022; HCU in core Mar 2024 |
| Helpful Content System folded into core (Mar 2024) | T1 | Google March-2024 core update | No longer a standalone signal |

## E. GEO / AI-citation
| Claim | Tier | Source | Note |
|---|---|---|---|
| **Citation decoupled from ranking — 66% of AI-Overview citations from outside top-20 organic** | PRIMARY | SEO_GEO 11-query probe | Being cited ≠ ranking |
| GEO levers (stats + quotations + cite sources, self-contained passages) lift generative visibility **+25–28%** | T4 | Aggarwal et al., GEO, KDD 2024 (arXiv:2311.09735) | Proven on Perplexity/GPT; inferred for Google AIO |
| The **"+40%" GEO figure is a contested ceiling** (one method, GEO-bench, proxy metric, domain-dependent) | T4 ⚠️ | same paper, full text | Flagged by corpus **and** SEO_GEO **and** deep-research — use +25–28% |
| AI engines favour triangulated facts: Reddit/YouTube/**Wikipedia** (ChatGPT ≈48% Wikipedia in top citations) | PRIMARY/T6 | SEO_GEO + studies | Seed genuine corroboration; no astroturf (SpamBrain) |
| Be visible in **Bing** (ChatGPT ≈87% aligned to Bing; ~11% domain overlap ChatGPT/Perplexity) | T6 | reverse-engineering | Different index → different winners |
| Numini own measure: "pet relocation dubai→uk" AIO cited 14 sources, **8 in top-10 organic** | PRIMARY | Research/Web_Persuasion harvest | AIO volatile; re-measure |
| **Disowned hacks:** llms.txt / AI-markdown files, content-shredding, schema-as-ranking | T2 | Google statements | No primary support |

## F. Topic clusters / structure
| Claim | Tier | Source | Note |
|---|---|---|---|
| Pillar + interlinked cluster builds topical authority | Tier-2 | HubSpot + SEO practitioners | |
| HubSpot 2016 internal-link → ranking | ⚠️CONTESTED | HubSpot 2016 report | Correlation (2-1); **causal version refuted 1-2** in our verify |
| Money pages vs supporting content; informational post must never be a dead end | Tier-2 | topical-cluster consensus | Every post links to a money page |
| TOFU/MOFU/BOFU intent→funnel mapping | Tier-2 | search-intent consensus | |

## G. Messaging / positioning frameworks
| Claim | Tier | Source | Note |
|---|---|---|---|
| **StoryBrand SB7** (Character-Problem-**Guide**-Plan-CTA-Failure-Success) | CONSENSUS | Miller, *Building a StoryBrand* (verified 3-0) | "clarity beats superiority" is an assertion, ⚠️ not a study |
| **April Dunford** 10-step positioning | CONSENSUS | *Obviously Awesome* | Define who you don't serve |
| MECLABS heuristic **C = 4m + 3v + 2(i−f) − 2a** | CONSENSUS | MECLABS/Flint McGlaughlin | Thinking tool, not a formula to compute |
| AIDA / PAS / Ogilvy headline 5× | CONSENSUS | classic direct-response canon | Ogilvy ratio is lore, not a measured constant |

## H. A/B testing statistics
| Claim | Tier | Source | Note |
|---|---|---|---|
| **p-value = P(data \| H0)**, not P(effect real) | T1 | ASA 2016 Statement (verified 3-0) | Core misunderstanding |
| **Peeking inflates false positives to 20–40%+**; fix sample size or use sequential testing | T1 | Kohavi/Tang/Xu 2020; Johari/Pekelis/Walsh | Don't stop when it "looks" significant |

## I. UX & technical
| Claim | Tier | Source | Note |
|---|---|---|---|
| Users read **~20–28%** of page words → front-load (inverted pyramid) | T1 | NN/G | |
| **F-pattern is one of several scan patterns, not a law** — good layout reshapes it | T1 | NN/G 2017 | Often mis-cited as universal |
| Nielsen's 10 usability heuristics = baseline | T1 | NN/G | |
| **Core Web Vitals good: LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1** (INP replaced FID Mar 2024) | T1 | web.dev/articles/vitals | |
| Hick's law (choices↑ → decision time↑); Fitts's law (target size/distance) | T1 | Hick 1952 / Fitts 1954 | Reduce options; big close CTAs |
| Working memory ≈ **4 chunks** (classically 7±2) → chunk content | T1 ⚠️ | Miller 1956 / Cowan 2001 | Exact capacity debated; use as heuristic |
| Schema/JSON-LD for **eligibility, not ranking**; LocalBusiness/Service materially affect local queries | T2/Tier-1 | Google structured-data docs | |

## J. AI-assisted writing guardrails (how this engine must operate)
| Claim | Tier | Source | Note |
|---|---|---|---|
| LLMs hallucinate plausible-but-false facts → **ground in a verified source (RAG), require citations, refuse to assert anything not in the knowledge base** | T4 | hallucination-survey lit (arXiv:2311.05232); RAG (Lewis 2020) | This is the engine's TRUTH_POLICY in one line |
| Readability formulas (Flesch) are weak predictors → guide, don't game | T4 ⚠️ | arXiv:2502.11150 | |
| Lead-gen blog measured by **qualified leads / CPL, not pageviews** | Tier-2 | lead-gen objective | 50k reads + 0 enquiries = failure |

---

### Standing caveats
- **Vendor/selection bias** dominates every conversion/email benchmark (Unbounce, Mailchimp, MailerLite, HubSpot report only their own paid/optimized customers). Cite as *attributed benchmarks*, never universal laws.
- **Correlation ≠ causation** for readability↔conversion and internal-links↔ranking.
- **Benchmarks drift annually** — re-pull before quoting.
- **Frameworks** (Cialdini, StoryBrand, AIDA/PAS) are solid as *structure*; their stronger commercial claims are practitioner assertions, not RCTs.
- Strongest, most durable items: **Google primary docs (E-E-A-T, CWV), Baymard, NN/G, the DOJ-testimony ranking mechanics, ASA/Kohavi statistics, and peer-reviewed GEO/RAG papers.**
