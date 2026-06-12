# PawRoute Content Engine — Operations Manual

*The master record. How the system runs, where the humans are essential, how we assure quality,
and an index of everything that's stored — so nothing lives only in someone's head.*

---

## 1. The operating system at a glance

```
Official sources + validated research (the truth)
        ↓
HUMAN brief: question · fear · angle · funnel stage           ← human judgment
        ↓
AI Writer (RAG-grounded) drafts → humanizes → self-checks 7-category QA
        ↓
Engine renders content + BFL images (writing + pictures only)
        ↓
audit/ scores it (5 lenses) · verify_claims screenshots every fact
        ↓
HUMAN review: fact-check · expert sign-off · approve            ← the gate
        ↓
Published → measured (GSC + AI-citation harness) → iterate
```

The machine accelerates; **the human decides.** AI never goes straight to the customer.

---

## 2. The HUMAN elements (where people are essential, and why)

AI is the production engine. It cannot feel a customer's fear, verify that a regulation is current,
judge whether a cost is realistic, carry legal/ethical responsibility, or be a *named, accountable
expert*. Those are human jobs. The non-negotiable human roles:

| Stage | Human role | Why it can't be AI |
|---|---|---|
| **Strategy / brief** | Choose the customer question, the real fear, the angle, the funnel stage | Empathy + market judgment; AI matches keywords, humans understand people |
| **Voice-of-Customer** | Decide which real customer words matter | Lived understanding of the worry behind the words |
| **Fact-checking** | Verify every claim against the official source; sign off | AI can't know if a rule is current or a source is official |
| **Expert review** | A named, credentialed specialist reviews regulated content | E-E-A-T + legal responsibility require a real, accountable person |
| **Named authorship** | A real person stands behind the content (byline + bio) | Trust is earned by identifiable expertise, not anonymous text |
| **Escalation** | Edge cases (wolf-hybrid, service animal, multi-country transit, rescue, commercial) go to a human | High-stakes ambiguity must be escalated, never guessed |
| **The publish gate** | A human approves before anything goes live | "AI → customer" is forbidden; workflow ends *Approved → Published* |
| **The relationship** | The actual customer conversation + WhatsApp/bot handoff + partnerships | People trust people, especially with their animals |
| **The judgment calls** | When to hedge, when to refuse a shortcut, when to say "I don't know" | Integrity is a human decision (Compliance > convenience) |

**Rule (Regulatory Principle 15):** *Official source → verification → human review → customer.*
Never AI → customer. The register marks AI-verified claims **"(pending human sign-off)"** until a
person signs them off — that field is the human gate made visible.

**Where the human is still TODO for PawRoute (flagged honestly):** a real named author + credentials,
a real expert reviewer, real reviews/testimonials, the physical address/licence. Placeholders are
clearly marked in `site.yml` (`author.person`) and the About page — a person must fill them; we never
fabricate a human or a credential.

---

## 3. Quality assurance & governance

**Content workflow states** (tracked in the registry):
`Idea → Validated Question → Researching → Brief Ready → Drafting → Editing → SEO/GEO Review →
QA Review → Approved → Published → Refreshing → Archived`. Nothing reaches *Published* without the
human *Approved* step.

**The QA gates, in order:**
1. **Truth gate** — every fact maps to an official source; un-verifiable facts are hedged/flagged.
2. **Auditor** (`audit/audit.py`) — 5-lens / 7-category score, page-type-aware, with risk caps + brief-alignment.
3. **Claim verification** (`audit/verify_claims.py`) — full-page screenshot of each official source; official domains only.
4. **Regulatory register** — source · URL · date verified · version · reviewer · **re-verify-by** (regs change).
5. **Human sign-off** — expert review + publish approval.
6. **Measurement** (post-launch) — GSC + AI-citation harness + Core Web Vitals; then re-calibrate.

**Honesty discipline (stored in every artifact):** scores are advisory proxies, not outcomes;
"100% sure" = a fact screenshot-verified against its official source *as of a date* + that the method
was applied — nothing else. See `SOURCING-METHOD.md`.

---

## 4. Complete index — everything that's stored

### Copy & Image Sciences — the Numini writing brain (primary source)
> These files came from the Numini Research Elevator. They are the scientific foundation
> for every writing rule, image decision, and trust signal in the engine.

| File | What it holds |
|---|---|
| `skills/copy_and_image_sciences/MASTER_FRAMEWORK.md` | **3,800+ line master framework** — 8 sections: Science of Writing (cognitive load, dual coding, fluency→trust, working memory), Copywriting Strategy (AIDA/PAS, buyer types, JTBD, value prop), Psychology of Persuasion (Cialdini, loss aversion, risk perception, fear appeals), Blog Writing 2026, Sector Writing Styles, Regulatory Content, Image Strategy (Kindchenschema, gaze direction, dual coding) |
| `skills/copy_and_image_sciences/THE_WRITING_SYSTEM.md` | 20 writing principles across 6 domains + 4 checklists (85 items) — the enforceable rules derived from the master framework; load into any AI writer session |
| `skills/copy_and_image_sciences/PET-RELOCATION-WRITING-TRUST-SYSTEM.md` | Same principles formatted for direct AI skills/prompt use |
| `skills/copy_and_image_sciences/claim_bank.csv` | 37 accepted claims (A1: 11, B2: 11, C1: 15) — Admiralty-graded, sourced; AI writer refuses unbanked facts |
| `skills/copy_and_image_sciences/claim_bank_quarantine.csv` | 7 killed claims (D1) — do not use; shows what was rejected and why |
| `skills/copy_and_image_sciences/Web_Persuasion_Knowledge_Base.md` | Synthesised knowledge base built from the claim bank; structured by chapter (reading psychology, persuasion, trust, CRO, SEO/GEO, blog, lead-gen) |
| `skills/copy_and_image_sciences/Validation_Report.md` | Gate 3 validation results — T1/T2/T3 tier breakdown, pillar coverage, 2 pillars needing seeding |

### Documentation (the "why")
| File | What it holds |
|---|---|
| `METHODOLOGY.md` | How we write, how we audit, what we're sure of, imagery rationale |
| `SOURCING-METHOD.md` | How the approach was derived; recurring patterns; what we're 100% sure of vs not |
| `OPERATIONS-MANUAL.md` | *(this)* the operating system, human elements, QA, master index |
| `skills/copywriting/KNOWLEDGE-BASE.md` | Validated, graded evidence book (10 pillars) |
| `skills/copywriting/15-PRINCIPLES.md` | Logic & voice doctrine |
| `skills/copywriting/HUMAN-WRITING-SYSTEM.md` | Elite-writer layers + 7 masters (Schwartz, Ogilvy, Handley, Wiebe, Godin, Dean, Shleyner) |
| `skills/copywriting/REGULATORY-PRINCIPLES.md` | Compliance governance (official-only, no guessing) |
| `skills/copywriting/EEAT-AUTHORITY-CHECKLIST.md` | Off-page/trust gaps that drive results |
| `skills/copywriting/BLOG-PLAYBOOK.md`, `SKILL.md`, `EVIDENCE.md` | Blog moves, 26-skill map, tiered claim bank |
| `skills/copywriting/MASTER-MODEL-COPYWRITING.md` | Theo's synthesis — "the brain buys, writing is the delivery mechanism"; 10-question brain test; 4 buyer personality types |
| `skills/copywriting/RESEARCH-METHODOLOGY.md` | Evidence methodology — source tier rules (T1–VENDOR), Admiralty coding, what we accept/reject |

### Research artifacts (from Numini deep-research runs)
| File | What it holds |
|---|---|
| `skills/copywriting/DEEP-RESEARCH-2026-06-11.md` | 108-agent deep research run — 122 claims extracted, 25 adversarially verified (11 confirmed 3-0, 7 killed, 7 pending); writing science, GEO, images, customer psychology |
| `skills/copywriting/FRAMEWORKS-VERIFIED-2026-06-12.md` | 28 copywriting frameworks adversarially verified (3-vote) — Fogg BM, Curiosity Gap, ELM, loss aversion, etc. — with confidence grades and boundary conditions |
| `skills/copywriting/BLOG-CHEATSHEET.md` | Quick-reference blog best practices (operational; use at publish) |

### The writer + QC
| File | Role |
|---|---|
| `skills/copywriting/AI_Writer_System_Prompt.md` | The RAG-bound, funnel-aware writer (how we draft) |
| `skills/copywriting/claim_bank.csv` (+ quarantine) | Validated evidence the writer grounds on |
| `skills/copywriting/voc-bank.md` | Real customer language (mined) |
| `skills/copywriting/{SEO_EEAT,GEO,Editing_Standards,AB_Test_Protocol,Lead_Gen_Playbook}` | Checklists |

### Engine code (the "how it's produced")
| File | Does |
|---|---|
| `engine/build.py` | Block renderer → HTML, JSON-LD (LocalBusiness/FAQ/Breadcrumb/Author), sitemap.xml, robots.txt |
| `engine/render_images.py` | BFL FLUX image rendering |
| `engine/templates/` | base + 30+ block partials (incl. article, story, compliance, tools, lead_form) + theme |
| `audit/audit.py` + `report.py` | The 5-lens auditor + HTML report |
| `audit/verify_claims.py` | Screenshot claim verifier (official sources only) |
| `audit/registry.py` | Content-Intelligence registry (the "memory") |
| `audit/regulatory_register.py` | Auditable regulatory claim register |
| `audit/ai_citation.py` | Live AI-citation test harness (Perplexity/Gemini/SerpApi) |
| `audit/gen_route_briefs.py` | Generates route content briefs |

### QA / evidence artifacts (the proof)
| Location | Holds |
|---|---|
| `audit/evidence/<set>/*.png` + `CLAIMS-LEDGER.md` | Official-source screenshots per claim |
| `sites/numini_pet_relocation/content/REGULATORY-REGISTER.md` / `.csv` | The auditable register (source/date/reviewer/re-verify) |
| `sites/numini_pet_relocation/content/CLAIMS-AUDIT.md` | Per-content claim audit + action items |
| `sites/numini_pet_relocation/content/REGISTRY.md` / `.csv` / `.json` | Every asset: status, grade, page type, funnel |
| `sites/numini_pet_relocation/content/CONTENT-MAP.md` | Cluster plan: built vs planned |
| `trustengine/skills/skill-official-source-research/data/` | Source bank xlsx (153 claims) + 143 PNG screenshot proofs |
| `trustengine/research/competitors/` | 21 confirmed competitors, trust scores, content-gap matrix |
| `trustengine/research/community/` | 69 community screenshots (Reddit + Facebook) + VoC quotes |

### Content (the writing + briefs)
| Location | Holds |
|---|---|
| `sites/numini_pet_relocation/pages/**/*.yml` | Built pages (route, hub, blog, tools, about, pricing) |
| `sites/numini_pet_relocation/research/trustengine-keywords.csv` | 598 Trust Engine keywords (UAE; fear/intent classified) |
| `sites/numini_pet_relocation/research/trustengine-page-briefs.csv` | 598 ready page briefs (keyword → fear → page type → CTA) |
| `sites/numini_pet_relocation/prompts/` | Master, editor, QA, and research prompts |
| `images/numini/**` | Rendered images for the numini site |
| `sites/pawroute/` | Earlier PawRoute brand build (same structure; kept for reference) |

### Trust Engine (the imported writing brain)
| Location | Holds |
|---|---|
| `trustengine/README.md` | What's here, what's excluded, relationship to the engine |
| `trustengine/skills/skill-customer-fear-intelligence/` | 12-fear DB + intent taxonomy + fear-classification prompt |
| `trustengine/skills/skill-content-structure/` | 5-layer page model + worked examples |
| `trustengine/skills/skill-trust-gap-analysis/` | Competitor master HTML + competitor evidence screenshots |
| `trustengine/customer-profile/` | 7 personas + verified voice-of-customer language |
| `trustengine/research/00-verdict.md` | Market-positioning verdict (uniqueness of the 5-method system) |
| `trustengine/research/market-positioning/` | Full 2026 SEO market positioning research |
| `trustengine/research/google-trends/` | Google Trends data for Dubai pet relocation keywords |

---

## 5. How to run it
```
py engine/build.py sites/numini_pet_relocation [--serve]  # render Numini site (primary)
py engine/build.py sites/pawroute [--serve]               # render PawRoute brand build
py engine/render_images.py "<prompt>" --out ...           # render an image (low-res by default)
py audit/audit.py <page-or-dist> [--site]                 # score content (5 lenses)
py audit/verify_claims.py audit/claims/<x>.json           # screenshot-verify official sources
py audit/regulatory_register.py                           # rebuild the auditable register
py audit/registry.py                                      # rebuild the content memory
py audit/ai_citation.py --domain <live-domain>            # measure AI-citation (needs key + live site)
```

**Nothing here lives only in memory — it's all in the repo.** This manual is the map to it.
