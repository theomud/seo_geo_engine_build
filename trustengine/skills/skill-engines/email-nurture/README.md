# Email Nurture (capture readiness) — Engine

Can the page even start a nurture relationship — capture the lead with a value-first offer?

## Run
```
python skill-engines/email-nurture/engine.py --url https://site.com --report out.html
python skill-engines/email-nurture/engine.py --serve 8101    # web checker
python skill-engines/email-nurture/engine.py --docs              # cheatsheet + learner manual
python skill-engines/email-nurture/engine.py --history           # a site's progress over time
python skill-engines/email-nurture/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
