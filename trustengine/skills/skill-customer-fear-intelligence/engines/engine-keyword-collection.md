---
Status: building
Area: skill-01
Priority: high
Activation: immediate
Last updated: 2026-05-26
Depends on: skill-01/01-google-search-discovery.md
Feeds into: skill-01-keyword-collection.xlsx, skill-01/02-intent-classification.md
---

# Skill 01 — Engine: Keyword Collection

---

## Purpose

Automates everything done manually in Sessions 1 and 2. Runs across all 27 seed keywords.
The manual sessions are the verification baseline. Engine output must match manual results at 80%+.

---

## Pre-Verified Manual Baseline

**Session 1 — Autocomplete + Alphabet a–h:**
- Blue Sky appears in letter b ✓
- DKC appears in letter d ✓
- Letter f returns 8 export destinations ✓
- India appears across 7 letters ✓

**Session 2 — PAA + Related Searches:**
- "Are people leaving pets behind in Dubai?" in PAA ✓
- "JetSet pets Dubai" in Related Searches ✓
- "careers" flagged as negative ✓
- CarryMyPet.ae ranking organically ✓

**Engine pass criteria:** All 8 baseline items confirmed in output = PASS. Any missing = INVESTIGATE before full run.

---

## Seasonal Intelligence (from Google Trends — verified 2026-05-26)

- Peak season: October–April (cooler months, airlines permit pet cargo)
- Dead season: June–September (summer embargo)
- Current status: May 2026 = entering dead season, value = 0
- Market trend: GROWING — 2025/2026 spikes 3–4× larger than 2022/2023
- Next surge: September/October 2026
- Column H default for all pet cargo keywords: Oct–Apr

---

## API Decision (verified from live manual testing)

| What We Need | Unofficial Google API | SerpApi |
|-------------|----------------------|---------|
| Autocomplete | ✅ | ✅ |
| Alphabet expansion | ✅ | ✅ |
| Question prefixes | ✅ | ✅ |
| People Also Ask | ❌ | ✅ |
| Related Searches | ❌ | ✅ |
| Organic results | ❌ | ✅ |
| Competitor detection | Autocomplete only | All sources |
| Negative detection | Autocomplete only | All sources |
| UAE targeting | ⚠️ Best effort | ✅ Reliable |
| Reliability | No SLA — can break | 99.95% SLA |

**SerpApi = primary. Unofficial Google API = autocomplete cross-check only.**

Proof: JetSet Pets Dubai and CarryMyPet.ae were found by SerpApi (Related Searches + Organic). The unofficial API cannot access these sources and would have missed both competitors entirely.

---

## The 27 Seeds (seeds.txt)

```
pet relocation Dubai
pet transport Dubai
pet shipping Dubai
pet movers Dubai
dog relocation Dubai
cat relocation Dubai
bring dog to Dubai
bring cat to Dubai
how to move a dog to Dubai
Dubai pet import rules
best pet relocation company Dubai
pet relocation Dubai cost
is it safe to fly a dog to Dubai
emergency pet relocation Dubai
pet relocation from Dubai to UK
pet relocation from Dubai to India
pet relocation from Dubai to South Africa
pet relocation from Dubai to Australia
Blue Sky pet relocation Dubai
JetSet pets Dubai
DKC pet relocation Dubai
CarryMyPet Dubai
Emirates pet policy
Etihad pet travel
UAE pet import requirements
pet quarantine Dubai
pet passport Dubai
```

---

## Complete Engine Architecture

```
INPUT
  seeds.txt — 27 seed keywords, one per line
  .env file in project root — all API keys loaded via python-dotenv
  skill-01-keyword-collection.xlsx — write target

FOR EACH SEED:

  CALL 1 — SerpApi autocomplete (base)
    engine=google_autocomplete, q={seed}, gl=ae, hl=en

  CALL 2 — Unofficial Google autocomplete (comparison)
    GET suggestqueries.google.com/complete/search
    ?client=firefox&hl=en&gl=ae&q={seed}
    Parse index [1] for suggestions list

  CALLS 3a–3z — Alphabet expansion (SerpApi)
    For each letter a–z:
    engine=google_autocomplete, q="{seed} {letter}", gl=ae, hl=en

  CALLS 4a–4g — Question prefixes (SerpApi)
    For each: how / can / will / is / what / why / does
    engine=google_autocomplete, q="{prefix} {seed}", gl=ae, hl=en

  CALL 5 — Full SERP (SerpApi)
    engine=google, q={seed}, gl=ae, hl=en, num=10
    Returns: PAA + Related Searches + Organic + SERP features

PROCESSING
  Deduplication: if keyword exists → update source + increment count
  Negative filter: trigger words → Sheet 5 only
  Competitor flag: unknown brands → Notes column + Sheet 6
  API comparison: SerpApi vs unofficial → Sheet 4

OUTPUT — 8 sheets
  Sheet 1: Keyword Collection
  Sheet 2: People Also Ask
  Sheet 3: Related Searches
  Sheet 4: Comparison Report (SerpApi vs unofficial)
  Sheet 5: Negative Keywords
  Sheet 6: Competitors Found
  Sheet 7: SERP Features
  Sheet 8: Organic Results

TOTAL CALLS: 36 per seed × 27 seeds = 972
RATE LIMITING: 1s between SerpApi calls, 0.5s between unofficial calls
SAVE: every 5 seeds — if Excel fails, save to backup CSV
```

---

## Negative Trigger Words

```
jobs, salary, vacancies, careers, volunteer, DIY,
free, van hire, wanted, apply, hiring, recruitment
```

---

## Test Protocol

**Phase 1 — Single seed validation (mandatory)**
Run on "pet relocation Dubai" only.
Verify all 8 baseline items above.
Review Sheet 4 comparison report.
Pass = 80%+ match. Fail = fix before continuing.

**Phase 2 — Three seed audit**
Run on 3 seeds: "pet relocation Dubai" + "dog relocation Dubai" + "pet relocation from Dubai to India"
Manually review every sheet.
Check deduplication is working.
Check negatives are routing correctly.
Check competitors are being flagged.

**Phase 3 — Full run**
Run all 27 seeds only after Phase 2 passes.
Full audit after completion.

---

## Post-Run Audit Checklist

After every run, verify all of these:

**Data integrity:**
- [ ] No duplicate rows in Sheet 1 (same keyword twice)
- [ ] Source Count is accurate — keywords in multiple sources have count > 1
- [ ] All keywords with "careers", "jobs", "salary" are in Sheet 5 only
- [ ] Blue Sky, DKC, JetSet Pets, CarryMyPet flagged in Sheet 6

**Baseline verification (Phase 1 only):**
- [ ] Blue Sky appears in Sheet 1 from letter b run
- [ ] DKC appears in Sheet 1 from letter d run
- [ ] "Are people leaving pets behind in Dubai?" in Sheet 2
- [ ] "JetSet pets Dubai" in Sheet 3
- [ ] "careers" in Sheet 5 — NOT in Sheet 1
- [ ] Letter f run returns 8+ export destinations
- [ ] India appears across multiple letter runs
- [ ] CarryMyPet.ae appears in Sheet 8 (organic results)

**Sheet 4 — API Comparison:**
- [ ] Match rate calculated for "pet relocation Dubai"
- [ ] SerpApi-only keywords listed (these are from PAA, Related, Organic — not accessible to unofficial API)
- [ ] Unofficial-only keywords listed (should be near zero — if high, investigate)

**Sheet 7 — SERP Features:**
- [ ] "pet relocation Dubai" has PAA = TRUE
- [ ] Local pack status noted
- [ ] Ads present status noted

**Final counts (record in Test Results Log):**
- [ ] Total unique keywords in Sheet 1
- [ ] Total PAA questions in Sheet 2
- [ ] Total related searches in Sheet 3
- [ ] Total negatives in Sheet 5
- [ ] Total competitors in Sheet 6
- [ ] SerpApi credits used

---

## Test Results Log

### Phase 1 Test — Single Seed
Date: 2026-05-27
Seed: pet relocation Dubai
Keywords collected: 83
PAA questions: 4
Related searches: 8
Negatives detected: 2 (jobs, careers)
Competitors flagged: 9 entries (Blue Sky, DKC, JetSet Pets, CarryMyPet)
SerpApi vs unofficial match rate: 56.2% (SerpApi=15, Unofficial=10, matched=9, SerpApi-only=6, Unofficial-only=1)
Baseline items passed: 8/8
Audit (independent sub-agent): 15/15 checks PASS = 100%
Decision: PASS

### Phase 2 Test — Three Seeds
Date: 2026-05-27
Seeds tested: pet relocation Dubai (rerun), dog relocation Dubai, pet relocation from Dubai to India
Total keywords: 107 (83 -> 107; seed 1 rerun added 0 new rows)
Deduplication working: YES (seed 1 rerun = 0 new rows; "pet relocation dubai" source count incremented 3->4, single row)
Negatives routing correctly: YES (0 trigger words in Sheet 1; both negatives in Sheet 5 only)
Competitors flagging correctly: YES (Blue Sky, DKC, JetSet Pets, CarryMyPet, Pawsome Pets UAE)
Issues found: None. 0 errors. All 3 seeds in Sheet 4 (rates 56.2/64.3/62.5%). Cols J/K empty, Col H populated all 107 rows.
Audit (independent sub-agent): 8/8 checks PASS = 100%
Decision: PASS

### Phase 3 — Full Run
Date: 2026-05-27
Phase: Phase 3 full 27-seed run
Total unique keywords (Sheet 1): 598
Total PAA questions (Sheet 2): 68
Total related searches (Sheet 3): 124
Total negatives (Sheet 5): 14
Total competitors (Sheet 6): 69 entries / 5 distinct brands (Blue Sky, DKC, JetSet Pets, CarryMyPet, Pawsome Pets UAE)
Comparison Report (Sheet 4): 27 seeds, one row each
SERP Features (Sheet 7): 31 rows; "pet relocation Dubai" PAA=TRUE, Local Pack=TRUE, Ads=TRUE
Organic Results (Sheet 8): 262 rows
SerpApi credits used: ~972 estimated (36 calls x 27 seeds)
New competitors found: none beyond the 5 detectable via Google
Unexpected findings: 3 of 8 known competitors NOT flagged — AirPaws, MovingBay, Relocate MENA. These were sourced from Facebook research, not Google, and appear nowhere in Google autocomplete/PAA/Related/Organic data, so the Google-only Phase 3 engine cannot surface them. Expected to appear in Phase 4 (Reddit) or manual Facebook entry. One borderline negative: "Dubai Airport Free Zone Center for Veterinary Quarantine" matched on trigger "free" (substring false-positive, harmless).
Seasonal peak column populated: YES (Column H: 462 Oct-Apr, 136 Year-round, 0 empty)
Data integrity: 0 duplicate keyword rows; 0 negative-trigger leaks into Sheet 1; Columns J (Intent Type) and K (Customer Fear) both fully EMPTY as required.
Log: 3506 lines, 0 ERROR / 0 WARN / 0 BLOCKED / 0 EXCEPTION; all 27 seeds have [SEED-DONE]; run ended with [FINAL][SAVE].
Audit pass rate (independent sub-agent): 90% (9/10 Phase 3 criteria PASS; only "all 8 competitors" FAILED for the reason above)
Decision: PHASE 3 PASSED

---

## Claude Code Build Prompt

Copy this exactly. Do not modify before pasting.

```
I need you to build a keyword collection engine for a pet relocation business in Dubai.

This engine collects Google search data using two APIs in parallel, runs full alphabet expansion
and question prefix methods on each seed keyword, collects People Also Ask and Related Searches,
detects negative keywords and competitor brands automatically, and writes everything into an
organised Excel spreadsheet with 8 sheets.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Language: Python
API keys: loaded from .env file in project root using python-dotenv
  Install: pip install python-dotenv serpapi openpyxl requests
  The script reads .env automatically — no manual export commands needed
Seeds file: seeds.txt (one keyword per line — I will create this)
Output file: skill-01-keyword-collection.xlsx (path from .env PROJECT_ROOT)
Log file: keyword_engine_log.txt (same folder as script)

The script must start with:
  from dotenv import load_dotenv
  import os
  load_dotenv()
  SERPAPI_KEY = os.getenv('SERPAPI_KEY')
  if not SERPAPI_KEY:
      raise ValueError("SERPAPI_KEY not found in .env — check project root .env file")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CALLS PER SEED KEYWORD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CALL 1 — SerpApi autocomplete (base keyword)
  params: engine=google_autocomplete, q={seed}, gl=ae, hl=en

CALL 2 — Unofficial Google autocomplete (cross-check)
  URL: https://suggestqueries.google.com/complete/search
  params: client=firefox, hl=en, gl=ae, q={seed}
  Parse: response[1] contains the suggestions list

CALLS 3a-3z — Alphabet expansion via SerpApi
  For each letter in [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]:
  params: engine=google_autocomplete, q="{seed} {letter}", gl=ae, hl=en

CALLS 4a-4g — Question prefix via SerpApi
  For each prefix in [how, can, will, is, what, why, does]:
  params: engine=google_autocomplete, q="{prefix} {seed}", gl=ae, hl=en

CALL 5 — Full SERP via SerpApi
  params: engine=google, q={seed}, gl=ae, hl=en, num=10
  This single call returns: People Also Ask, Related Searches,
  Organic results, Featured snippet, SERP features present

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROCESSING RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DEDUPLICATION:
  Before adding any keyword to Sheet 1, check if it already exists
  (case-insensitive, strip whitespace)
  If EXISTS: update Source field to include new source, increment Source Count
  If NEW: add as new row

NEGATIVE KEYWORD DETECTION:
  If keyword contains any of these words (case-insensitive):
  jobs, salary, vacancies, careers, volunteer, DIY, free,
  van hire, wanted, apply, hiring, recruitment
  → Route to Sheet 5 "Negative Keywords" ONLY
  → Do NOT add to Sheet 1 under any circumstances

COMPETITOR DETECTION:
  If keyword contains a brand name not present in seeds.txt:
  → Add "COMPETITOR — research needed" to Notes column in Sheet 1
  → Add full entry to Sheet 6 "Competitors Found"
  Known competitors to watch for: Blue Sky, DKC, JetSet, CarryMyPet,
  JetSet Pets (also flag any other brand names discovered)

SEASONAL PEAK:
  For all keywords related to pet transport/cargo/shipping/relocation:
  → Set Column H (Seasonal Peak) = "Oct–Apr"
  For all keywords related to regulations/documents/requirements:
  → Set Column H = "Year-round"

SOURCE LABELLING:
  Autocomplete base = "serpapi-autocomplete"
  Unofficial Google = "google-unofficial"
  Both returned it = "both"
  Alphabet expansion = "alphabet-{letter}"
  Question prefix = "prefix-{prefix}"
  People Also Ask = "PAA"
  Related Searches = "related"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT — 8 SHEETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sheet 1 "Keyword Collection":
  Columns: Keyword | Source | Source Count | Date | Location |
           Device | Volume | Seasonal Peak | Status |
           Intent Type | Customer Fear | Notes
  Defaults: Location="UAE (gl=ae)" | Device="automated" |
            Status="pending-volume" | Intent Type="" | Customer Fear=""
  Note: Intent Type and Customer Fear columns MUST exist but stay empty.
  They are filled in the next phase (File 02 and File 03). Do not fill them.

Sheet 2 "People Also Ask":
  Columns: Question | Source Keyword | Date | Notes

Sheet 3 "Related Searches":
  Columns: Search | Source Keyword | Date | Notes

Sheet 4 "Comparison Report":
  Columns: Seed Keyword | SerpApi Count | Unofficial Count |
           Matched | SerpApi Only | Unofficial Only | Match Rate % | Notes
  One row per seed keyword.

Sheet 5 "Negative Keywords":
  Columns: Keyword | Trigger Word Detected | Source | Date | Reason

Sheet 6 "Competitors Found":
  Columns: Brand Name | Appeared In Keyword | Source | Date | Research Status
  Default Research Status = "pending"

Sheet 7 "SERP Features":
  Columns: Seed Keyword | Featured Snippet | People Also Ask Present |
           Local Pack | Ads Present | Video Carousel | Date

Sheet 8 "Organic Results":
  Columns: Seed Keyword | Position | URL | Title | Date

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RATE LIMITING AND ERROR HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rate limiting:
  SerpApi: 1 second wait between every call
  Unofficial Google: 0.5 second wait between every call

Save frequency:
  Save Excel file after every 5 seeds complete
  If Excel save fails: write all data to backup CSV files
  (one CSV per sheet, same folder as script)

Error handling:
  SerpApi error (any): log the error with seed + call type, skip that call, continue
  Unofficial API 429 or 503: log "blocked", skip for this keyword, continue
  Unofficial API blocked 3 times in a row: disable unofficial API for rest of run, log warning
  Unexpected exception anywhere: log full traceback, save current progress, exit cleanly
  Never crash silently — every error must appear in the log file

Logging — write every line to keyword_engine_log.txt:
  Format: [TIMESTAMP] [LEVEL] [SEED] [CALL TYPE] [MESSAGE]
  Log every API call with result count
  Log every deduplication (keyword found, source count updated)
  Log every negative keyword detected with trigger word
  Log every competitor detected with keyword it appeared in
  Log every save event
  Log every error

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
END OF RUN — CONSOLE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Print a clean summary after run completes:

═══════════════════════════════════════
KEYWORD ENGINE — RUN COMPLETE
═══════════════════════════════════════
Seeds processed: X of 27
Total unique keywords (Sheet 1): X
Total PAA questions (Sheet 2): X
Total related searches (Sheet 3): X
Total negative keywords (Sheet 5): X
Total competitors flagged (Sheet 6): X
───────────────────────────────────────
API Comparison (Sheet 4):
  Average match rate: X%
  Seeds where unofficial API was blocked: X
───────────────────────────────────────
SerpApi credits used (estimated): X
  (1 credit per call × 36 calls per seed)
───────────────────────────────────────
Errors encountered: X
  (see keyword_engine_log.txt for details)
═══════════════════════════════════════

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EXECUTION — DO THIS IN THIS EXACT ORDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1:
  Show me the complete Python script.
  Do not run anything yet.
  Wait for me to review it.

STEP 2:
  Show me the seeds.txt content you will use.
  Wait for me to confirm it is correct.

STEP 3:
  Ask me to confirm the Excel file path.
  Ask me to confirm SERPAPI_KEY is set.
  Ask me to confirm seeds.txt is created.

STEP 4 — PHASE 1 TEST (single seed):
  Run on "pet relocation Dubai" only.
  Show me the complete output after it finishes:
  - How many keywords went into Sheet 1
  - How many PAA questions in Sheet 2
  - How many related searches in Sheet 3
  - What went into Sheet 4 comparison report
  - What negative keywords were detected (Sheet 5)
  - What competitors were flagged (Sheet 6)
  - What SERP features were found (Sheet 7)
  - What organic results appeared (Sheet 8)
  - The full console summary
  Then STOP and wait for me to verify against my manual research.

STEP 5 — VALIDATION:
  I will compare your output against my manual screenshots.
  I must confirm these 8 items are present:
  1. Blue Sky appears from letter b run
  2. DKC appears from letter d run
  3. "Are people leaving pets behind in Dubai?" in Sheet 2
  4. "JetSet pets Dubai" in Sheet 3
  5. "careers" in Sheet 5 — NOT in Sheet 1
  6. Letter f returns 8+ export destinations
  7. India appears across multiple letter runs
  8. CarryMyPet appears in Sheet 8
  If any are missing — tell me and we fix before continuing.
  Do not continue to Step 6 until I give you explicit confirmation.

STEP 6 — PHASE 2 TEST (three seeds):
  Run on: "pet relocation Dubai" + "dog relocation Dubai" +
  "pet relocation from Dubai to India"
  Show me a summary of all sheets after completion.
  Check deduplication is working — "pet relocation Dubai"
  keywords should NOT be duplicated.
  Wait for my confirmation before Step 7.

STEP 7 — PHASE 3 FULL RUN:
  Only run this after I explicitly say "run full set".
  Run all 27 seeds from seeds.txt.
  Show progress updates as it runs — after each seed, print:
  "[seed name] complete — X keywords added, X PAA, X related, X negatives"
  Show full console summary when done.
  Do not close or exit until I confirm I have saved the Excel file.

Excel file full path: [PASTE YOUR FULL FILE PATH HERE]
```

---

## Phase 4 — Reddit API Full Integration

### Why Reddit API Instead of SerpApi Workaround

SerpApi with `site:reddit.com` returns Google's index of Reddit posts — titles and snippets only. You cannot see the full comments, the full thread, or the voted-up answers.

Reddit's official API via PRAW (Python Reddit API Wrapper) returns:
- Full post body
- Every comment and reply
- Vote counts (higher votes = more people relate to this)
- The entire thread conversation
- Real customer language unfiltered

The comments are more valuable than the post itself. One post is one person's question. The comments are 10–30 people's fears, experiences, warnings, and recommendations in their exact words. This is irreplaceable for fear mapping.

### Reddit API Setup — 10 Minutes

1. Go to `reddit.com/prefs/apps`
2. Click "Create App" or "Create Another App"
3. Choose type: **script**
4. Name: trust-engine-research (or anything)
5. Redirect URI: `http://localhost:8080`
6. Submit — you get `client_id` and `client_secret` immediately
7. No approval process — script apps are granted immediately

Store in project root `.env` file (already created — just fill in your values):
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_USER_AGENT=trust-engine-research/1.0
```
Script loads automatically: `load_dotenv()` then `os.getenv('REDDIT_CLIENT_ID')`

### Subreddits to Search

| Subreddit | Why | Access |
|-----------|-----|--------|
| r/dubai | Largest Dubai expat community | Public |
| r/expats | International relocators | Public |
| r/PetTravel | Pet travel specific | Public |
| r/DubaiExpats | Dubai-specific expats | Public |
| r/uae | UAE general | Public |
| r/dubai_pets | Dubai pet owners | Public |

### Search Queries Per Subreddit

```python
search_queries = [
    "pet relocation",
    "move dog Dubai",
    "bring cat Dubai",
    "fly dog Dubai",
    "pet import UAE",
    "pet export Dubai",
    "Emirates pet",
    "Etihad pet",
    "pet cargo Dubai",
    "dog quarantine Dubai",
    "cat quarantine UAE",
    "MOCCAE pet",
    "pet transport UAE",
    "moving with pets Dubai"
]
```

### What to Extract Per Thread

```python
for post in subreddit.search(query, limit=100, sort='relevance'):
    extract:
        post.title           # The question/topic
        post.selftext        # Full post body
        post.score           # Upvotes (higher = more people relate)
        post.created_utc     # Date
        post.url             # Link to thread

    for comment in post.comments.list():
        extract:
            comment.body     # Full comment text
            comment.score    # Upvotes
            comment.author   # Username
            comment.created_utc
```

### Processing Rules

- Minimum score threshold: include posts with score >= 2 (filters out zero-engagement posts)
- Sort comments by score descending — highest voted comments first
- Flag any comment mentioning a company/service name → Sheet 6 Competitors Found
- Flag any comment containing a fear keyword → Community Language tab
- Flag any comment containing price data → Source Bank candidate

### Output Destination

| Data | Goes To |
|------|---------|
| Post titles | Sheet 1 Keyword Collection (as keyword candidates) |
| Post body quotes | Community Language tab |
| High-score comment quotes | Community Language tab |
| Company names mentioned | Sheet 6 Competitors Found |
| Price data mentioned | Notes column + Source Bank flag |
| New routes mentioned | New seed candidate list |

### Rate Limiting

Reddit API allows 60 requests per minute for authenticated script apps.
Add 1 second delay between requests to stay well within limits.
PRAW handles rate limiting automatically if configured correctly.

### Claude Code Integration

Add to engine script as Phase 4. Runs after Phase 3 Google keyword collection completes.
Same output spreadsheet. New data appends to existing sheets — does not overwrite.

### PRAW Installation

```bash
pip install praw
```

---

## Competitor List — Updated (8 Confirmed)

Found via Google tools (4):
1. Blue Sky Pet Relocation Dubai
2. DKC Pet Relocation Dubai
3. JetSet Pets Dubai
4. CarryMyPet.ae

Found via Facebook community research (4):
5. AirPaws Relocation
6. MovingBay.com
7. Pawsome Pets UAE — pawsomepets.ae (10 years operating)
8. Relocate MENA — relocatemena.com

**All 8 need Trust Score research using the 10-point system.**
