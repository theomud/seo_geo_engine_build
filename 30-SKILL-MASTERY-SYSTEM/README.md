# 30 — SKILL MASTERY SYSTEM

> The capability layer of the Content Intelligence Operating System.
> Knowledge explains what is true. **Skills are what you can repeatedly *do*.**

Most vaults organise by topic. This system organises by **capability**:

```
Knowledge → Skills → Frameworks → Systems → Execution → Results
```

This section is the single home for every skill the engine can perform. Each skill
is catalogued, rated for real-world performance, mapped to the actual playbooks that
execute it, and — per the evidence standard below — backed **only** by peer-reviewed
research (PubMed / OpenAlex / PMC / DOI) and named expert practitioners.

---

## What lives here

| File / folder | Purpose |
|---|---|
| `README.md` | This file — the model, the map, the standards |
| `SKILL-REGISTER.md` | Master catalogue of **all** skills, rated and mapped to source playbooks |
| `_TEMPLATE-skill-profile.md` | The structure every domain profile follows |
| `domains/` | One profile per skill domain (the 22 capabilities) |
| `evidence/` | Citation bank — DOIs, PMIDs, OpenAlex IDs, expert sources per domain |

The **executable playbooks** themselves stay where they already live (`skills/`,
`trustengine/skills/`, `copywriting/`, `copy_and_image_sciences/`). This section is the
**mastery layer on top** — it catalogues, rates, and research-backs them without
duplicating the files (duplication causes drift). Every profile links to the real asset.

---

## The 22 skill domains

| # | Domain | Primary question it answers |
|---|---|---|
| 01 | [[research]] | What is actually true about this market and customer? |
| 02 | [[critical-thinking]] | Is this reasoning sound, or am I fooling myself? |
| 03 | [[writing]] | Can a normal person understand and act on this? |
| 04 | [[copywriting]] | Does this make the reader take the next step? |
| 05 | [[storytelling]] | Does this create emotional engagement and memory? |
| 06 | [[psychology]] | Why do humans actually decide and act? |
| 07 | [[visual-design]] | Does the image build trust and aid the decision? |
| 08 | [[seo]] | Will search engines rank and surface this? |
| 09 | [[geo]] | Will AI answer engines cite this? |
| 10 | [[content-strategy]] | What to build, in what order, for what intent? |
| 11 | [[authority-building]] | Why should anyone treat us as the expert? |
| 12 | [[trust-building]] | Why should a fearful buyer believe us? |
| 13 | [[lead-generation]] | Does content turn into qualified enquiries? |
| 14 | [[cro]] | Does the page convert attention into action? |
| 15 | [[sales]] | Does the conversation close the deal? |
| 16 | [[ai-systems]] | Are we using AI safely and systematically? |
| 17 | [[prompt-engineering]] | Does the prompt reliably produce the outcome? |
| 18 | [[knowledge-management]] | Can we find, trust, and reuse what we know? |
| 19 | [[business-strategy]] | Are we applying the engine to the right market? |
| 20 | [[project-management]] | Does the work actually ship? |
| 21 | [[decision-making]] | Are we choosing well under uncertainty? |
| 22 | [[systems-thinking]] | Do the parts compound into a working whole? |

---

## What every domain profile contains

Each `domains/*.md` file follows `_TEMPLATE-skill-profile.md`:

1. **Theory** — what the capability is, in evidence-based terms
2. **Principles** — the laws that hold across cases (each cited)
3. **Frameworks** — how experts structure the work (named, sourced)
4. **Models** — decision tools
5. **Examples** — real input → output
6. **Practice** — how to drill it
7. **QA Standard** — how to measure quality / pass-fail
8. **Common Mistakes** — failure modes
9. **Best Practices** — what world-class looks like
10. **Mastery Definition** — the L7 / Authority bar
11. **Skill Rating** — the rating block (below)
12. **Engine Assets** — links to the executable playbooks that run this skill
13. **Evidence** — the cited research and expert sources

---

## Rating framework

Skills are rated for **performance, not knowledge** — the gold standard (per Theo) is
*"can this repeatedly produce the desired outcome in the real world?"* Results beat theory.

Each skill is scored **K × E × R × T**, 1–10 each, **/40** (consistent with
`skills/SKILLS-SCORECARD.md`):

| Dim | Question |
|---|---|
| **K** Knowledge | Does it encode the proven know-how (frameworks, data)? |
| **E** Execution | Can you actually *do* it from this — steps, templates, thresholds? |
| **R** Results | Does following it move the needle (leads / rankings / conversions)? |
| **T** Teaching | Does it explain *why*, so the user/AI adapts to new cases? |

**Mastery ladder (Dreyfus):** Novice → Advanced Beginner → Competent (L4) →
Proficient (L5) → Mastery (L6) → Authority (L7).
≥34/40 = Authority-tier · 28–33 = Proficient · 24–27 = Competent · <24 = cut.

Each profile also carries the blueprint rating block:

```
Skill:
Current Level:   X/40  (Tier)
Target Level:    Y/40  (Tier)
Last Reviewed:   YYYY-MM-DD
Evidence:        [what proves the level — research + production results]
Projects Applied: [where it has been used]
```

> Scores from a structured audit of the playbooks are **paper scores** (L5 ceiling).
> L6 Mastery / L7 Authority is *earned in production* once real lead/conversion data
> is fed back. See `skills/SKILLS-SCORECARD.md`.

---

## EVIDENCE STANDARD (non-negotiable)

This section fills **only with evidence-based research and named expert practice.**
Nothing enters a domain profile without a source. Three tiers, in priority order:

1. **Peer-reviewed science** — PubMed (PMID), PMC, OpenAlex (Work ID), or a resolvable
   **DOI**. Used for any claim about human behaviour, cognition, trust, attention,
   memory, persuasion, decision-making, learning, or measurement.
2. **Authoritative practitioner frameworks** — named experts with a track record and a
   citable artifact (book, paper, documented method). E.g. Alex Hormozi (offers / value
   equation), Robert Cialdini (influence), Eugene Schwartz (awareness stages),
   Daniel Kahneman (dual-process), Ann Handley (writing), Rand Fishkin / Google docs (SEO).
3. **Primary official sources** — government, standards bodies, platform documentation —
   for facts and rules (regulations, ranking guidance, accessibility standards).

Rules (aligned with `GOVERNANCE/TRUTH_POLICY.md` and `KNOWLEDGE/evidence_registry.yml`):
- **No claim without a citation.** Every principle, framework, and number carries its source.
- **No fabricated citations.** A DOI/PMID must resolve. If a claim cannot be sourced, it
  goes to [[../23-WORKING]] as a hypothesis, not into the profile as fact.
- **Separate science from opinion.** Practitioner frameworks are labelled as such, not
  presented as peer-reviewed fact.
- Citations are stored in `evidence/<domain>.md` and referenced by ID from the profile.

---

## How Claude should use this section

Before producing any content, walk the capability chain:

```
Who is the customer?  → [[research]] [[psychology]]
What must be true?    → evidence standard above
Which skill applies?  → this register
Which playbook runs it? → Engine Assets link in the profile
What does "good" mean? → the QA Standard in the profile
```

This is how the engine stays consistent across markets (pet relocation → any future
market) while adapting to different customer types — the *skill* is stable, the
*application* flexes.

---

## Operating flow

```
Knowledge (01-29 sections)
    ↓
Skill (this section: what we can do)
    ↓
Framework (29-FRAMEWORK-LIBRARY: how experts think)
    ↓
System (the engine: how it runs)
    ↓
Execution (skills/ playbooks)
    ↓
Results (24-TRACKING: measured outcomes)
    ↓
Re-rate (feed results back → move L5 → L6/L7)
```

Related: [[../skills/SKILLS-SCORECARD|Skills Scorecard]] ·
[[../skills/ANATOMY_GUIDE|Skill Anatomy Guide]] ·
[[../GOVERNANCE/TRUTH_POLICY|Truth Policy]]
