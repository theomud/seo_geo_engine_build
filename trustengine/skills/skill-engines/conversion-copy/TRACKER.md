# Conversion Copy — Tracker

Every `--url` run is appended to `tracker.csv` so a site's progress is **provable** over time — the money loop: audit → fix → re-audit → show the lift.

## Columns

`timestamp · url · domain · score · grade · word_count · top_fix`

## Use it

```
python engine.py --url https://site.com/page      # scores + auto-appends a row
python engine.py --url https://site.com/page --no-track   # score without logging
python engine.py --history                         # full history + per-URL trend
python engine.py --history https://site.com/page   # one URL's trend (e.g. 41 → 78 ▲+37)
```

The trend line shows first → latest score and the delta, so you can show a client exactly how much a fix moved this skill.
