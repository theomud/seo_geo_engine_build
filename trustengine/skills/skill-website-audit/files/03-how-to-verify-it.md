---
Status: complete (PROVEN 47/47) — 2026-06-01
Area: skill-website-audit
Depends on: skill-website-audit/files/02-how-to-do-it-manually.md
Feeds into: skill-website-audit/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that prove an audit is evidence-backed, defensible, prioritised, and client-ready

---

## Why verification matters

An audit fails in the way that is hardest to catch: it *looks* authoritative. A report can be long,
confidently scored, and full of dimension tables — yet assign every /10 from vibe instead of evidence,
quote nothing from the actual site, score a maximum-risk site against a low-risk bar, bury the real
problem under cosmetic ones, or end in a list of observations no owner can act on. A wrong audit is
worse than none, because the client *acts* on it — builds the wrong page, fixes the wrong thing.
Verification proves the four things that make an audit trustworthy: **every score is backed by evidence
quoted from the live site, the scores are defensible and reproducible, the gaps are prioritised by
consequence, and the report is client-ready.**

---

## Gate set A — per-dimension integrity (run on each of the 13 dimensions)

| Gate | Passes when |
|------|-------------|
| A1 · Scored | The dimension has an explicit /10 (no blanks, no "N/A" on an applicable dimension). |
| A2 · Evidenced | The score cites **at least one piece of evidence quoted from the live site** — an opening line, a CTA, a claim, a screenshot. No quote = fail. *(P-03, P-07)* |
| A3 · Calibrated | The score is assigned against the site's **risk-calibrated** proof bar (M-04) — a max-risk site is held to "official source for every claim." |
| A4 · Defensible | A second reader, seeing only the quoted evidence, would land within ±1 of the score. No unjustifiable outliers. |

A1 catches the skipped dimension; A2 catches the vibe score; A3 catches the miscalibrated bar; A4
catches the score the evidence doesn't support.

---

## Gate set B — the threshold check (the README's Functional Quality Threshold)

The report clears all four Check-46 gates:

1. **All 13 dimensions scored with specific site-quoted evidence** — 13/13.
2. **Every identified gap RICE-scored** — each action carries an explicit `(R × I × C) ÷ E` and a rank.
3. **At least one content brief generated, ready to execute** — a complete 9-element prompt for the
   top gap, Inputs filled with real audit data.
4. **The report passes the client-ready test** — a business owner could act on the executive summary
   unaided.

Any gate unmet = the audit is not done. A missing dimension, an unevidenced score, an un-RICE'd gap,
a brief with placeholder Inputs, or a jargon-only summary each fail the threshold on their own.

---

## The independent re-check (the core check)

A second party (a sub-agent or a different human) re-verifies **blind to the auditor's scores**:

- **Re-open the live site** and confirm each quoted piece of evidence actually appears on the page —
  a quote that isn't on the site is fabricated evidence (A2 fail) and voids that dimension.
- **Re-score 3–4 dimensions from the evidence alone** and check they land within ±1 of the report's
  scores (A4). A systematic gap means the scoring is biased, not evidenced.
- **Re-compute every RICE value** from its R/I/C/E and confirm the ranking order follows.
- **Read only the executive summary** and ask: could a business owner act on this? If it needs the
  framework explained, the client-ready gate fails.

This is the gate polish can't fake: the evidence is either on the live site or it isn't, and the
arithmetic either reproduces or it doesn't.

---

## The audit sub-agent — verifying the verifier

After the audit, a sub-agent re-runs A1–A4 on all 13 dimensions, re-checks the quoted evidence against
the live site, re-computes the RICE ranking, and applies the client-ready test. *(Library: P-07
Independent Verification.)* Pass threshold: **13/13 evidenced**, scores reproducible within ±1, all
gaps RICE-scored, brief runnable, summary client-ready. A fabricated quote, an unscored dimension, a
miscalibrated proof bar, or a jargon-only summary is a **hard fail** regardless of the rest.

---

## Worked check (the DKC audit)

A blind re-checker: A2 — re-opens dkc.ae and confirms the report's quoted homepage opening line is
actually there (and that the confiscation fear genuinely is *not*) ✔; A3 — confirms the audit applied
the maximum-risk bar to DKC's permit/fee claims ✔; A4 — re-scores D1, D3, D9 from the quotes and lands
within ±1 ✔; RICE — re-computes the confiscation-page action and confirms it tops the queue ✔;
client-ready — reads the exec summary and confirms a DKC owner could act on "you never address the
deepest fear in your market; build this page" ✔. Result: threshold **passes**; the live citation of
DKC's own words is the proof the scores aren't invented.

---

## The post-delivery check (the independence flag)

The gates above are everything the auditor controls. The outcome the audit is *for* — a client acting
on it and the fix moving the metric — can only be confirmed **after delivery**: the owner builds the
recommended page, and its ranking/citation/conversion is observed. *(Library: F-05 — the action loop
closes outside the report.)* This is the **Check-47 analogue**, flagged **NOT YET TESTED** until a
second party independently runs an audit to threshold (or a client acts on one). The on-page threshold
fully passes before this step.

---

## What downgrades / forces a re-audit

- A dimension score with no quoted evidence from the live site (a vibe score).
- A quote in the report that isn't actually on the site (fabricated evidence).
- A maximum-risk site scored against a low-risk proof bar.
- A gap in the action plan with no RICE value, or a ranking the arithmetic doesn't support.
- A content brief with placeholder Inputs instead of real audit data.
- An executive summary only the framework's author could act on.

---

## Output of the verification phase

All 13 dimensions are scored /10 with site-quoted evidence, calibrated to the risk level, and
reproducible within ±1; every gap is RICE-ranked; the content brief is runnable; the summary is
client-ready; an independent re-check reproduces the result against the live site. That verified
discipline is what makes File 04's automation safe — the engine collects evidence and does the RICE
maths, but it only ever scores against real, quoted, on-site evidence, and the human owns the /10.
