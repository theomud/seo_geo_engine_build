# Content Monitoring (freshness) — Engine

Does the page show it's kept current — visible dates, recent facts, review markers?

## Run
```
python skill-engines/content-monitoring/engine.py --url https://site.com --report out.html
python skill-engines/content-monitoring/engine.py --serve 8102    # web checker
python skill-engines/content-monitoring/engine.py --docs              # cheatsheet + learner manual
python skill-engines/content-monitoring/engine.py --history           # a site's progress over time
python skill-engines/content-monitoring/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
