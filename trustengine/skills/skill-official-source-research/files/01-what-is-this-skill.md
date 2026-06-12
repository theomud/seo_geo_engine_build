---
Status: draft — built 2026-05-28
Area: skill-02
Depends on: skill-02/customer-profile/customer-profile-snapshot.md
Feeds into: skill-02/files/02-how-to-do-it-manually.md, skill-02/files/04-automation-spec.md
---

# Skill 02 · File 01 — What This Skill Is
## Niche-agnostic definition of Official Source Research

---

## The problem this skill solves

In regulated service markets — pet relocation, immigration, medical travel, tax compliance, licensing — the cost of wrong information is not a lost sale. It is real harm. A customer who follows a confidently-written but incorrect page may have their pet confiscated at a border, their visa denied, their procedure cancelled, or their business shut down.

Customers know this. They are not searching for content; they are searching for *trust*. Their dominant feeling on arrival at a page is **"Every website says something different — I don't know who to trust."** The first provider to systematically prove every claim against an official source wins the market.

Most content operations skip this step. Writers paraphrase competitors, then competitors paraphrase each other, and the conventional wisdom of a niche detaches from the actual regulations. **Official Source Research is the discipline of breaking that loop.**

---

## What Official Source Research produces

A single artefact: the **Source Bank** — a spreadsheet where every regulation, price, timeline, or process claim relevant to the niche has a row with five mandatory fields.

| Field | What it is |
|-------|-----------|
| Claim | The exact statement to be made on a page (e.g. "rabies titer test results take 2–3 weeks") |
| Official URL | The government, airline, or industry body page that confirms the claim |
| Date checked | The date the URL was last visited and the quote re-verified |
| Exact quote | The verbatim text from the official source — copy/paste, never paraphrased |
| Plain English | The same fact written in a sentence a customer can understand |

Plus a **Status** column: **Verified** · **Unverifiable** (no official source exists) · **Conflicting** (community says X, official says Y — both documented).

Nothing gets published in any content piece unless it can be traced back to a Source Bank row. The Source Bank is the only approved source of truth for content writers.

---

## Why this is a standalone skill — not a step inside writing

This skill is deliberately upstream of writing. Three reasons:

1. **It outlives any single page.** A regulation changes once, and a single row update propagates to every page that cites it.
2. **It produces a defensible commercial asset.** A verified Source Bank is licensable on its own to anyone publishing in the same niche.
3. **It changes the brand position.** Pages that cite verified sources read fundamentally differently from pages that hedge. The skill earns the right to make confident statements.

---

## How it differs from generic fact-checking

| Generic fact-checking | Official Source Research |
|----------------------|--------------------------|
| Confirms a statement is "true" | Confirms a statement matches a *named, dated, official* source |
| Done at publish time | Done before any writing starts |
| One-off per article | Continuous — claims are re-checked on a schedule |
| Output is internal note | Output is a structured spreadsheet that anyone can audit |
| Accepts any reputable source | Accepts only the regulating body, the airline operating the route, the destination authority, or a recognised industry body |

---

## The five-phase methodology (every regulated niche)

This skill applies the universal research methodology from MASTER-SYSTEM:

1. **Market research** — list every published claim across competitor sites about the regulation. (Output of `skill-trust-gap-analysis`.)
2. **Community research** — collect every customer-stated claim from forums, groups, screenshots. (Output of `skill-customer-fear-intelligence`.)
3. **Manual verification** — visit each official source by hand, extract the quote, record the row.
4. **Automation spec** — Playwright visits the same URLs at scale; Anthropic matches extracted text against pending claim text; the human approves the row.
5. **Audit** — a sub-agent re-verifies a sample of rows by re-fetching the live page and re-comparing the quote.

---

## What is in scope, what is out of scope

**In scope.** Any factual statement about: requirements, documents, timelines, costs (when published by the regulator or carrier), restricted categories (breeds, types, items), processes, fees, validity windows, and official contact points.

**Out of scope.** Opinions, customer reviews, market commentary, route recommendations, brand positioning, and pricing from operators that is not officially published. These belong in other skills (`skill-trust-gap-analysis`, `skill-customer-fear-intelligence`, `skill-conversion-copy`).

---

## What "good" looks like

A Source Bank is good when:

- Every row that touches regulation cites a `.gov` / official airline / official industry-body URL.
- Every row has a date checked within the last 90 days.
- Conflicts between community-stated and officially-stated facts are documented as a `Conflicting` row, not deleted.
- Unverifiable claims are explicitly marked — content writers know to soften the language ("commonly reported as ~X — not officially published").
- The spreadsheet is the input to writing, not a reference checked afterwards.

Skill 02 is complete when the Source Bank exists for the proof niche, every pending claim has a status, and the audit sub-agent passes a 20% re-verification sample.
