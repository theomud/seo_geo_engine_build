# Trust Gap Analysis — Engine

The 10 trust signals that decide whether a worried visitor believes you enough to act.

## Run
```
python skill-engines/trust-gap/engine.py --url https://site.com --report out.html
python skill-engines/trust-gap/engine.py --serve 8091    # web checker
python skill-engines/trust-gap/engine.py --docs              # cheatsheet + learner manual
python skill-engines/trust-gap/engine.py --history           # a site's progress over time
python skill-engines/trust-gap/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
