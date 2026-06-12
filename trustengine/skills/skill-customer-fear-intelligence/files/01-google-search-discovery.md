---
Status: verified — manual sessions complete, engine building
Area: skill-01
Priority: high
Activation: immediate
Last verified: 2026-05-26
Depends on: customer-profile/01-master-customer-profile.md
Feeds into: skill-01/engine-keyword-collection.md, skill-01/02-intent-classification.md, skill-01-keyword-collection.xlsx
---

# Skill 01 — File 01: Google Search Discovery
## How to learn what people actually search for — and how to collect it at scale

---

## Purpose

Before writing a single word of content, you must know exactly what your customers type into Google when they are afraid, confused, or ready to buy.

Google Autocomplete is not a keyword tool. It is a live feed of real human fears. Every suggestion Google shows is based on what real people have actually typed. When Google suggests "can my dog die on a plane to Dubai" — that is a record of real people, in real fear, typing that exact phrase.

**Research-verified (May 2026):** The methodology this file is part of — combining multi-source keyword collection with fear-acknowledging query classification — does not exist anywhere as a published framework. No enterprise SEO tool, no published agency, no academic paper has this combination. Full verdict: `research/00-verdict.md`

**The correct framing:** This system *acknowledges* customer fears and pairs each one with verified official solutions. The term is "fear-acknowledging" — not "emotional SEO" (low-credibility term used by blogs with no methodology) and not "fear-exploiting" (which would be the opposite of what builds trust). The defensible positioning: voice-of-customer research + fear-acknowledging classification + verified official information = The Trust Engine methodology.

This file covers:
1. What the three data types are and what each one looks like
2. How to collect them manually (do this first — always)
3. Which APIs collect which data types and why
4. Why SerpApi is the primary API
5. Why the unofficial Google API is a cross-check only
6. What was found in live manual collection sessions
7. How the collection feeds into the spreadsheet
8. What comes next

---

## Phase 1 Scope — Locked Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| Location | UAE only (`gl=ae`) | Build Dubai market first. Expand when verified. |
| Language | English only | Primary search language for target expat audience |
| Audience | B2C only | Validate business model before B2B complexity |
| Platform | Google only | Dominant search engine in UAE market |
| APIs | SerpApi + unofficial Google | SerpApi = primary. Unofficial = free comparison check |

**Deferred to Phase 2 — documented here, not built yet:**
- Origin country collection: UK (`gl=gb`), South Africa (`gl=za`), USA (`gl=us`), Australia (`gl=au`)
- Arabic language keywords (`hl=ar`) — requires native speaker for validation
- B2B / corporate relocation keywords — separate file and strategy
- YouTube autocomplete — Skill 21 territory
- Bing autocomplete — lower priority
- DataForSEO API — replaces manual Keyword Planner in Phase 2

---

## The Three Data Types — What Each One Is

There are three separate things Google shows you for any keyword. Each appears at a different moment. Each reveals a different layer of customer intent. All three are needed. None of them can replace the others.

---

### Data Type 1 — Autocomplete (Before Enter)

**What it is:** The dropdown list of suggestions that appears as you type — before pressing enter.

**When it appears:** While typing. Disappears when you press enter.

**What it reveals:** How people START their search. What words they reach for when they first think of the problem. The raw language of the market.

**Real example collected 2026-05-26 — "pet relocation Dubai h":**
```
pet relocation dubai ... how much
pet relocation dubai ... head office
pet relocation dubai ... how long
pet relocation south africa to dubai
pet relocation south africa
pet relocation services south africa
pet worldwide relocations
pet relocation dubai cost
```

**How to collect manually:**
1. Open Google on your phone
2. Type the keyword — do NOT press enter
3. Screenshot the dropdown
4. Repeat with each letter a–z added after the keyword

**How to collect automatically:**
- SerpApi: `engine=google_autocomplete, q={keyword}, gl=ae, hl=en`
- Unofficial Google API: `suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=ae&q={keyword}`
- Both return the same type of data — used in parallel for comparison

---

### Data Type 2 — People Also Ask (After Enter, Mid-Page)

**What it is:** A box titled "People also ask" with 4 expandable questions. Tap any question — 3 more appear. Keep tapping to expand the tree.

**When it appears:** After pressing enter, mid-way down the results page — after the first 1–2 organic results.

**What it reveals:** Questions people ask AFTER they start researching. Deeper fears and more specific confusions than autocomplete surfaces. The questions people type when they want a direct answer, not a provider.

**Real example collected 2026-05-26 — "pet relocation Dubai":**
```
How much does it cost to move your pet to Dubai?
Are people leaving pets behind in Dubai?
Can you move your pet to Dubai?
How to transfer pet ownership in Dubai?
```

**How to collect manually:**
1. Press enter on the keyword
2. Scroll past the first 1–2 results
3. Find the "People also ask" box
4. Tap every question to expand more
5. Screenshot each expansion
6. Record exact wording — never paraphrase

**How to collect automatically:**
- SerpApi: `engine=google, q={keyword}, gl=ae, hl=en` — returns PAA inside the full SERP response
- Unofficial Google API: **CANNOT collect this** — has no way to access the full results page

---

### Data Type 3 — Related Searches / People Also Search For (After Enter, Bottom)

**What it is:** A section at the very bottom of results showing 6–8 keyword phrases. May be labelled "Related searches" or "People also search for."

**When it appears:** After pressing enter, at the very bottom of the page — after all organic results.

**What it reveals:** What people search NEXT after this keyword. Maps the customer journey from discovery to decision. Also surfaces competitor brand names and negative keywords.

**Real example collected 2026-05-26 — "pet relocation Dubai":**
```
Pet relocation Dubai costs
Best pet relocation services Dubai
Pet relocation Dubai to UK
Pet relocation Dubai to India
Pet relocation dubai careers       ← NEGATIVE — employment seeker
JetSet pets Dubai                  ← COMPETITOR — research needed
```

**How to collect manually:**
1. Press enter on the keyword
2. Scroll all the way to the bottom — past every result
3. Find "Related searches" or "People also search for"
4. Screenshot the full section

**How to collect automatically:**
- SerpApi: same `engine=google` call that collects PAA — both come back in one response
- Unofficial Google API: **CANNOT collect this** — has no access to the full results page

---

## API Decision — Why SerpApi and Not Unofficial Google API

This is not a preference. It is based on what each API can and cannot access. The unofficial Google API is a single lightweight endpoint. It returns one JSON list of autocomplete suggestions. That is everything it can do. It has no mechanism to load a full results page, parse the DOM, or extract anything that appears after pressing enter.

SerpApi is a full SERP API. It simulates a complete Google search, loads the entire results page, and parses every element on it. That is why it can return things the unofficial API cannot.

---

### Complete API Capability Comparison

| Data Type | What It Is | Unofficial Google API | SerpApi | DataForSEO (Phase 2) |
|-----------|-----------|----------------------|---------|----------------------|
| Autocomplete | Dropdown before enter | ✅ Yes | ✅ Yes | ✅ Yes |
| Alphabet expansion | Seed + each letter a–z | ✅ Yes | ✅ Yes | ✅ Yes |
| Question prefixes | How/can/will/is/what/why/does + seed | ✅ Yes | ✅ Yes | ✅ Yes |
| People Also Ask | Fear questions mid-page | ❌ No | ✅ Yes | ✅ Yes |
| Related Searches | Next-step keywords at bottom | ❌ No | ✅ Yes | ✅ Yes |
| Organic results | Who currently ranks | ❌ No | ✅ Yes | ✅ Yes |
| Featured snippets | Position zero answer box | ❌ No | ✅ Yes | ✅ Yes |
| Local pack / map results | Google Maps businesses | ❌ No | ✅ Yes | ✅ Yes |
| Ad results | Paid ads for this keyword | ❌ No | ✅ Yes | ✅ Yes |
| SERP features present | What features appear | ❌ No | ✅ Yes | ✅ Yes |
| Negative keyword detection | Wrong-audience signals | Autocomplete only | All sources | All sources |
| Competitor brand detection | Other companies in market | Autocomplete only | All sources | All sources |
| Search volume | Monthly searches | ❌ No | ❌ Separate call | ✅ Built in |
| Keyword difficulty | How hard to rank | ❌ No | ❌ No | ✅ Yes |
| CPC estimate | Cost per click | ❌ No | ❌ No | ✅ Yes |
| UAE targeting (gl=ae) | Results as seen from UAE | ⚠️ Best effort | ✅ Reliable | ✅ Reliable |
| Arabic support (hl=ar) | Arabic search language | ⚠️ Limited | ✅ Yes | ✅ Yes |
| Reliability | Can you depend on it | ❌ No SLA, unofficial | ✅ 99.95% SLA | ✅ 99.95% SLA |
| Rate limits | How fast you can call it | ❌ Undocumented | ✅ Published | ✅ Published |
| Can break without warning | Google may kill it | ❌ Yes, any time | ✅ No — commercial | ✅ No — commercial |
| Cost | Price to use | ✅ Free | Monthly plan | $0.0006–0.002/call |

---

### Why We Still Use the Unofficial Google API

Even though it is limited, it is free and it returns autocomplete data. We use it in parallel with SerpApi for the autocomplete step only — as a cross-check.

**The comparison test:**
Run both APIs for the same keyword at the same time. If SerpApi returns "best pet relocation company Dubai" and the unofficial API also returns it — that keyword is double-verified. If only SerpApi returns it — it might be personalised or location-specific. If only the unofficial API returns it — unusual, needs manual verification.

**The match rate is a verified data quality signal.** It is documented in Sheet 4 of the spreadsheet after every engine run.

**The unofficial API will never be the primary source.** Any keyword that only appears in the unofficial API and not in SerpApi is flagged for manual verification before being approved.

---

### Why DataForSEO Is Phase 2

DataForSEO does everything SerpApi does plus it returns search volume, keyword difficulty, and CPC in the same call. This eliminates the manual Google Keyword Planner step entirely.

For Phase 1, SerpApi + manual Keyword Planner is sufficient. The system is not yet at the scale where automating the volume check justifies switching APIs. When Phase 2 begins, DataForSEO replaces both SerpApi and Keyword Planner in one move.

---

## Negative Keywords — What They Are and How They Are Handled

Negative keywords are searches that look relevant but attract the wrong audience — people who will never pay for a premium concierge pet relocation service.

**Why they matter:** If you build content for a negative keyword, you attract traffic that will never convert. You waste months of effort. You train Google to associate your site with the wrong audience.

**Where negative keywords appear:**
- In autocomplete suggestions (e.g. "pet relocation Dubai jobs" appears in the dropdown)
- In Related Searches (e.g. "pet relocation Dubai careers" appeared at the bottom of results)
- In PAA (rare but possible — employment or DIY questions)
- In organic results (a page ranking here shows Google associates the query with this topic)

**Confirmed negative keywords from live collection:**

| Keyword | Source Found In | Trigger Word | Why Negative |
|---------|----------------|-------------|-------------|
| pet relocation Dubai jobs | autocomplete | jobs | Employment seeker — not a customer |
| pet relocation Dubai salary | autocomplete | salary | Employment seeker — not a customer |
| pet relocation Dubai vacancies | autocomplete | vacancies | Employment seeker — not a customer |
| pet relocation Dubai careers | Related Searches | careers | Employment seeker — not a customer |
| pet relocation Dubai volunteer | autocomplete | volunteer | Not paying for service |
| DIY pet relocation Dubai | autocomplete | DIY | Will never pay for concierge service |
| free pet relocation Dubai | autocomplete | free | Wrong price expectation |
| pet transport van Dubai | autocomplete | van hire | Local van — not international relocation |

**How the engine handles negative keywords:**
Automatically detects any keyword matching the negative trigger word list and routes it directly to Sheet 5 "Negative Keywords." Never added to the main collection sheet. In Phase 2 these become paid campaign exclusions so ads never show for these searches.

---

## Competitor Detection — What It Is and Why It Matters

Competitor brand names appear as keywords when customers search for a specific company by name. This signals brand recognition — customers know this company exists and are looking for it or checking its reviews.

**Why competitor keywords matter:**
- They reveal who has market recognition in the Dubai pet relocation space
- High search volume for a competitor brand means they are well-known — a bigger threat
- Comparison-intent customers ("Blue Sky pet relocation Dubai reviews") are close to buying — high value
- These keywords become research inputs for the Competitor Analysis Engine (Skill 17)

**Confirmed competitors found in live manual collection:**

| Competitor | How Found | Source | Strategic Priority |
|-----------|----------|--------|--------------------|
| Blue Sky Pet Relocation Dubai | Appeared in letter b autocomplete | SerpApi + unofficial API | High — brand recognition confirmed |
| DKC Pet Relocation Dubai | Appeared in letter d autocomplete | SerpApi + unofficial API | High — brand recognition confirmed |
| JetSet Pets Dubai | Appeared in Related Searches | SerpApi only | High — unofficial API missed this |
| CarryMyPet.ae | Ranking organically in results page | SerpApi only | High — actively ranking for main keyword |

**Important:** The unofficial Google API found Blue Sky and DKC because they appeared in autocomplete. It missed JetSet Pets (Related Searches) and CarryMyPet.ae (organic results) because it cannot access those sources. This is a concrete example of why SerpApi is the primary API.

**How the engine handles competitor keywords:**
Flags any keyword containing a brand name not in seeds.txt. Adds "COMPETITOR — research needed" to the Notes column. Logs them in Sheet 6 "Competitors Found" for research using the 10-point Trust Score.

---

## Manual Collection Sessions — The Verification Baseline

Every engine run is compared against these manual sessions. If the engine output matches — it is trusted. If it diverges — investigate before proceeding.

---

### Session 1 — Autocomplete + Alphabet Expansion
**Date:** 2026-05-26
**Seed keyword:** pet relocation Dubai
**Method:** Phone, Google.com, no VPN, manual typing
**Letters completed:** a, b, c, d, e, f, g, h

**Screenshot log:**

| File | Query | What It Proved |
|------|-------|----------------|
| 1000305211.jpg | pet relocation Dubai (base) | India, UK, Philippines, reddit, costs, australia all confirmed |
| 1000305212.jpg | pet relocation Dubai b | Blue Sky competitor found. Best + reviews intent confirmed |
| 1000305213.jpg | pet relocation Dubai b (alt) | Same results — consistency check passed |
| 1000305214.jpg | pet relocation Dubai c | Company/cost keywords confirmed. Canada route found |
| 1000305215.jpg | pet relocation Dubai d | DKC competitor found. Cost fear keyword confirmed |
| 1000305216.jpg | pet relocation Dubai e | Emirates + Etihad airline keywords. South Africa import confirmed |
| 1000305217.jpg | pet relocation Dubai f | Full export cluster — 8 destinations in one letter |
| 1000305218.jpg | pet relocation Dubai g | Germany route. Guide intent. India cost confirmed again |
| 1000305219.jpg | pet relocation Dubai e (alt) | South Africa standalone market confirmed |
| 1000305220.jpg | pet relocation Dubai f (alt) | Export cluster consistency confirmed |
| Screenshot_20260526_154909_Chrome.jpg | pet relocation Dubai h | How much, how long confirmed. Pet worldwide relocations found |

**All 47 keywords extracted from Session 1:**

| Keyword | Letter | Notes |
|---------|--------|-------|
| pet relocation dubai | base | Core seed |
| pet relocation dubai to india | base | India route — high priority |
| pet relocation dubai to uk | base | UK route confirmed |
| pet relocation dubai to india price | base | Cost + India |
| pet relocation dubai to philippines | base | Philippines route |
| pet relocation dubai reddit | base | Community seeking behaviour |
| pet relocation dubai costs | base | Cost intent |
| pet relocation dubai to australia | base | Australia route |
| pet relocation agency dubai | a | Agency terminology |
| pet relocation agent dubai | a | Agent terminology |
| pet travel agency dubai | a | Different wording |
| pet relocation dubai to australia | a | Duplicate — source count +1 |
| pet travel agent dubai | a | Agent terminology |
| pet relocation dubai to south africa | a | SA route |
| dubai pet relocation agency uae | a | UAE qualifier |
| can i take my dog to dubai from india | a | Fear keyword — India origin |
| best pet relocation dubai | b | Commercial intent |
| blue sky pet relocation dubai | b | COMPETITOR |
| blue sky pet relocation dubai reviews | b | Competitor review seeking |
| best pet relocation services dubai | b | Commercial intent |
| can i take my dog to dubai from india | b | Duplicate — source count +1 |
| pet relocation cost from dubai to india | b | Export + cost |
| can i move my dog to dubai | b | Fear/informational |
| pet relocation dubai costs | c | Duplicate — source count +1 |
| pet relocation company dubai | c | Company terminology |
| best pet relocation company dubai | c | Commercial intent |
| pet relocation from india to dubai cost | c | Import + cost |
| pet relocation from dubai to canada | c | Canada export route |
| pet relocation cost from dubai to philippines | c | Philippines cost |
| can i take my dog to dubai from india | c | Duplicate — source count +1 |
| dkc pet relocation dubai | d | COMPETITOR |
| can i take my dog to dubai from india | d | Duplicate — source count +1 |
| can i move my dog to dubai | d | Duplicate — source count +1 |
| pet relocation cost from dubai to india | d | Duplicate — source count +1 |
| how much does it cost to fly a dog to dubai | d | Cost fear keyword |
| pet relocation dubai to south africa | d | SA export route |
| pet relocation dubai emirates | e | Airline keyword |
| pet relocation dubai email address | e | Contact seeking |
| pet relocation dubai etihad | e | Airline keyword |
| pet relocation dubai egypt | e | Egypt route |
| pet relocation south africa to dubai | e | SA import route |
| pet relocation south africa | e | SA standalone market |
| pet relocation from dubai to india | f | India export confirmed |
| pet relocation from dubai to philippines | f | Philippines export |
| pet relocation from dubai | f | Generic export |
| pet relocation from dubai to uk | f | UK export |
| pet relocation from dubai to usa | f | USA export |
| pet relocation from dubai to canada | f | Canada export |
| pet relocation from dubai to london | f | London city-specific |
| pet relocation from dubai to australia | f | Australia export |
| pet relocation dubai to germany | g | Germany route |
| pet relocation dubai guide | g | Informational intent |
| pet relocation dubai how much | h | Cost question |
| pet relocation dubai head office | h | Contact seeking |
| pet relocation dubai how long | h | Timeline question |
| pet worldwide relocations | h | Industry terminology |
| pet relocation dubai cost | h | Duplicate — source count +1 |

**Key findings from Session 1:**
1. India is the highest-frequency route — appeared in letters a, b, c, d, f. Confirmed Tier 1.
2. Blue Sky and DKC are competitor brands with search volume — real market presence.
3. Export cluster is massive — letter f alone returned 8 different destinations.
4. Philippines appearing repeatedly — check volume, may be Tier 2.
5. Both "agency" and "company" and "agent" are used interchangeably by customers — all need content.
6. London appears separately from UK — city-specific and country-level pages both needed.

---

### Session 2 — People Also Ask + Related Searches
**Date:** 2026-05-26
**Seed keyword:** pet relocation Dubai
**Method:** Phone, Google.com, pressed enter, scrolled full results page

**Screenshot log:**

| File | What Was Captured | What It Proved |
|------|------------------|----------------|
| Screenshot_20260526_180157_Chrome.jpg | Organic results + PAA box | CarryMyPet.ae ranking. 4 PAA questions confirmed |
| Screenshot_20260526_180633_Chrome.jpg | Related Searches / People Also Search For | JetSet Pets competitor found. Careers negative confirmed |

**People Also Ask questions extracted:**

| Question | Fear Behind It | Content Priority |
|----------|---------------|-----------------|
| How much does it cost to move your pet to Dubai? | Hidden fees, being overcharged, not knowing what's fair | High — dedicated cost page needed |
| Are people leaving pets behind in Dubai? | Customers have heard stories of abandoned pets when expats leave — fear this will happen to them | Critical — no competitor addresses this. Unique content opportunity |
| Can you move your pet to Dubai? | Basic uncertainty — is it even possible? Am I allowed? | Medium — answered on service page |
| How to transfer pet ownership in Dubai? | Different journey — not relocating pet, handing it over | New customer type discovered — needs separate content |

**Related Searches extracted:**

| Search | Type | Action |
|--------|------|--------|
| Pet relocation Dubai costs | Content keyword | Add to collection — cost cluster |
| Best pet relocation services Dubai | Commercial keyword | Add to collection — commercial cluster |
| Pet relocation Dubai to UK | Route keyword | Add to collection — UK export cluster |
| Pet relocation Dubai to India | Route keyword | Add to collection — India export cluster |
| Pet relocation dubai careers | NEGATIVE | Route to Sheet 5 — employment seeker |
| JetSet pets Dubai | COMPETITOR | Flag for research — found via Related Searches only |

**Key findings from Session 2:**
1. JetSet Pets Dubai found — only appears in Related Searches, not autocomplete. Unofficial API would have missed this entirely.
2. CarryMyPet.ae is ranking organically — active competitor in the market.
3. "Are people leaving pets behind in Dubai?" is a deep emotional fear with no quality content addressing it. This is a high-priority content gap.
4. "How to transfer pet ownership" is a different customer journey — some customers are not relocating their pet, they are giving it to someone else. This audience has completely different fears and needs different content.
5. Careers confirmed as negative — route to Sheet 5.

---

### What the Manual Sessions Proved — Consolidated

| Finding | Evidence | Action Required |
|---------|----------|----------------|
| India is Tier 1 route | Letters a, b, c, d, f + Related Searches | Update customer profile. Build India import seed cluster. |
| 4 competitors confirmed | Autocomplete (Blue Sky, DKC) + Related (JetSet) + Organic (CarryMyPet) | Research all 4 using 10-point Trust Score |
| Export cluster is large | Letter f — 8 destinations | Build separate export seeds.txt before running engine |
| Abandonment fear exists | PAA question | Build dedicated page — "Are people leaving their pets behind in Dubai?" |
| Careers is a negative | Related Searches | Add to negative trigger word list |
| London needs own page | Autocomplete | London + UK = separate content pages |
| Unofficial API misses JetSet + CarryMyPet | Not in autocomplete | Confirms SerpApi must be primary — unofficial is incomplete |
| Agency/agent/company all used | Autocomplete variations | All three must be in seed list and keyword clusters |

---

## The Collection Spreadsheet

**File:** `skill-01-keyword-collection.xlsx`
**Tabs:** 4 tabs pre-built. Engine adds tabs 5–8 when it runs.

**Tab structure:**

| Tab | Name | Purpose |
|-----|------|---------|
| 1 | Keyword Collection | All validated keywords — the main collection |
| 2 | People Also Ask | All PAA questions |
| 3 | Related Searches | All related searches |
| 4 | Comparison Report | SerpApi vs unofficial API results per seed |
| 5 | Negative Keywords | All detected negatives — engine adds this |
| 6 | Competitors Found | All competitor signals — engine adds this |
| 7 | SERP Features | Features present per keyword — engine adds this |
| 8 | Organic Results | Who ranks for each seed — engine adds this |

**Columns A–I are filled in this file. Columns J and K are filled in File 02 (intent) and File 03 (fear).**

---

## Validation Rules — When a Keyword Is Approved

A keyword is **collection-validated** when it passes both:

**Point 1 — Appears in 2+ sources**
Found in at least 2 of: autocomplete, alphabet, question prefix, PAA, related searches, community research. Multiple sources confirms real demand.

**Point 2 — Has volume OR is route-specific**
Check in Google Keyword Planner. If it shows any volume — pass. If zero — do not automatically reject. A keyword like "emergency pet relocation Dubai tonight" may show zero volume but represents a real high-value customer. Document the decision in the Notes column.

**Validation statuses:**
- `collection-validated` — passed both points, ready for File 02
- `pending-volume` — needs Keyword Planner check
- `negative` — confirmed wrong audience, in Sheet 5
- `phase-2` — valid but out of Phase 1 scope

---

## Collection Targets — Before Moving to File 02

| Target | Minimum | Ideal |
|--------|---------|-------|
| Total keywords collected | 80 | 500+ (after engine runs) |
| Collection-validated keywords | 50 | 300+ |
| PAA questions collected | 30 | 100+ |
| Related searches collected | 20 | 80+ |
| Negative keywords documented | 10 | 20+ |
| Competitors identified | 4 (done) | All known |
| Seeds with manual baseline | 1 (done) | 3 before full engine run |

---

## Seasonal Intelligence — Google Trends Data

**Screenshot file:** `1000305262.jpg`
**Date collected:** 2026-05-26
**Settings:** Google Trends, "pet relocation Dubai", United Arab Emirates, Past 5 years

**What the chart shows:**

| Period | Trend Value | Interpretation |
|--------|------------|----------------|
| May 2026 (now) | 0 | Bottom of cycle — summer embargo beginning |
| March 2025 | 100 | Highest point in 5 years — peak demand |
| Oct–Apr (each year) | 20–100 | Active season — cooler months, airlines allow pet cargo |
| Jun–Sep (each year) | 0–5 | Dead season — summer embargo, most airlines suspend pet cargo |
| 2022 peak | ~28 | Market baseline |
| 2025/2026 peaks | 35–100 | Market is growing significantly |

**Critical strategic findings:**

1. **The market is growing fast.** The 2025/2026 spikes are 3–4× larger than 2022/2023 spikes. This is not a stable market — it is an expanding one. Getting in now is the right time.

2. **You have a 4-month window.** It is currently May 2026. The next search surge begins approximately September/October 2026. Pages must be built AND ranking before then. Google takes 3–6 months to rank new content for competitive keywords. Build now.

3. **The content calendar is defined by the embargo.** Two distinct seasons drive two distinct content strategies:
   - **October–April (active season):** Commercial pages, route-specific pages, cost pages — all conversion-focused
   - **June–September (embargo season):** Educational content, future planning guides, "what to do when airlines resume" — traffic now, convert in October

4. **Urgency keywords peak in April/May.** The week before the embargo begins, people panic. "Can I still move my dog before summer Dubai" is a real search that spikes every April. This needs a dedicated urgent-intent page.

5. **Column H (Seasonal Peak) for all pet cargo keywords = Oct–Apr.** Any keyword related to actual pet transport has a seasonal peak in the cooler months. This is the default to enter in the spreadsheet for all cargo/transport keywords.

**File saved:** `/research/screenshots/1000305262.jpg`

---

## What Comes Next

This file feeds into:

1. **`skill-01/engine-keyword-collection.md`** — the engine automates everything in this file at scale
2. **`skill-01/02-intent-classification.md`** — every validated keyword gets an intent type (Column J)
3. **`skill-01/03-fear-formula.md`** — every validated keyword gets a customer fear mapped (Column K)
4. **`skill-01-keyword-collection.xlsx`** — the spreadsheet receives all output

---

## Verification Checklist

- [x] Manual Session 1 completed — autocomplete + alphabet a–h for seed keyword 1
- [x] Manual Session 2 completed — PAA + Related Searches for seed keyword 1
- [x] API capabilities verified and documented
- [x] Negative keywords identified and confirmed
- [x] Competitors identified: Blue Sky, DKC, JetSet Pets, CarryMyPet.ae
- [x] India confirmed as Tier 1 route
- [x] Export cluster confirmed — separate seed list needed
- [x] Spreadsheet built with all columns
- [ ] Letters i through z completed for seed keyword 1
- [ ] Remaining 13 original seeds manually checked
- [x] Google Trends check completed — UAE + 5 year view — seasonal pattern confirmed, market growing, next surge Sep/Oct 2026
- [ ] Keyword Planner volume check for top 20 validated keywords
- [ ] Competitor Trust Score research for all 4 competitors
- [ ] Engine built and tested in Claude Code
- [ ] Engine output verified against manual sessions (80%+ match required)

---

## Community Research — Facebook Group Sessions

### Facebook Group: Pet Moving and Relocation
**Date:** 2026-05-26
**Screenshots:** 1000305296.jpg, 1000305297.jpg, 1000305298.jpg, 1000305300.jpg, 1000305302.jpg, 1000305304.jpg

---

### New Competitors Found in Facebook Group

This session brought the total confirmed competitor count to 8. All 4 new competitors were found only through community research — they do not appear in Google autocomplete or Related Searches.

| Competitor | Website | How Found | Notes |
|-----------|---------|----------|-------|
| AirPaws Relocation | Not captured | Julia Na commenting in multiple posts | Active in community, responding to leads directly |
| MovingBay.com | movingbay.com | Paid ad post in group by Biju Varghese | Running paid Facebook ads — budget to spend |
| Pawsome Pets UAE | pawsomepets.ae | Kirsty Kavanagh comment | 10 years in business — most established competitor found |
| Relocate MENA | relocatemena.com/pet-relo/ | Deborah Bellis comment | MENA-focused positioning |

**Full competitor list — now 8 confirmed:**
1. Blue Sky Pet Relocation Dubai (Google autocomplete)
2. DKC Pet Relocation Dubai (Google autocomplete)
3. JetSet Pets Dubai (Google Related Searches)
4. CarryMyPet.ae (Google organic results)
5. AirPaws Relocation (Facebook group)
6. MovingBay.com (Facebook group)
7. Pawsome Pets UAE — pawsomepets.ae (Facebook group)
8. Relocate MENA — relocatemena.com (Facebook group)

**Critical finding:** 4 of 8 competitors were only discoverable through Facebook community research. Google tools found 4. Community research found 4 more. This confirms that community research is not optional — it is the only way to find the full competitive landscape.

---

### Community Language — Exact Quotes

Every quote below is the real language real customers use. This feeds directly into:
- Keyword candidates (Column A of spreadsheet)
- Fear mapping (Column K — File 03)
- Content briefs
- FAQ sections
- Page headlines

| Platform | Date | Person | Exact Quote | Fear/Insight | New Keyword |
|---------|------|--------|-------------|-------------|-------------|
| FB Group | 16 Apr | Anonymous | "trying to work out all stages of taking an up to date vaccinated cat to Spain as cheaply as possible" | Cost fear — customers feel the price is arbitrary | pet relocation Dubai to Spain cost |
| FB Group | 16 Apr | Anonymous | "been quoted some ridiculous prices from companies and vets" | Price shock — customers feel ripped off before starting | how much should pet relocation cost Dubai |
| FB Group | 16 Apr | Anonymous | "Fit to fly 200 AED, MOCCAE 400 AED, Cargo village attestation + airline 1500 AED" | REAL PRICE DATA from a customer | MOCCAE pet export cost, fit to fly certificate Dubai |
| FB Group | 16 Apr | Shelorina | "I asked Emirates for my cat and they don't accept BSH" | Breed restriction fear — British Shorthair rejected | Emirates BSH cat policy, Emirates restricted cat breeds |
| FB Group | 08 Apr | Menna El | "does anyone know how to transport a cat from UAE to USA, is there a service?" | Basic discovery — doesn't know services exist | cat transport UAE to USA service |
| FB Group | 02 Apr | Tilda Maria | "do they allow 2 dogs in same crate? Emirates cargo or excessive luggage" | Specific operational fear — nobody covers this | Emirates 2 dogs same crate, Emirates pet cargo crate rules |
| FB Group | 13 Apr | Anonymous | "What vaccinations, paperwork, and import permits are required for bringing a cat into the UAE? Are there any quarantine rules or specific airline requirements?" | Classic new customer — overwhelmed by process | cat import UAE requirements, cat vaccination Dubai import |
| FB Group | 5d ago | Parida Natty | "There is any agency for pet transport from UAE - OMAN by car please?" | NEW ROUTE — UAE to Oman by road. 5 likes, 10 comments — high demand | pet transport UAE Oman by car, pet relocation Oman road |
| FB Group | 15 May | Arell Tadeo | "looking for affordable dog relocation. UAE to Philippines" | Philippines route confirmed + affordability angle | affordable dog relocation UAE Philippines |
| FB Group | 17 May | Anonymous | "planning on traveling with my cat in cabin with Etihad in 2 weeks. Their measurements for the carrier is quite unusual — soft carrier 40x40x22cm. Has anyone faced this issue?" | Carrier measurement fear — cannot find fitting carrier | Etihad cabin cat carrier size, Etihad soft carrier 40x40x22 |
| FB Group | 3h ago | Arfa Usama | "We plan to travel Oman from UAE for a few days by road and wish to take our pets along" | Temporary road travel — different from relocation | temporary pet travel UAE Oman, take pets to Oman by car |
| FB Group | 6h ago | Craig White | "We are starting to plan our return with our two cats and one dog to the Philippines end of July or beginning of August. It cost a fortune to bring them here. Looking for a more cost effective way. Does anyone have experience or advice on finding flight buddies?" | Cost fear + Philippines export + FLIGHT BUDDIES — new concept | flight buddies pet Philippines, cheap pet relocation Philippines |
| FB Group | 2h ago | Humi Parekh | "I thought animals couldn't come back into UAE from Oman without a quarantine period because Oman is high risk for rabies. Could be wrong though." | Rabies quarantine fear for Oman↔UAE crossing | UAE Oman pet quarantine, Oman rabies risk pets |

---

### Key Insights From Facebook Session

**1. Oman is a completely separate service category — never considered before**
Multiple posts about UAE↔Oman pet travel by road. This is NOT relocation. These are people taking pets on short trips or weekend breaks to Oman. Completely different customer, completely different service, completely different regulations. Road crossing at land borders. High demand — Parida Natty's post got 5 likes and 10 comments within days.

New content cluster needed: `UAE to Oman pet travel by car`

**2. Flight buddies is a real thing customers search for**
Craig White is looking for "flight buddies" — someone to escort pets on the plane as excess luggage or in cabin when the owner cannot fly on that route. This is a niche service that is searched for but almost no provider addresses it.

New keyword: `flight buddies pet relocation UAE Philippines`

**3. REAL PRICE DATA is publicly available and unverified**
Anonymous customer broke down actual costs: Fit to fly 200 AED, MOCCAE account 400 AED, cargo attestation + airline ~1500 AED. This is unverified community data. It needs to be checked against official sources. But it tells us what customers expect to pay and confirms the MOCCAE process is a known pain point.

Note: MOCCAE account setup appearing in Facebook confirms this needs its own content page — what is it, how to do it, how long it takes, what it costs.

**4. Breed restrictions are a huge hidden fear**
BSH (British Shorthair) rejected by Emirates. Customers discover this only when they call the airline — at which point they may have already booked. This fear needs dedicated content: "Which cat breeds can fly on Emirates?" and "What to do if your breed is rejected."

**5. Carrier measurements are a genuine operational nightmare**
Etihad requires soft carrier 40x40x22cm. Customers cannot find carriers that fit. This is a content page, a checklist, and potentially a product recommendation opportunity. "Etihad approved cat carrier — where to buy in Dubai."

**6. Competitors are actively fishing for leads in Facebook groups**
AirPaws Relocation (Julia Na) commented on at least 2 different posts offering help. Pawsome Pets UAE left a comment with their website. MovingBay.com posted a paid ad. Relocate MENA dropped their link. The Facebook group is a direct lead generation channel for competitors. This means:
- Your competitors are doing community outreach — you need to also
- The 10:1 rule applies — give value 10 times before mentioning your service
- This is Skill 26 (Community Authority) territory — build it now, not later

**7. Philippines is confirmed as Tier 2 at minimum**
Appeared in: Google autocomplete (multiple letters), Related Searches, and now 2 Facebook posts with engagement. UAE to Philippines is a real high-demand route with cost-conscious customers (different persona from corporate expat).

---

### New Keywords From Facebook — Add to Spreadsheet

These go into the Community Language tab AND into the main keyword collection if they have search potential:

```
pet relocation Dubai to Spain
pet relocation Dubai to Spain cost
MOCCAE pet export cost
MOCCAE account setup Dubai
fit to fly certificate Dubai cost
fit to fly certificate UAE vet
Emirates BSH cat policy
Emirates restricted cat breeds Dubai
Emirates 2 dogs same crate
Emirates pet cargo crate rules
cat transport UAE to USA service
cat import UAE requirements
cat vaccination Dubai import requirements
pet transport UAE Oman by car
pet transport UAE Oman road
pet relocation Oman from Dubai
temporary pet travel UAE Oman
take pets to Oman by road
Oman pet import requirements from UAE
UAE Oman pet quarantine rules
Oman rabies risk pet travel
affordable dog relocation UAE Philippines
flight buddies pet relocation UAE
flight buddies pet Philippines
cheap pet relocation Philippines
Etihad cabin cat carrier size requirements
Etihad soft carrier dimensions 40x40x22
Etihad approved cat carrier Dubai
how much should pet relocation cost Dubai
cargo village attestation Dubai pet
```

---

### Reddit Research — Method and Plan

**Why not Reddit's own API:**
Reddit's API requires OAuth application approval, verified account, and approval process. Cannot be used immediately without going through that process.

**SerpApi Reddit method — available now:**
SerpApi can query Google with `site:reddit.com` to find indexed Reddit posts about pet relocation in UAE. This is added as Phase 4 of the engine — after Google keyword collection is verified.

SerpApi call for Reddit:
```
engine=google
q="pet relocation Dubai" site:reddit.com
gl=ae (or gl=gb, gl=us for different perspectives)
hl=en
```

This returns the most popular Reddit threads Google has indexed on this topic. The posts and comments within those threads contain the exact language customers use.

**Subreddits to search:**
- r/dubai — "pet relocation", "move dog", "bring cat", "fly pet"
- r/expats — "Dubai pet", "UAE pet", "pet Dubai"
- r/PetTravel — "Dubai", "UAE"
- r/DubaiExpats — all pet-related posts
- r/uae — pet travel posts

**Reddit data collected this way goes into:**
- Community Language tab — exact quotes
- Keyword Collection — any new keywords not already captured
- Competitor tracking — any new services mentioned

**Phase 4 engine addition:** Add Reddit search via SerpApi site:reddit.com to the engine after Phase 3 Google keyword run completes and is verified.

---

### Updated Verification Checklist

- [x] Manual Session 1 — autocomplete + alphabet a–h for seed keyword 1
- [x] Manual Session 2 — PAA + Related Searches for seed keyword 1
- [x] API capabilities verified and documented
- [x] Negative keywords identified and confirmed
- [x] Competitors identified — now **21 confirmed** (expanded 2026-05-27 from 8 via Reddit + Facebook batches)
- [x] India confirmed as Tier 1 route
- [x] Export cluster confirmed
- [x] Spreadsheet built with all columns
- [x] Google Trends check — UAE + 5 year view — market growing, next surge Sep/Oct 2026
- [x] Facebook group research — Pet Moving and Relocation — 6 screenshots, 13 quotes, 4 new competitors, Oman route discovered
- [x] Facebook group research — **Dog Lovers In UAE — 10 screenshots** (Muze Gu confiscation fear, Global Paws, Snoopy Pets, Egypt/Jordan routes)
- [x] Reddit research **r/dubai — 9 screenshots** (9 Lives AE, Pet Express, Sandy Paws, Sharjah hack, export process)
- [x] Reddit research **r/UAE — 10 screenshots** (Etihad nightmare timeline, Turkish/Lufthansa alternatives)
- [x] Letters i through z — handled by engine (full 27-seed run complete)
- [x] Remaining seeds — all 27 seeds processed by engine
- [ ] Keyword Planner volume check — after engine run
- [ ] Competitor Trust Score research — all **21** competitors
- [x] Engine built and tested in Claude Code
- [x] Engine Phase 1 test — single seed validated against manual baseline
- [x] Engine Phase 2 test — three seeds validated
- [x] Engine Phase 3 — full run (598 keywords, 27/27 seeds)
- [x] Post-run audit checklist completed — Phase 3 PASSED 90%
- [ ] Phase 4 — Reddit search via SerpApi added to engine

**New content gaps discovered (2026-05-27):** confiscation-at-airport fear (dog taken, never returned), UAE export step-by-step, Etihad booking survival guide, airport comparison (Sharjah vs Dubai vs Abu Dhabi), airline cabin comparison, bird/parrot/turtle/rabbit relocation, rabies titer cost+timeline transparency, and the UAE pet abandonment crisis. Full detail: `research/community/2026-05-26-facebook-group-findings.md`.
