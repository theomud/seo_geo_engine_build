# WEBSITE AUDIT
## Score any website on all 13 Trust Engine skills — 130 points, real evidence, a RICE-ranked action plan

---

## What This Skill Is

Most "website audits" grade surface mechanics — page speed, meta tags, a Lighthouse score — and tell a
business owner nothing about why visitors don't trust them enough to act. This skill is different: it
turns the **entire 13-skill Trust Engine** into a single scoring instrument and runs a complete
**130-point audit** of any website, landing page, or blog. Each of the 13 skills becomes one audit
**dimension** scored out of 10, every score is backed by **specific evidence quoted from the live
site**, and the whole thing resolves into a **RICE-ranked action plan** and a **ready-to-execute
content brief** for the single highest-priority gap. It is the Trust Engine pointed back at a site to
answer one question: *where is this site losing trust, and what is the highest-leverage thing to fix
first?*

It is built on the proven foundation — the same 45/47-check audit discipline (F-11), the same
fear-acknowledging methodology (P-04), the same proof-over-promise bar (P-03) — but aimed outward at a
real site. The output is **client-ready**: a business owner who has never heard of the Trust Engine can
read the executive summary and act on it.

**Skill Value Score: 22/25**
- Difficulty: 3/5
- Automation Potential: 4/5
- Market Uniqueness: 5/5
- Commercial Value: 5/5
- Teachability: 5/5

**Status:** ✅ PROVEN 47/47 (proof run: DKC / dkc.ae → 67/130, the Dubai pet-relocation benchmark, 2026-06-01)
**Niche-agnostic:** Yes — every market has a website, a trust bar, and competitors; only the fears and verified facts change

---

## The 13 Dimensions (one per Trust Engine skill)

Each dimension is scored **/10** with quoted evidence from the site. Together they total **/130**.

| # | Dimension | Governing skill | Key MFP |
|---|-----------|-----------------|---------|
| 1 | Fear Intelligence | Customer Fear Intelligence | P-04 |
| 2 | Trust Gap Score | Trust Gap Analysis | M-05 · F-03 |
| 3 | Source Verification | Official Source Research | P-02 · M-13 · P-07 |
| 4 | Content Structure | Content Structure for Trust | F-08 |
| 5 | Editorial Quality | Editorial Judgment | M-10 · F-06 |
| 6 | Conversion Copy | Conversion Copy | P-04 |
| 7 | Visual Evidence | Visual Evidence Architecture | M-13 · F-08 |
| 8 | Site Architecture | Content Architecture | M-24 |
| 9 | Authority Assets | Authority Asset Creation | P-13 · M-13 |
| 10 | Email Nurture | Email Nurture Sequences | F-05 |
| 11 | AI Citation | AI Citation & GEO | M-22/GEO |
| 12 | Monitoring Evidence | Content Intelligence Monitoring | M-27 · F-05 |
| 13 | Market Position | synthesis (uniqueness · Trust Score vs market · AI visibility) | M-24 · P-22 |

The **action plan** scores every identified gap with **RICE (M-27)** and routes it through
**Dashboard-to-Action (F-05)**. **Risk Continuum (M-04)** calibrates the proof bar before scoring
begins; **E-E-A-T (M-24)** with **Trust at the centre (P-22)** is the parent model the whole framework
hangs on.

---

## What It Produces

| Output | What it is |
|--------|-----------|
| Executive summary | Overall **/130** + market position, top-3 strengths, top-3 critical gaps, and the single most important action — written for a business owner |
| 13 dimension scores | Each **/10** with status and the top finding, plus detailed evidence quoted from the live site |
| RICE-ranked action plan | Every gap scored `(Reach × Impact × Confidence) ÷ Effort`, prioritised |
| Content brief | A complete 9-element prompt for the highest-priority missing page, ready to execute |
| Competitor comparison | The same 13 dimensions scored side-by-side against named competitors (optional) |

The report format is fixed by `engines/AUDIT-REPORT-TEMPLATE.md`; the scoring methodology is
`engines/engine-website-audit.md`.

---

## Functional Quality Threshold (Check 46)

This skill's real output is **proven** only when an audit report meets all four gates:

1. **All 13 dimensions scored with specific evidence** — every dimension has a /10 score and at least
   one piece of evidence **quoted from the live site** (never a generic assertion).
2. **RICE scores for all identified gaps** — every gap in the action plan carries an explicit
   `(R × I × C) ÷ E` value and lands in a priority order.
3. **At least one content brief generated, ready to execute** — a complete 9-element prompt for the
   highest-priority page, filled with real data found during the audit.
4. **The report passes the client-ready test** — a business owner who has not read the framework could
   read the executive summary and act on it without further explanation.

Measured on the real DKC audit in `data/audit-dkc-2026-06-01.md`: **DKC scored 67/130**, with
**13/13 dimensions scored from evidence quoted on the live site**, every action-plan gap RICE-scored
(top action 12.15 — the airport-confiscation page), one ready-to-execute content brief, and a
client-ready executive summary. All four gates met.

---

## Inputs and Outputs

| Input | Source | Required |
|-------|--------|----------|
| The site to audit (URL + key pages) | the client / the live web | Yes |
| The market's fears + verified facts (to score D1–D3) | the Source Bank + fear data, or built fresh for a new niche | Yes |
| The 13-skill scoring methodology | `engines/engine-website-audit.md` | Yes |
| Competitor URLs (for the comparison) | the market | No |

| Output | Format | Contains |
|--------|--------|----------|
| Audit report | Markdown | exec summary + 13 dimension scores + detailed findings + RICE action plan + content brief + competitor comparison |

---

## Proof

**Status:** ✅ PROVEN 47/47 — Dubai pet relocation
**Real output:** a complete 130-point audit of **DKC (Dubai Kennels & Cattery — dkc.ae)**, the market
benchmark (Trust Score 8.0/10 in the prior Trust Gap Analysis), produced by visiting the live site —
`data/audit-dkc-2026-06-01.md`. All 13 dimensions scored with evidence quoted from DKC's actual pages;
every gap RICE-scored; a ready-to-execute content brief for DKC's deepest missing page (the
airport-confiscation fear — the Muze Gu scenario the gap matrix flags as missing on 9/9 competitors,
DKC included).
**Threshold result:** **DKC = 67/130** ("market leader by brand and breadth, mid-tier on trust-content"
— reconciles with the prior 8.0/10 Trust Score: best in a weak market, real absolute gaps) · 13/13
dimensions evidenced from the live site · all gaps RICE-scored · 1 content brief (the confiscation page) ·
client-ready exec summary. All four Check-46 gates met.
**Skill Value Score (confirmed on completion):** 22/25.

---

## Environment Variables

```
PROJECT_ROOT=          # absolute path to the project root on this machine

# Optional — only for the automated collectors. The audit's scoring judgement needs no keys;
# a human (or Claude reading the live pages) scores each dimension against the rubric.
ANTHROPIC_API_KEY=     # optional scoring assist + the content-brief draft
SERPAPI_KEY=           # optional — competitor SERP / AI-Overview checks for D11/D13
```

Automation 4/5: page fetching, screenshot capture, schema/structure checks, and the RICE arithmetic
are automatable; **assigning each dimension's /10 and judging client-readiness stay human** (the audit
is an act of evidenced judgement, not a checklist a script can fake). See `files/04-automation-spec.md`.

---

## Standalone Test

Someone in any market can use this skill alone: take a URL, calibrate the risk level (M-04), score the
13 dimensions /10 with evidence quoted from the live site, RICE-rank the gaps, and write one content
brief for the top gap. The method — score every trust dimension with real evidence, then prioritise by
consequence — is fully portable; only the market's fears and verified facts are niche-specific.
