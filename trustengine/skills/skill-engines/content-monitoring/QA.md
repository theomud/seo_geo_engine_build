# Content Monitoring (freshness) — QA

`--qa` runs a **contract self-audit**: it proves this engine honours its output contract so a score is never silently malformed. Result is logged to `qa-log.csv`.

## What QA checks (static, no network)

- Metadata present: `SKILL_ID/NAME/TAGLINE/INTRO`
- `measure()` is callable
- Every measurement has a **how**, a **why**, and a matching **action** in `ACTIONS`
- Each not-measurable row is well-formed (honest off-page flags)
- Grade boundaries sane: `_grade(100)=A`, `_grade(0)=F`

## Optional live smoke test

- `score` is an int in 0..100, checks are returned, fixes are sorted by recoverable points

## Use it

```
python engine.py --qa                       # static contract audit (exit 0 = PASS)
python engine.py --qa --live https://site.com/   # also run a live smoke test
```
