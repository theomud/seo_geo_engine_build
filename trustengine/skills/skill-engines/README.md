# SKILL ENGINES

Each skill is its **own standalone engine** — not an agent, not "a skill". One engine
per job, each started and run separately. Every engine obeys `/DEPARTMENT.md` and
`/department/` (charter, core principles, good-to-great, architecture decision).

## What an engine is
```
skill-engines/<skill>/
  engine.py          — the runner (CHECKER mode: --url / --serve ; on the protected core)
  START.md           — identity + how to run
  01-GOVERNANCE.md   — what governs it (charter, evidence tiers, honesty limits)
  02-CHECKER.md      — how it scores (the checks) — CHECKER mode
  03-REAL-SKILL.md   — how it does the real skill — DOER mode
```
`_core.py` is the shared thin runner; the protected low-level core (fetch · render ·
parse · score) lives in `seo-geo-audit-tool/` and is never forked (principle #8).

## Run any engine
```
python skill-engines/<skill>/engine.py --url https://site.com [--report out.html] [--json out.json]
python skill-engines/<skill>/engine.py --serve <port>     # web checker
```

## Engine roster
| Engine | Folder | Port |
|---|---|---|
| AI Citation | `skill-engines/ai-citation/` | 8090 |
| Trust Gap | `skill-engines/trust-gap/` | 8091 |
| Editorial Quality | `skill-engines/editorial/` | 8092 |
| Content Structure | `skill-engines/content-structure/` | 8093 |
| Visual Evidence | ⏳ to build | 8094 |
| Content Architecture | ⏳ | 8095 |
| Conversion Copy | ⏳ | 8096 |
| Authority Assets | ⏳ | 8097 |
| Official Source Research | ⏳ | 8098 |
| Customer Fear Intelligence | ⏳ | 8099 |
| Prompt Engineering | ⏳ | 8100 |
| Email Nurture | ⏳ | 8101 |
| Content Monitoring | ⏳ | 8102 |
| **SEO Engine** (audit split) | ⏳ separate engine | 8110 |
| **GEO Engine** (audit split) | ⏳ separate engine | 8111 |

Built one at a time. New engine = a measure module on the shared core + a folder here
(engine.py + START + 3 docs). No agents.
