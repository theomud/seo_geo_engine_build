---
Status: draft — built 2026-05-30
Area: skill-authority-assets
Depends on: skill-authority-assets/files/02-how-to-do-it-manually.md
Feeds into: skill-authority-assets/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that prove an asset is documented, un-fakeable, and dense with real proof

---

## Why verification matters

An authority asset has exactly one job an ordinary page doesn't: to be the thing AI and
competitors **cannot** produce. The failure mode is an asset that *looks* authoritative —
long, confident, well-structured — but is actually the generic mush dressed up: no real
failure, claims that float without proof, figures that could be invented. That asset earns
no links and no citations, because there is nothing in it only the person who did the work
could know. Verification proves the two things that make it un-fakeable: **enough real proof
(density)** and **a documented reality an AI prompt can't reproduce (the Hormozi test).**

---

## Gate set A — asset integrity (per asset)

| Gate | Passes when |
|------|-------------|
| A1 · A real failure is documented | The asset contains at least one named failure/surprise from the actual work — not a generic "challenges can arise". *(P-15)* |
| A2 · Every claim carries proof | Each factual statement has a C-ID, a named figure, a dated fact, or an honest hedge. A floating claim fails. *(M-13)* |
| A3 · Proof density ≥1 per 200 words | Counted: verifiable proof items ÷ (words/200) ≥ 1. Under that = too much prose. *(M-13)* |
| A4 · The Hormozi test passes | A basic AI prompt for the same topic **cannot reproduce** the asset's real specifics — confirmed by actually running the prompt. *(P-13)* |

A1 and A4 are the two that catch dressed-up mush: no real failure (A1) or an asset a generic
prompt covers (A4) is not an authority asset, however polished.

---

## Gate set B — the threshold check

The asset clears the README's two-part Functional Quality Threshold:

1. **Proof density** ≥ **1 verifiable item per 200 words** — counted and shown.
2. **The Hormozi test passes** — the generic-AI version is produced and the asset's
   un-reproducible specifics are listed against it.

Either unmet = the asset is not done.

---

## The independent re-check (the core check — run the prompt)

A second person (a sub-agent or different human) verifies **blind to the builder's notes**:

- **Re-count the proof density** from the text itself — the count must reproduce. A builder
  who counted a vague sentence as "proof" gets caught here.
- **Run the Hormozi test for real.** The re-checker takes a basic AI prompt for the same
  topic, generates the generic version, and compares: does the documented asset contain real
  specifics (named failure, dated C-IDs, exact figures) the AI version cannot? If the AI's
  generic output covers everything the asset says, **the asset fails A4** — it is mush. This
  is the gate that cannot be faked: the AI either can or cannot reproduce it.

---

## The audit sub-agent — verifying the verifier

After the asset is built, a sub-agent independently re-counts proof density and **re-runs the
Hormozi test** (generates the generic version, lists what the documented asset has that it
lacks). *(Library: P-07 Independent Verification.)*

Pass threshold: proof density confirmed **≥1 per 200 words**, **a real failure present**, and
the Hormozi test **passes** (the sub-agent's generic AI version demonstrably cannot reproduce
the asset's documented specifics). A missing failure or an asset a generic prompt covers is a
**hard fail** — no density score rescues it.

---

## Worked check (the airport-confiscation case)

A blind re-checker: A1 — confirms the documented failure (the lab turnaround that didn't match
reality; re-test with one day to spare) is real and specific, not generic ✔; A2 — confirms
each claim carries a C-ID (C-019, C-003, C-010) or an honest hedge ✔; A3 — re-counts: 4
citations + 1 documented failure across ~900 words = ≥1 per 200 ✔; A4 — **runs** "write a case
study about a pet held at Dubai airport", gets "ensure documentation is in order", and lists
what it can't produce (the C-IDs, the turnaround surprise, the one-day-to-spare outcome) →
**passes**. If the re-checker's generic AI output had matched the asset, that's a real A4 fail
→ add un-fakeable detail, don't ship.

---

## What downgrades / forces a rewrite

- No real failure/surprise documented (a hypothetical dressed as a case).
- A factual claim with no C-ID, figure, or honest hedge (a floating claim).
- Proof density under 1 item per 200 words (too much prose).
- A basic AI prompt reproduces the asset's substance (the Hormozi test fails).
- A "proof" item that turns out to be a vague sentence, not a verifiable specific.

---

## Output of the verification phase

The asset has a documented real failure, a C-ID beside every claim, proof density ≥1 per 200
words, and a passing Hormozi test confirmed by actually running the generic prompt; an
independent re-check reproduces the count and the test result. That verified discipline is
what makes File 04's automation safe — the engine can count density, but the authority is
trusted because the un-fakeable real detail was verified by a human running the AI against it.
