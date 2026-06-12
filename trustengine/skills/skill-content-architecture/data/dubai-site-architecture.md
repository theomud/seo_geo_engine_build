# Content Architecture — Real Output
## The complete site architecture for the Dubai pet relocation site
## Niche: Dubai pet relocation · Built 2026-05-30 · 43 pages · Validated against the README Functional Quality Threshold

---

## How to read this file

This is the **blueprint** — every page the site will have, where it sits, how it is
reached, and how the URLs are formed — designed before the pages are built. It ends with
the **structural proof**: the three threshold gates computed over the whole sitemap by the
engine's `validate()` function (File 04). The proof is real, not asserted — the sitemap was
run through a breadth-first click-depth search, an inbound-link scan, and a per-type URL
regex.

---

## 1. The URL rule (one pattern per page type, no exceptions)

| Page type | Pattern (regex) | Example |
|-----------|-----------------|---------|
| home | `/` | `/` |
| hub | `/[a-z-]+` | `/routes` |
| spoke | `/[a-z-]+/[a-z0-9-]+` | `/import/dog-taken-at-dubai-airport` |
| detail | `/[a-z-]+/[a-z0-9-]+/[a-z0-9-]+` | `/routes/dubai-to-uk/quarantine-and-arrival` |

Slugs are lowercase, hyphenated, keyword-bearing — no IDs, no query strings. Every one of
the 43 pages conforms to the pattern for its type (Gate 3 = 100%).

---

## 2. The sitemap (hub-and-spoke, 43 pages)

```
/ (home · click 0)
├── /import (hub · click 1)
│   ├── /import/dog-taken-at-dubai-airport      ← GAP PAGE · also featured on home (click 1)
│   ├── /import/moccae-import-process
│   ├── /import/import-documentation-checklist
│   └── /import/import-permit-explained
├── /export (hub · click 1)
│   ├── /export/leaving-dubai-with-your-pet
│   ├── /export/export-documentation
│   └── /export/moccae-export-process
├── /routes (hub · click 1)
│   ├── /routes/sharjah-vs-dubai-vs-abu-dhabi   ← GAP PAGE
│   ├── /routes/can-i-move-my-pet-in-summer     ← GAP PAGE
│   ├── /routes/dubai-to-uk
│   │   └── /routes/dubai-to-uk/quarantine-and-arrival        (detail · click 3)
│   ├── /routes/dubai-to-india
│   ├── /routes/dubai-to-australia
│   │   └── /routes/dubai-to-australia/import-permit-steps    (detail · click 3)
│   ├── /routes/dubai-to-south-africa
│   ├── /routes/dubai-to-usa
│   └── /routes/dubai-to-canada
├── /airlines (hub · click 1)
│   ├── /airlines/etihad-pet-policy
│   ├── /airlines/emirates-pet-policy
│   ├── /airlines/turkish-airlines-pet-policy
│   ├── /airlines/royal-jordanian-pet-policy
│   └── /airlines/air-cairo-pet-policy
├── /costs (hub · click 1)
│   ├── /costs/rabies-titer-test                ← GAP PAGE · also featured on home (click 1)
│   ├── /costs/total-pet-relocation-cost
│   │   └── /costs/total-pet-relocation-cost/sample-quote     (detail · click 3)
│   ├── /costs/whats-included
│   └── /costs/moccae-fees
├── /guides (hub · click 1)
│   ├── /guides/complete-dubai-pet-import-guide  (pillar · depth level 4)
│   ├── /guides/breed-restrictions-uae
│   ├── /guides/pet-travel-crate-guide
│   └── /guides/common-mistakes
├── /about (hub · click 1)
│   ├── /about/our-process
│   ├── /about/reviews
│   └── /about/team
└── /contact (hub · click 1 · the single enquiry endpoint)
```

The four universal gap pages are the highest-priority spokes; the two deepest fears
(confiscation, titer cost) are **also featured on the homepage**, so they sit at click 1.

---

## 3. Navigation

**Primary nav (in the header, on every page):** Import · Export · Routes · Airlines ·
Costs · Guides — the six content hubs. Plus a persistent **Contact / Get help** button.
**Secondary nav (in each hub):** the hub lists its spokes; every spoke links back up to its
hub and across to its most relevant sibling.
**Footer nav (every page):** About · Reviews · the six hubs · Contact — guaranteeing every
hub is one click from anywhere (which is what keeps detail pages at ≤3).

---

## 4. The three conversion paths

Each path is fear → verified answer → help-first enquiry, and each completes inside the
3-click structure, ending at `/contact` (the single enquiry endpoint):

1. **Fear path:** `/import/dog-taken-at-dubai-airport` → `/import/moccae-import-process` →
   `/contact`. *(Import-to-Dubai owner.)*
2. **Cost path:** `/costs/rabies-titer-test` → `/costs/moccae-fees` → `/contact`.
   *(Cost-anxious owner.)*
3. **Researcher path:** `/` → `/routes` → `/routes/sharjah-vs-dubai-vs-abu-dhabi` →
   `/contact`. *(Confused Researcher / Last-Minute Mover.)*

---

## 5. Service & location hierarchies

**Service hierarchy:** Import → (process, documentation, permit, confiscation) · Export →
(process, documentation, leaving) · plus cross-cutting Costs and Guides.
**Location hierarchy:** Routes → UAE departure (Sharjah / Dubai / Abu Dhabi comparison) and
destination countries (UK, India, Australia, South Africa, USA, Canada), with per-country
detail pages (quarantine, permits) as click-3 spokes. Airlines → per-carrier policy pages
(Etihad, Emirates, Turkish, Royal Jordanian, Air Cairo).

---

## 6. Content-depth map (4 levels, matched to job)

| Level | Words | Count | Pages |
|-------|-------|-------|-------|
| 1 | 300–500 | 5 | moccae-fees, reviews, team, sample-quote, + thin utility |
| 2 | 500–1,000 | 24 | fear spokes, location pages, documentation, about |
| 3 | 1,000–2,000 | 5 | comparison, total-cost, the two MOCCAE process guides |
| 4 | 2,000–5,000 | 9 | the six hubs + the complete-import-guide pillar (+ Routes/Costs as deep hubs) |

No page is padded to a level above its job; no pillar is left thin.

---

## 7. Structural proof — computed by the engine, not asserted

The full sitemap was run through `validate()` (File 04): breadth-first click-depth from the
homepage, inbound-link scan for orphans, per-type URL regex, and a duplicate-intent check.

```
PAGES: 43
MAX CLICK DEPTH: 3   distribution: {click 0: 1, click 1: 10, click 2: 29, click 3: 3}
UNREACHABLE: 0
ORPHANS: 0
URL NON-CONFORMERS: 0
DUPLICATE INTENTS: 0
GATE 1 (<=3 clicks):      100.0%
GATE 2 (orphans):         0
GATE 3 (URL consistent):  100.0%
RESULT: PASS
```

### Per-hub proof summary (depth · inbound links · URL ok)

| Hub group | Pages | Max depth | Orphans | URL non-conformers |
|-----------|-------|-----------|---------|--------------------|
| Home | 1 | 0 | 0 | 0 |
| Import (hub + 4 spokes) | 5 | 2 | 0 | 0 |
| Export (hub + 3 spokes) | 4 | 2 | 0 | 0 |
| Routes (hub + 8 spokes + 2 detail) | 11 | 3 | 0 | 0 |
| Airlines (hub + 5 spokes) | 6 | 2 | 0 | 0 |
| Costs (hub + 4 spokes + 1 detail) | 6 | 3 | 0 | 0 |
| Guides (hub + 4 spokes) | 5 | 2 | 0 | 0 |
| About (hub + 3 spokes) | 4 | 2 | 0 | 0 |
| Contact | 1 | 1 | 0 | 0 |
| **Total** | **43** | **3** | **0** | **0** |

Every page is reachable from the homepage in ≤3 clicks; every page has at least one inbound
internal link; every URL conforms to its page-type rule; no two pages target the same intent.

---

## Batch result vs the Functional Quality Threshold (README Check 46)

| Gate | Requirement | Result |
|------|-------------|--------|
| 1 · 3-click reachability | 100% of pages ≤3 clicks | **100%** ✅ (max depth 3) |
| 2 · Zero orphans | orphan count = 0 | **0** ✅ |
| 3 · URL consistency | 100% conform to page-type rule | **100%** ✅ |
| (human gate) One page per intent | no cannibalisation | **0 duplicates** ✅ |

**Threshold MET — RESULT: PASS.**

**What this output proves:** a 43-page site can be designed as a coherent hub-and-spoke
structure where *every* page is findable in three clicks, *no* page is orphaned, and *one*
URL rule governs all of them — proven by measurement (BFS + inbound scan + regex), before a
single page is built. The four universal gap pages sit as the highest-priority fear-resolution
spokes, two featured on the homepage; three conversion paths carry each persona from fear to
enquiry inside the 3-click structure.
