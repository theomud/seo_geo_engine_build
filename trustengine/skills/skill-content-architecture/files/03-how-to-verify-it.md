---
Status: draft — built 2026-05-30
Area: skill-content-architecture
Depends on: skill-content-architecture/files/02-how-to-do-it-manually.md
Feeds into: skill-content-architecture/files/04-automation-spec.md
---

# Skill · File 03 — How To Verify It
## The gates that prove the structure: ≤3 clicks, zero orphans, one URL rule, one page per intent

---

## Why verification matters

Architecture fails quietly. Nothing breaks the day a page is buried at click 5 or
shipped with no inbound link — it just never ranks and never converts, and by the time
the traffic data shows it, forty pages are live and the fix is a migration. This skill's
gates are unusually **objective** (click depth, orphan count, URL pattern are countable,
not matters of taste), which is the point: the structure is proven by measurement before
it calcifies, not diagnosed after. Verification counts the three gates across **every**
page — one failing page fails the architecture.

---

## Gate set A — structural integrity (per page)

| Gate | Passes when |
|------|-------------|
| A1 · Reachable in ≤3 clicks | The page's shortest path from the homepage is **≤3 clicks**, shown in the click-depth table. A page at 4+ fails. *(F-33)* |
| A2 · Not an orphan | The page has **≥1 inbound internal link** from another page, named in the table. Zero inbound = fail. *(P-37)* |
| A3 · URL conforms to the rule | The page's URL matches the documented pattern for its page type **exactly** — lowercase, hyphenated, no IDs/query strings. *(P-36)* |
| A4 · One intent only | No other page targets the same query. A second page on the same intent fails both (merge them). *(P-23)* |

A1–A3 are countable and should be automated (File 04). A4 is the human gate — only a
person reading the inventory catches two pages quietly chasing the same search.

---

## Gate set B — the threshold check (whole architecture)

The architecture clears the README's three-part Functional Quality Threshold, measured
across all 40+ pages:

1. **3-click reachability** — **100%** of pages ≤3 clicks (not "most").
2. **Zero orphans** — orphan count is **exactly 0**.
3. **URL consistency** — **100%** of pages conform to their page-type rule, no exceptions.

Any gate under 100% = the architecture is not done. There is no "95% consistent" — one
exception breaks the rule.

---

## The independent re-check (the core check)

A second person (a sub-agent or different human) re-derives the three gates **from the
sitemap itself**, blind to the builder's proof table — they re-trace each page's click
depth from the homepage, re-scan for inbound links, and re-test each URL against the
rule. Then compare:

- **The counts must match.** Builder's click-depth table, orphan count, and consistency
  figure must reproduce. A discrepancy means the builder's table is wrong → fix the
  table or the structure, don't accept the optimistic number.
- **Cannibalisation pass.** The re-checker independently looks for two pages on one
  intent — the gate a click-count can't catch.

---

## The audit sub-agent — verifying the verifier

After the architecture is built, a sub-agent independently re-derives all three gates
across the full sitemap (this skill audits **100%**, not a 20% sample — the gates are
cheap to count and one bad page fails the whole). *(Library: P-07 Independent
Verification.)*

Pass threshold: the sub-agent's independent counts must confirm **100% ≤3 clicks, 0
orphans, 100% URL consistency**, and **no two pages on one intent**. Any miss → fix and
re-derive before the architecture is called done.

---

## Worked check (the airport-comparison page)

A blind re-checker re-traces from the homepage: Home → Routes → the page = **2 clicks ✔
(A1)**; scans inbound links and finds the Routes hub + the summer-embargo sibling →
**not an orphan ✔ (A2)**; tests `/routes/sharjah-vs-dubai-vs-abu-dhabi` against the
spoke rule `/<hub>/<slug>` → **conforms ✔ (A3)**; checks no other page targets the same
airport-comparison intent → **one page ✔ (A4)**. If the re-checker found the page also
existed at `/airports/comparison`, that's a real A4 fail → merge to one canonical URL,
don't ship both.

---

## What downgrades / forces a restructure

- Any page reachable only in 4+ clicks from the homepage.
- Any page with zero inbound internal links (an orphan).
- Any URL that breaks the documented page-type pattern — even one.
- Two pages targeting the same intent (cannibalisation).
- A builder proof table whose counts don't reproduce on an independent re-derive.

---

## Output of the verification phase

Every page passes A1–A4; the whole-architecture threshold is met at 100% / 0 / 100%; an
independent re-derive reproduces the counts and finds no cannibalisation. That verified
structure is what makes File 04's automation trustworthy — the engine counts click depth
and orphans against the documented sitemap, but the architecture is trusted because the
design judgements (hubs, URL rule, one-page-per-intent) were verified by a human first.
