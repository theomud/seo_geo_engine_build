---
Status: draft — built 2026-05-29
Area: skill-content-structure
Depends on: skill-content-structure/files/01-what-is-this-skill.md, skill-content-structure/customer-profile/customer-profile-snapshot.md
Feeds into: skill-content-structure/files/03-how-to-verify-it.md, skill-content-structure/files/04-automation-spec.md
---

# Skill 03 · File 02 — How To Do It Manually
## Building one page with the 5-layer structure, by hand, before any automation

---

## Why manual first

The automation spec (File 04) generates first drafts of all five layers from the same inputs you use here. But until you have built several pages by hand — felt where the fear acknowledgement reads as genuine versus formulaic, chosen the page type without hesitating, pulled the verified facts and pasted the citations — the engine is guessing at judgment it has never seen exercised. **Build the first four pages (the four universal gaps) manually, then let automation scale the pattern.**

Time required: **45–90 minutes per page.** Tools: the fear-mapped keyword spreadsheet (`skill-customer-fear-intelligence`, Columns J + K), the Source Bank (`skill-official-source-research/data/skill-02-source-bank.xlsx`, **Verified rows only**), the source screenshots folder, and a browser.

---

## Step 1 — Identify the primary fear and the intent

Open the keyword spreadsheet. For the keyword you are building, read two columns:

- **Column J — Intent** (Fear / Informational / Commercial / Research / Urgency)
- **Column K — Fear statement** (the customer's actual fear, in their language)

If Column K is generic ("worried about cost"), sharpen it against the **Fear Hierarchy** in `customer-profile/customer-profile-snapshot.md` — eight ranked fears, each with a verbatim community quote. Example: a titer-cost keyword maps to Fear #3 *"being price-gouged with no way to know if it's fair"* — quote: *"relocation companies are shamelessly charging an insane amount of money" (IrbisKat, 24 upvotes)*.

**One page resolves one primary fear.** If the keyword carries two fears, the secondary one becomes a related-fear link in Layer 4 — not a second section competing for the opening.

---

## Step 2 — Select the page type (Intent × Fear matrix, 4 seconds)

Intent + Fear = Page Type. No deliberation. Intent comes from the **8 intent types** in Customer Fear Intelligence (Informational, Problem, Fear, Urgency, Emergency, Commercial, Transactional, Research/Navigational):

| Intent | Fear category | Page type |
|--------|--------------|-----------|
| Fear | Confiscation | Fear Resolution Page |
| Informational | Overwhelm | Process Guide |
| Commercial | Price gouging | Cost Transparency Page |
| Commercial | Route documentation mistake | Route/Variant Page |
| Research | Wrong provider | Comparison Page |
| Urgency | Deadline approaching | Urgency Page |
| Emergency | Acute crisis happening now | Emergency Page |
| Problem | "Will this work for someone like me?" | Case Study Page |
| Research | "Can I trust this provider at all?" | Trust Page |

The three newer types: an **Emergency Page** is shorter and harder-edged than an Urgency Page — the visitor's pet is stuck or the flight is imminent, so Layer 1 is one line and Layer 5 is an immediate-contact CTA above the fold. A **Case Study Page** documents one real, completed relocation end-to-end as proof (Layer 3 carries the page). A **Trust Page** concentrates licences, accreditations, named team, and guarantees for the visitor whose primary fear is the provider itself.

The page type sets the structural variation (which layer carries the most weight) and the CTA flavour. Write the chosen type at the top of the brief before writing a word of copy.

---

## Step 3 — Layer 1: Fear acknowledgement (first 100 words)

Open with the customer's exact fear, in their language — not the company's. Use the **Opening Formula**:

```
[Fear statement in customer language] + [Reassurance bridge] + [What this page gives them]
```

Worked example (airport confiscation page):
> "If you've been told your dog could be taken at Dubai airport and not given back — that fear is real, and it has happened to people. This page explains exactly what triggers it, and the three documented steps that prevent it."

Pull the fear wording from the verbatim community quote where possible (Layer 1 of the confiscation page can quote Muze Gu directly). The test for every opening: **does this make the customer feel understood, or more anxious?** If it amplifies the fear to sell, rewrite it — that is fear-*exploiting*, which this skill forbids.

---

## Step 4 — Layer 2: The verified answer

Directly answer the fear. Every factual claim is pulled from the Source Bank and must be a **Verified** row — never Unverifiable, never Pending. Paste three things from the row:

- **Plain English** (the customer-readable sentence — this is the body copy)
- **Exact quote** (shown as a cited blockquote)
- **URL + date verified** (the link and "verified 2026-05-28")

Example (confiscation page, using a Verified MOCCAE row): plain English *"To release a dog at the Cargo Village you pay a 500 AED release fee"*, cited to the MOCCAE import-of-pets page (C-003, Verified 2026-05-28).

**When the only data is Unverifiable** (e.g. the 700–1,300 AED titer cost — MOCCAE publishes no figure), you do not assert it. You hedge, in the page, exactly as the Source Bank status dictates: *"Community reports consistently put this in the 700–1,300 AED range; no official figure is published — confirm directly with the lab before you book."* The Unverifiable status is not a gap in the page; it is the page's honesty advantage.

---

## Step 5 — Layer 3: Process or evidence

Give the step-by-step, or show the proof. This is where the screenshots earn their place:

- Embed at least one screenshot of the official source document from `skill-official-source-research/data/source-screenshots/` (e.g. `UK-gov-uk-C-024-2026-05-28.png` showing the quarantine rule on gov.uk). **Proof, not decoration** — no stock images, no generic "trusted by" badges.
- For a Process Guide, number the steps and cite each regulated step to its Verified row.
- A screenshot of an official page that is *silent* on a claim is also evidence — it proves the figure is community-sourced (see the MOCCAE Unverifiable example in `skill-official-source-research/guides/skill-02-study-manual.html`).

---

## Step 6 — Layer 4: Related fears + internal links

Name two or three related fears this customer almost certainly also has, and link each to the page that resolves it. Use the Fear Hierarchy to pick neighbours: a confiscation page links to the documentation-mistake page (Fear #2) and the timeline/embargo page (Fear #6). This keeps the reader moving toward a decision instead of leaving to compare competitors.

If the linked page does not exist yet, record it as a required page in the brief — Layer 4 is how the site's internal-link map writes itself.

---

## Step 7 — Layer 5: The help-first CTA

The CTA offers something immediately useful that resolves a specific fear — it never asks the customer to do work before getting value.

| Good (help-first) | Bad (ask-first) |
|-------------------|-----------------|
| "Download the Dubai pet import checklist (verified against MOCCAE 2026)" | "Get a Free Quote" |
| "See the full timeline — how far ahead you need to start" | "Contact Us Today" |
| "Check if your breed is restricted before you book" | "Request a Consultation" |

Match the CTA to the page type: Cost Transparency → cost estimator; Comparison → Trust Score comparison; Urgency → emergency consultation.

---

## Step 8 — Record the brief and save the template

Write the page into a brief row (`data/content-structure-briefs.md`): keyword, intent, fear statement, page type, the five layers' content, the Source Bank IDs cited, the screenshots used, and the related-fear links. When a page type is built for the first time, save its skeleton to `data/content-structure-templates/` so the next page of that type starts from structure, not blank.

---

## Planning the page set — hierarchy and depth

A single page is built with Steps 1–8. But pages do not live alone: they sit inside a service and location hierarchy and at a chosen depth. Plan these before building the set, so the internal links in Layer 4 have real targets.

> The page-level planning below is what a writer needs to place one page correctly. The **full architecture methodology** — sitemap and URL structure, navigation logic, conversion-path design, and the architecture document template — belongs to **Skill 31 — Content Architecture** (`skill-content-architecture/`). Use this section to position a page; use Skill 31 to design the whole site.

### Service hierarchy design

Map the niche's services from broadest to most specific, parent → child. Each level is a page; children link up to their parent and the parent links down to each child.

```
Pet Relocation (pillar / top service)
├── Dog relocation
│   ├── Large-breed dog relocation
│   └── Snub-nosed (brachycephalic) breed relocation
├── Cat relocation
└── Exotic / other pets (birds, rabbits, reptiles)
```

Rule: a child page exists only when it has its own primary fear that the parent cannot resolve in one section (e.g. snub-nosed breeds carry a distinct cargo-safety fear). Otherwise it is a section on the parent, not a page. The pillar page is a Process Guide or Trust Page; the children are Fear Resolution, Route, or Cost Transparency pages.

### Location hierarchy design

Map the geography the same way — country → city → route — one page per level that has distinct verified facts or a distinct fear.

```
Move pets from the UAE (country gateway)
├── From Dubai   ├── From Abu Dhabi   ├── From Sharjah
└── Routes: Dubai → UK · Dubai → India · Dubai → Australia · …
```

Rule: a location page earns its place only when the official requirements or the route experience actually differ (the Sharjah-airport route differs materially from Dubai — it gets a page; "from Deira" does not — same rules as Dubai). Route pages are Route/Variant pages citing the destination authority's Verified Source Bank rows.

### Content depth planning — 4 levels

Match the page's depth (and word-count target) to its intent and position in the hierarchy. Depth is a decision, not an accident:

| Level | Word target | Use for | Page types |
|-------|-------------|---------|------------|
| 1 — Quick answer | 300–500 | Acute need, single fact, fast exit | Emergency Page; thin FAQ |
| 2 — Focused | 500–1,000 | One specific fear or cost, fully resolved | Fear Resolution, Cost Transparency |
| 3 — Comprehensive | 1,000–2,000 | A full process or head-to-head | Process Guide, Comparison, Route/Variant |
| 4 — Pillar / authority | 2,000–5,000 | Top-of-hierarchy hub that links to the cluster | Service pillar, Trust Page, in-depth Case Study |

Pick the level at briefing time. Over-writing a Level 1 Emergency page buries the contact CTA; under-writing a Level 4 pillar leaves it unable to rank or to anchor its cluster. Depth follows the job, and the job follows intent + hierarchy position.

---

## Worked example — the four universal gaps, in order

These four pages are built first because all nine scored competitors are missing them:

1. **"What happens if your dog is taken at Dubai airport?"** — Fear / Confiscation → Fear Resolution Page. Opening quotes Muze Gu; Layer 2 cites the Verified MOCCAE release-fee and permit rows.
2. **"Can I move my pet to Dubai in summer?"** — Informational / Timeline → Process Guide. Opening names the June–September heat embargo; Layer 3 is the month-by-month timeline.
3. **"How much does the rabies titer test cost in Dubai?"** — Commercial / Price gouging → Cost Transparency Page. Opening quotes IrbisKat; Layer 2 hedges the 700–1,300 AED range as Unverifiable + one-lab/2–3-week wait.
4. **"Sharjah vs Dubai vs Abu Dhabi — which airport?"** — Research / Documentation mistake → Comparison Page. Opening names the Sharjah hack (~20 min, no airline pre-comms); Layer 3 is the airport comparison table.

---

## What you must not do

- **Do not open with the company.** The first sentence is the customer's fear, not "Welcome to…".
- **Do not assert an Unverifiable claim as fact.** Hedge it exactly as the Source Bank status dictates.
- **Do not exploit the fear.** Acknowledge to resolve, never amplify to sell.
- **Do not put two primary fears on one page.** The second fear gets its own page and a Layer 4 link.
- **Do not use stock imagery as "evidence."** Layer 3 proof is official-source screenshots and named sources only.
- **Do not end with "Get a Quote."** The CTA earns the click by giving something useful first.

---

## Output of this manual phase

When the first four pages are built by hand you have: four completed briefs across four page types, a saved template per type, the internal-link map between the related-fear pages, and a confident answer to *"for this niche, what does a trust-first page actually look like, layer by layer?"* That answer is what makes File 04's automation implementable — without it, automation just rearranges paragraphs.
