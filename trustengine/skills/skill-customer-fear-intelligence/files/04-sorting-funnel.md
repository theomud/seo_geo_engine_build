---
Status: draft — build after Files 02 and 03 complete
Area: skill-01
Priority: high
Activation: after intent classification and fear formula complete
Last updated: 2026-05-26
Depends on: skill-01/02-intent-classification.md, skill-01/03-fear-formula.md
Feeds into: skill-03/content-structure.md, skill-05/keyword-clustering.md, skill-09/conversion-copy.md
---

# Skill 01 — File 04: The 4-Second Sorting Funnel
## Given any keyword — instantly know the page, the opening, and the CTA

---

## Purpose

Files 02 and 03 populate Column J (intent) and Column K (fear) for every keyword. File 04 uses those two columns together to produce a third output: the complete page brief in one line.

The 4-second sorting funnel is the decision system that converts a classified, fear-mapped keyword into an actionable content brief. When you look at any keyword and its intent + fear combination, you know in 4 seconds:

1. What page type to build
2. What the opening sentence should be
3. What the primary CTA should be

This is the bridge between keyword research and content creation. It feeds directly into Skill 03 (Content Structure for Trust).

---

## The Funnel — Intent + Fear = Page Brief

| Intent Type | Fear Category | Page Type | Opening Sentence Pattern | Primary CTA |
|------------|--------------|-----------|------------------------|-------------|
| Fear | Pet safety | Reassurance page | "Your fear is real — here is the verified answer" | Talk to an expert |
| Fear | Documentation mistake | Process clarity page | "This is exactly what you need and when" | Download checklist |
| Fear | Rejection at customs | Prevention guide | "Here is how to make sure this never happens to you" | Get verified guidance |
| Urgency | Time running out | Action page | "You have [X weeks] — here is exactly what to do now" | WhatsApp us now |
| Informational | Process confusion | Step-by-step guide | "Moving your pet to Dubai involves 7 steps — here is each one verified" | Download timeline |
| Commercial | Wrong provider | Trust comparison | "Here is what separates a reliable service from a risky one" | See how we compare |
| Transactional | Any | Service page | "We handle every step so nothing gets rejected" | Get a quote today |
| Research | Competitor fear | Alternative page | "Here is how we handle the concerns you read about" | See our reviews |

---

## The 4-Second Decision

Given any keyword + intent + fear:

**Second 1:** Read the intent type
**Second 2:** Read the fear category
**Second 3:** Match to the funnel table above
**Second 4:** Write the page brief in one line

**Example:**
Keyword: "will my dog need quarantine in Dubai"
Intent: Fear
Fear: Rejection/quarantine separation
Page type: Reassurance page
Opening: "Quarantine in Dubai is rare — but only if these specific conditions are met"
CTA: Download the official quarantine requirements checklist

That is the complete brief. From keyword to brief in 4 seconds.

---

## Automation

Once Columns J and K are populated, Claude Code can generate page briefs automatically for every keyword using the funnel table above. The output goes into a new Sheet called "Page Briefs" with columns:

Keyword | Intent | Fear | Page Type | Opening Sentence | Primary CTA | Priority Score

Priority Score = Source Count × Intent Weight
- Urgency intent × 3
- Fear intent × 2.5
- Commercial intent × 2
- Informational intent × 1.5
- Transactional intent × 1

Highest priority score = build first.

---

## Completion Criteria

- [x] Every keyword has a page brief generated (598 / 598)
- [x] Page briefs reviewed for highest-priority keywords (top 20)
- [x] Priority score calculated for all keywords
- [x] Content calendar for first 3 months identified from top priorities (top of the priority-sorted "Page Briefs" sheet)
- [x] Brief format confirmed and handed to Skill 03

## Test Results Log

**Sorting funnel run — COMPLETE (2026-05-27)**
- Engine: `sorting_funnel_engine.py` (deterministic, offline — no API).
- Output: new **"Page Briefs"** sheet in `skill-01-keyword-collection.xlsx` — `Keyword · Intent · Fear Category · Customer Fear · Page Type · Opening Sentence · Primary CTA · Priority Score`, sorted highest priority first (build-first order).
- Briefs generated: **598 / 598** (0 skipped).
- Priority Score = Column C Source Count × intent weight (Urgency 3 · Fear 2.5 · Commercial 2 · Research 2 · Informational 1.5 · Transactional 1). *Research weight (2) was not specified in this file's table; assigned here as evaluative, comparable to Commercial.*
- Page-type distribution: Step-by-step 275 · Alternative 147 · Trust comparison 147 · Service 13 · Reassurance 12 · Action 2 · Prevention guide 1 · Process clarity 1.
- Top build-first briefs: DKC / Blue Sky research keywords (Research × high source count), then cost/route Commercial keywords.
- Audit sub-agent verdict: **PASS (6/6)** — exact row coverage, no blanks, all funnel mappings correct, all priority math correct, sorted descending.
