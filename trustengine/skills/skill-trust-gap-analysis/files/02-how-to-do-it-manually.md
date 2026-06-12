---
Status: draft — built 2026-05-29
Area: skill-trust-gap-analysis
Depends on: skill-trust-gap-analysis/files/01-what-is-this-skill.md, skill-trust-gap-analysis/README.md
Feeds into: skill-trust-gap-analysis/files/03-how-to-verify-it.md, skill-trust-gap-analysis/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Scoring competitors and building the Content Gap Matrix, by hand, before automation

---

## Why manual first

The automation (File 04) scores the long tail of competitors with Playwright + Anthropic. But until you have scored the top three by hand — opened each page, felt where the fear is unacknowledged, found the missing citation — the engine has no calibrated standard to imitate. **Score the top 3 manually, then let automation scale the pattern.**

Time required: **~30 min per competitor page** manually (top 3 = ~1.5 hours), plus ~1 hour for discovery and ~30 min to build the matrix. The whole manual pass for a niche is half a day.

**Inputs (optional, per P-12):** a competitor list — pull it from Customer Fear Intelligence community research if you have it, *or* bring your own. This skill works either way; it does not hard-depend on any other skill.

---

## Step 0 — Place the niche on the Risk Continuum (before visiting any site)

Decide the proof threshold **first** — it changes how you score every dimension. (Library: **M-04 Risk Continuum Model**.)

| Level | User risks | Proof threshold |
|-------|-----------|-----------------|
| Low — Entertainment | Seconds of time | Low — personality wins |
| Medium-Low — B2C education | Appearance / minor habits | Moderate — live demo beats text |
| Medium-High — B2C financial/legal | Real money / legal standing | High — third-party credentials |
| High — Regulated services | Irreversible harm | Maximum — every claim traces to an official source |

**Dubai pet relocation = maximum risk.** A pet confiscated at the border is catastrophic, so a page that gives advice without official-source proof scores low on the citation and proof dimensions no matter how polished it reads. Write the niche's risk level at the top of the scoring sheet.

---

## Step 1 — Competitor discovery (Google AND community)

List every competitor, not just Google page 1:

1. **Google** — search the head terms and the route/variant terms; record every provider and content site that ranks.
2. **Community** — Facebook groups and Reddit threads name providers Google tools miss. In the Dubai proof run, **4 of 9 scored competitors were only discoverable through community research.**
3. Record each competitor + the specific URL you will score (the page that targets the key fear/keyword, not the homepage).

A discovery pass that stops at Google is incomplete. (Library: community discovery is part of the method, echoing **F-02 Five-Phase Research**.)

---

## Step 2 — Manual scoring of the top 3 (the 10-Point Trust Score)

Open each page in a browser, **screenshot it**, and award one point per dimension present. (Library: **M-05 Trust Score Model**, scored via **F-03 Trust Score Competitor Scoring**.)

| # | Dimension | Point if… |
|---|-----------|-----------|
| 1 | Fear in first 100 words | Opens with the customer's specific worry, not "Professional Pet Services" |
| 2 | Official source cited | Links a government/regulatory body, not an uncited claim |
| 3 | Specific route/variant named | Names the specific case, not "all international routes" |
| 4 | Step-by-step process | Numbered steps with timing, not generic bullets |
| 5 | Timeline included | Specific durations |
| 6 | Cost ranges shown | Real numbers + honest disclaimers, not "contact us for a quote" |
| 7 | Common-mistakes section | Edge cases addressed |
| 8 | Original visuals | Real photos, not stock |
| 9 | CTA feels like help | Assists, doesn't pressure |
| 10 | Proof interstitial | Proof beside each claim throughout — **not** only a testimonials block |

**Score bands:** 0–2 displace · 3–4 weak (exploit gaps) · 5–6 decent (target gaps) · 7–8 strong (study & surpass) · 9–10 excellent (learn from everything).

For each page record: the score, a screenshot filename, and a **gap list** (which dimensions scored 0 and why). The gap list is the raw material for the matrix.

---

## Step 3 — Score the remaining competitors

Repeat Step 2 for the rest. Beyond the first 3 this is where automation takes over (File 04: Playwright extracts page text, Anthropic scores the 10 dimensions) — but the manual method is identical, and any competitor the engine flags as low-confidence comes back to a human. Screenshot every page regardless of who scores it.

---

## Step 4 — Build the Content Gap Matrix

Count how many competitors fail each dimension. **Most failures = highest-priority content to build first.** (Library: this ranking is the skill's signature output; the 4-step flow is **F-01/F-03**.)

| Gap | Competitors missing | Priority |
|-----|--------------------|----------|
| Airport confiscation fear | 9/9 | 🔴 Highest |
| Summer embargo warning | 9/9 | 🔴 Highest |
| Titer test cost + timeline | 9/9 | 🔴 Highest |
| Airport comparison | 9/9 | 🔴 Highest |
| Proof interstitial throughout | 9/9 | 🔴 Highest |
| Official source citation | 7/9 | 🟡 High |
| Common-mistakes section | 8/9 | 🟡 High |

The gaps missed by nearly every competitor are the **universal gaps** — the first pages to build. This matrix is the deliverable that feeds the content build (optionally, Content Structure consumes it as its page list).

---

## Hand off

When the matrix is built you have: a risk level, a scored competitor set (each with a screenshot and gap list), and a ranked list of content opportunities. A content team builds the universal gaps first, knowing exactly which trust dimension each competitor failed.

---

## What you must not do

- **Do not skip Step 0.** Scoring without the risk level set gives every page an inflated score in a maximum-risk niche.
- **Do not stop discovery at Google.** Community-only competitors are real competitors.
- **Do not score a citation-free claim as if cited.** In a maximum-risk niche, generic reassurance is not proof. (Library: **P-02 Wrong Information Causes Real Harm**, **P-22 Trust Is the Centre**.)
- **Do not skip the screenshot.** A score with no screenshot can't be audited. (Library: **P-06 Screenshots Are Proof**.)
- **Do not misrepresent a competitor** to inflate a gap. The matrix is only useful if the scores are honest.

---

## Output of this manual phase

A scored competitor set (top 3 by hand, screenshots + gap lists), the niche's Risk Continuum placement, and the ranked Content Gap Matrix with the universal gaps identified. That output is what makes File 04's automation trustworthy — the engine scales a standard a human has already demonstrated.
