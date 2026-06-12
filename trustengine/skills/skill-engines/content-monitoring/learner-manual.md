# Content Monitoring (freshness) — Learner Manual

Every page is true the day it's published and decaying after. The monitoring SYSTEM (watching 12 streams, RICE-scoring changes) is off-page — but its result shows on the page as visible freshness. This engine scores those freshness signals; the monitoring cadence and drift detection are shown as Not Measurable.

## How to run the engine
- Score a page: `python skill-engines/content-monitoring/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/content-monitoring/engine.py --serve 8102`
- These docs: `python skill-engines/content-monitoring/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Visible date

**How we measure it:** We look for a published/updated date (text or schema).

**Why it works:** A visible recent date tells readers and engines the fact is current.

**What to do:** Add a visible 'last updated' date (and dateModified schema).

## Example (what NOT to do -> what to do)
- DON'T: (no date)
- DO: Last updated: June 2026.

## 2. Recent-year reference

**How we measure it:** We check for a recent year (≥2025).

**Why it works:** On volatile topics, recency is a ranking and trust signal.

**What to do:** Refresh facts and reference the current year.

## Example (what NOT to do -> what to do)
- DON'T: facts cite 2021
- DO: rules current for 2026.

## 3. Review / verification marker

**How we measure it:** We look for 'reviewed/verified/current as of'.

**Why it works:** Showing the page is actively checked is what builds trust in YMYL topics.

**What to do:** Add 'reviewed/verified [date]' to show active checking.

## Example (what NOT to do -> what to do)
- DON'T: (none)
- DO: Verified against MOCCAE, reviewed monthly.

## 4. Tracks changes

**How we measure it:** We look for changelog / 'what's new' / rule-change language.

**Why it works:** Surfacing updates proves the content is monitored, not abandoned.

**What to do:** Note recent rule changes / a short what's-new line.

## Example (what NOT to do -> what to do)
- DON'T: (none)
- DO: 2026 update: summer embargo dates changed.

## Monitoring cadence (12 streams) (human-judged)

Off-page — whether you watch regulators/airlines/competitors isn't on the page.

## RICE prioritisation of changes (human-judged)

Off-page — the scoring/queue lives in the monitoring system.

## 90-day re-verification (human-judged)

Off-page — the re-check schedule isn't observable here.
