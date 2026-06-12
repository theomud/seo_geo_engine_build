---
Status: draft — built 2026-05-30
Area: skill-visual-evidence-architecture
Depends on: skill-visual-evidence-architecture/files/02-how-to-do-it-manually.md, skill-visual-evidence-architecture/files/03-how-to-verify-it.md
Feeds into: skill-visual-evidence-architecture/engines/engine-visual-evidence-architecture.md
---

# Skill · File 04 — Automation Spec
## What the visual-evidence engine assembles and render-checks, and what stays human

---

## Automation target

**~25% of the work can be automated** — the lowest ceiling of the writing skills,
and deliberately so. The thing that makes a screenshot proof — a **real date stamp
captured from the live official source** — is destroyed the moment a bot fetches it
(no human-verifiable date, easily a cached copy). So **capture is always manual**.
The engine only assembles the brief into a layout, generates the data infographics
from already-sourced figures, and **render-checks at 390px**. *(Library: P-06
Screenshots Are Proof; F-08 Proof Interstitial.)*

What gets automated:
- **Generate the data infographics** — build the summer-embargo calendar and
  airport-comparison table HTML from a sourced-figures table (each figure already
  carrying a C-ID or HEDGE).
- **Render-check at 390px** — load each infographic at a 390px viewport and assert
  `scrollWidth == clientWidth` (no horizontal scroll); fail the build otherwise.
- **Flag claims with no visual** — any page claim marked "needs proof" with no visual
  in the brief.
- **Flag screenshots missing metadata** — any brief entry of type screenshot lacking
  a capture date, source URL, or C-ID.
- **Lay out proof beside claim** — place each screenshot/caption adjacent to its claim
  per the interstitial pattern.

What stays manual (the 75%):
- **Capturing every official-source screenshot** — by hand, from the live page, with
  the date visible. The engine never fetches a regulator page and calls it proof.
- **Shooting the real process photos** — the crate, vet check, handover.
- **The proof verdict** — does this visual actually prove the claim (A1–A4)? Human.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| The page's claims (each with C-ID) | list | conversion copy / brief + Source Bank |
| Sourced-figures table for infographics | table | Source Bank (C-ID or HEDGE per figure) |
| Captured screenshots (manual) | image files + metadata | hand-captured from live official sources |
| 390px render-check harness | Playwright | local |

The engine is **forbidden** from fetching an official page itself and treating the
result as a dated screenshot — that is not proof.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Generated infographic HTML (calendar, airport table) | `data/` |
| 390px render-check result per infographic (pass/fail + scrollWidth) | `data/screenshots/` + build log |
| Flagged claims with no visual | build report |
| Flagged screenshots missing date/URL/C-ID | build report |
| Assembled page layout (proof beside claim) | build report |

The engine never declares a visual "proof" — it assembles, render-checks, and flags;
the human owns the proof verdict.

---

## Engine flow per build

```
for each page brief:
    1. for each claim marked "needs proof": if no visual in brief -> FLAG (missing proof)
    2. for each screenshot entry: if missing {date, source_url, c_id} -> FLAG
    3. lay out each screenshot + caption adjacent to its claim (interstitial)
for each infographic (from sourced-figures table):
    4. generate HTML (every figure prints its C-ID or HEDGE inline)
    5. render at 390px viewport -> assert scrollWidth == clientWidth
       -> if horizontal scroll: FAIL the build, save the 390px screenshot as evidence
    6. write the build report + the 390px screenshots
```

---

## The render-check (the automatable core)

```python
# 390px render-check — the one hard, automatable gate
from playwright.sync_api import sync_playwright
def check_390(path):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width":390,"height":844})
        pg.goto("file:///" + path)
        sw = pg.evaluate("document.documentElement.scrollWidth")
        cw = pg.evaluate("document.documentElement.clientWidth")
        pg.screenshot(path=path.replace(".html","-390px.png"), full_page=True)
        b.close()
        return sw <= cw + 1   # True = no horizontal scroll = pass
```

This is the gate that can be made fully deterministic — a build fails automatically if
an infographic breaks at 390px. (It is the same harness used to verify the guides.)

---

## Worked example (the summer-embargo calendar)

Fed a sourced-figures table (embargo windows per airline, each row a C-ID or HEDGE),
the engine generates the calendar HTML with each date labelled by its source, then
render-checks at 390px. If a wide table forces horizontal scroll, the build **fails**
and saves the 390px screenshot showing the overflow — the builder switches the table
to a stacked phone layout and re-runs. The engine never invents an embargo date; it
only lays out figures it was given.

---

## Test phase (the 4 gap pages + 2 infographics, then PAUSE)

The engine assembles the four briefs and builds both infographics, then stops. The
human checks: did it flag every claim missing a visual? Did it flag any screenshot
missing a date/URL/C-ID? Did both infographics pass the 390px render-check? If it
passes an infographic that actually breaks at 390px, fix the harness before scaling.

---

## Audit (after a build)

A sub-agent re-runs the 390px render-check on **20%** (here both infographics) and
re-checks the missing-visual / missing-metadata flags against a manual pass. Pass
threshold: **90%** agreement, with **zero** infographics passed that break at 390px and
**zero** undated screenshots accepted as proof (each a hard fail). *(Library: P-07.)*

---

## When automation must hand back to humans

- **Capturing any official-source screenshot** — always manual, from the live page,
  dated.
- **The real process photography** — always manual.
- **The proof verdict (A1–A4)** — does the visual genuinely prove the claim? Human.
- **Any flagged claim/screenshot** — the engine flags; the human captures/fixes.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| Infographic generation + render-check | seconds per asset (local, no API) |
| Cost | ≈ $0 (Playwright is local; no paid API needed) |
| Assets render-checked per minute | ~30 |

---

## Files in this skill (created by the build)

```
skill-visual-evidence-architecture/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   ├── visual-brief-4-pages.md          ← the 4 page briefs (real output)
│   ├── summer-embargo-calendar.html     ← infographic, 390px-verified
│   ├── airport-comparison-table.html    ← infographic, 390px-verified
│   ├── screenshot-integration-guide.md  ← the capture standard
│   └── screenshots/                     ← 390px render-check evidence
└── engines/
    └── engine-visual-evidence-architecture.md
```
