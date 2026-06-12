---
Status: draft — built 2026-05-30
Area: skill-content-architecture
Depends on: skill-content-architecture/files/02-how-to-do-it-manually.md, skill-content-architecture/files/03-how-to-verify-it.md
Feeds into: skill-content-architecture/engines/engine-content-architecture.md
---

# Skill · File 04 — Automation Spec
## What the architecture engine validates, and what stays human

---

## Automation target

**~30% of the work can be automated** — low, because the architecture is a design
judgement (which pages exist, what the hubs are, how the URL rule reads) and that is
human. But the **three structural gates are graph problems** and validate perfectly:
click depth is a breadth-first search from the homepage, an orphan is a node with no
inbound edge, and URL consistency is a regex per page type. The engine **validates and
flags**; it never designs the sitemap. *(Library: M-34 PageRank Flow / link graph;
F-33 3-Click Rule; P-37 No Orphans.)*

What gets automated:
- **Compute click depth** — BFS from the homepage over the internal-link graph; flag any
  page at depth ≥4.
- **Detect orphans** — any page with zero inbound internal links.
- **Check URL consistency** — each page's URL tested against the regex for its page type;
  flag any non-conformer.
- **Emit the proof table** — per page: click depth, inbound-link count, URL pass/fail.

What stays manual (the 70%):
- **Designing the sitemap** — which pages exist, the hubs, the spoke groupings.
- **Writing the URL rule** — the patterns themselves (the engine checks conformance,
  not whether the rule is good).
- **One-page-per-intent (A4)** — detecting two pages quietly chasing the same query
  needs semantic judgement, not a graph.
- **The three conversion paths** — a design and persuasion decision.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| The sitemap as structured data | table/CSV/JSON: `url, page_type, intent, links_to[]` | the architecture document |
| The URL rules (regex per page type) | table | the architecture document |
| Homepage node | the root | the sitemap |

The engine reads the **documented sitemap**, not a live crawl — it validates the
blueprint before the site is built.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Click-depth table (BFS result per page) | build report |
| Orphan list (pages with 0 inbound links) | build report |
| URL non-conformers (page + expected pattern) | build report |
| The three-gate summary (% ≤3 clicks, orphan count, % URL-consistent) | `data/` |

The engine never designs or repairs — it reports the three gates; the human restructures.

---

## Engine flow

```
load sitemap: nodes = pages {url, type, intent, links_to[]}
1. build inbound map: for each page, who links to it
2. CLICK DEPTH: BFS from homepage over links_to
   -> depth[page]; flag any depth >= 4
3. ORPHANS: any page with inbound count == 0 -> flag
4. URL CHECK: for each page, test url against URL_RULES[page_type]
   -> flag non-conformers
5. emit proof table + the 3-gate summary (% <=3 clicks, orphan count, % consistent)
   -> hand to human for A4 (one-page-per-intent) + any restructure
```

---

## The validation core (deterministic)

```python
from collections import deque
def validate(pages, url_rules, home="/"):
    links = {p["url"]: p["links_to"] for p in pages}
    inbound = {p["url"]: 0 for p in pages}
    for p in pages:
        for t in p["links_to"]:
            if t in inbound: inbound[t] += 1
    # BFS click depth from home
    depth = {home: 0}; q = deque([home])
    while q:
        u = q.popleft()
        for v in links.get(u, []):
            if v not in depth:
                depth[v] = depth[u] + 1; q.append(v)
    import re
    report = []
    for p in pages:
        u = p["url"]
        report.append({
            "url": u,
            "depth": depth.get(u, None),          # None = unreachable (worse than orphan)
            "deep": depth.get(u, 99) >= 4,
            "orphan": inbound[u] == 0 and u != home,
            "url_ok": bool(re.fullmatch(url_rules[p["page_type"]], u)),
        })
    return report
```

Unreachable (`depth == None`) is flagged distinctly — a page no path reaches is worse
than a deep page.

---

## Worked example (the documented Dubai sitemap)

Fed the 40+ page sitemap, the engine should return: every fear-resolution spoke at
depth 2, every detail spoke at depth ≤3, **zero** pages at depth ≥4, **zero** orphans,
and **100%** URL conformance to `/<hub>/<slug>`. If a country page were linked only from
another country page (not its hub), BFS would still reach it but it might sit at depth 4
→ flagged → the human links it from the Routes hub to pull it to depth 2.

---

## Test phase (the documented architecture, then PAUSE)

The engine validates the full documented sitemap and stops. The human checks: does the
BFS depth match the hand-drawn click-depth table? Did it catch every orphan? Did the URL
regex flag the right non-conformers? Then the human runs the A4 cannibalisation pass the
engine can't. If the engine's counts disagree with the manual table, reconcile before
the architecture is called done.

---

## Audit (after a build)

A sub-agent re-runs the validator on the full sitemap (100% — the gates are cheap) and
compares to the manual proof table. Pass threshold: the engine confirms **100% ≤3
clicks, 0 orphans, 100% URL consistency**, with **zero unreachable pages**, and the
human-run A4 pass finds no cannibalisation. Any miss → restructure and re-validate.
*(Library: P-07 Independent Verification.)*

---

## When automation must hand back to humans

- **Designing the sitemap, hubs, and URL rule** — always human.
- **One-page-per-intent (A4)** — semantic, not graph; human.
- **The three conversion paths** — design decision.
- **Any restructure** — the engine flags a deep/orphan/non-conforming page; the human
  moves it.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| Validation runtime | milliseconds (graph over ~40 nodes, local) |
| Cost | ≈ $0 (pure Python, no API) |
| Sitemaps validated per minute | hundreds |

---

## Files in this skill (created by the build)

```
skill-content-architecture/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   └── dubai-site-architecture.md       ← the 40+ page architecture + proof table (real output)
└── engines/
    └── engine-content-architecture.md
```
