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
├── .env                  # secrets (gitignored): BFL_API_KEY, etc.
├── engine/               # the engine itself (generic, business-agnostic)
│   ├── build.py          # renders content (sites/*) into a preview build (dist/*)
│   ├── render_images.py  # renders pictures with BFL FLUX -> images/*
│   ├── export_portable.py# exports a preview that opens offline (file://) + zips it
│   └── templates/        # content blocks (hero, key_facts, sources, faq, cta, …)
├── sites/                # one folder per business = its content
│   ├── pawroute/         #   site.yml (brand config) + pages/*.yml (the writing)
│   └── northside/        #   second test business (proves it's generic)
├── images/               # rendered pictures, one subfolder per business
├── skills/
│   └── image/SKILL.md    # the image-production guide (models, prompts, sizes, OG)
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
py engine/build.py sites/pawroute          # render content -> dist/pawroute/
py engine/build.py sites/pawroute --serve  # + preview at http://localhost:8000
```

The preview is for **reviewing the writing** — the real design is downstream.
To hand a preview to someone, export an offline copy:

```bash
py engine/export_portable.py dist/pawroute "C:/Users/Theo/Downloads/PawRoute-website"
```

### Render pictures (BFL FLUX)

```bash
py engine/render_images.py "warm photo of a happy dog beside an IATA pet crate at an airport gate, soft morning light, photorealistic, no text" \
   --out images/pawroute/uae-to-uk/hero.png --width 1440 --height 960

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

## Test sites

- **pawroute** — UAE pet relocation (export routes + Dubai-import fear pages).
- **northside** — a coffee roastery, proving the engine is not pet-specific.
