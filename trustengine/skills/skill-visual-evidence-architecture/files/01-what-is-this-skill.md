---
Status: draft — built 2026-05-30
Area: skill-visual-evidence-architecture
Depends on: skill-visual-evidence-architecture/README.md
Feeds into: skill-visual-evidence-architecture/files/02-how-to-do-it-manually.md, skill-visual-evidence-architecture/files/04-automation-spec.md
---

# Skill · File 01 — What This Skill Is
## Niche-agnostic definition of Visual Evidence Architecture

---

## The problem this skill solves

A frightened reader does not trust words. They have read ten sites that all *say*
"trusted", "experienced", "stress-free" — and one of them quoted them an outrageous
price anyway. By the time they reach your page, a claim they cannot **see proven** is
worth nothing. The text can be true, sourced, and well-written, and still not move
them, because trust at this stage is built with the eyes, not the paragraph.

Visual Evidence Architecture is the system that puts **visible proof beside every
claim**: a dated screenshot of the official regulation next to the rule it states; a
real photo of the actual crate and handover instead of a stock golden retriever; the
data drawn as an infographic the reader can scan on a phone. It decides, per page,
exactly which visuals are needed and what each one proves — then builds the reusable
ones.

---

## What this skill produces

| Output | What it is |
|--------|-----------|
| Visual brief per page | Which screenshots, photos, and infographics each page needs — and the specific fear each lowers |
| Built infographics | The summer-embargo calendar and airport-comparison table, as HTML that renders at 390px |
| Screenshot integration guide | How an official-source screenshot embeds beside a claim — caption, date stamp, source URL |

The rule that makes it scorable: **every gap page carries at least one proof-visible
screenshot**, and **every built infographic renders on a phone**.

---

## The core idea — a visual is evidence with a job

Every visual must lower a named fear by **showing** what the text can only assert.
*(Library: F-08 Proof Interstitial — the proof sits beside the claim; M-13 Proof
Density — proof next to every claim, not in a gallery.)*

| The text says (assertion) | The visual proves (evidence) |
|---------------------------|------------------------------|
| "We handle MOCCAE documentation" | a dated screenshot of the stamped MOCCAE certificate |
| "There's a release fee" | the official MOCCAE fee page showing **500 AED** (C-003), captured today |
| "Etihad's pet fee is disputed" | the official Etihad fee page (**USD 399**) beside the community screenshot (USD 1,500) (C-015) |
| "Your dog flies safely" | a real photo of *your* crate and *your* handover — not stock |

A decorative image proves nothing and is cut. Proof beside the claim is the whole skill.

---

## Real photos beat stock — and it's measured

*(Library: M-37 Real-Photo Conversion-Lift; P-39 Replace Stock with Real Photos;
P-40 Contextual Relevance Beats Novelty.)* Stock "happy customer" photos are
literally ignored — eye-tracking shows readers skip them as ad-like. Real photos of
the real process convert: 37signals' A/B test lifted paid signups **+102.5%** by
swapping a generic image for a real person. In the proof niche, a real photo of the
crate, the vet check, and the airport handover is proof the operator did the work —
the kind of thing AI and competitors cannot fake.

---

## A worked example (the proof niche)

The four universal gap pages, each with its anchor proof-visible visual:

| Page | The proof-visible visual that lowers the fear |
|------|----------------------------------------------|
| Dog taken at the airport | dated screenshot of the MOCCAE rule + the required titer wording (C-019/C-003) |
| Move a pet in summer | the **summer-embargo calendar** infographic, airline dates sourced |
| Rabies titer test cost | a screenshot proving **no official price is published** — the honest hedge, shown |
| Sharjah vs Dubai vs Abu Dhabi | the **airport-comparison table** infographic + the Etihad fee screenshot (C-015) |

A competitor's version of any page uses a stock dog and asserts trust in words.
Ours shows the regulator's own page, dated, beside the claim — which is exactly the
gap the trust analysis found across all 9 competitors (none show original proof).

---

## How it differs from neighbouring skills

| Skill | Owns |
|-------|------|
| Conversion Copy | the **words** that name and resolve the fear |
| Official Source Research | **verifying** the claim and storing the URL + quote (the C-ID) |
| **Visual Evidence Architecture** | making the proof **visible on the page** — the screenshot, photo, infographic beside the claim |

Source research proves the fact exists and stores its URL. This skill takes that URL,
captures it as a dated screenshot, and specifies exactly where it sits on the page.

---

## Why this is a standalone skill

1. **Trust at the decision moment is visual.** The best copy still needs the proof
   shown, or the wary reader doesn't believe it.
2. **Real proof is un-fakeable and un-AI-able.** A dated regulator screenshot and a
   real process photo are exactly what a competitor's stock-photo page cannot match.
3. **It is a portable, teachable method.** Every regulated market has official
   sources to screenshot, a real process to photograph, and data to visualise.

---

## In scope / out of scope

**In scope.** Specifying the visual brief per page (which screenshot/photo/infographic
and what it proves); the screenshot integration method (date stamp, caption, source
URL); building the reusable data infographics so they render on a phone.

**Out of scope.** Verifying the underlying fact (done upstream in source research —
this skill *shows* the verified claim, it doesn't decide it's true), writing the
page's words (conversion copy), and the page architecture (content structure). This
skill makes the proof visible; it does not originate the proof or the prose.

---

## What "good" looks like

- **Every gap page has ≥1 proof-visible screenshot** specified in its brief — a dated
  official-source capture beside a specific claim, never a decorative image.
- **Every built infographic renders at 390px** with no horizontal scroll.
- Every screenshot carries a **date stamp and source URL** so the proof is checkable.
- Stock "happy customer" imagery is replaced by **real process photos** wherever the
  brief calls for a photograph.

This skill is complete when the four gap pages have visual briefs meeting the
proof-visible rule, the summer-embargo calendar and airport-comparison table are built
and phone-verified, the screenshot integration guide exists, and the audit passes.
