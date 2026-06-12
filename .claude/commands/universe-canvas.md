---
description: Generate a neat, precise "universe" Obsidian canvas — a 3x3 orbital grid with a central sun, 8 evenly-spaced constellations, and deep-space graph embeds. Use when a vault's 00_UNIVERSE.canvas looks messy, cramped, or needs rebuilding.
---

# Universe Canvas — Precision Orbital Layout

Generate `00_UNIVERSE.canvas` as a **mathematically precise orbital map**, not a messy grid.
Every node is aligned to a fixed coordinate system so nothing ever looks cramped.

## The Design Law

The layout is a **3×3 grid** centred on the sun, with **800px of empty space**
("orbital gap") between every cell. Eight constellations sit on the eight compass
points; the sun occupies the centre cell; the giant graph canvases live in "deep space"
far below.

```
   PERSONAL   ·   WORLD STATE   ·   CIVILIZATION     (north)
   GALAXIES   ·      ☀ SUN      ·     SYSTEMS        (equator)
  KNOWLEDGE   ·    FEEDBACK     ·     ENGINES        (south)
                       ↓
            ▒▒▒  DEEP SPACE — graph embeds  ▒▒▒
```

## Fixed Coordinate System (do not improvise)

Constellation groups are all **1700 wide × 1250 tall**. Column left-edges and row
top-edges are fixed so all three columns and rows align perfectly:

| | Left col (x) | Centre col (x) | Right col (x) |
|---|---|---|---|
| **Top row (y=-2675)** | -3350 | -850 | 1650 |
| **Mid row (y=-625)** | -3350 | *(sun)* | 1650 |
| **Bottom row (y=825)** | -3350 | -850 | 1650 |

- **Sun**: `x:-450, y:-450, w:900, h:900` (centre cell, centred on origin).
- **Gaps**: 800px between every cell, both axes. Total grid 6700×5350, centred on origin.
- **Deep space group**: `x:-6500, y:2900, w:13000, h:6900`. Two graph canvases inside
  at `w:6000, h:6000` — left at `x:-6300`, right at `x:300`, both `y:3500`. Labels above
  each at `y:2980, h:480`.

## Internal Layout Rules (per group)

- Inner padding: **50px** all sides; **90px** reserved at top for the group label.
- Inner usable area = 1400 wide × 960 tall (x from groupX+50, y from groupY+90).
- **File nodes** (preview content) for the most important items; **text nodes** with
  `[[wikilinks]]` for the overflow so nothing is lost.
- Common internal templates:
  - **Hero + row-of-4 + strip**: hero `1400×250` on top; four `325×300` cards (gap 33)
    at `y+280`; full-width text strip `1400×350` at `y+610`.
  - **2-column files**: card `680` wide (gap 40), rows `217` tall (gap 30) — for 7 galaxies.
  - **2×2 / 2×3 text grid**: cards `680` wide; heights split the 960 inner height evenly.

## Constellation Assignments

| Compass | Cell (x,y) | Content | Color |
|---|---|---|---|
| NW | -2650,-2050 | 👤 Personal — 90/70/80 + 🔒 Private (red) | 4 |
| N | -750,-2050 | ⚡ World State — Current_Reality hero + boot files | 1 |
| NE | 1150,-2050 | ⚖️ Civilization — Constitution hero + Vision/Mission/Values/Principles | 5 |
| W | -2650,-550 | 🌌 7 Galaxies — Business/Personal/AI/Knowledge/Finance/Health/Spiritual | 5 |
| E | 1150,-550 | ⚙️ Systems — Prime Directive hero + 11 rules + 8 personas | 6 |
| SW | -2650,950 | 📚 Knowledge Layers — 00_INBOX→50_ARCHIVE | 2 |
| S | -750,950 | 📊 Feedback — 91-94 measure + 95/97/98 memory | 3 |
| SE | 1150,950 | 🚀 Engines — Pet engine + workspace + roadmap | 2 |

## Edges (orbital paths)

Nine edges form a symmetric "fountain": sun→top three groups (fromSide top),
sun→bottom three (fromSide bottom), sun→galaxies (left), sun→systems (right),
plus feedback→deepspace. Each edge carries a short lowercase label
(`boot #1`, `the law`, `7 galaxies`, `rules & agents`, etc.) and matches the
target group's color.

## Obsidian canvas colors

`1` red · `2` orange · `3` yellow · `4` green · `5` cyan · `6` purple.

## Process

1. Read the existing `00_UNIVERSE.canvas` to inventory what files/folders exist.
2. Map every real file to a node; represent empty folders as text nodes (lose nothing).
3. Write the canvas using the fixed coordinates above — never eyeball positions.
4. **Obsidian rewrites the file on save.** If the Write fails with "modified since read",
   re-read the file (it will be minified) and write again. Tell the user to fully close
   Obsidian before the final write if it keeps reverting.
5. Verify no group overlaps the sun (sun spans -400..400 on both axes; all groups clear it).

## Anti-patterns (what made it messy before)

- ❌ Packing everything into ~8000px with 300px bands → cramped. Use the full 5300×4100 grid.
- ❌ Variable, eyeballed gaps → misaligned. Use fixed 400px gaps and the coordinate table.
- ❌ Cramming 11 file-preview nodes into one group → unreadable. Hero file + text overflow.
- ❌ Treating it as a dashboard grid. It is a **solar system**: sun centre, orbits around it.
