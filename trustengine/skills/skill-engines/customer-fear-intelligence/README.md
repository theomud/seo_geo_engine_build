# Customer Fear Intelligence — Engine

Does the page speak to the customer's real fears and the questions they actually ask?

## Run
```
python skill-engines/customer-fear-intelligence/engine.py --url https://site.com --report out.html
python skill-engines/customer-fear-intelligence/engine.py --serve 8099    # web checker
python skill-engines/customer-fear-intelligence/engine.py --docs              # cheatsheet + learner manual
python skill-engines/customer-fear-intelligence/engine.py --history           # a site's progress over time
python skill-engines/customer-fear-intelligence/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
