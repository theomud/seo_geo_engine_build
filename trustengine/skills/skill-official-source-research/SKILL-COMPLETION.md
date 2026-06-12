# SKILL COMPLETION DOCUMENT
## Official Source Research — proven on Dubai pet relocation

---

## SKILL IDENTITY

**Skill Name:** Official Source Research
**Folder:** skill-official-source-research/
**Date Started:** 2026-05-28 (Source Bank build began)
**Date Completed:** 2026-05-29 (live screenshot capture + re-verification + 45-check audit PASS)
**Completed By:** Claude Code + human (David)
**Proof Niche:** Dubai pet relocation
**Skill Value Score (confirmed):** 19/25 (Difficulty 3 · Automation 3 · Uniqueness 4 · Commercial 5 · Teachability 4)

---

## PHASE 1 — MARKET RESEARCH

**What was researched:**
- [x] Google search for existing fact-verification / citation workflows
- [x] How competitors source and cite regulation claims (they mostly don't)
- [x] Google Search Quality Rater Guidelines (factual accuracy, YMYL)
- [x] Standard practice for content fact-checking

**Key findings:**
Generic fact-checking confirms a statement is "true." This skill confirms a statement matches a **named, dated, official** source, and is done *before* writing starts — producing a reusable **Source Bank** rather than a one-off note. No competitor in the niche publishes their source set, so a verified Source Bank is a defensible, licensable asset on its own.

**Sources reviewed:**
| Source | URL | Key Insight |
|--------|-----|-------------|
| Google Search Quality Rater Guidelines | google.com | Factual accuracy + YMYL; pet relocation is YMYL-adjacent → maximum proof burden |
| Project methodology check (May 2026) | — | No published framework combines all 5 Trust Engine methods (incl. cross-verification + manual-before-automation) |
| Official regulators (MOCCAE, gov.uk, DAFF, etc.) | per Source Bank | The only acceptable sources — government body / destination authority / operating airline / recognised industry body |

**Market research verdict:**
Novel + improved. Fact-checking exists; a structured, dated, screenshot-backed Source Bank built upstream of writing — with explicit Verified / Unverifiable / Conflicting statuses — does not.

---

## PHASE 2 — COMMUNITY RESEARCH

**Communities searched:**
- [x] Reddit r/dubai, r/UAE
- [x] Facebook groups (pet relocation / Dog Lovers In UAE)
- [x] Competitor pages (claims to verify)

**Screenshots taken:** 143 live official-source screenshots (this skill) + 69 community screenshots (upstream research)
**Screenshot folder:** skill-official-source-research/data/source-screenshots/ (+ data/verification-screenshots/)

**Key community findings:**
The claims that needed verifying came from what customers and competitors actually assert — prices, timelines, breed rules. Verifying them surfaced **conflicts between community belief and official publication**, which are the most valuable rows in the bank.

**Real quotes / conflicts from research:**
| Claim | Community said | Official source said | Action |
|-------|---------------|---------------------|--------|
| Etihad cabin pet fee (C-015) | USD 1,500 | USD 399 promotional (official Etihad pets page, to 31 May 2026) | Unverifiable + conflict flagged |
| Air Cairo advance notice (C-017) | "no pre-flight communication needed" | "Pets not registered in advance may not be accepted" (official Air Cairo page) | Unverifiable + conflict flagged |
| Rabies titer cost (C-001) | 700–1,300 AED | MOCCAE publishes no figure | Unverifiable (hedge in content) |

**Community research verdict:**
Confirmed the skill protects customers: acting on the community's $1,500 Etihad figure or the "no advance notice" Air Cairo belief would cost money or a missed flight. The Source Bank catches both.

---

## PHASE 3 — MANUAL VERIFICATION

**What was done manually:**
Visited each official source in a **real browser** (not a headless fetcher), re-derived the correct current URL for each authority, found the exact phrase, copied the verbatim quote, recorded the row, and captured a screenshot.

**Manual test date:** 2026-05-28
**Time taken:** ~4–8 hours for the initial Source Bank across 27 countries
**Who did it:** human + Claude Code (Claude in Chrome)

**Step-by-step record:**
1. Built the claim list (153 claims) from community + competitor research.
2. Mapped each claim to the regulating authority via the source hierarchy.
3. Re-derived correct URLs with the 4-slot search formula when stored links were dead (authority name + country + content type + local-language term + `site:` filter).
4. Opened each in a real browser; classified by the 3-outcome loop (loads-with-content / wrong-page / domain-unreachable); copied verbatim quotes; captured screenshots.

**Screenshots of manual process:**
| Screenshot | What it shows | File |
|------------|--------------|------|
| GOV.UK bring-a-pet | Verified quarantine rule on the official page | data/source-screenshots/UK-gov-uk-C-024-2026-05-28.png |
| MOCCAE import-of-pets | Loads perfectly but is SILENT on titer cost → proof the cost is community-sourced | data/source-screenshots/UAE-moccae-gov-C-001-2026-05-28.png |
| Etihad pets page | Official USD 399 fee vs community's USD 1,500 (conflict) | data/source-screenshots/UAE-etihad-com-C-015-2026-05-28.png |

**Real output produced:**
The Source Bank — data/skill-02-source-bank.xlsx (153 claims) + data/source-screenshots/SOURCE-INDEX.md (per-claim status, URL, screenshot, size).

**What failed or surprised:**
- **A failed URL almost never means the information doesn't exist — it means the wrong address.** Government sites had migrated domains (Austria verbrauchergesundheit.gv.at → bavg.gv.at; India animalquarantineindia.gov.in → aqcsindia.gov.in). Re-deriving the URL recovered them.
- **A real browser distinguishes three outcomes a headless script blurs into one "fail"** — this is why the original headless engine returned 47 "Pending — load failed" rows that were mostly just wrong addresses or JS-rendered pages.
- **2 domains were genuinely unreachable even in a real browser** (Belgium health.belgium.be HTTP/2 error; Jordan moa.gov.jo timeout) → 10 rows marked FAILED with the exact reason — the failure is itself evidence the claim is community-sourced only.

**Manual verification verdict:**
The method works and produced File 05 (the manual verification recipe) as a reusable artifact. The one spec change: screenshots, originally a known gap with headless capture, are now captured via headed Playwright + `networkidle`.

---

## PHASE 4 — AUTOMATION

**What was automated:**
URL visiting, text extraction, claim-matching, status proposal, and **live full-page screenshot capture**.

**Engine built:** yes — engines/source_research_engine.py (spec: engines/engine-source-research.md); screenshots via the headed-Playwright capture tool (143 captured this session)
**Automation level:** 70% (humans keep URL mapping, legal-language interpretation, conflict resolution, final plain-English approval)
**Cost per run:** ≈ $0.001–0.003 per claim (Anthropic); a full re-verification run < $0.30
**Time per run:** 5–15 minutes for the full bank

**Automation test results:**
The engine verifies cooperative government sites cleanly; cert-broken / JS-rendered / WAF-blocked sites are routed to human review (a fifth engine-only "Manual review required" status). The 143 live screenshots were captured headed (Chromium 148, `ignore_https_errors`, `wait_until=networkidle`); 30 of 32 unique URLs captured, 2 domains (Belgium, Jordan) FAILED — corroborating their Unverifiable status.

---

## PHASE 5 — AUDIT RESULTS

**Audit date:** 2026-05-29
**Audited by:** independent sub-agent (did not build the skill)
**Audit report:** skill-official-source-research/SKILL-AUDIT-REPORT.md

**Scores:**
| Layer | Score | Status |
|-------|-------|--------|
| Layer 1 — Skill Completeness | 20/20 | ✅ PASS |
| Layer 2 — Learner Guide | 15/15 | ✅ PASS |
| Layer 3 — Cheatsheet | 10/10 | ✅ PASS |
| **OVERALL** | **45/45** | ✅ PASS |

**Failed checks and fixes applied:** none — all 45 pass on first 45-check audit (the skill was already fully packaged with standard file naming 01–06).

---

## REAL OUTPUT EVIDENCE

**Output file:** data/skill-02-source-bank.xlsx (+ data/source-screenshots/SOURCE-INDEX.md)
**Output stats:** 153 claims across 27 countries — **51 Verified · 102 Unverifiable · 0 Pending**
**Date produced:** 2026-05-28 (verified), live screenshots 2026-05-29
**Niche:** Dubai pet relocation

**Data evolution (real, worth recording):** the Phase-1 automated run produced **7 Verified / 99 Unverifiable / 47 Pending**. This session's manual re-verification + 143 live headed-browser screenshots resolved all 47 Pending and re-verified the bank, lifting it to **51 Verified / 102 Unverifiable / 0 Pending**. The jump from 7→51 Verified is the measurable payoff of manual-in-a-real-browser over headless fetching.

**What the output contains:**
Per claim: the statement, the official URL, date checked, verbatim quote, plain-English translation, status, and a dated full-page screenshot (or a FAILED note with the exact failure for the 10 unreachable rows).

**Screenshot evidence:**
143 live full-page screenshots in data/source-screenshots/, spanning 27 countries (UAE + 26 destinations), each named `[country]-[authority]-[claim-id]-[date].png`, with sizes recorded in SOURCE-INDEX.md (a real byte size = a real render).

---

## WHAT THIS SKILL PROVED

**The core finding:**
In a regulated market, the scarce asset is not information — it is *proof*. A dated screenshot of an official page (even one that is SILENT on a claim) is what converts an assertion into evidence. And a "failed" source is almost always the wrong address, not missing information — re-deriving the URL recovers it.

**What changed from the original spec:**
- Screenshots, originally flagged as the one gap (headless capture failed on JS-rendered pages), are now captured via headed Playwright + `networkidle` — closing the gap File 05 identified.
- File 05 (the manual verification recipe) was added as a reusable artifact discovered during the proof run.

**What competitors or published frameworks do not do:**
No competitor publishes their source set, and generic fact-checking neither dates its sources nor records Unverifiable/Conflicting as first-class statuses. The Conflicting rows (Etihad $399 vs $1,500; Air Cairo advance notice) are unique, customer-protecting findings.

---

## LEARNER GUIDE AND CHEATSHEET

**Study manual built:** yes — skill-official-source-research/guides/skill-02-study-manual.html (incl. the Source Evidence gallery + the File 05 manual-verification recipe)
**Cheatsheet built:** yes — skill-official-source-research/guides/skill-02-cheatsheet.html (5 fields · statuses · source hierarchy · 5 gates)

**Real proof used in the guide:**
The Verified (UK gov.uk), Unverifiable-but-loaded (MOCCAE silent on cost), and Conflicting (Etihad $399 vs $1,500) screenshots; the 5 gates; the source hierarchy.

**Phone test result:**
Layer 3 (cheatsheet) scored 10/10 — renders at 390px, all text ≥12px, no horizontal scroll.

---

## HOW TO APPLY TO A NEW NICHE

**What changes per niche:**
- The authorities (each market's regulators / destination authorities / operators)
- The claim list (that market's community + competitor assertions)
- The local-language terms in the 4-slot search formula

**What stays the same:**
- The Source Bank model (URL + date + quote + plain English), the Verified/Unverifiable/Conflicting statuses
- The source-authority hierarchy, the 4-slot search formula, the 3-outcome classify loop, the 5 gates
- The engine (headed Playwright + Anthropic) and the 90-day re-verification cadence

**Time estimate for a new niche:**
Manual: ~4–8 hours for the initial bank
Automated: 5–15 minutes per re-verification run

---

## SKILL STATUS

**Status:** ✅ PROVEN — clean 45/45 on the 45-check Skill Auditor (all 3 layers pass)
**Ready to sell:** yes
**Ready to teach:** yes
**Next review date:** 2026-08-27 (90 days; government sites re-verified quarterly per the cadence rule)

**Note:** the README result table still narrates the Phase-1 counts (7/99/47); the live Source Bank is 51 Verified / 102 Unverifiable / 0 Pending. A README refresh to match the current xlsx is recommended (non-blocking; did not affect the audit).

---

## SIGN-OFF

Completed by: Claude Code + David
Date: 2026-05-29
GitHub commit: committed in "feat: complete official-source-research packaging and completion doc, update all 3 proven skills to PROVEN status in SKILL-COMPLETE-LIST"
