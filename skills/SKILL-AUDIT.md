# Skill conformance audit — against `HOW-TO-BUILD-SKILLS-CORRECTLY.md`

> Standard: the 5-part Anatomy (Face · Brain · Memory · Spine · Pulse) + the self-check.
> **Conformed 2026-06-12 by a 60-agent fan-out** (30 conform → 30 adversarial verify).
> Result: **30/30 conformed · 22 pass adversarial verify · 8 flagged.** Each skill committed
> separately. The 8 flags are almost all trivial section-ORDER nits (the content is present),
> plus one genuine one-skill-two-jobs case (`marketingskills/image`).

## Remaining 8 flags (all low-effort except where noted)

| Skill | Flag | Fix |
|-------|------|-----|
| `claude-blog/blog-brief` | North Star + Freedom Dial sit BEFORE "How to use" (secs 1–2 inverted); 3 `references/*.md` pointers dangle | Move "How to use" to top; create the 3 ref files or inline |
| `marketingskills/ai-seo` | No dedicated "Real examples" section; inline examples are `[placeholder]` templates | Add a Real-examples section with one concrete worked input/output |
| `marketingskills/copy-editing` | "Anti-patterns" + "Real examples" exist as content but not as named headers | Rename "Common Copy Problems" → Anti-patterns; add Real-examples header |
| `marketingskills/image` | Missing Real-examples header; "Common Mistakes" ≠ "Anti-patterns"; **does 2 jobs** (create + optimize) | Rename header; **split** image-optimization into its own skill |
| `seo-geo-skills/content-quality-auditor` | Secs 4→5→6 inverted (Self-check before Examples before Anti-patterns); no North-Star header; dup pointer line | Reorder tail; add North Star; dedupe |
| `seo-geo-skills/geo-content-optimizer` | "Example" sits before "Anti-patterns"; refs point to remote GitHub URLs not local siblings | Move Example after Anti-patterns; repoint refs to local `references/` (files exist!) |
| `seo-geo-skills/meta-tags-optimizer` | "Real example" before "Anti-patterns"; refs point off-repo | Reorder; repoint refs |
| `seo-geo-skills/seo-content-writer` | Example before Anti-patterns; 3 sections trail AFTER "Known gaps" | Reorder so Known gaps is last |

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
| 1 | `seo-geo-skills/content-quality-auditor` | 690 lines — worst length violation | Push the long rubric/example blocks into a sibling `references/` Memory file; Brain points to it conditionally | ⚠️ open |
| 2 | `claude-blog/blog-write` | 559 lines | Extract template/example detail to Memory files (already references a `references/` dir — move more there) | ⚠️ open |
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
