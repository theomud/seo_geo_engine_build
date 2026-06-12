---
Status: draft — built 2026-05-30
Area: skill-visual-evidence-architecture
Depends on: skill-visual-evidence-architecture/files/01-what-is-this-skill.md, skill-visual-evidence-architecture/README.md
Feeds into: skill-visual-evidence-architecture/files/03-how-to-verify-it.md, skill-visual-evidence-architecture/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Building the visual brief, capturing the proof, and rendering the infographics

---

## Why manual first

The proof has to be *real*. A screenshot's value is its **date stamp from the live
official source** — you cannot automate that without losing the thing that makes it
proof (P-06). So the capture is done by hand, from the real regulator/airline page,
on the day. Automation later only assembles and lays out; the evidence is always
captured manually.

Two inputs on the desk before you start a page:
1. **The page's claims** — every factual statement the page makes (from the copy /
   brief), each with its C-ID from the Source Bank.
2. **The named fear** the page resolves — so each visual is judged on whether it
   *lowers that fear*, not on whether it looks nice.

---

## Step 1 — List the claims, mark the one that needs proof shown

Write out every claim on the page. For each, ask: *would a wary reader believe this
without seeing it?* The ones they won't — fees, rules, disputed figures, "we do X" —
need a proof-visible visual. *(Library: M-13 Proof Density — proof beside the claim.)*

**Rule:** every gap page must end Step 1 with **at least one claim marked
"proof-visible screenshot"**. A page with zero is not done.

---

## Step 2 — Choose the visual type for each marked claim

| Claim type | Visual that proves it |
|------------|----------------------|
| A regulation, fee, or official rule | **Official-source screenshot** (dated, with URL) |
| "We do the real work" (process, care) | **Real process photo** — the crate, vet check, handover |
| A comparison or a set of numbers | **Infographic** — table or calendar, phone-rendered |
| An *absence* (no official price exists) | **Screenshot of the official page showing nothing** — the honest hedge, made visible |

Decoration ("a happy dog") is not on this list. If a visual doesn't prove a claim,
it's cut. *(Library: P-39 Replace Stock with Real Photos; P-40 Contextual Relevance.)*

---

## Step 3 — Capture the official-source screenshot (the core craft)

For each official-source screenshot, capture from the **live** page and record:

1. **The visible claim** — frame the screenshot so the fee/rule is legible.
2. **The date stamp** — capture with the date visible (or annotate "captured
   2026-05-30"); a screenshot with no date is not proof, it's an image.
3. **The source URL** — the exact page (e.g. the MOCCAE export-services page).
4. **The C-ID** — link it back to the Source Bank row it proves.
5. **The caption** — one line telling the reader what they're looking at and why.

*(Library: P-06 Screenshots Are Proof; F-08 Proof Interstitial — it sits beside the
claim, not in a gallery.)*

---

## Step 4 — Specify the real process photos

Where the brief calls for a photo, specify **what to shoot and when** — the crate
being prepared, the vet's titer check, the airport handover. Real, this operator's,
this dog. Never stock. *(Library: M-37 Real-Photo Conversion-Lift — +102.5% in the
37signals test.)* The spec names the shot, the moment, and the fear it lowers.

---

## Step 5 — Build the data infographics (phone-first)

Build the reusable data visuals — the **summer-embargo calendar** and the
**airport-comparison table** — as HTML that **renders at 390px with no horizontal
scroll**. Source every figure (C-ID or honest hedge) inside the graphic. Test at
390px before it's done; a desktop-only infographic fails this market (most readers
are on a phone).

---

## Step 6 — Assemble the visual brief

For each page, write the brief: the list of visuals, each with type, the claim it
proves, the C-ID, the caption, and (for screenshots) the source URL + capture date.
The brief is the deliverable a designer/builder can execute without asking questions.

---

## Worked example — the airport-confiscation page

**Named fear:** dog taken at the airport (Muze Gu).
**Claims marked for proof:** (a) the rabies titer is required for entry; (b) there is
a release fee.

| Visual | Type | Proves | Source |
|--------|------|--------|--------|
| MOCCAE import-rule screenshot | official-source screenshot | titer required for entry | C-019, moccae.gov.ae export page, dated |
| MOCCAE fee screenshot | official-source screenshot | **500 AED** release fee | C-003, dated |
| Crate + handover photo | real process photo | the operator does the real work | this operator, not stock |

≥1 proof-visible screenshot ✔ (two, in fact). Each carries a date stamp, URL, C-ID,
and a caption. The page now *shows* the rule the reader is terrified of getting wrong
— which 9/9 competitors never do.

---

## What you must not do

- **Do not use a screenshot with no date stamp.** Undated = an image, not proof.
- **Do not use stock "happy customer" photos.** They're ignored (P-39); use the real
  process or no photo.
- **Do not ship an infographic that breaks at 390px.** Phone-first or it fails.
- **Do not add a visual that proves nothing.** Decoration is cut — every visual has a
  claim and a fear it lowers.
- **Do not capture from a cached/third-party copy.** Proof must come from the live
  official source so the date and URL are real.

---

## Output of this manual phase

Each gap page has a visual brief (≥1 proof-visible screenshot, each with date/URL/
C-ID/caption); the summer-embargo calendar and airport-comparison table are built and
390px-verified; the screenshot integration guide records the capture standard. That
brief set is the real output and the input to File 04 — automation assembles and lays
out; the evidence is always captured by hand.
