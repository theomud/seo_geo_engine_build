# 06 — Models, Frameworks & Principles
## Skill — Content Architecture
## House standard: 3 sections (MODELS / FRAMEWORKS / PRINCIPLES), each ≥3 entries. Codes reference **MFP-LIBRARY.md**.
## Built 2026-05-30 against the canonical MFP library. `⟳` = updated citation.

---

## MODELS — the data structures and mental models this skill uses

- **M-35 — Hub-and-Spoke / Silo Architecture.** The shape of the whole site: a few topic
  **hubs** (pillars), each linking down to its **spokes** and each spoke linking back up.
  For the proof niche the hubs are Import · Export · Routes · Airlines · Costs; the fear,
  country, and cost pages are their spokes. This is the model that prevents a flat pile of
  unrelated pages. *Source:* Bruce Clay / Search Engine Land siloing canon.
- **M-34 — PageRank Flow / Link-Equity Distribution.** Link equity flows **down** from
  hubs to spokes and **back up** from spokes to hubs — so a page's place in the graph
  determines the authority it can accumulate. An orphan (no inbound edge) receives none;
  a page four clicks deep receives little. This is why click depth and orphans are
  structural, not cosmetic. *Source:* Google PageRank patent (Brin & Page); Hobo-Web 2024.
- **M-11 — Content Depth Model.** Each page is assigned one of **four depth levels**
  (300–500 · 500–1,000 · 1,000–2,000 · 2,000–5,000 words) matched to its job, so a cost
  page isn't padded to 3,000 words and a pillar isn't left at 400. *Source:* the
  "comprehensive content" pillar (Nielsen 1999).

*Also used:* **M-08** Nine-Page-Type Model (each page is one of the nine types, which sets
its depth and place) · **M-32** Hierarchy of Effects (awareness → consideration →
conversion — the spine of the three conversion paths).

## FRAMEWORKS — the decision systems and processes

- **F-16 — Content Architecture Hierarchy.** The core method of this skill: design the
  sitemap, URL rule, navigation, and conversion paths as **one blueprint** before pages
  are built, top-down from home → hubs → spokes. *Source:* internal.
- **F-33 — 3-Click-Depth Rule for Important Pages.** Every important page must be reachable
  from the homepage in **≤3 clicks**; computed as a breadth-first search over the internal
  link graph. The first of the three threshold gates. *Source:* Incremys / Linkbot
  internal-linking guides.
- **F-24 — GSC Conversion-Query Cluster Method.** Groups pages into clusters by the
  conversion query they serve — the basis for assigning spokes to the right hub and for
  drawing conversion paths from fear-query to enquiry. *Source:* Search Engine Land,
  "Complete Guide to Topic Clusters."

*Also used:* **F-31** Who/How/Why (the verification re-derive — does this structure hold
when an independent checker re-traces it).

## PRINCIPLES — the non-negotiable rules

- **P-37 — Eliminate Orphan Pages.** Every page has **at least one inbound internal link**;
  an orphan is invisible to readers and crawlers alike. The second threshold gate — orphan
  count must be exactly **0**. *Source:* Screaming Frog audit practice.
- **P-23 — One Page per Intent.** No two pages target the same query — the structural
  defence against cannibalisation. This is the human gate (A4) a click-count can't catch:
  two pages quietly chasing one search are **merged**. *Source:* Conductor / Semrush.
- **P-36 — Anchor-Text Diversity.** Clean, keyword-bearing, hyphenated slugs (no IDs or
  query strings) feed clean, varied anchors and underpin the **100% URL-consistency** gate
  — one documented pattern per page type, no exceptions. *Source:* Backlinko; Penguin
  post-mortems.

*Also used:* **P-07** Independent Verification (the blind re-derive of the three gates
from the sitemap itself).

---
*Skill-map note (MFP-LIBRARY.md):* Content Architecture is a new skill (nearest library
row is Internal Linking: M-34, M-35 · F-33 · P-36, P-37). Built to the ≥3-per-section
house standard with the START-prompt codes plus genuinely-used M-11, M-08, M-32, F-16,
F-24, P-23. The eight components (sitemap · URL rule · navigation · conversion paths ·
service hierarchy · location hierarchy · content depth · architecture template) are this
skill's internal method, governed by M-35 + F-16 + the three gates (F-33, P-37, P-36).
Full citations in `MFP-LIBRARY.md`.
