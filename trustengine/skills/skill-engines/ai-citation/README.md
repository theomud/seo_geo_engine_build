# AI Citation Readiness — Engine

How likely AI answer engines are to quote this page — and exactly what to fix.

## Run
```
python skill-engines/ai-citation/engine.py --url https://site.com --report out.html
python skill-engines/ai-citation/engine.py --serve 8090    # web checker
python skill-engines/ai-citation/engine.py --docs              # cheatsheet + learner manual
python skill-engines/ai-citation/engine.py --history           # a site's progress over time
python skill-engines/ai-citation/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
