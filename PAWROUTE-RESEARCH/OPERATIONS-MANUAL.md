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

### Documentation (the "why")
| File | What it holds |
|---|---|
| `METHODOLOGY.md` | How we write, how we audit, what we're sure of, imagery rationale |
| `SOURCING-METHOD.md` | How the approach was derived; recurring patterns; what we're 100% sure of vs not |
| `OPERATIONS-MANUAL.md` | *(this)* the operating system, human elements, QA, master index |
| `skills/copywriting/KNOWLEDGE-BASE.md` | Validated, graded evidence book (10 pillars) |
| `skills/copywriting/15-PRINCIPLES.md` | Logic & voice doctrine |
| `skills/copywriting/HUMAN-WRITING-SYSTEM.md` | Elite-writer layers + masters |
| `skills/copywriting/REGULATORY-PRINCIPLES.md` | Compliance governance (official-only, no guessing) |
| `skills/copywriting/EEAT-AUTHORITY-CHECKLIST.md` | Off-page/trust gaps that drive results |
| `skills/copywriting/BLOG-PLAYBOOK.md`, `SKILL.md`, `EVIDENCE.md` | Blog moves, 26-skill map, tiered claim bank |

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
| `sites/pawroute/content/REGULATORY-REGISTER.md` / `.csv` | The auditable register (source/date/reviewer/re-verify) |
| `sites/pawroute/content/CLAIMS-AUDIT.md` | Per-content claim audit + action items |
| `sites/pawroute/content/REGISTRY.md` / `.csv` / `.json` | Every asset: status, grade, page type, funnel |
| `sites/pawroute/content/CONTENT-MAP.md` | Cluster plan: built vs planned |

### Content (the writing + briefs)
| Location | Holds |
|---|---|
| `sites/pawroute/pages/**/*.yml` | Built pages (route, hub, blog, tools, about) |
| `sites/pawroute/content/*.json` | Writing-asset deliverables (e.g. cost page, cost blog) |
| `sites/pawroute/content/blogs-to-dubai/*.json` | The inbound (→ Dubai) blogs, with sourcing blocks |
| `sites/pawroute/research/` | 598 keywords + page briefs |
| `images/pawroute/**` | Rendered images |

---

## 5. How to run it
```
py engine/build.py sites/pawroute [--serve]      # render content + images + sitemap/robots
py engine/render_images.py "<prompt>" --out ...  # render an image (low-res by default)
py audit/audit.py <page-or-dist> [--site]        # score content (5 lenses)
py audit/verify_claims.py audit/claims/<x>.json  # screenshot-verify official sources
py audit/regulatory_register.py                  # rebuild the auditable register
py audit/registry.py                             # rebuild the content memory
py audit/ai_citation.py --domain <live-domain>   # measure AI-citation (needs key + live site)
```

**Nothing here lives only in memory — it's all in the repo.** This manual is the map to it.
