---
domain: <NN-domain-slug>
title: <Domain Name>
priority: <P1 copy | P1 image | P2 | P3>   # copy & image are P1 — the system's core promise
status: <strong | partial | gap>
current: <X/40>
target: <Y/40>
last_reviewed: <YYYY-MM-DD>
tags: [skill-mastery, <domain>]
---

# <NN> — <Domain Name>

> One-sentence definition of the capability, in plain language.
> **Market-agnostic rule:** state how this skill works the same in *any* market, and
> what single input makes it adapt (almost always: the validated customer + the evidence).

---

## 1. Theory — what this capability is
Plain-language explanation. A normal person must understand it. No jargon without a
definition. Every factual claim carries an inline source tag like `[E1]`, resolved in
the Evidence section.

## 2. Principles — the laws that hold across markets
Numbered. Each principle is **one sentence + why it's true + its source**.
1. **<Principle>.** Why. `[E#]`
2. ...
> Principles are market-independent. If a "principle" only holds in one market, it's a
> tactic — move it to the market file, not here.

## 3. Frameworks — how experts structure the work
Named frameworks only, each attributed to a named expert/source and shown as a usable
structure (not just named). E.g. value equation, awareness stages, dual-process.
- **<Framework>** — <expert/source> `[E#]` — <the structure, briefly> — *when to use it*

## 4. Models — decision tools
The if/then tools that turn the frameworks into choices. Tables, ladders, scoring rubrics.

## 5. Examples — real input → output
At least one concrete worked example. Input shown, output shown. No abstract description.
Where possible, drawn from a live engine asset (link it).

## 6. Practice — how to drill this
Specific exercises to move up the ladder. Repeatable, with a self-scorable outcome.

## 7. QA Standard — how to measure quality
Pass/fail or scored checklist. This is what an audit of the output checks. Ties to the
relevant gate in `QA/` or the skill's own self-check.

## 8. Common Mistakes — failure modes
Numbered, specific, each with the fix.

## 9. Best Practices — what world-class does
The behaviours that separate Authority-tier from Competent.

## 10. Mastery Definition — the Authority (L7) bar
One paragraph: what "the best in any market" looks like for this skill, and how you'd
*prove* it (the production evidence that earns L6/L7, not paper score).

---

## Skill Rating
```
Skill:            <name>
Current Level:    X/40  (Tier)        # K×E×R×T — see README
Target Level:     Y/40  (Tier)
Last Reviewed:    YYYY-MM-DD
Evidence:         <what proves the level — research loaded + production results>
Projects Applied: <where used; e.g. Dubai Pet Relocation>
```

## Engine Assets — the executable playbooks that run this skill
- `path/to/SKILL.md` — <one line>
- ...
*(These execute the skill. This profile is the mastery/validation layer above them.)*

## Evidence — validated sources only
> Tier 1 peer-reviewed (PMID/PMC/DOI/OpenAlex) · Tier 2 named expert · Tier 3 official.
> No claim above is unsourced. Full bibliographic detail in `evidence/<domain>.md`.

| ID | Claim it supports | Type | Source (resolvable ID) |
|---|---|---|---|
| E1 | <claim> | peer-reviewed | DOI:… / PMID:… / OpenAlex:W… |
| E2 | <claim> | expert | <Author, Work, year> |
| E3 | <claim> | official | <body, doc, URL> |

---
*Profile follows `_TEMPLATE-skill-profile.md`. Validation standard: [[README#EVIDENCE STANDARD non-negotiable]].*
