# Content Structure for Trust — Engine

Is the page built around the visitor's fear, in the 5 layers that convert?

## Run
```
python skill-engines/content-structure/engine.py --url https://site.com --report out.html
python skill-engines/content-structure/engine.py --serve 8093    # web checker
python skill-engines/content-structure/engine.py --docs              # cheatsheet + learner manual
python skill-engines/content-structure/engine.py --history           # a site's progress over time
python skill-engines/content-structure/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
