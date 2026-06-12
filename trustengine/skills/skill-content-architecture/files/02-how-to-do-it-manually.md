---
Status: draft — built 2026-05-30
Area: skill-content-architecture
Depends on: skill-content-architecture/files/01-what-is-this-skill.md, skill-content-architecture/README.md
Feeds into: skill-content-architecture/files/03-how-to-verify-it.md, skill-content-architecture/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Designing the sitemap, URL rule, navigation, and conversion paths — then proving the structure

---

## Why manual first

Architecture is a design judgement made once and lived with for years. Automation can
*check* a finished sitemap (click depth, orphans, URL consistency), but the decisions —
which pages exist, what the hubs are, how the URL rule reads — are human. Design the
whole structure by hand, then let the checks (File 04) keep it honest as the site grows.

Two inputs on the desk before you start:
1. **The page inventory** — every page the site will have, each tied to **one intent**
   (one page per query — no two pages chasing the same search).
2. **The verified entities** — the real routes, airlines, countries, costs (from the
   Source Bank) that the service and location hierarchies organise.

---

## Step 1 — Inventory the pages, one per intent

List every page. Beside each, write its single target intent/query. If two pages share
an intent, **merge them** — that is cannibalisation caught before it's built. *(Library:
P-23 One Page per Intent.)* This list is the raw material for the sitemap.

---

## Step 2 — Write the URL rule (one pattern per page type)

Decide the URL structure **before** placing pages, so every page conforms from the
start. One rule per page type, no exceptions:

| Page type | URL pattern | Example |
|-----------|-------------|---------|
| Topic hub | `/<hub>` | `/routes` |
| Fear-resolution spoke | `/<hub>/<slug>` | `/import/dog-taken-at-dubai-airport` |
| Location page | `/routes/<from>-to-<to>` | `/routes/dubai-to-uk` |
| Cost page | `/costs/<slug>` | `/costs/rabies-titer-test` |

Slugs are lowercase, hyphenated, keyword-bearing, no IDs or query strings. *(Library:
P-36 Anchor-Text Diversity — clean slugs feed clean anchors.)*

---

## Step 3 — Group into hubs and spokes

Cluster the pages into a few **topic hubs** (pillars), each with its **spokes**.
*(Library: M-35 Hub-and-Spoke / Silo.)* Every spoke links up to its hub and the hub
links down to its spokes. For the proof niche: Import · Export · Routes · Airlines ·
Costs are the hubs; the fear pages, country pages, and cost pages are their spokes.

---

## Step 4 — Assign click depth (≤3 for every page)

Map each page's shortest path from the homepage and write the click number. *(Library:
F-33 3-Click-Depth Rule.)* Home = 0, hubs = 1, primary spokes = 2, detail spokes = 3.
**Any page at click 4+ is restructured** — promote it, or link it from a hub — until
nothing is deeper than 3.

---

## Step 5 — Check for orphans

For every page, confirm **at least one other page links to it**. *(Library: P-37
Eliminate Orphan Pages.)* A page with zero inbound links is an orphan — wire it into its
hub (and any sibling spokes) before the architecture is done. Zero orphans is the rule.

---

## Step 6 — Map the three conversion paths

Draw the routes a reader takes from arrival to enquiry — each one **fear → verified
answer → help-first CTA**. *(Library: M-32 Hierarchy of Effects — awareness →
consideration → conversion.)* For the proof niche: (1) fear page → process guide →
enquiry; (2) cost page → comparison → enquiry; (3) homepage → hub → fear page → enquiry.
Every conversion path must reach an enquiry within the 3-click structure.

---

## Step 7 — Assign content depth (4 levels)

Match each page to one of four depth levels so effort fits the job. *(Library: M-11
Content Depth Model.)*

| Level | Words | Page type |
|-------|-------|-----------|
| 1 | 300–500 | thin utility (a single cost, a short FAQ answer) |
| 2 | 500–1,000 | fear-resolution spoke, location page |
| 3 | 1,000–2,000 | comparison, process guide |
| 4 | 2,000–5,000 | topic-hub pillar, definitive guide |

A cost page padded to 3,000 words and a pillar left at 400 are both depth-mismatches —
fix at this step.

---

## Step 8 — Write the architecture document + the proof table

Assemble the deliverable: the sitemap (hubs + spokes), the URL rule, the navigation, the
three conversion paths, the service + location hierarchies, the depth map — and the
**proof table** showing every page's click depth, its inbound link (no orphan), and its
URL conforming to the rule. The document is what a builder executes without asking
questions.

---

## Worked example — placing the airport-comparison page

**Intent:** "sharjah vs dubai vs abu dhabi pet airport" (one page, no duplicate).
**Hub:** Routes. **URL:** `/routes/sharjah-vs-dubai-vs-abu-dhabi` (conforms to the
spoke rule). **Click depth:** Home → Routes (1) → the page (2) = **2 ✔**. **Inbound
links:** from the Routes hub and from the summer-embargo page (sibling) = **not an
orphan ✔**. **Conversion path:** comparison → enquiry. **Depth:** Level 3 (comparison,
1,000–2,000w). Every structural gate passes before a word is written.

---

## What you must not do

- **Do not build two pages for one intent.** Merge them — cannibalisation is the
  failure this skill exists to prevent.
- **Do not leave a page at click 4+.** Restructure until everything is ≤3.
- **Do not ship an orphan.** Every page needs at least one inbound internal link.
- **Do not break the URL rule "just once".** One exception becomes ten; the rule is 100%
  or it isn't a rule.
- **Do not pad to a depth level.** Depth matches the page's job, not a word quota.

---

## Output of this manual phase

The architecture document exists with the sitemap, URL rule, navigation, three
conversion paths, service + location hierarchies, and depth map; the proof table shows
every page ≤3 clicks, zero orphans, 100% URL consistency. That document is the real
output (`data/dubai-site-architecture.md`) and the input to File 04 — automation
validates click depth and orphans against the documented sitemap; the design stays human.
