# The Engine

A business-agnostic static-site generator. It turns a single brand config plus
block-composed page files into a complete, SEO + GEO optimised website. Nothing
in `engine/` knows about pets, routes, or the UAE — that all lives in a site
folder under `sites/`. Swap the site folder, get a different business's site.

## Run it

```bash
py engine/build.py sites/numini_pet_relocation            # build primary site -> dist/numini-pet-relocation/
py engine/build.py sites/numini_pet_relocation --serve    # build + preview at http://localhost:8000
py engine/build.py sites/pawroute                         # build PawRoute brand -> dist/pawroute/
```

Requires Python 3 with `jinja2` and `pyyaml` (already installed on this machine).

## How a site is structured

```
sites/<business>/
  site.yml              # brand tokens, contact, nav, footer, analytics — ALL brand-specific config
  assets/               # optional static files (images, favicon) copied to /assets
  pages/
    home.yml            # -> /
    pricing.yml         # -> /pricing/
    destinations/
      index.yml         # -> /destinations/   (set `url:` explicitly for index pages)
      uae-to-uk.yml     # -> /destinations/uae-to-uk/
```

Each page is a list of **blocks**. A block has a `type` and its own fields:

```yaml
title: "Page title for <title> + SEO"
meta_description: "Under ~155 chars, with a hook."
schema: service            # optional: emits Service JSON-LD
blocks:
  - type: hero
    heading: "..."
  - type: pricing_tiers
    tiers: [ ... ]
  - type: faq
    items: [ {q: "...", a: "..."} ]   # any faq block auto-emits FAQPage JSON-LD
```

## Available block types

`hero`, `trust_bar`, `card_grid`, `steps`, `checklist`, `pricing_tiers`,
`table`, `prose`, `callout`, `faq`, `quote_form`, `cta`, `section_header`.

Each maps to a partial in `engine/templates/blocks/<type>.html.j2`. Add a new
block type by dropping in a new partial — the engine includes it by name.

## What the engine generates automatically

- Per-page SEO `<title>`, meta description, canonical, Open Graph tags.
- JSON-LD graph (Organization/LocalBusiness + Service + FAQPage) for GEO /
  answer-engine visibility — built from page data, safe-encoded for `<script>`.
- A CSS theme compiled from `site.yml` design tokens (`theme.css`).
- `sitemap.xml` and `robots.txt`.
- Mobile nav + a no-backend quote form that hands off to WhatsApp / email.

## Adding a new business

1. Copy `sites/numini_pet_relocation/` to `sites/<new>/`.
2. Edit `site.yml` (name, colours, contact, nav).
3. Replace the page YAML with the new business's content (compose blocks).
4. `py engine/build.py sites/<new>`.

No engine code changes required.
