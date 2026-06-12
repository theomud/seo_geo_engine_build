# Engine — Authority Asset Creation
## Spec for the proof-density counter + Hormozi foil (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. It **counts and flags
only** (the ~20% automation ceiling — the lowest in the collection). It never writes the case
study: the moment an AI authors the asset, it becomes the generic mush the skill exists to
avoid. The documented failure and the Hormozi verdict are irreducibly human.

## What it does (per asset)
1. **Count proof density** — verifiable items (C-ID citations + named figures) ÷ (words / 200);
   flag if < 1. The documented failure is added to the count by the human (+1) — no regex
   detects "the surprise."
2. **Flag floating claims** — factual-looking sentences with no C-ID, figure, or hedge nearby.
3. **Generate the Hormozi foil (optional)** — produce the *generic* AI version from a basic
   prompt so the reviewer can list, plainly, what the documented asset has that it lacks. The
   engine produces the foil, never the asset.

## The density-count core (deterministic)
```python
import re
CID = re.compile(r'\bC-\d{3}\b')
FIG = re.compile(r'\b\d[\d,]*\s?(AED|USD|%|days?|hours?)\b', re.I)
def proof_density(text):
    words = len(re.findall(r'\b\w+\b', text))
    items = len(CID.findall(text)) + len(FIG.findall(text))   # + documented failure (human, +1)
    ratio = items / (words / 200) if words else 0
    return {"words": words, "proof_items": items,
            "ratio_per_200w": round(ratio, 2), "pass": ratio >= 1}
```

## Inputs / outputs / guardrails
- **Inputs:** the human-written case-study draft, the verified facts (C-IDs), a basic AI prompt
  for the topic (to generate the foil), `PROJECT_ROOT` (+ optional `ANTHROPIC_API_KEY` for the foil).
- **Outputs:** the proof-density count (items, words, ratio, pass/fail), the floating-claim flags,
  and the generic-AI foil draft for the Hormozi comparison.
- **Never** writes or co-writes the case study; **never** declares an asset "authoritative";
  **never** judges the Hormozi test (it supplies the foil, the human decides).
- **Hand back to human:** documenting the case; the failure/surprise; the Hormozi verdict;
  confirming a cited fact is true.
- **Audit:** re-count density + re-run the Hormozi comparison; a missing failure or a foil that
  matches the asset is a hard fail regardless of density.

## Status
**Spec complete; the density counter was run live on the real case study (the proof).**
`data/case-study-airport-confiscation.md` was measured by `proof_density()`: 782 words, 19
pattern-matched items + 1 documented failure = 20, density **5.12 per 200 words → PASS**; the
Hormozi test passes (5 specifics the generic foil cannot produce). The engine counts; the
documenting and the verdict stay human.

## Library codes
M-14 Documentation Types · M-13 Proof Density · M-11 Content Depth · F-07 Documentation Loop ·
F-14 Free Work Bootstrap · F-29 Skyscraper · F-30 Reverse Outreach · P-13 Hormozi Test · P-15
Deliver Then Document · P-31 Linkable-Asset Standard · P-03 Proof Over Promise. Full citations
in `MFP-LIBRARY.md`.
