# Editorial Quality — Engine

Is this page publish-ready, or generic AI mush? The quality gate, automated.

## Run
```
python skill-engines/editorial/engine.py --url https://site.com --report out.html
python skill-engines/editorial/engine.py --serve 8092    # web checker
python skill-engines/editorial/engine.py --docs              # cheatsheet + learner manual
python skill-engines/editorial/engine.py --history           # a site's progress over time
python skill-engines/editorial/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
