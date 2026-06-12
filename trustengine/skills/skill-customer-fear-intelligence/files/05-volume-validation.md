---
Status: draft — build after engine Phase 3 completes
Area: skill-01
Priority: high
Activation: after engine Phase 3 complete — can run in parallel with Files 02 and 03
Last updated: 2026-05-26
Depends on: skill-01-keyword-collection.xlsx (Sheet 1 populated)
Feeds into: skill-05/keyword-clustering.md, skill-01/04-sorting-funnel.md (priority scoring)
---

# Skill 01 — File 05: Volume Validation
## Checking real search volume for every validated keyword

---

## Purpose

The engine collects keywords based on what Google suggests and what communities discuss. This tells you what people search for. Volume validation tells you how often they search for it — which determines content priority, not content value.

A keyword with 10 monthly searches in the Dubai pet relocation market can be worth more than a keyword with 1,000 searches — if the 10 searchers are people with a confirmed move date and a dog that needs relocating. Volume is a priority signal, not a value signal. This file explains how to collect it and how to use it correctly.

---

## Phase 1 — Manual (Google Keyword Planner)

**Setup:** Free Google Ads account at ads.google.com. No spend required.

**Process:**
1. Open Keyword Planner → Discover new keywords
2. Paste batches of 100 keywords from Column A
3. Set location: United Arab Emirates
4. Set language: English
5. Export results
6. Match volume data back to Column G in spreadsheet
7. Update status from "pending-volume" to "collection-validated" or "phase-2"

**Volume recording rules:**
- Exact number if available (e.g. 1,300)
- "< 10" if shown as very low
- "not found" if keyword returns no data
- Never delete a keyword just because volume is zero or low

**The zero-volume rule:**
A keyword with zero Google Keyword Planner volume is NOT automatically rejected. Keyword Planner undercounts niche markets significantly. Authority Hacker documented a case where their #1 ranking keyword showed far less traffic than Planner predicted and a "zero volume" keyword outperformed it.

Keep zero-volume keywords if:
- They appeared in 3+ sources during collection
- They contain a specific route/location/fear combination
- They match real community language from Facebook or Reddit
- They are question-format fear keywords

Document the reasoning in the Notes column.

---

## Phase 2 — Automated (DataForSEO)

When the system scales beyond Phase 1 manual checking, DataForSEO replaces this entire file. One API call returns volume + difficulty + CPC alongside keyword suggestions — eliminating the manual Keyword Planner step entirely.

Environment variable: `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` in `.env`
Cost: approximately $0.001 per keyword at scale

---

## Completion Criteria

- [ ] All "pending-volume" keywords checked in Keyword Planner
- [ ] Column G populated for all collection-validated keywords
- [ ] Column H (Seasonal Peak) updated — Oct–Apr for cargo keywords, Year-round for regulation keywords
- [ ] All zero-volume decisions documented in Notes column
- [ ] Status column updated — no keywords left as "pending-volume"
- [ ] Volume data handed to Skill 05 for cluster prioritisation
