# PawRoute research — keyword data (Trust Engine only)

**Source:** Trust Engine `skill-01-keyword-collection.xlsx` (the fear/intent-classified set).
Per instruction we use **only the Trust Engine keywords** — the raw 18k "MASTER" set is NOT used.

## Files
- **`trustengine-keywords.csv`** — 598 keywords. Columns: `Keyword · Source · Source Count · Date ·
  Location · Device · Volume · Seasonal Peak · Status · Intent Type · Customer Fear · Notes`.
  Location = UAE (gl=ae); seasonal peak Oct–Apr (summer embargo is the off-season).
- **`trustengine-page-briefs.csv`** — 598 ready briefs. Columns: `Keyword · Intent · Fear Category ·
  Customer Fear · Page Type · Opening Sentence · Primary CTA · Priority Score` (sorted build-first).

## What the data says

### Intent mix (598)
Informational **275** · Commercial **147** · Research **147** · Fear **14** · Transactional **13** · Urgency **2**.

### Page-type plan (from the briefs)
Step-by-step guide **275** · Alternative page **147** · Trust comparison **147** · Service **13** ·
Reassurance **12** · Action **2** · Prevention **1** · Process-clarity **1**.

### The fears driving demand (top themes)
1. **Emirates/Etihad will reject or cancel my pet** (biggest single cluster)
2. **Choosing the wrong relocation company** (→ competitor "alternative" pages: DKC, Blue Sky, Carry My Pet)
3. **I'll get the paperwork/documents wrong / miss a requirement**
4. **I'm being overcharged / quoted an insane price**
5. **Dogs/cats/my breed aren't allowed** (breed bans, airline rules)
6. **Handing my pet to a stranger / pet will suffer in cargo**
7. **My pet will be taken/held at customs** (confiscation)
8. **I don't know where to start**

### Highest-priority briefs (build first)
- **Competitor "alternative" pages** — `dkc relocations`, `blue sky pets relocation`, `carry my pet dubai reviews`
  → Page type *Alternative*, fear "choosing the wrong company", CTA "Here is how we handle the concerns you read about."
- **Cost "trust comparison" pages** — `pet relocation cost from dubai`, `pet relocation dubai to uk cost`
  → Page type *Trust comparison*, fear "being overcharged / paperwork", CTA "Here is what separates a reliable service…"
- **`uae pet import regulations`** → *Step-by-step guide*, fear "miss a requirement", CTA "Moving your pet to Dubai involves…"

## How to use
Each brief is a ready content spec: **keyword → fear → page type → opening sentence → CTA**, in
build-first priority order. Feed a brief into the blog pipeline (`BLOG-PLAYBOOK.md` §5) → write
fear-led, sourced, GEO-optimized, with a content upgrade. Page-type → block recipe:
*Alternative* = comparison + trust; *Trust comparison* = comparison table + sources; *Step-by-step* =
key_facts + steps + sources; *Reassurance* = the fear-resolution template we already built.
