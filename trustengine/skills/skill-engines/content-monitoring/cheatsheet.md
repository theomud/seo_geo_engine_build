# Content Monitoring (freshness) — Cheatsheet

*Does the page show it's kept current — visible dates, recent facts, review markers?*

| # | Measurement | What to do | Example (don't &rarr; do) |
|---|---|---|---|
| 1 | Visible date | Add a visible 'last updated' date (and dateModified schema). | DON'T: (no date) &rarr; DO: Last updated: June 2026. |
| 2 | Recent-year reference | Refresh facts and reference the current year. | DON'T: facts cite 2021 &rarr; DO: rules current for 2026. |
| 3 | Review / verification marker | Add 'reviewed/verified [date]' to show active checking. | DON'T: (none) &rarr; DO: Verified against MOCCAE, reviewed monthly. |
| 4 | Tracks changes | Note recent rule changes / a short what's-new line. | DON'T: (none) &rarr; DO: 2026 update: summer embargo dates changed. |
| – | Monitoring cadence (12 streams) (human-judged) | reviewed by a person | — |
| – | RICE prioritisation of changes (human-judged) | reviewed by a person | — |
| – | 90-day re-verification (human-judged) | reviewed by a person | — |

**Run:** `python skill-engines/content-monitoring/engine.py --url <URL>` or `--serve 8102` (web checker).
