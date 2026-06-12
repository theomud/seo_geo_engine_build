# SKILL 02 — OFFICIAL SOURCE RESEARCH
## Dubai Pet Relocation — Reference Implementation

---

## What This Skill Is

Official Source Research builds the Source Bank — a verified database where
every regulation claim is confirmed against an official government or airline
source before it appears in any content.

In regulated service markets, wrong information does not just lose a sale —
it causes real harm. A pet owner who follows incorrect advice may have their
animal confiscated at the border. This skill exists to prevent that.

The Source Bank is the only approved source of truth for content writers.
Nothing gets published without a Source Bank entry.

**Skill Value Score: 19/25** *(confirmed post-build — not estimated)*
- Difficulty: 3/5
- Automation Potential: 3/5 — cooperative gov sites verify cleanly; cert-broken/JS-rendered/WAF-blocked sites still require human review
- Market Uniqueness: 4/5 — no competitor publishes their source set; defensible asset
- Commercial Value: 5/5 — Source Bank is licensable on its own
- Teachability: 4/5 — methodology is 5 fields + 5 gates; copyable per niche

**Status:** ✅ Proven on Dubai pet relocation — 2026-05-28
**Niche-agnostic:** Yes — every regulated market has official sources

## Phase 1 + 2 Results (2026-05-28)

**153 claims across 27 authorities** (UAE + 26 destination countries):

| Outcome | Count | Detail |
|---|---:|---|
| Verified | 51 | Confirmed against the live official page in a real browser (e.g. UK gov.uk, France DGDDI, Norway Mattilsynet, Portugal DGAV, Austria BAVG, …) |
| Unverifiable | 102 | No official source publishes the specific claim, or the domain is unreachable — honest finding, written as "No official source publishes this; community-sourced range is …" |
| Pending | 0 | All resolved on 2026-05-29 via real-browser re-verification + live headed-Playwright screenshots (the Phase-1 run had 47 Pending) |

*Data evolution: the Phase-1 automated run produced 7 Verified / 99 Unverifiable / 47 Pending; manual re-verification + live screenshots lifted it to **51 Verified / 102 Unverifiable / 0 Pending**.*

**143 live full-page screenshots** saved to `data/source-screenshots/` with `[country]-[authority]-[claim-id]-[date].png` naming (10 rows FAILED — Belgium and Jordan domains unreachable even in a real browser; the FAILED note is itself the evidence). `SOURCE-INDEX.md` records each screenshot's filename + byte size.

**Key methodological finding:** out of 21 destination countries × 5 facets, exactly **1** facet was verifiable from a top-level URL. The rest need either deep-link mapping (a human task) or the page genuinely doesn't carry that fact. **This is the value the Source Bank surfaces** — competitor pages routinely claim things no official authority publishes, and the Bank gives content writers the precise language to hedge instead of fabricate.

---

## What Goes In

| Input | Source | Format | Required |
|-------|--------|--------|---------|
| Community claims to verify | research/community/ + 69 screenshots | .md | Yes |
| Competitor claims | research/competitors/COMPETITOR-MASTER.html | .html | Yes |
| Official source URLs | MOCCAE, airlines, destination authorities | URLs | Yes |

---

## What Comes Out

| Output | Destination | Format | Description |
|--------|-------------|--------|-------------|
| Source Bank | skill-02/data/skill-02-source-bank.xlsx | .xlsx | Every verified claim |
| Verification log | skill-02/source_verification_log.txt | .txt | Every URL checked + date |

---

## How To Do This Manually

**Time required:** 4-8 hours for initial build, 30 min/month to maintain
**Tools needed:** Browser, moccae.gov.ae, airline policy pages
**Skill level:** Intermediate

1. List every regulation claim from community research (69 screenshots)
2. Find the official source URL for each claim
3. Visit the URL and find the exact relevant text
4. Record: URL + date + exact quote + plain English translation
5. Flag any conflicts between community data and official data
6. Mark as Verified, Unverifiable, or Conflicting

---

## How To Automate

**Automation level:** 70% — Playwright visits URLs, Anthropic extracts claims
**What stays manual:** Judgment on conflicting sources, interpreting legal language
**Audit required:** Yes — audit agent checks 20% of verified claims manually

APIs used:
- Playwright: visits official source URLs, extracts page text
- Anthropic API: matches extracted text against pending claims

---

## APIs and Tools

| Tool | Purpose | Cost | Phase |
|------|---------|------|-------|
| Playwright | Visit + extract official source pages | Free | Active |
| Anthropic API | Match claims to source text | ~$0.10/run | Active |

**Can Chrome help?** Yes — visit moccae.gov.ae manually for complex pages.
Playwright handles straightforward pages. Human handles government portals
that require login or have CAPTCHAs.

---

## Environment Variables Needed

```
ANTHROPIC_API_KEY=     # Already in .env — shared
PROJECT_ROOT=          # Already in .env — shared
SKILL_NUMBER=02
SKILL_SPREADSHEET=skill-02-source-bank.xlsx
```

No additional keys needed for this skill.

---

## Official Sources for This Niche

| Source | URL | What It Covers |
|--------|-----|---------------|
| MOCCAE | moccae.gov.ae | All UAE pet import/export |
| MOCCAE Export Page | site.moccae.gov.ae/en/services/export-import-services/... | Export permit process |
| Emirates | emirates.com/ae/english/travel-information/travelling-with-pets | Emirates pet policy |
| Etihad | etihad.com/en-ae/fly-etihad/pets | Etihad pet policy |
| Turkish Airlines | turkishairlines.com | Cabin pet policy |
| Royal Jordanian | rj.com | Cabin pet policy + fees |
| UK APHA | apha.gov.uk | UK pet import requirements |
| India DAHD | dahd.gov.in | India pet import |
| Australia DAFF | agriculture.gov.au | Australia pet import |
| IPATA | ipata.com | Industry standards |

---

## Claims To Verify (Priority Order)

### PRICING DISCREPANCIES
- [ ] Titer test cost: 700 AED (community) vs 1,300 AED (community)
- [ ] MOCCAE vet release fee: 500 AED (community)
- [ ] Fit to fly certificate: 200 AED (community)

### TIMELINE CONFLICTS
- [ ] Titer test results: 1 week vs 2-3 weeks
- [ ] Vaccine timing before travel: 21 days vs 30 days
- [ ] Cargo Village health cert validity: 10 days
- [ ] Import permit validity: 90 days (DKC)

### PROCESS QUESTIONS
- [ ] Does pet need to physically go to MOCCAE for export?
- [ ] Can pet passport be prepared with no travel date set?
- [ ] What breeds are restricted by Emirates — official list?
- [ ] Is excess baggage into Dubai possible or always cargo?

### AIRLINE-SPECIFIC
- [ ] Etihad cabin pet fee: current price
- [ ] Royal Jordanian from Dubai: $100 USD — confirm current price
- [ ] Air Cairo: no pre-communication needed — confirm
- [ ] Sharjah airport process time: 20 minutes — confirm standard

---

## Customer Profile — Relevant Excerpts

**Fears most relevant to this skill:**
- Documentation mistake fear — wrong info = pet rejected at border
- Overwhelm fear — conflicting information from different sources
- Price gouging fear — no transparency on what things actually cost

**Community quotes that drive this skill:**
- "Every website says something different — I don't know who to trust" — r/dubai
- "I am being quoted endless amounts for a plain test" — 7Ssisi, Reddit
- "Please do all the paperwork especially important rabies titers without it
  your dog will be taken away in airport and never give back" — Muze Gu, Facebook

**Most relevant persona:** Persona 4 — The Confused Researcher
Fear: "What if I follow the wrong advice?"
Message: "We check destination-specific rules and build the correct process"

Full profile: customer-profile/01-master-customer-profile.md

---

## Functional Quality Threshold

This skill is functional when 100% of facts in the Source Bank (`data/skill-02-source-bank.xlsx`) carry a C-ID, a candidate official-source URL, and a verification date, and every **Verified** fact is backed by a live full-page screenshot in `data/source-screenshots/` (or `verification-screenshots/`). Minimum scale: ≥50 facts verified against live official sources. **Measured 2026-05-29: 153 facts, all (100%) with C-ID + URL + date; 51 Verified, all (100%) screenshot-backed; 143/153 facts (93%) screenshot-backed overall — the 10 without screenshots are the Belgium and Jordan rows whose official domains were unreachable in a real browser, recorded as FAILED (the failure note is the evidence). Threshold MET.**

**Independence Test (Check 47): NOT YET TESTED** — only the original builder has produced the Source Bank; no second person has independently re-verified the facts. Acceptable addressed state for PROVEN; blocks COMMERCIALLY READY until TESTED.

---

## Verification Checklist

- [x] Manual process documented (files/01-04) with screenshot evidence
- [x] Source Bank spreadsheet built with all pending claims (153 rows)
- [x] Automated verification engine tested on 5 claims (Phase 1 test pass)
- [x] All MOCCAE claims **attempted** against moccae.gov.ae (16 Unverifiable + 7 Pending — homepage doesn't carry specifics; deep pages cert/JS-blocked)
- [x] All airline claims **attempted** against official airline pages (Emirates, Etihad, Royal Jordanian, Flydubai, Air Cairo)
- [x] Conflicting / pricing claims documented with the standard hedging note ("No official source publishes this cost. Community-sourced price range: ...")
- [x] Phase 1 full run completed (48 rows · 6 Verified · 20 Unverifiable · 22 Pending)
- [x] Phase 2 full run completed (105 rows · 1 Verified · 79 Unverifiable · 25 Pending)
- [x] Full-page screenshots saved for every URL attempted (153 PNGs)
- [x] SOURCE-INDEX.md auto-generated from the spreadsheet
- [x] Study manual built (`guides/skill-02-study-manual.html`)
- [x] Cheatsheet built (`guides/skill-02-cheatsheet.html`)
- [x] Git committed and pushed
- [ ] *Future:* deep-link mapping for European/regional destination authorities (move ~50 Unverifiable rows toward Verified)
- [ ] *Future:* manual browser verification of the 47 Pending rows (sites blocked headless)
- [ ] *Future:* formal audit sub-agent re-verification of the 7 Verified rows on 90-day cadence
