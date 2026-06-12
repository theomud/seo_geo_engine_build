---
Status: draft — built 2026-05-30
Area: skill-visual-evidence-architecture
Depends on: skill-visual-evidence-architecture/files/02-how-to-do-it-manually.md
Feeds into: skill-visual-evidence-architecture/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that keep a visual genuine proof — dated, official, phone-rendered

---

## Why verification matters

A visual either proves a claim or it doesn't. The failure mode is a page *looking*
evidenced while proving nothing: an undated screenshot the reader can't trust, a
stock dog dressed up as "our process", an infographic that's unreadable on the phone
most readers use. In a market where a wrong claim gets a pet refused, a visual that
looks like proof but isn't is worse than no visual — it manufactures false confidence
(P-02). Verification checks that every visual is **real, dated, official, and visible
where the reader actually is**.

---

## Gate set A — visual integrity (per visual)

| Gate | Passes when |
|------|-------------|
| A1 · It proves a specific claim | The visual is tied to a named claim + C-ID; a decorative image with no claim fails. *(M-13)* |
| A2 · Screenshots are dated | Every official-source screenshot shows or is annotated with a capture date. Undated = an image, not proof — fail. *(P-06)* |
| A3 · Screenshots are from the live official source | The source URL is the regulator/airline's own page, not a cached or third-party copy. *(P-07)* |
| A4 · Photos are real, not stock | Any "process" photo is the real operator/dog/crate; a stock library image fails. *(P-39)* |
| A5 · Infographics render at 390px | The built graphic shows no horizontal scroll at 390px, verified by screenshot. |

A2 and A5 are the two gates that catch the most common fakes: undated screenshots and
desktop-only infographics. A visual failing any A-gate is recaptured/rebuilt or cut.

---

## Gate set B — the threshold check (per page + per build)

The output clears the README's two-part Functional Quality Threshold:

1. **Proof-visible coverage** — every gap page's brief specifies **≥1 proof-visible
   screenshot** (dated, official, tied to a claim). A page with zero fails.
2. **Phone-rendered infographics** — the summer-embargo calendar and airport-comparison
   table each render at **390px with no horizontal scroll**.

Either unmet = the output is not done.

---

## The independent re-check (the core check)

A second person (a sub-agent or different human) checks the brief and the built assets
**blind to the builder's notes**, seeing only: the page's claims, the visual brief,
and the rendered infographics. Then:

- **The proof verdict is the hard test.** For each marked claim, does the specified
  visual actually prove it, dated and from the official source? A "looks proven but
  isn't" (undated / decorative / stock) is a fail, not a quibble.
- **390px agreement.** The re-checker opens each infographic at 390px and confirms no
  horizontal scroll independently — not from the builder's screenshot alone.

---

## The audit sub-agent — verifying the verifier

After the briefs and infographics are built, a sub-agent independently re-checks
**20%** (minimum 3 — here all 4 pages + both infographics) per the method above.
*(Library: P-07 Independent Verification.)*

Pass threshold: **90%** agreement on the proof verdict **and** zero infographics that
break at 390px **and** zero undated screenshots accepted. An undated screenshot or a
stock photo passed as proof is a **hard fail** regardless of the percentage. Below
that → recapture/rebuild before anything publishes.

---

## Worked check (the confiscation page)

A blind re-checker sees two specified screenshots (MOCCAE titer rule C-019, MOCCAE fee
C-003) and one process photo. They verify: A1 — each ties to a claim + C-ID ✔; A2 —
each screenshot carries a capture date ✔; A3 — the URL is moccae.gov.ae, the live
official page ✔; A4 — the crate photo is the real operator's, not stock ✔. Proof-visible
coverage: 2 ≥ 1 ✔. If the fee screenshot turned out undated, that's a legitimate fail
→ recapture with the date visible, don't wave it through because "the number is right".

---

## What downgrades / forces a recapture or rebuild

- A screenshot with no visible/annotated capture date.
- A screenshot from a cached page or a third-party blog, not the official source.
- A "process" photo that is stock or generic.
- An infographic with horizontal scroll at 390px.
- A visual on the page that proves no specific claim (decoration).
- A gap page with zero proof-visible screenshots.

---

## Output of the verification phase

Every gap page's brief has ≥1 dated, official, claim-tied screenshot; both
infographics render at 390px; every visual proves a specific claim; and an independent
re-check agrees on the proof verdict with ≥90% agreement and zero hard fails. That
verified discipline is what makes File 04's automation safe — the engine assembles and
lays out, but the evidence is trusted only because each capture is real, dated, and
official.
