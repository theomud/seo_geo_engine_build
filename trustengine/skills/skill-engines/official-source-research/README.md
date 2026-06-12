# Official Source Research — Engine

Is every claim traced to a named, dated, official source — or just asserted?

## Run
```
python skill-engines/official-source-research/engine.py --url https://site.com --report out.html
python skill-engines/official-source-research/engine.py --serve 8098    # web checker
python skill-engines/official-source-research/engine.py --docs              # cheatsheet + learner manual
python skill-engines/official-source-research/engine.py --history           # a site's progress over time
python skill-engines/official-source-research/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
