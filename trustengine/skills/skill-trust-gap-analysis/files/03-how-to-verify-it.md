---
Status: draft — built 2026-05-29
Area: skill-trust-gap-analysis
Depends on: skill-trust-gap-analysis/files/02-how-to-do-it-manually.md
Feeds into: skill-trust-gap-analysis/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates a competitor score and a gap matrix must pass before they drive the content build

---

## Why verification matters

The Content Gap Matrix decides what gets built first. A wrong score propagates: mark a competitor's uncited claim as "cited" and you under-rank a gap, and the universal gap that should have been page one never gets built. Verification is how a score becomes defensible in a client or team review — and how the matrix can be trusted to set the build order.

Every competitor score is checked three ways: the **score integrity gates** (was each dimension scored against real evidence?), the **risk-calibration gate** (was the proof threshold applied?), and the **matrix gate** (do the counts and the universal gaps hold up?). A score that fails is re-scored before it enters the matrix.

---

## The score-integrity gates (per competitor page)

Walk every scored page through these — each pass/fail:

| Gate | Passes when |
|------|-------------|
| 1 · Screenshot exists | A dated screenshot of the exact scored page is saved. No screenshot → the score can't be audited → fail. (Library: **P-06 Screenshots Are Proof**.) |
| 2 · Correct URL scored | The page scored is the one targeting the key fear/keyword — not the homepage standing in for it. |
| 3 · Each dimension has evidence | For all 10 dimensions, the point (or zero) is justifiable by a specific element on the page, not a general impression. |
| 4 · Citation dimension is literal | Dimension 2 scores a point only if an actual link to a government/regulatory source is present — not a claim that *sounds* official. (Library: **P-02**, **P-22**.) |
| 5 · Proof-interstitial is literal | Dimension 10 scores only if proof sits beside claims *throughout* — a single testimonials block fails it. |
| 6 · No misrepresentation | The competitor is described accurately; no gap is inflated by understating what the page actually does. |

A page failing any gate is re-scored. Gate 4 is the highest-stakes in a maximum-risk niche — scoring uncited reassurance as "cited" is the failure that most distorts the matrix.

---

## The risk-calibration gate

Confirm Step 0 was done and applied: the niche's Risk Continuum level is recorded, and the proof-dependent dimensions (2 official source, 6 cost honesty, 10 proof interstitial) were scored against **that** threshold. (Library: **M-04 Risk Continuum Model**.) In a maximum-risk niche, a page that reads well but proves nothing should land in the 3–5/10 band — if your top competitors are all scoring 7+, the threshold was applied too loosely; re-calibrate and re-score.

---

## The matrix gate

Before the matrix drives the build:
- **Counts reconcile** — each gap's "competitors missing" count equals the number of scored pages that scored 0 on that dimension.
- **Universal gaps are real** — a gap marked 🔴 (missed by nearly all) is spot-checked against 2–3 of the actual pages to confirm they truly omit it.
- **Benchmark present** — the highest-scoring competitor is identified (Dubai proof: DKC 8/10) so the build target is "beat the benchmark," not "beat the average."

---

## The audit sub-agent — verifying the verifier

After scoring (manual or the File 04 engine), a sub-agent independently re-scores **20%** of competitors (minimum 3), blind to the existing scores — it opens the same URLs, scores the 10 dimensions itself, and compares. (Library: aligns with **F-11 Forty-Five-Check Audit**.)

Pass threshold: **90%** agreement on the dimension-level scores of sampled pages. Below 90% → the scoring standard drifted; re-score the affected set against File 02's rubric before trusting the matrix. (Same audit discipline as Official Source Research and Content Structure.)

---

## What downgrades a score (re-score required)

- No screenshot, or the wrong page was scored.
- A dimension point awarded on impression rather than a specific on-page element.
- Uncited reassurance scored as Dimension 2 "official source cited."
- A testimonials-only page scored as Dimension 10 "proof interstitial."
- The risk threshold not applied (inflated scores in a maximum-risk niche).
- A competitor misrepresented to inflate or hide a gap.

---

## Output of the verification phase

A scored competitor set where every page has a dated screenshot and an evidence-justified 10-dimension score, a recorded risk level applied consistently, an audit sample logged at ≥90% agreement, and a Content Gap Matrix whose counts reconcile and whose universal gaps are spot-checked. That verified matrix is the trustworthy input to the content build and to the File 04 automation run.
