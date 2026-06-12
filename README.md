# SEO + GEO Content Engine

An engine that produces two things for marketing pages:

1. **The writing** — accurate, evidence-based, SEO- and GEO-optimized content
   (titles, meta, headings, body copy, fear-led openings, sourced facts, FAQs, CTAs).
2. **The pictures** — AI-rendered images for those pages, via BFL **FLUX**.

It is **not** a website-design tool. No layout, CSS, or UI design is the
deliverable — the actual site is built/designed downstream. This engine writes
the content and renders the images, then hands off.

> Scope, stated by the owner: *"this is only for writing… and rendering pictures.
> this is what this engine is going to do."*

---

## Repo layout

```text
seo_geo_engine_build/
├── README.md
├── METHODOLOGY.md        # writing doctrine, audit approach, confidence levels
├── OPERATIONS-MANUAL.md  # operating system, human elements, QA, master index
├── .env                  # secrets (gitignored): BFL_API_KEY, etc.
├── engine/               # the engine itself (generic, business-agnostic)
│   ├── build.py          # renders content (sites/*) into a preview build (dist/*)
│   ├── render_images.py  # renders pictures with BFL FLUX -> images/*
│   ├── export_portable.py# exports a preview that opens offline (file://) + zips it
│   └── templates/        # content blocks (hero, key_facts, sources, faq, cta, …)
├── sites/                # one folder per business = its content
│   ├── numini_pet_relocation/ # PRIMARY: Numini Pet Relocation (numini.ai/pet-relocation)
│   │   ├── site.yml           #   brand config, nav, footer
│   │   ├── pages/**/*.yml     #   built pages (destinations, blog, tools, about, pricing…)
│   │   ├── content/           #   registry, regulatory register, claims audit, content map
│   │   ├── research/          #   598 Trust Engine keywords + page briefs
│   │   ├── prompts/           #   master, editor, QA, and research prompts
│   │   └── templates/         #   page schema, publishing package, QA checklist
│   ├── pawroute/         #   earlier PawRoute brand build (same content, different brand)
│   └── northside/        #   second test business (proves engine is not pet-specific)
├── trustengine/          # imported Trust Engine writing brain (9 Jun 2026)
│   ├── README.md         #   what's here and why it matters for writing
│   ├── skills/           #   17 Trust Engine skill folders (methodology, prompts, evidence)
│   ├── customer-profile/ #   7 personas + verified voice-of-customer language
│   └── research/         #   competitor intel · community VoC · market positioning verdict
├── images/               # rendered pictures, one subfolder per business
├── skills/               # SEO/GEO + marketing skill library (29 curated playbooks)
│   ├── SKILL-AUDIT.md    #   conformance audit results (30/30 + fix-pass 2)
│   ├── SKILLS-SCORECARD.md #  performance scores K×E×R×T for all 29 skills
│   ├── copy_and_image_sciences/ # ★ NUMINI WRITING BRAIN — primary source
│   │   ├── MASTER_FRAMEWORK.md  #   3,800+ lines: cognitive load, persuasion psychology,
│   │   │                        #   Cialdini, loss aversion, fear appeals, image science
│   │   ├── THE_WRITING_SYSTEM.md #  20 writing principles + 4 checklists (85 items)
│   │   ├── claim_bank.csv       #   37 Admiralty-graded accepted claims (AI writer feeds from this)
│   │   └── Web_Persuasion_Knowledge_Base.md # synthesised knowledge base
│   ├── seo-geo-skills/   #   6 geo/SEO execution skills
│   ├── marketingskills/  #   18 marketing skills (incl. image + image-optimize)
│   ├── claude-blog/      #   6 blog production skills
│   └── copywriting/      #   copywriting playbooks, HUMAN-WRITING-SYSTEM, claim bank, VoC
├── audit/                # 5-lens auditor, claim verifier, regulatory register, registry
├── docs/                 # explainer/diagram artifacts
└── dist/                 # generated preview output (not the final design)
```

A "site" is just data: `sites/<business>/site.yml` (brand, contact, nav) plus
`pages/*.yml`, where each page is an ordered list of **content blocks**. Swap the
folder → a different business, no code changes.

---

## Quickstart

Requires Python 3 with `jinja2` + `pyyaml` (already installed). Use `py`, not `python`.

### Write content (and preview it)

```bash
py engine/build.py sites/numini_pet_relocation          # render content -> dist/numini-pet-relocation/
py engine/build.py sites/numini_pet_relocation --serve  # + preview at http://localhost:8000
```

The preview is for **reviewing the writing** — the real design is downstream.
To hand a preview to someone, export an offline copy:

```bash
py engine/export_portable.py dist/numini-pet-relocation "C:/Users/Theo/Downloads/Numini-website"
```

### Render pictures (BFL FLUX)

```bash
py engine/render_images.py "warm photo of a happy dog beside an IATA pet crate at an airport gate, soft morning light, photorealistic, no text" \
   --out images/numini/uae-to-uk/hero.png --width 1440 --height 960

py engine/render_images.py --batch jobs.json   # [{prompt,out,width,height}, …]
```

- Model: `flux-2-pro`. Key: `BFL_API_KEY` in `.env`.
- **Each render is a real, paid call** — render only what's needed.
- See `skills/image/SKILL.md` for model choice, prompting, dimensions, optimization.

---

## Core rules for the writing

- Never invent facts or sources; cite the official source, hedge the unknown.
- Lead with the customer's real fear, then resolve it with verified information.
- No keyword stuffing; write for meaning and the human behind the search.
- Every claim is either **verified** (with a source) or clearly **hedged**.
- Never guarantee delivery dates; never give medical/veterinary advice.

## Sites

- **numini_pet_relocation** — Numini Pet Relocation (primary, `numini.ai/pet-relocation`). UAE pet relocation: export routes, Dubai-import fear pages, 598 Trust Engine keywords, regulatory register. Run: `py engine/build.py sites/numini_pet_relocation`
- **pawroute** — earlier PawRoute brand build (same content structure as numini_pet_relocation).
- **northside** — a coffee roastery, proving the engine is not pet-specific.
