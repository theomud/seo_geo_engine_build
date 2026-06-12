# Conversion Copy — Engine

Does the copy convert a worried reader — fear-acknowledging headline, opening, and a help-first CTA?

## Run
```
python skill-engines/conversion-copy/engine.py --url https://site.com --report out.html
python skill-engines/conversion-copy/engine.py --serve 8095    # web checker
python skill-engines/conversion-copy/engine.py --docs              # cheatsheet + learner manual
python skill-engines/conversion-copy/engine.py --history           # a site's progress over time
python skill-engines/conversion-copy/engine.py --qa                # contract self-audit
```

## Files
- `engine.py` — runner
- `ENGINE.md` — governance + real skill + MFP (that fit)
- `measurements/` — every measurement broken out (what · how · why · what-to-do)
- `cheatsheet.md/.html` · `learner-manual.md/.html`
- `TRACKER.md` + `tracker.csv` — provable score history per site
- `QA.md` + `qa-log.csv` — contract self-audit
- `.env` / `.env.example`
