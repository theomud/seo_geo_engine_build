---
Status: draft — built 2026-05-29
Area: skill-editorial-judgment
Depends on: skill-editorial-judgment/files/02-how-to-do-it-manually.md
Feeds into: skill-editorial-judgment/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that keep a /50 score honest before a page is allowed to publish

---

## Why verification matters

A quality gate is only as good as the honesty of the score behind it. The failure mode is a **lenient or gamed score** — an editor (human or engine) waving a 41/50 through to hit a deadline, or scoring on vibe with no reason recorded. That ships exactly the AI mush this skill exists to stop. Verification checks two things: that each score is **justified by a specific reason**, and that an **independent re-score lands at the same publish/hold decision**.

---

## Gate set A — score integrity (per scored page)

| Gate | Passes when |
|------|-------------|
| A1 · Every criterion has a written reason | The edit notes give a one-line reason per criterion — no bare numbers. A score with no reasons is not a score. |
| A2 · "True" is cited, not asserted | Criterion 1 scores ≥4 only if every fact cites a Verified row **or** is honestly hedged. An uncited claim caps True at 2. *(M-01)* |
| A3 · "Specific" passes the any-business test | Criterion 2 scores ≥4 only if the page could **not** apply to any other business — real numbers/names/examples. "Competitive pricing" caps Specific at 2. *(P-11)* |
| A4 · The 7 patterns are removed, not just noted | Each weak pattern is physically gone from the draft, not flagged-and-left. |
| A5 · The gate is applied honestly | Publish only at **40+/50 with no criterion below 3**. A 39, or a 41-with-a-2, is a hold — no rounding up. |

A page that fails any A-gate is re-scored or held. A2 and A3 are the anti-leniency gates — they are where a soft score gets caught.

---

## Gate set B — the publishing checklist

The page clears all three blocks (File 02): **Content** (the 10 criteria) · **SEO** (title 50–60 + keyword, meta 150–160, H1 keyword, keyword in first paragraph, internal links) · **Conversion** (clear CTA, correct contact info, visible trust signals, objections addressed). *(Library: F-11 — maps onto NN/g's 53 trust recommendations.)* Any unchecked box = hold.

---

## The independent re-score (the core check)

A second scorer (a sub-agent, or a different human) re-scores the page **blind to the original score** — they see only the page and the 10-criteria rubric. Then compare:

- **Decision agreement is the hard test:** both must reach the same **publish (≥40) / hold (<40)** verdict. A split decision = the page is re-examined, not shipped.
- **Score agreement:** the two /50 totals should be within **±4 points**. A wider gap means the rubric was applied inconsistently — reconcile which criterion they read differently.

---

## The audit sub-agent — verifying the verifier

After a batch of pages is scored, a sub-agent independently re-scores **20%** (minimum 3) blind, per the re-score method above. *(F-31 — who/how/why applied to each criterion.)*

Pass threshold: **90%** of sampled pages match on the publish/hold decision **and** fall within ±4 points. Below 90% → the scoring is miscalibrated (usually leniency on True or Specific); recalibrate against A2/A3 and re-score the batch before any of it publishes.

---

## Worked check (the confiscation page, 47/50)

A blind re-score should land in the high 40s and **agree on PUBLISH**. The live gates: A2 — confirm every fact (C-019/010/003) is actually cited and C-001 is hedged, not asserted; A3 — confirm the specifics (500 AED, Muze Gu quote) are real, not generic. If a re-scorer comes back 39 because they read "Commercial" as a 2, that's a legitimate split → reconcile before publishing, don't average to 43 and ship.

---

## What downgrades / forces a re-score

- A criterion scored with no written reason in the edit notes.
- "True" ≥4 on a page with an uncited claim.
- "Specific" ≥4 on a page with a could-apply-to-anyone sentence.
- A weak pattern flagged but left in the draft.
- A publish decision on 39/50, or on a page with any criterion below 3.
- The independent re-score disagrees on publish/hold.

---

## Output of the verification phase

Every scored page carries a reasoned /50, passes the publishing checklist, and has survived an independent re-score that agrees on the publish/hold decision; the batch audit logs ≥90% agreement. That verified scoring discipline is what makes File 04's automation safe — the engine pre-scores and flags patterns, but the publish gate is only trusted because the scores behind it are reproducible.
