---
Status: draft — built 2026-05-30
Area: skill-authority-assets
Depends on: skill-authority-assets/files/02-how-to-do-it-manually.md, skill-authority-assets/files/03-how-to-verify-it.md
Feeds into: skill-authority-assets/engines/engine-authority-assets.md
---

# Skill · File 04 — Automation Spec
## What the authority-asset engine counts, and what stays irreducibly human

---

## Automation target

**~20% of the work can be automated** — the lowest ceiling in the collection, and
necessarily so. The asset's entire value is that it documents real work an AI never saw; the
moment an AI writes it, it is the mush the skill exists to avoid. So the engine **counts and
flags only** — it counts proof density, flags claims with no citation, and (optionally)
generates the *generic* AI version for the reviewer to compare against. It never writes the
case and never judges the Hormozi test. *(Library: M-13 Proof Density; P-13 Hormozi Test;
P-15 Deliver Then Document.)*

What gets automated:
- **Count proof density** — verifiable proof items (C-ID citations + named figures + dated
  facts) ÷ (words / 200); flag if < 1.
- **Flag floating claims** — sentences that read as factual assertions but carry no C-ID,
  figure, or hedge nearby.
- **Generate the Hormozi comparison draft** — produce the *generic* AI version from a basic
  prompt, so the reviewer can see plainly what the documented asset has that it lacks. (The
  engine produces the foil, not the asset.)

What stays manual (the 80%):
- **Documenting the case** — the real account, start to finish. Always human.
- **The failure/surprise** — the un-fakeable core; an AI cannot supply what it never saw.
- **The Hormozi judgement** — does the asset contain real specifics the generic version
  can't? A human decides; the engine only provides the foil.
- **Confirming a claim is true** — the engine sees a citation, not whether it's correct.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| The documented case study (draft) | Markdown | the human writer |
| The verified facts (C-IDs) | list | the verified-source store |
| A basic AI prompt for the topic | text | the reviewer (for the foil) |
| `PROJECT_ROOT` | env | `.env` |

The engine is **forbidden** from writing the case study itself — it may only measure a
human-written draft and generate the generic foil for comparison.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Proof-density count (items, words, ratio, pass/fail) | build report |
| Floating-claim flags (sentence + "no proof nearby") | build report |
| The generic-AI foil draft (for the Hormozi comparison) | build report |
| (human-added) the list of what the asset has that the foil lacks | the asset |

The engine never declares an asset "authoritative" — it counts density, flags claims, and
hands the reviewer the foil; the human owns the Hormozi verdict.

---

## Engine flow per asset

```
for the documented case study draft:
    1. tokenise -> word count
    2. count verifiable proof items: C-ID patterns + named figures + dated facts
    3. density = items / (words / 200); flag if density < 1
    4. scan sentences: flag factual-looking sentences with no C-ID/figure/hedge within N tokens
    5. generate the GENERIC AI foil from the basic prompt (for comparison only)
    6. emit the count + flags + foil; hand to human for the failure check + Hormozi verdict
```

---

## The density-count core (deterministic)

```python
import re
CID = re.compile(r'\bC-\d{3}\b')                       # source-bank citations
FIG = re.compile(r'\b\d[\d,]*\s?(AED|USD|%|days?|hours?)\b', re.I)  # named figures
def proof_density(text):
    words = len(re.findall(r'\b\w+\b', text))
    items = len(CID.findall(text)) + len(FIG.findall(text))
    # the documented failure is counted manually (+1) — code can't detect "the surprise"
    ratio = items / (words / 200) if words else 0
    return {"words": words, "proof_items": items,
            "ratio_per_200w": round(ratio, 2), "pass": ratio >= 1}
```

The engine counts what it can pattern-match (C-IDs, figures); the **documented failure** is
added to the count by the human, because no regex detects "the thing that went wrong."

---

## Worked example (the airport-confiscation case)

Fed the ~900-word draft, the engine counts: C-019, C-003, C-010 (3 C-IDs) + "500 AED",
"90 days" (figures) = ~5 pattern-matched items; the human adds the documented failure (+1);
ratio ≈ 6 / (900/200) ≈ **1.3 per 200w → pass**. It flags any sentence like "the process can
be stressful" as floating (no proof) → the human cuts or grounds it. It generates the generic
foil ("ensure all documentation is in order…") so the reviewer can list, plainly, the C-IDs
and the turnaround surprise the foil lacks → Hormozi **passes**.

---

## Test phase (the one case study, then PAUSE)

The engine measures the case study and stops. The human checks: does the density count match a
manual count? Did it flag the genuinely floating sentences (and not real proof)? Is the foil a
fair generic version? Then the human runs the failure check and the Hormozi verdict the engine
cannot. If the engine miscounts a vague sentence as proof, tighten the patterns before reuse.

---

## Audit (after a build)

A sub-agent re-counts proof density and **re-runs the Hormozi comparison** (regenerates the
foil, lists the gap). Pass threshold: density confirmed **≥1 per 200 words**, **a real failure
present**, Hormozi **passes**. A missing failure or a foil that matches the asset is a **hard
fail** regardless of density. *(Library: P-07 Independent Verification.)*

---

## When automation must hand back to humans

- **Writing the case** — always human; the engine never authors the asset.
- **The failure/surprise** — the un-fakeable core; human only.
- **The Hormozi verdict** — the engine supplies the foil; the human decides if the asset beats it.
- **Confirming a cited fact is true** — the engine sees a citation, not correctness.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| Density count + claim scan | milliseconds (local regex) |
| Foil generation (optional) | one AI call ≈ $0.01–0.03 |
| Cost | ≈ $0 for the count; a few cents if generating the foil |

---

## Files in this skill (created by the build)

```
skill-authority-assets/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   └── case-study-airport-confiscation.md   ← the documented case study (real output)
└── engines/
    └── engine-authority-assets.md
```
