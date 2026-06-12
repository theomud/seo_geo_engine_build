---
Status: draft — build after engine Phase 3 completes
Area: skill-01
Priority: high
Activation: after engine Phase 3 complete
Last updated: 2026-05-29 (expanded 6 → 8 intent types: added Problem, split Urgency/Emergency)
Depends on: skill-01/01-google-search-discovery.md, skill-01-keyword-collection.xlsx (Sheet 1 populated)
Feeds into: skill-01-keyword-collection.xlsx (Column J), skill-01/03-fear-formula.md, skill-05/keyword-clustering.md
---

# Skill 01 — File 02: Intent Classification
## Assigning the 8 intent types to every validated keyword

---

## Purpose

Every keyword in Column A of the spreadsheet has an intent behind it. The person is in a specific moment in their journey — researching, comparing, ready to buy, panicking, confused. Intent classification assigns that moment to each keyword so the right content type, the right page structure, and the right CTA are used for every page built from this keyword.

Without intent classification, you build the wrong page for the right keyword. A keyword with informational intent needs an educational guide. The same keyword treated as commercial intent gets a service page that nobody trusts because they were not ready to buy yet.

Intent classification fills Column J. It must be done before fear mapping (File 03) because the fear statement depends on knowing what stage of the journey the person is in.

---

## The 8 Intent Types

These are not the standard 4 Broder buckets. They are adapted for high-stakes regulated service markets where the standard taxonomy loses critical nuance. Expanded from 6 to 8 (2026-05-29): **Problem** added, and the old single **Urgency** split into **Urgency** (a deadline approaching) and **Emergency** (a crisis happening now) — the two demand completely different pages.

### 1. Informational
The person wants to understand something. They are not ready to buy. They need education.

**Signals:** how, what, why, guide, checklist, steps, process, requirements, rules
**Example:** "how to move a dog to Dubai" — they want to understand the process
**Page type:** Process Guide — step-by-step process, timelines, documents list
**CTA:** download checklist, subscribe to updates, not "get a quote" yet

### 2. Problem
The person has a concrete obstacle and wants the fix — not general education, and not (yet) an emotional fear. Something has gone wrong, or there is a specific task to accomplish, and they need the method or proof that it can be solved.

**Signals:** failed, rejected, wrong, not accepted, "what to do if", "how to fix", next steps, isn't working, denied (as an event that has happened)
**Example:** "dog failed rabies titer test what next" — a concrete problem needing a resolution path
**Page type:** Case Study Page or problem-solution guide — document how the exact problem was solved
**CTA:** see how we solved this, talk to someone who has fixed this
**Distinction:** Informational = "how does X work" (learning). Problem = "X went wrong / I must get X done — give me the fix" (solving). Fear = the emotional worry about a possible bad outcome, before it has happened.

### 3. Fear
The person has a specific worry they need resolved before they can move forward. This is the highest-converting intent type in regulated service markets.

**Signals:** safe, risk, can, will, what if, is it, danger, mistake, "could my pet be", quarantine, confiscated
**Example:** "is it safe to fly a dog to Dubai" — they are afraid of something specific
**Page type:** Fear Resolution Page — acknowledge fear first, then verified answer, then social proof
**CTA:** talk to an expert, get a free consultation — reassurance not purchase

### 4. Urgency
The person has a real deadline approaching. There is still lead time — days or weeks — but it is tightening. Time is a primary constraint, not yet a crisis.

**Signals:** before summer, before the embargo, this month, by [date], soon, deadline, last minute (planning sense)
**Example:** "move pet to Dubai before summer embargo" — a deadline is coming, plan now
**Page type:** Urgency Page — clear action path and timeline, decisive CTA
**CTA:** see the timeline, book your slot now, start today

### 5. Emergency
The person is in an acute crisis happening now — hours, not weeks. The pet is stuck, the flight is imminent, something has just gone wrong at the airport. They cannot read a long page.

**Signals:** emergency, stuck at airport, flight tomorrow/today, right now, stranded, asap, "happening now", pet held
**Example:** "pet stuck at Dubai airport help" — an in-progress crisis
**Page type:** Emergency Page — one-line acknowledgement, immediate contact above the fold, minimal reading
**CTA:** call now, WhatsApp now — speak to someone immediately
**Distinction:** Urgency = a deadline in days/weeks (still plannable). Emergency = a crisis in progress measured in hours.

### 6. Commercial
The person is comparing options and moving toward a decision. They know services exist and are evaluating.

**Signals:** best, top, compare, vs, review, cost, price, quote, company, service
**Example:** "best pet relocation company Dubai" — they are shortlisting providers
**Page type:** trust-building page — credentials, testimonials, process transparency, pricing framework
**CTA:** get a quote, book a consultation

### 7. Transactional
The person has made the decision and wants to take action now.

**Signals:** book, hire, contact, get a quote, service, company + location, near me
**Example:** "pet relocation company Dubai" with no question words — they want to hire
**Page type:** service page — clear offer, clear process, clear CTA, trust signals
**CTA:** get started, book now, speak to our team

### 8. Research / Navigational
The person is looking for a specific resource, tool, or brand. They know what they want.

**Signals:** brand names, IPATA, specific airline, MOCCAE, specific form name, specific regulation
**Example:** "Blue Sky pet relocation Dubai" — they want to find or compare a specific company
**Page type:** comparison or alternative page — do not pretend to be the brand, be the better option
**CTA:** why choose us instead, see how we compare

---

## How to Classify — The Decision Process

For each keyword, ask these questions in order (most acute / most specific first):

**Q1: Does it signal a crisis happening now (stuck, today, flight tomorrow, right now, stranded)?**
If yes → Emergency. Stop.

**Q2: Does it signal a deadline approaching (before summer/embargo, by [date], this month, soon)?**
If yes → Urgency. Stop.

**Q3: Does it contain fear signals (safe, risk, will, can, what if, danger)?**
If yes → Fear. Stop.

**Q4: Does it describe a concrete problem to fix (failed, rejected, "what to do if", "how to fix", next steps)?**
If yes → Problem. Stop.

**Q5: Does it contain a brand name or specific named resource?**
If yes → Research/Navigational. Stop.

**Q6: Does it contain commercial signals (best, compare, cost, price, review)?**
If yes → Commercial. Stop.

**Q7: Does it contain transactional signals (book, hire, contact, get a quote)?**
If yes → Transactional. Stop.

**Default → Informational.**

---

## Edge Cases — Where Human Judgment Is Required

These are the keywords that the automated classifier will get wrong. Review these manually:

**Ambiguous cost keywords**
"pet relocation Dubai cost" — is this Informational (how much does it cost, explain the factors) or Commercial (I want a quote to compare)?
→ Rule: if it says "cost" without "quote" or "get" — Informational. If it says "quote" or "price" with commercial context — Commercial.

**Route keywords without question words**
"pet relocation Dubai to India" — Informational or Commercial?
→ Rule: if no other signal present, default to Commercial. Someone searching a specific route is usually past the education phase.

**Compound fear + commercial**
"safest pet relocation company Dubai" — Fear or Commercial?
→ Rule: Fear wins. Address the safety concern first, then present the commercial offer.

**Competitor brand keywords**
"Blue Sky pet relocation Dubai reviews" — Research or Commercial?
→ Rule: "reviews" = Research. They are evaluating, not deciding.

---

## Automation — Claude Code Classification

80%+ of keywords can be classified automatically. The remaining 20% need human review.

Claude Code classification prompt:
```
You are classifying pet relocation search keywords by intent type.

The 8 intent types are:
1. Informational — wants to understand, not ready to buy
2. Problem — has a concrete obstacle/task, wants the fix (not yet emotional fear)
3. Fear — has a specific worry that blocks progress
4. Urgency — has a deadline approaching (days/weeks), needs to plan fast
5. Emergency — a crisis happening now (hours), cannot wait
6. Commercial — comparing options, moving toward decision
7. Transactional — has decided, wants to act now
8. Research/Navigational — looking for specific brand or resource

For each keyword, output ONLY the intent type. No explanation unless it is an edge case.

Classify these keywords:
[paste Column A keywords here]
```

After automated classification:
- Review every "Fear" classification manually — these are the highest-value pages
- Review every "Emergency" and "Urgency" classification — confirm crisis-now vs deadline-approaching is correct; these need the fastest, most decisive pages
- Review every "Problem" classification — confirm it is a concrete fix-needed keyword, not general Informational
- Review every keyword containing a brand name
- Review any keyword you personally feel uncertain about

---

## Spreadsheet Update

Column J = Intent Type
Dropdown options in Column J: Informational / Problem / Fear / Urgency / Emergency / Commercial / Transactional / Research

> **Re-classification note (2026-05-29):** the 598 keywords already classified under the old 6-type scheme need a re-review pass against the two new types. Specifically, re-scan the existing **Urgency** rows and split out true **Emergency** (crisis-now) keywords, and re-scan **Informational** + **Fear** rows for **Problem** (concrete-fix) keywords. Until that pass is run, Column J reflects the old 6 types for legacy rows.

After classification, the spreadsheet gains a new analytical capability:

**Count by intent type:**
- How many Fear keywords? These are the priority pages.
- How many Urgency keywords? These need the fastest build.
- How many Commercial? These are your money pages.
- How many Informational? These build authority and feed the funnel top.

This count determines the content calendar in Skill 05 (Keyword Clustering).

---

## Completion Criteria

File 02 is complete when:
- [ ] Column J populated for all collection-validated keywords in Sheet 1
- [ ] All 8 intent types represented in the classification (legacy 598-row re-review pass run for Problem + Emergency)
- [ ] Fear keywords manually reviewed — every one confirmed correct
- [ ] Edge cases documented with reasoning
- [ ] Intent type count summary recorded
- [ ] Ready to pass every keyword to File 03 (Fear Formula)
