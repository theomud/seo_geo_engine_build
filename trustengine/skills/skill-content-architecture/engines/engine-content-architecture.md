# Engine — Content Architecture
## Spec for the architecture validator (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. It **validates and
flags**; it never designs the sitemap (the ~30% automation ceiling — the design is human).
It reads the **documented sitemap** (the blueprint), not a live crawl, so the structure is
proven before the site is built.

## What it does (per build)
1. **Compute click depth** — breadth-first search from the homepage over the internal-link
   graph; flag any page at depth ≥4, and any unreachable page (worse than deep).
2. **Detect orphans** — any page with zero inbound internal links.
3. **Check URL consistency** — test each page's URL against the regex for its page type; flag
   non-conformers.
4. **Emit the proof table + the 3-gate summary** (% ≤3 clicks, orphan count, % URL-consistent)
   and hand to a human for the A4 one-page-per-intent (cannibalisation) pass.

## The validation core (deterministic)
```python
from collections import deque
import re
def validate(pages, url_rules, home="/"):
    links={p["url"]:p["links_to"] for p in pages}
    inbound={p["url"]:0 for p in pages}
    for p in pages:
        for t in p["links_to"]:
            if t in inbound and t!=p["url"]: inbound[t]+=1
    depth={home:0}; q=deque([home])
    while q:
        u=q.popleft()
        for v in links.get(u,[]):
            if v not in depth: depth[v]=depth[u]+1; q.append(v)
    return [{"url":p["url"],"depth":depth.get(p["url"]),
             "orphan":inbound[p["url"]]==0 and p["url"]!=home,
             "url_ok":bool(re.fullmatch(url_rules[p["page_type"]],p["url"]))} for p in pages]
```
`depth == None` = unreachable (no path from home) and is flagged distinctly.

## Inputs / outputs / guardrails
- **Inputs:** the documented sitemap as structured data (`url, page_type, intent, links_to[]`),
  the URL rules (regex per page type), the homepage node, `PROJECT_ROOT`.
- **Outputs:** the click-depth table, the orphan list, the URL non-conformer list, and the
  3-gate summary (% ≤3 clicks, orphan count, % URL-consistent).
- **Never** designs or repairs the sitemap; **never** judges one-page-per-intent (semantic —
  human). It reports the three gates; the human restructures.
- **Hand back to human:** designing the sitemap/hubs/URL rule; the A4 cannibalisation pass;
  the three conversion paths; any restructure of a flagged page.
- **Audit:** re-run on 100% of the sitemap (the gates are cheap); confirm 100% ≤3 clicks, 0
  orphans, 100% URL consistency, 0 unreachable, and a human cannibalisation pass with 0 dupes.

## Status
**Spec complete; the validator was run live on the documented Dubai sitemap (the proof).**
`data/dubai-site-architecture.md` records the 43-page architecture and the engine's actual
output: 100% ≤3 clicks, 0 orphans, 0 unreachable, 100% URL-consistent, 0 duplicate intents —
RESULT: PASS. The engine validates; the architecture design stays human.

## Library codes
M-35 Hub-and-Spoke/Silo · M-34 PageRank Flow · M-11 Content Depth · M-08 Nine-Page-Type ·
M-32 Hierarchy of Effects · F-16 Content Architecture Hierarchy · F-33 3-Click-Depth Rule ·
F-24 Conversion-Query Cluster · P-37 No Orphans · P-23 One Page per Intent · P-36 Anchor-Text
Diversity · P-07 Independent Verification. Full citations in `MFP-LIBRARY.md`.
