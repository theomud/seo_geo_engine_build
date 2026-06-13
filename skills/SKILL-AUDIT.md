# Skill conformance audit — against `HOW-TO-BUILD-SKILLS-CORRECTLY.md`

> Standard: the 5-part Anatomy (Face · Brain · Memory · Spine · Pulse) + the self-check.
> **Conformed 2026-06-12 by a 60-agent fan-out** (30 conform → 30 adversarial verify).
> Result: **30/30 conformed · 22 pass adversarial verify · 8 flagged.** Each skill committed
> separately. The 8 flags are almost all trivial section-ORDER nits (the content is present),
> plus one genuine one-skill-two-jobs case (`marketingskills/image`).
>
> **Fix-pass 2 completed 2026-06-12 (commit 8aa9900) — all 8 flags resolved.**
>
> **7 new skills added 2026-06-13 (commit 21f3457) — built to spec, conform on creation.**

## New skills 2026-06-13 — book-extraction pack (7 skills)

Seven skills authored directly to the 5-part Anatomy from the six ingested books
(`17-TEMPLATES/cheatsheets/books/`). Built conformant — not retrofitted — so no fix-pass needed.

| Skill | Source book | Face <1k | 7-section spine | Dial | Real example | Known gaps |
|-------|-------------|:-:|:-:|------|:-:|:-:|
| `marketingskills/offer-architecture` | Hormozi, $100M Offers | ✅ | ✅ | MIXED | ✅ PawRoute | ✅ |
| `marketingskills/money-models` | Hormozi, $100M Money Models | ✅ | ✅ | MIXED | ✅ PawRoute | ✅ |
| `marketingskills/bfd-brief` | Bly / Masterson | ✅ | ✅ | HIGH | ✅ PawRoute + Bly IT | ✅ |
| `marketingskills/headline-scoring` | Bly, Copywriter's Handbook | ✅ | ✅ | MIXED | ✅ PawRoute walk-through | ✅ |
| `marketingskills/motivating-sequence` | Bly, Copywriter's Handbook | ✅ | ✅ | MIXED | ✅ PawRoute service page | ✅ |
| `marketingskills/pillar-strategy` | Starak, Blog Profits Blueprint | ✅ | ✅ | MIXED | ✅ PawRoute 6-pillar map | ✅ |
| `marketingskills/blog-taxonomy` | Hostinger/Surfer, Blog Writing | ✅ | ✅ | HIGH | ✅ PawRoute classification | ✅ |

**Conformance checks (all 7):**
- **Face <1,000 chars:** ✅ all pass (range ~590–810). Each Face has when-to-load + trigger phrases + sibling defer-note.
- **File <500 lines:** ✅ all pass (range 269–387). No Memory-extraction needed yet.
- **7-section spine in order:** ✅ How-to-use → North Star → Freedom Dial → Before Starting → core → Output Format → Anti-patterns → Real examples → Self-check → Known gaps → Related Skills.
- **Freedom Dial set correctly:** ✅ — judgment skills (`bfd-brief`, `blog-taxonomy`) are HIGH; the scoring/sequencing skills are MIXED (LOW on the mechanical part: Value Equation, 4 U's rubric, 30-day math, step order).
- **Real examples concrete:** ✅ all use the PawRoute/Maya pet-relocation domain with worked input/output (not abstract description).
- **Cross-links resolve:** ✅ every Related Skills pointer targets an existing sibling in the pack.

**Also upgraded:** `marketingskills/programmatic-seo` v2.0 → v2.1 — added pSEO 2.0 (JSON-schema/AI),
batch-publishing strategy, tech-stacks table, 4 case studies (Zapier/Flyhomes/KrispCall/Jake Ward),
the "useful-without-search-engines" test, and the no-feedback-loop anti-pattern. Spine preserved; still conformant.

> **Pack total after this addition: 37 SKILL.md files** (30 original conformed + 7 new).

## Fix-pass 2 — all 8 flags resolved

| Skill | Original Flag | Resolution |
|-------|---------------|------------|
| `claude-blog/blog-brief` | North Star + Freedom Dial before "How to use"; 3 dangling ref pointers | "How to use" moved to top; 3 `references/*.md` files created ✅ |
| `marketingskills/ai-seo` | No dedicated "Real examples" section; placeholders only | Real-examples section added with worked input/output ✅ |
| `marketingskills/copy-editing` | "Common Copy Problems" ≠ Anti-patterns header; Real-examples unnamed | Headers renamed to standard; Real-examples header added ✅ |
| `marketingskills/image` | Missing Real-examples; "Common Mistakes" ≠ Anti-patterns; **2 jobs** | Anti-patterns renamed; **`image-optimize` spun out as its own skill** ✅ |
| `seo-geo-skills/content-quality-auditor` | Secs 4→5→6 inverted; no North-Star; dup pointer | Tail reordered (Anti-patterns → Examples → Self-check); North Star added; deduped; **690 → 419 lines** ✅ |
| `seo-geo-skills/geo-content-optimizer` | Example before Anti-patterns; refs → remote GitHub URLs | Reordered; refs repointed to local `references/` siblings ✅ |
| `seo-geo-skills/meta-tags-optimizer` | Real example before Anti-patterns; refs off-repo | Reordered; refs repointed locally ✅ |
| `seo-geo-skills/seo-content-writer` | Example + 3 sections trail after Known gaps | Reordered so Known gaps is final section ✅ |

> **Note on 3 genuinely external refs** in `geo-content-optimizer` and `meta-tags-optimizer`:
> `entity-geo-handoff-schema.md`, `skill-contract.md`, and `CONNECTORS.md` have no local copies
> and remain as external refs — not a conformance failure.

**Pattern:** the imported `seo-geo-skills/*` pack consistently places its worked Example mid-body
(before Anti-patterns) and links references to upstream `github.com/aaron-he-zhu` URLs even though
the files exist locally. A single sweep fixes all four.

---

## Original first-pass notes (pre-fan-out, retained for context)

> Mechanical heuristics flag the hard rules (Face length, file length, trigger phrases); the
> Spine/Dial columns needed a human read.

## Hard-rule results (mechanical)

- **Face <1,000 chars:** ✅ all 30 pass (range 249–820).
- **File <500 lines:** ⚠️ **2 violations** — `claude-blog/blog-write` (559), `seo-geo-skills/content-quality-auditor` (690).
- **Face has trigger phrases / when-to-use:** ✅ all 30 now pass (`copywriting` fixed 2026-06-12 — was a bare label).

## Priority fixes (ranked)

| # | Skill | Issue | Fix | Status |
|---|-------|-------|-----|--------|
| 1 | `seo-geo-skills/content-quality-auditor` | 690 lines — worst length violation | Pushed long rubric/example blocks into `references/` Memory; Brain points to it | ✅ done 2026-06-12 (690 → 419 lines) |
| 2 | `claude-blog/blog-write` | 559 lines | Extracted template/example detail to Memory files | ✅ done 2026-06-12 (559 → 432 lines) |
| 3 | `copywriting/SKILL.md` | Face was a label, no triggers | Rewrote Face with when-to-load + trigger phrases | ✅ done 2026-06-12 |

## Spine skeleton — first-pass coverage

The 7-section skeleton (How-to-use · North Star · Core · Anti-patterns · Examples · Self-check ·
Known gaps) is applied **inconsistently**. Most-missing sections across the pack:

- **Explicit "Known gaps"** — present in only ~7/30. Highest-value Pulse addition; prevents the
  model attempting work out of the skill's depth.
- **Explicit "Self-check / validation"** — present in ~16/30.
- **Explicit "How to use" header** — present in ~10/30 (many open straight into instructions).

These are **content additions, not rewrites** — safe to add incrementally. They do NOT require
touching the skill's actual logic.

## Freedom Dial — needs human read (not yet scored)

Whether each skill sets the dial correctly (principles for judgment work; mechanical checklist
for precision work) can't be detected mechanically. Candidates to check first:

- **Precision skills** that should be low-freedom checklists: `marketingskills/schema`,
  `seo-geo-skills/meta-tags-optimizer`, `claude-blog/blog-factcheck`.
- **Judgment skills** that should be high-freedom principles: `marketingskills/copywriting`,
  `marketingskills/cro`, `marketingskills/marketing-psychology`.

## Notes / constraints

- `seo-geo-skills/*` are an **imported third-party pack** (Apache-2.0, `aaron-he-zhu` GitHub).
  Conform the shape, but preserve license/attribution frontmatter when editing.
- Frontmatter schema varies across packs (`metadata.version`, `when_to_use`, `argument-hint`).
  The standard governs content/shape; a unified frontmatter schema is a separate, optional pass.

## Recommended next action

Do the 2 length extractions (#1, #2) and add "Known gaps" sections pack-by-pack. Each is a
contained, reviewable change — not a 30-file blind rewrite.
