# Customer Profile Snapshot — Prompt Engineering
## Only the excerpts a prompt-writer needs to fill the 9 elements
## Full profile: ../../01-master-customer-profile.md

---

## Why this matters for prompt engineering

A 9-element prompt is only as good as what you put in **Context**, **Audience**, **Inputs**, and **Constraints**. For the Dubai pet-relocation proof niche, those four elements are filled from the items below: the fear language (Column K), the personas, the page type, and the verified inputs. Nothing else from the master profile is needed to write a prompt — this is the working subset.

---

## The fears (Column K language) → Audience + Constraints + the opening

Use the customer's verbatim words; never invent a fear. Each fear is the Audience's state and the line the page must open with:

| Fear | Verbatim community language (use in the prompt) |
|------|-------------------------------------------------|
| Confiscation | "without it your dog will be taken away in airport and never give back… Still when I remember I crying" — Muze Gu |
| Price gouging | "relocation companies are shamelessly charging an insane amount of money" — IrbisKat (24 upvotes) |
| Wrong provider | "Please do proper research and read reviews before handing over your pet" — Curious_cat_2912 (16 upvotes) |
| Don't-know-who-to-trust | "Every website says something different — I don't know who to trust" |
| Timeline / embargo | "We are moving soon. Is there still time?" |
| Pet suffering | "Just the thought she's gonna be so stressed out breaks my heart" |

> **Constraints rule for this niche:** open with the fear in these words; acknowledge to resolve, never amplify. (Fear-acknowledging, not fear-exploiting.)

---

## The personas → the Audience element

Pick the persona the keyword belongs to and write Audience from it:

| Persona | Primary fear (Audience state) |
|---------|-------------------------------|
| Expat Leaving Dubai | Documentation mistake at the border |
| Family With Children | Pet suffering + timeline |
| Last-Minute Mover | Running out of time |
| Confused Researcher | Overwhelm — doesn't know where to start |
| Safety-First Owner | Pet suffering in cargo |
| Import-to-Dubai Owner | Confiscation at the airport |
| Remote Relocator | No one to manage the process |

---

## The 9 page types → which template to open (Objective + Output Format)

The prompt's Objective and Output Format follow the page type (full templates in `data/prompt-template-library.md`):
Fear Resolution · Process Guide · Cost Transparency · Comparison · Route/Variant · Urgency · Emergency · Case Study · Trust Page.

Intent (Column J, 8 types: Informational · Problem · Fear · Urgency · Emergency · Commercial · Transactional · Research) + fear → page type → template.

---

## The content brief inputs → the Inputs element

What goes into **Inputs** for this niche (always cited, never invented):
- **Verified facts** from the Source Bank, by C-ID — e.g. C-003 (MOCCAE release fee 500 AED/dog), C-010 (permit valid 90 days), C-019 (permit applied online), C-007 (rabies ≥21 days).
- **Unverifiable claims** to hedge (passed in so the prompt knows to hedge, never assert) — e.g. C-001 (titer cost: no official figure; community 700–1,300 AED).
- **Conflicts** — e.g. C-015 (Etihad official USD 399 vs community USD 1,500).
- **Community quotes** — the verbatim fear language above, for the Layer-1 opening.
- **Official-source screenshots** — for the Layer-3 evidence reference (`skill-official-source-research/data/source-screenshots/`).

---

## How to use this snapshot

When writing a prompt: read the keyword → pick the persona (Audience) and page type (Objective/Format) → pull the fear quote (opening) and the Verified/Unverifiable/Conflict inputs by C-ID (Inputs) → set the hedge + fear-first + no-generic Constraints. That fully loads the four hardest elements before you write a word of the brief.
