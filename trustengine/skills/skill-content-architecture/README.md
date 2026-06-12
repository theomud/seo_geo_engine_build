# CONTENT ARCHITECTURE
## The whole site's structure, decided before page 11 goes live — so pages don't cannibalise each other

---

## What This Skill Is

Most content operations build pages one at a time and discover too late that three of
them target the same query, the highest-converting page is four clicks from the
homepage, and half the URLs follow different rules. Content Architecture is the skill
that designs the **entire site structure first** — the sitemap, the URL pattern, the
navigation, and the conversion paths — so every page added later has a place, a parent,
and a job.

It is the blueprint, not the building. Without it, a 40-page site is 40 pages fighting
each other for the same rankings and leaking the trust the other skills worked to
build. With it, every page is findable in three clicks, no page is an orphan, and one
URL rule governs all of them.

**Skill Value Score: 17/25**
- Difficulty: 4/5
- Automation Potential: 2/5
- Market Uniqueness: 3/5
- Commercial Value: 5/5
- Teachability: 3/5

**Status:** 🔨 Building (Dubai pet relocation, 2026-05-30)
**Niche-agnostic:** Yes — every multi-page service site needs a sitemap, URL rule, navigation, and conversion paths

---

## The Eight Components

1. **Sitemap design** — every page planned (40+), grouped into hubs and spokes.
2. **URL structure** — one consistent rule per page type, no exceptions.
3. **Navigation logic** — primary + secondary nav that reaches every important page.
4. **Conversion paths** — the routes from fear → answer → enquiry (3 mapped).
5. **Service hierarchy** — import, export, routes, airlines, organised.
6. **Location hierarchy** — UAE airports and destination countries, organised.
7. **Content depth planning** — each page assigned one of 4 depth levels.
8. **Architecture document template** — the reusable deliverable a builder executes.

---

## What It Produces

| Output | What it is |
|--------|-----------|
| The site architecture document | The complete blueprint — sitemap, URL rule, nav, conversion paths, hierarchies, depth — for the proof niche |
| The 3-click / no-orphan / URL-consistency proof | The audit table showing every page reachable in ≤3 clicks, zero orphans, 100% URL consistency |
| The architecture template | The reusable structure any new niche fills in |

---

## Functional Quality Threshold (Check 46)

This skill's real output is **proven** only when all three hold for the built
architecture (40+ pages):

1. **3-click reachability:** every page is reachable from the homepage in **≤3 clicks**
   (verified by a click-depth table — F-33). No page deeper than 3.
2. **Zero orphan pages:** every page has **at least one internal link pointing to it**
   (P-37). Zero orphans.
3. **URL consistency:** the URL structure is **100% consistent** — one documented rule
   per page type, every page conforming, no exceptions.

Output that misses any of the three is not done. The architecture and its proof table
live in `data/dubai-site-architecture.md`.

---

## Inputs and Outputs

| Input | Source | Required |
|-------|--------|----------|
| The page inventory (gap pages + service/location pages) | the content-gap analysis + existing page drafts | Yes |
| The 4 universal gap pages already drafted | the existing page drafts | Yes |
| Verified routes/airlines/countries | the verified-source store (by source ID) | Yes |
| Target keywords + intents (one page per intent) | the keyword/intent map | Yes |

| Output | Format | Contains |
|--------|--------|----------|
| Site architecture document | Markdown | sitemap, URL rule, nav, 3 conversion paths, hierarchies, depth map |
| Click-depth + orphan + URL-consistency proof | table | the Check-46 evidence |
| Architecture template | Markdown | the reusable blueprint for a new niche |

---

## Proof

**Status:** 🔨 Building — Dubai pet relocation
**Real output (target):** a complete 40+ page architecture document for the Dubai pet
relocation site — full sitemap, URL structure, primary/secondary navigation, 3
conversion paths, service + location hierarchies, content-depth assignments — with the
3-click / zero-orphan / URL-consistency proof table.
**Anchor:** the four universal gap pages (confiscation, summer, titer cost, airport
comparison) are placed in the sitemap as the highest-priority fear-resolution spokes.
**Skill Value Score (confirmed on completion):** 17/25.

---

## Environment Variables

```
PROJECT_ROOT=          # absolute path to the project root on this machine
```

Manual-first skill (Automation 2/5) — the architecture is a design judgement; no API
keys are required to produce it. Automation later only validates click-depth and
orphan checks against the documented sitemap.

---

## Standalone Test

Someone in a different multi-page service market can use this skill alone: take their
own page inventory, apply the URL rule, build the sitemap into hubs and spokes, map
their conversion paths, and run the 3-click / orphan / consistency checks. The method
is portable; only the pages and hierarchies are niche-specific.
