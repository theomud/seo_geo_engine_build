# SKILL COMPLETION DOCUMENT
## Customer Fear Intelligence — proven on Dubai pet relocation

---

## SKILL IDENTITY

**Skill Name:** Customer Fear Intelligence
**Folder:** skill-customer-fear-intelligence/
**Date Started:** 2026-05-26 (keyword discovery + community research began)
**Date Completed:** 2026-05-27 (598-keyword classification run + audit PASS); intent taxonomy expanded 2026-05-29
**Completed By:** Claude Code + human (David)
**Proof Niche:** Dubai pet relocation
**Skill Value Score (confirmed):** 21/25 (Difficulty 3 · Automation 4 · Uniqueness 5 · Commercial 5 · Teachability 4)

---

## PHASE 1 — MARKET RESEARCH

**What was researched:**
- [x] Google search for existing keyword-research and intent-classification frameworks
- [x] Standard keyword tools (Semrush/Ahrefs/Keyword Planner) and what they output
- [x] Published search-intent taxonomies (the 4 Broder buckets)
- [x] What current SEO practice does with keyword lists

**Key findings:**
Standard keyword tools return volume, difficulty, and CPC — they tell you *what* people search, never *what they are afraid of* behind the search. The 4-bucket intent taxonomy (informational/commercial/navigational/transactional) loses the critical nuance in high-stakes regulated markets. The gap this skill fills: it maps every keyword to a visceral, verbatim **fear statement** ("I'm afraid that…") and an expanded **8-type intent** model, then routes each to the right page. No published framework combines multi-source collection + fear-acknowledging classification + intent×fear mapping.

**Sources reviewed:**
| Source | URL | Key Insight |
|--------|-----|-------------|
| External methodology check (project, May 2026) | — | No published SEO framework combines all 5 Trust Engine methods (multi-source collection, fear-acknowledging classification, manual verification, cross-verification, verbatim community language) |
| Broder search-intent taxonomy | — | The standard 4 buckets are insufficient for fear-led regulated markets |
| Google search-intent classification | google.com | Informational/commercial/navigational/transactional — the base extended here with PMT threat appraisal |
| Protection Motivation Theory (Rogers 1975) | — | Severity/susceptibility/efficacy — the academic basis the Fear Hierarchy maps onto (MFP M-20) |

**Market research verdict:**
Novel. Keyword tools and intent taxonomies exist, but none produce a per-keyword fear statement in the customer's own language. The fear layer is what makes the downstream content (Skill 03) convert.

---

## PHASE 2 — COMMUNITY RESEARCH

**Communities searched:**
- [x] Reddit r/dubai, r/UAE
- [x] Facebook group: "Pet Moving and Relocation", "Dog Lovers In UAE"
- [x] Other: PAA questions + Related Searches (fears expressed as queries)

**Screenshots taken:** 69 community screenshots
**Screenshot folder:** research/community/screenshots/ (findings: research/community/2026-05-26-facebook-group-findings.md)

**Key community findings:**
Customers do not arrive curious — they arrive afraid. The research surfaced a 12-fear database spanning confiscation, documentation mistakes, price gouging, airline disaster, pet suffering, timeline pressure, abandonment, and choosing the wrong provider. The same keyword carries different fears for different origin communities (the multi-community insight). Fears were matched to documented community language, never invented.

**Real quotes from community research:**
| Quote | Source | Platform | Date |
|-------|--------|----------|------|
| "without it your dog will be taken away in airport and never give back… Still when I remember I crying" | Muze Gu | Facebook "Dog Lovers In UAE" | 2026-05 |
| "relocation companies are shamelessly charging an insane amount of money" | IrbisKat (24 upvotes) | Reddit r/dubai | 2026-05 |
| "Please do proper research and read reviews before handing over your pet to them" | Curious_cat_2912 (16 upvotes) | Reddit | 2026-05 |
| "Every website says something different — I don't know who to trust" | (community, FB research) | Facebook | 2026-05-26 |

**Community research verdict:**
Confirmed the skill is essential. The deepest fear in the entire dataset — airport confiscation (Muze Gu) — is unaddressed by any competitor and became the #1 priority fear feeding Skill 03's content build.

---

## PHASE 3 — MANUAL VERIFICATION

**What was done manually:**
Manual keyword discovery (Google Autocomplete a–h + PAA + Related Searches for the seed set), then hand-classification of a sample by intent (Column J) and fear (Column K) to calibrate the rubric before automating.

**Manual test date:** 2026-05-26 → 2026-05-27
**Time taken:** ~1–2 days across discovery, classification calibration, and the 15% manual audit
**Who did it:** human + Claude Code

**Step-by-step record:**
1. Collected keywords from multiple sources (Autocomplete, PAA, Related Searches, community).
2. Hand-classified a sample by the 6 intent types; confirmed the rubric and the decision order (urgency → fear → brand → commercial → transactional → default informational).
3. Wrote fear statements by hand for the highest-priority clusters, drawing wording from real community quotes.
4. Manually audited 15% of the highest-priority clusters (these become page headlines/openings).

**Screenshots of manual process:**
| Screenshot | What it shows | File |
|------------|--------------|------|
| Facebook group findings | Source of the 12-fear database + verbatim quotes | research/community/screenshots/ (69 captures) |

**Real output produced:**
The keyword spreadsheet with Columns J (intent) + K (fear) filled — skill-customer-fear-intelligence/data/skill-01-keyword-collection.xlsx (8 tabs, 598 keywords).

**What failed or surprised:**
- The **same keyword carries different fears for different origin communities** (a UK-route searcher vs an Indian-route searcher fear different things) — this multi-community insight became the defensible long-term upgrade (Phase 2 fear database).
- The deepest fear (confiscation) was not hypothetical — it appeared with real distress ("Still when I remember I crying").
- Urgency (2) and Transactional (13) were thinly represented in the 598-row set — a real distribution finding, not a bug.

**Manual verification verdict:**
The method works. The fear statement must be specific and visceral — generic statements ("I'm worried about the process") were rejected in the manual audit. Real community language beats invented language every time.

---

## PHASE 4 — AUTOMATION

**What was automated:**
Bulk intent + fear classification of all 598 keywords. The engine reads Column A, classifies intent, and writes a fear statement to Column K, drawing on the 12-fear community database.

**Engine built:** yes — fear_classification_engine.py (run log: fear_classification_log.txt); keyword collection via keyword_engine.py. *(Both engines currently live at repo root — see packaging note in Skill Status.)*
**Automation level:** ~80% classified automatically; ~20% (Fear/Urgency clusters + brand keywords) reviewed by hand
**Cost per run:** low — Anthropic claude-sonnet-4-6, 598 single-keyword classifications
**Time per run:** the full 598-keyword run completed in one session (run start 2026-05-27 08:21)

**Automation test results:**
- Keywords classified: **598 / 598** (Column J intent + Column K fear), **0 errors**.
- Intent breakdown (original 6-type run): Informational 275 · Commercial 147 · Research 147 · Fear 14 · Transactional 13 · Urgency 2.
- Audit sub-agent verdict: **PASS** — 100% of fears start with "I'm afraid", all ≤30 words, all 6 intent types present, 78% of fear statements unique (top duplicate ×11).

---

## PHASE 5 — AUDIT RESULTS

**Audit date:** 2026-05-29 (45-check Skill Auditor, post-packaging) · fear-classification audit 2026-05-27
**Audited by:** independent sub-agent (did not build the skill)
**Audit report:** skill-customer-fear-intelligence/SKILL-AUDIT-REPORT.md; fear-classification audit also logged in files/03-fear-formula.md "Test Results Log"

**Scores (45-check Skill Auditor — post-packaging re-audit):**
| Layer | Score | Status |
|-------|-------|--------|
| Layer 1 — Skill Completeness | 20/20 | ✅ PASS |
| Layer 2 — Learner Guide | 15/15 | ✅ PASS |
| Layer 3 — Cheatsheet | 10/10 | ✅ PASS |
| **OVERALL** | **45/45** | ✅ PASS |

**Failed checks and fixes applied:** (first benchmark 33/45 → re-audit 45/45 after packaging)
| Check # | What failed | Fix applied | Date fixed |
|---------|-------------|-------------|------------|
| 1, 6–9, 11–15 (Layer 1) | Spec files 01–05 + engines + output were not inside the skill folder | Moved spec files → files/, engines + run log → engines/, output xlsx in data/ | 2026-05-29 |
| 1, 3, 4 (Layer 1) | No skill README.md or .env.example | Created README.md (with the confirmed 5-dimension scorecard) + .env.example (real vars) | 2026-05-29 |
| 5 (Layer 1) | No customer-profile snapshot in skill | Built customer-profile/customer-profile-snapshot.md (excerpts only) | 2026-05-29 |
| (intent taxonomy) | 6 intent types | Expanded to 8 (added Problem, split Urgency/Emergency); 598-row re-classification pass still flagged | 2026-05-29 (spec); re-run pending |

**Non-blocking note from the re-audit:** intent study-manual 02 / cheatsheet 02 still teach the legacy 6 intent types (the spec + xlsx now use 8) — a recommended guide refresh; it did not affect the score.

---

## REAL OUTPUT EVIDENCE

**Output file:** data/skill-01-keyword-collection.xlsx
**Output stats:** 598 keywords, 8 tabs, Columns J (intent) + K (fear) populated
**Date produced:** 2026-05-27
**Niche:** Dubai pet relocation

**What the output contains:**
598 validated keywords each with an intent classification and a verbatim-grounded fear statement, plus supporting tabs (Autocomplete, PAA, Related Searches, Community Language). Real run evidence in fear_classification_log.txt (116 KB).

**Screenshot evidence:**
69 community screenshots in research/community/screenshots/ — the source of the 12-fear database and every verbatim quote used.

---

## WHAT THIS SKILL PROVED

**The core finding:**
Behind every keyword is a person in a specific emotional state. Classifying intent tells you what they want to find; mapping fear tells you what they are afraid of — and only the fear layer makes downstream content convert. A keyword like "pet relocation Dubai to India" is not an information request; it is "I'm afraid the paperwork has a mistake that gets my dog rejected at the border."

**What changed from the original spec:**
- Intent types expanded **6 → 8** (added **Problem**; split **Urgency → Urgency + Emergency**) on 2026-05-29; the legacy 598 rows need a re-classification pass for the two new types.
- The multi-community fear database (Phase 2) was added as the defensible long-term upgrade after manual testing showed the same keyword carries different fears per community.

**What competitors or published frameworks do not do:**
No keyword tool outputs a fear statement. No standard intent taxonomy captures Fear/Urgency/Emergency/Problem as distinct, page-determining types. The "I'm afraid that…" formula tied to verbatim community language is unique to this skill.

---

## LEARNER GUIDE AND CHEATSHEET

**Study manual built:** yes — skill-customer-fear-intelligence/guides/ (skill-02 Intent Classification, skill-03 Fear Formula, skill-04 Sorting Funnel, skill-05 Volume Validation study manuals)
**Cheatsheet built:** yes — matching cheatsheets for each (intent decision tree; 12 fears + "I'm afraid that…" starters; intent+fear→page brief; volume rules)

**Real proof used in the guide:**
The 12-fear database, real community quotes (Muze Gu, IrbisKat), the 598-keyword intent breakdown, and the "I'm afraid that…" formula with real examples.

**Phone test result:**
Layer 3 (cheatsheet) scored 8/10 PASS in the 45-check benchmark — renders at 390px.

---

## HOW TO APPLY TO A NEW NICHE

**What changes per niche:**
- The seed keywords and the communities searched (that market's Reddit/Facebook)
- The fear database (that market's verbatim community language)
- The intent/fear distribution

**What stays the same:**
- Multi-source keyword collection, the 8-type intent model, the "I'm afraid that…" Fear Formula
- The classify-then-fear-map order, the sorting funnel, the 15% manual audit
- The engines (point them at new seeds)

**Time estimate for a new niche:**
Manual: ~1–2 days (discovery + classification calibration + 15% audit)
Automated: one classification run for the full keyword set

---

## SKILL STATUS

**Status:** ✅ PROVEN — clean 45/45 on the 45-check Skill Auditor (all 3 layers pass), on top of the 598-keyword run + fear-classification audit PASS
**Ready to sell:** yes
**Ready to teach:** yes
**Next review date:** 2026-08-27 (90 days from completion)

**Packaging note:** the skill was fully packaged into its folder on 2026-05-29 — spec files 01–05 → files/, engines + run log → engines/, output xlsx in data/, README.md + .env.example + customer-profile snapshot added — taking the 45-check audit from a 33/45 benchmark to a clean **45/45**. One recommended follow-up remains (non-blocking): refresh intent study-manual 02 / cheatsheet 02 to teach all 8 intent types (they still show the legacy 6).

---

## SIGN-OFF

Completed by: Claude Code + David
Date: 2026-05-29
GitHub commit: committed in "feat: complete customer-fear-intelligence packaging, add README, .env, re-audit to PROVEN"
