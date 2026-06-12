---
Status: complete (PROVEN 47/47) — 2026-06-01
Area: skill-website-audit
Depends on: skill-website-audit/files/02-how-to-do-it-manually.md, skill-website-audit/files/03-how-to-verify-it.md
Feeds into: skill-website-audit/engines/engine-website-audit.md
---

# Skill · File 04 — Automation Spec
## What the audit engine collects, checks and computes — and what stays human

---

## Automation target

**~60–70% of the work is automatable (Automation 4/5).** The engine can fetch every page, capture
full-page screenshots, extract the evidence a human needs (opening lines, CTAs, claims, schema,
internal links, freshness dates), run the deterministic structural checks, do the RICE arithmetic, and
assemble the report into the template. What it **must not** do is the act the whole deliverable rests
on: **assign each dimension's /10 and judge client-readiness.** The moment a model scores from its own
impression rather than from quoted on-site evidence, you have a confident report that audits nothing.
So the engine **collects, checks, computes, and assembles — and hands the scoring to a human.**
*(Library: P-03 Proof Over Promise; P-07 Independent Verification; F-11 audit discipline; M-27 RICE.)*

What gets automated:
- **Evidence collection** — fetch the key pages; capture screenshots; extract the homepage/service
  opening lines, headlines, CTA text, every numeric claim, FAQ/Organization schema, the nav/internal
  links, and any visible freshness date.
- **Deterministic checks** — D8 architecture (click-depth, orphan/URL hygiene), D11 schema presence
  (FAQPage/Organization JSON-LD valid?), D2 mechanical points (is a source link present? a
  cost range? a steps list?), D3 claim extraction (pull every number for a human to re-trace to a C-ID).
- **RICE arithmetic + ranking** — given a human's R/I/C/E per gap, compute and sort the action plan.
- **Report assembly** — pour the scored dimensions, evidence, plan, and brief into
  `engines/AUDIT-REPORT-TEMPLATE.md` and write `data/audit-[site]-[date].md`.

What stays manual:
- **Assigning each dimension's /10** — an act of evidenced judgement against the risk-calibrated bar.
- **Calibrating the risk level (M-04)** — a human decides the proof bar before scoring.
- **Re-tracing claims to a verified source (D3)** — the engine extracts the number; a human confirms
  it against an official source / C-ID.
- **Judging the fear/copy dimensions (D1, D6, D9)** — does the copy *acknowledge or exploit* the fear
  (P-04)? does an asset pass the Hormozi test (P-13)? Human.
- **Writing the content brief and the executive summary**, and applying the **client-ready test**.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| The site URL + key page list | list | the client / human |
| The market's fears (Column K) + verified facts (C-IDs) | tables | the customer-profile snapshot |
| The risk level (M-04) | one value | the human, before scoring |
| Per-gap R/I/C/E | numbers | the human, against the rubric |
| Optional API keys | env | `.env` (ANTHROPIC for draft assist, SERPAPI for D11/D13) |

The engine is **forbidden** from inventing a score or a quote — it only surfaces evidence that exists
on the live page; a page it could not fetch is reported "not retrieved," never scored.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Collected evidence pack (quotes + screenshots + extracted claims/schema/links per page) | working notes |
| Deterministic check results (D8/D11/D2-mechanical/D3-claims) | feeds the human's scores |
| RICE-ranked action plan (from human R/I/C/E) | the report |
| Assembled audit report | `data/audit-[site]-[date].md` |

The engine never assigns a /10 and never declares the audit client-ready — it presents evidence and
arithmetic; the human scores and signs off.

---

## Engine flow

```
for each key page of the site:
    fetch page (headless browser) -> full-page screenshot
    extract: opening line, headline, CTA text, numeric claims, FAQ/Org schema, nav + internal links, freshness date
    run deterministic checks: click-depth, URL hygiene, schema validity, mechanical Trust-Score points
present the evidence pack + checks to the HUMAN, grouped by dimension (D1..D13)
human: calibrate risk (M-04) -> assign each dimension /10 WITH a quoted evidence line
human: list gaps -> assign R/I/C/E
engine: RICE = (R*I*C)/E per gap -> sort -> action plan
human: write the content brief (top gap) + the executive summary
engine: assemble into AUDIT-REPORT-TEMPLATE.md -> write data/audit-[site]-[date].md
```

## The deterministic core (what code can decide alone)
```python
def rice(reach, impact, confidence, effort):
    if effort <= 0: raise ValueError("effort must be > 0")
    return round((reach * impact * confidence) / effort, 2)

def click_depth_ok(page, home, max_depth=3): ...   # D8
def schema_present(html): ...                       # D11: valid FAQPage/Organization JSON-LD?
def extract_claims(text): ...                       # D3: pull every numeric claim for human re-trace
# none of these assign a dimension /10 — they feed the human's evidenced score.
```

---

## Worked example (the DKC audit)

Fed dkc.ae, the engine fetches the homepage + relocation-service + about/contact pages, screenshots
each, and extracts DKC's actual opening line, CTA, permit/fee claims, schema, and nav. The human reads
the evidence pack, calibrates **maximum risk**, and scores the 13 dimensions — e.g. D1 low, with the
quoted homepage opening as evidence that the confiscation fear is never named. The human lists the
gaps and sets R/I/C/E; the engine computes RICE and ranks the confiscation page first. The human writes
that page's brief and the exec summary; the engine assembles `data/audit-dkc-2026-06-01.md`. Every
score traces to a DKC quote the engine pulled from the live site.

---

## Test phase (one site, then PAUSE)

Run the engine on one real site (DKC); confirm it fetches and screenshots every key page, extracts the
evidence, runs the deterministic checks, and assembles a report whose every dimension carries a
real on-site quote and whose RICE ranking re-computes. Confirm a page it can't fetch is marked "not
retrieved," not scored. **Then pause for the audit sub-agent.**

---

## Audit (after a build)

A sub-agent re-opens the live site and confirms every quoted piece of evidence appears there, re-scores
3–4 dimensions within ±1, re-computes the RICE ranking, and applies the client-ready test. A
fabricated quote, an unscored dimension, a miscalibrated bar, or a jargon-only summary is a **hard
fail**. *(Library: P-07.)*

---

## When automation must hand back to humans

- **Every dimension /10** — always human; the engine presents evidence, never the score.
- **Risk calibration (M-04)** and **D3 source re-tracing** — human.
- **The fear/copy/authority judgements (D1, D6, D9 — P-04, P-13)** — human.
- **The content brief, the executive summary, and the client-ready sign-off** — human.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| Evidence collection + screenshots (per page) | seconds (headless browser, no paid key) |
| Deterministic checks + RICE arithmetic | milliseconds |
| Optional SERP/AI-Overview checks (D11/D13) | a few SerpApi calls — cents |
| Human cost | the scoring read + the brief + the summary — the irreducible core |

---

## Files in this skill (created by the build)

```
skill-website-audit/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   └── audit-dkc-2026-06-01.md          ← the real 130-point DKC audit (proof)
└── engines/
    ├── engine-website-audit.md          ← the scoring methodology / Claude Code prompt
    └── AUDIT-REPORT-TEMPLATE.md          ← the fixed report structure
```
