---
Status: draft — built 2026-05-30
Area: skill-content-architecture
Depends on: skill-content-architecture/README.md
Feeds into: skill-content-architecture/files/02-how-to-do-it-manually.md, skill-content-architecture/files/04-automation-spec.md
---

# Skill · File 01 — What This Skill Is
## Niche-agnostic definition of Content Architecture

---

## The problem this skill solves

A site is built one page at a time, and the structural decisions are made by accident.
By page thirty you discover three pages competing for the same query, the
highest-converting page buried four clicks deep where no one finds it, a dozen pages
no internal link points to, and URLs that follow four different patterns because four
different people guessed. Each page might be individually excellent — and the site
still underperforms, because nothing decided how the pages relate.

Content Architecture is the skill that makes those structural decisions **on purpose,
before they calcify**: the sitemap, the URL rule, the navigation, and the conversion
paths, designed as one blueprint so every page added afterwards has a place, a parent,
a link, and a job. It is the difference between forty pages and a forty-page *site*.

---

## What this skill produces

| Output | What it is |
|--------|-----------|
| The site architecture document | The complete blueprint — sitemap, URL rule, nav, conversion paths, hierarchies, depth map |
| The structural proof table | Every page reachable in ≤3 clicks, zero orphans, 100% URL consistency |
| The architecture template | The reusable blueprint a new niche fills in |

The rule that makes it scorable: **every page ≤3 clicks from home, zero orphans, one
URL rule with no exceptions.**

---

## The core idea — hubs and spokes, three clicks deep

A coherent site is a **hub-and-spoke** structure: a few topic hubs (pillars), each
linking down to its spoke pages, each spoke linking back up. *(Library: M-35
Hub-and-Spoke / Silo Architecture; M-34 PageRank Flow — link equity flows down to
spokes and back to hubs.)* Two non-negotiable structural rules govern it:

- **The 3-click rule** — every important page is reachable from the homepage in **three
  clicks or fewer**. *(Library: F-33 3-Click-Depth Rule.)* A page at click 5 is a page
  no one finds.
- **No orphans** — every page has **at least one internal link pointing to it**.
  *(Library: P-37 Eliminate Orphan Pages.)* An orphan is invisible to readers and
  crawlers alike.

On top of the structure sit the **URL rule** (one consistent pattern per page type) and
**content-depth planning** (each page assigned one of four depth levels — M-11 — so a
cost page isn't padded to 3,000 words and a definitive guide isn't 400).

---

## A worked example (the proof niche)

The Dubai pet relocation site, as a hub-and-spoke architecture:

| Layer | Pages | Click depth |
|-------|-------|-------------|
| Home (hub 0) | the homepage | 0 |
| Topic hubs | Import · Export · Routes · Airlines · Costs | 1 |
| Fear-resolution spokes | the 4 universal gap pages (confiscation, summer, titer, airport) | 2 |
| Detail spokes | per-country routes, per-airline rules, per-cost breakdowns | 2–3 |

The four gap pages — already drafted as templates — are placed as the
highest-priority **fear-resolution spokes at click 2**, each linked from its hub
(confiscation under Import, airport comparison under Routes) and back. URL rule:
`/<hub>/<spoke-slug>` (e.g. `/routes/sharjah-vs-dubai-vs-abu-dhabi`), every page
conforming. Three conversion paths run fear → verified answer → help-first enquiry.

A site built without this has the confiscation page floating with no hub, a `/page?id=7`
URL, and no link pointing to it — individually good, structurally invisible.

---

## How it differs from neighbouring skills

| Skill | Owns |
|-------|------|
| Content Structure | the **inside of one page** — the 5 layers, the page type |
| Internal Linking | the **links between pages** once they exist |
| **Content Architecture** | the **whole map** — which pages exist, where they sit, how they're reached |

Content Structure designs a page; Internal Linking wires built pages together; Content
Architecture decides **what pages exist and how the site is shaped** in the first place
— the blueprint both of the others operate inside.

---

## Why this is a standalone skill

1. **Structure is decided once and lived with for years.** Retrofitting a sitemap onto
   forty live pages is far more expensive than designing it before page eleven.
2. **It is what stops cannibalisation.** One page per intent, each in its place, is the
   structural defence against pages competing with each other.
3. **It is portable and checkable.** Every multi-page service site needs a sitemap, a
   URL rule, navigation, and conversion paths — and the 3-click / orphan / consistency
   tests are objective, not taste.

---

## In scope / out of scope

**In scope.** Designing the sitemap (hubs + spokes), the URL rule, the navigation, the
three conversion paths, the service + location hierarchies, and the content-depth
assignment; producing the architecture document and the structural proof table.

**Out of scope.** Writing the pages' words (conversion copy), designing the inside of a
page (content structure), the visual proof on a page (visual evidence), and the
detailed internal-link anchor text (internal linking — this skill sets the *shape*; that
skill optimises the links). This skill draws the map; it does not write the territory.

---

## What "good" looks like

- **Every page is ≤3 clicks from the homepage** — proven by a click-depth table.
- **Zero orphan pages** — every page has at least one inbound internal link.
- **The URL structure is 100% consistent** — one documented rule per page type, every
  page conforming, no exceptions.
- **One page per intent** — no two pages target the same query (no cannibalisation).
- Every page is assigned a **content-depth level** matched to its job.

This skill is complete when the 40+ page architecture document exists for the proof
niche, the click-depth / orphan / URL-consistency proof table passes all three gates,
the reusable template exists, and the audit passes.
