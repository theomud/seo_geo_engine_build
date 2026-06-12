# Visual Evidence Architecture — Engine

Does the page SHOW proof — real photos, dated screenshots, data visuals — beside its claims?

## Run
```
python skill-engines/visual-evidence/engine.py --url https://site.com --report out.html
python skill-engines/visual-evidence/engine.py --serve 8094    # web checker
python skill-engines/visual-evidence/engine.py --docs              # cheatsheet + learner manual
python skill-engines/visual-evidence/engine.py --history           # a site's progress over time
python skill-engines/visual-evidence/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
