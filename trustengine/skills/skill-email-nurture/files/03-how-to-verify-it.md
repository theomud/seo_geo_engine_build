---
Status: draft — built 2026-06-01
Area: skill-email-nurture
Depends on: skill-email-nurture/files/02-how-to-do-it-manually.md
Feeds into: skill-email-nurture/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that prove the sequence acknowledges fear, cites verified facts, and stays help-first

---

## Why verification matters

A nurture sequence fails in two characteristic ways, and both *look* fine from a distance. The
first is the **brochure** — warm, generic, fear-free ("We're here to help with your move!") —
which the reader deletes because it sounds like every other company. The second is the
**fear-exploiter** — it names the fear vividly but offers no credible way out, then pushes the
sale, which raises the reader's distrust instead of lowering it. Verification proves the
sequence is neither: that **every email names a real fear, resolves it with a verified answer,
and offers help before any ask.** A sequence that misses any of the three is not nurture — it
is noise or pressure.

---

## Gate set A — per-email integrity (run on each of the 7)

| Gate | Passes when |
|------|-------------|
| A1 · A real, named fear opens it | The opening uses a real, attributable customer fear (a community quote or verbatim enquiry), not an invented emotion. One fear only. *(P-04, P-05)* |
| A2 · The fear is resolved with a verified answer | The body cites ≥1 Source Bank C-ID, or states an official source's *absence* honestly and anchors that hedge to a verified C-ID in the same email. No floating claim. *(M-01, M-20)* |
| A3 · It ends help-first | The CTA offers a useful thing before asking; one primary CTA only; no manufactured urgency. *(P-19, P-21)* |
| A4 · It sits in the right place in the arc | Fear depth and stage match the AIM arc — deepest fear early, booking ask only at the end. *(F-23, M-32)* |

A1 catches the brochure (no real fear); A2 catches both the brochure (no proof) and the
fear-exploiter (fear with no credible answer); A3 catches the sales-push failure.

---

## Gate set B — the threshold check

The sequence clears the README's three-part Functional Quality Threshold, counted across all 7:

1. **Named fear in real customer language** (Column K category) — **7/7**.
2. **≥1 verified Source Bank C-ID** (hedges anchored) — **7/7**.
3. **Help-first CTA, no sales push** — **7/7**.

Any email failing any gate = the sequence is not done.

---

## The independent re-check (the core check)

A second person (a sub-agent or a different human) verifies **blind to the builder's notes**,
reading the emails themselves:

- **Confirm each opening fear is real and attributable** — can the quote be traced to a real
  community source / enquiry, or was an emotion invented? An invented fear fails A1.
- **Re-trace every factual claim to a C-ID or an honest hedge** — open the Source Bank table and
  check each citation resolves; a claim with no citation and no hedge is a floating claim (A2
  fail). A hedge that isn't anchored to a verified C-ID in the same email also fails A2.
- **Read each CTA cold** — does it offer help before asking, or is it a quote-grab / a fake
  countdown? A sales push fails A3.

This is the gate that cannot be faked by polish: a confident, well-written email that names no
real fear, or cites nothing, or pushes the sale, fails regardless of how good it sounds.

---

## The audit sub-agent — verifying the verifier

After the sequence is built, a sub-agent independently re-scores all 7 emails on A1–A4 and
re-counts the three-gate threshold from the emails themselves. *(Library: P-07 Independent
Verification.)*

Pass threshold: **7/7** on each of the three gates, every fear real and attributable, every
factual claim cited or honestly hedged, every CTA help-first. A single brochure email (no real
fear), a single floating claim, or a single sales-push CTA is a **hard fail** for that email —
fix it and re-audit; a high score elsewhere does not rescue it.

---

## Worked check (the proof-niche sequence)

A blind re-checker: A1 — confirms all 7 openings use real attributable fears (Muze Gu, 7Ssisi,
IrbisKat, unnnabear, and the documented summer/trust fears) ✔; A2 — re-traces every figure to
C-019 / C-003 / C-010 / C-015, and confirms the titer-price and embargo hedges are honest and
anchored (C-001; C-010) ✔; A3 — reads all 7 CTAs and confirms each offers help first with one
CTA and no fake countdown (Email 7's booking ask is explicitly "when you're ready") ✔; A4 —
confirms the deepest fear opens (Email 1) and the booking ask closes (Email 7) ✔. Result: 7/7
on all three gates → **passes**.

---

## What downgrades / forces a rewrite

- An email opening with an invented emotion instead of a real, attributable fear (the brochure).
- A factual claim with no C-ID and no honest hedge (a floating claim).
- A hedge not anchored to a verified C-ID in the same email.
- A CTA that asks for the sale before offering help, a second CTA, or a manufactured countdown.
- Two fears stacked in one email, or the booking ask placed too early in the arc.

---

## Output of the verification phase

All 7 emails name a real fear, resolve it with a cited verified answer (or an anchored honest
hedge), and end help-first; an independent re-check reproduces 7/7 on the three gates from the
emails themselves. That verified discipline is what makes File 04's automation safe — the engine
sends on a cadence and personalises tokens, but it only ever sends copy a human wrote and an
independent re-check confirmed meets every gate.
