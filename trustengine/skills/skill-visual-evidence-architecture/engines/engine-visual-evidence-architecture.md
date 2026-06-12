# Engine — Visual Evidence Architecture
## Spec for the visual-evidence assembly + render-check engine (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. It **assembles
and render-checks**; it never captures a screenshot and never declares a visual
"proof" (the ~25% automation ceiling — the lowest of the writing skills). Capture is
always manual, because a screenshot's proof-value is its real date stamp from the live
official source, which a bot fetch destroys.

## What it does (per build)
1. For each page claim marked "needs proof": if no visual in the brief → **FLAG** (missing proof).
2. For each screenshot entry: if missing `{date, source_url, c_id}` → **FLAG**.
3. Lay out each screenshot + caption **adjacent to its claim** (the proof interstitial, F-08).
4. **Generate the data infographics** from a sourced-figures table (each figure prints its C-ID or HEDGE inline).
5. **Render-check at 390px** — load each infographic at a 390px viewport, assert `scrollWidth <= clientWidth`; on horizontal scroll, **FAIL the build** and save the 390px screenshot as evidence.
6. Write the build report + the 390px screenshots.

## The render-check (the automatable core)
```python
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
This is the one fully-deterministic gate — the same harness that verified the guides
and both infographics (all `scrollWidth == clientWidth == 390`).

## Inputs / outputs / guardrails
- **Inputs:** the page briefs (claims + C-IDs), the sourced-figures table for the infographics, the hand-captured screenshots + metadata, `PROJECT_ROOT`.
- **Outputs:** generated infographic HTML, per-asset 390px render-check result + screenshot, flagged missing-proof claims, flagged screenshots missing date/URL/C-ID, the assembled layout.
- **Never** fetches an official page itself and treats the result as a dated screenshot (that is not proof); **never** declares a visual "proof" — it assembles, render-checks, and flags; the human owns the proof verdict.
- **Hand back to human:** capturing every official-source screenshot; the real process photography; the proof verdict (A1–A4); any flagged claim/screenshot.
- **Test phase:** assemble the 4 briefs + build both infographics, PAUSE, human review before scaling.
- **Audit:** 20% blind re-check; 90% agreement, with zero infographics passed that break at 390px and zero undated screenshots accepted as proof (each a hard fail).

## Status
**Spec complete; the four visual briefs + both infographics are built by hand (the proof).** `data/visual-brief-4-pages.md` (5 proof-visible screenshots, every page ≥1), `data/summer-embargo-calendar.html` and `data/airport-comparison-table.html` (both 390px-verified), and `data/screenshot-integration-guide.md` are the real output. The Python engine scales the assembly + render-check when built; the evidence is always captured manually.

## Library codes
M-37 Real-Photo Conversion-Lift · M-13 Proof Density · M-19 Nielsen's 4 Credibility Factors · F-08 Proof Interstitial · F-07 Documentation Loop · F-04 Source Verification · P-06 Screenshots Are Proof · P-39 Replace Stock with Real Photos · P-40 Contextual Relevance · P-13 Hormozi Test · P-07 Independent Verification. Full citations in `MFP-LIBRARY.md`.
