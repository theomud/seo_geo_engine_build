# Prompt Engineering (output clarity) — Engine

Does the page read like a clear, well-briefed output — structured, specific, machine-readable?

## Run
```
python skill-engines/prompt-engineering/engine.py --url https://site.com --report out.html
python skill-engines/prompt-engineering/engine.py --serve 8100    # web checker
python skill-engines/prompt-engineering/engine.py --docs              # cheatsheet + learner manual
python skill-engines/prompt-engineering/engine.py --history           # a site's progress over time
python skill-engines/prompt-engineering/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
