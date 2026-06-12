# Authority Asset Creation — Engine

Could only someone who did the real work have written this — or could any AI have?

## Run
```
python skill-engines/authority-assets/engine.py --url https://site.com --report out.html
python skill-engines/authority-assets/engine.py --serve 8096    # web checker
python skill-engines/authority-assets/engine.py --docs              # cheatsheet + learner manual
python skill-engines/authority-assets/engine.py --history           # a site's progress over time
python skill-engines/authority-assets/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
