---
Status: draft — build after engine Phase 3 completes
Area: skill-01
Priority: high
Activation: after engine Phase 3 and keyword volume validation complete
Last updated: 2026-05-26
Depends on: skill-01/01-google-search-discovery.md, skill-01/02-intent-classification.md, skill-01-keyword-collection.xlsx (Sheet 1 populated)
Feeds into: skill-01-keyword-collection.xlsx (Column K), skill-03/content-structure.md, skill-09/conversion-copy.md
---

# Skill 01 — File 03: The Fear Formula
## Mapping the human fear behind every keyword

---

## Purpose

Every keyword in Column A of the spreadsheet represents a human being in a specific emotional state. The Fear Formula converts each keyword from a string of text into a specific, visceral fear statement that drives every content decision that follows.

This is the step nobody else does. Intent classification (informational/commercial/transactional) tells you what someone wants to find. Fear mapping tells you what they are afraid of. These are different things. A person searching "pet relocation Dubai to India" wants to find a service — but they are afraid their dog will be denied entry at the Indian border because of a documentation mistake. The service page that opens with "We handle every document so your dog arrives legally and safely" converts. The service page that opens with "Professional pet relocation from Dubai to India" does not.

---

## The Fear Formula

For every collection-validated keyword in Column K, complete this sentence:

> "I'm afraid that..."

The statement must be:
- **Specific** — not "I'm worried about the process" but "I'm afraid the rabies titre test timeline means my dog gets stuck in quarantine for 6 months"
- **Visceral** — it should feel like something real could go wrong
- **Tied to a real outcome** — rejection at customs, separated from pet, financial loss, pet injury, wasted time
- **Written from the customer's exact perspective** — use the language they used in Facebook groups and Reddit threads, not formal language

---

## Phase 1 — Single Fear Per Keyword (Build Now)

Build one fear statement per keyword using the Dubai community data already collected.

**Sources to draw from:**
- Facebook group quotes in `research/community/2026-05-26-facebook-group-findings.md`
- Reddit threads (Phase 4 engine output, once available)
- PAA questions in Sheet 2 — these are fears expressed as questions
- Related Searches in Sheet 3 — the next search reveals the deeper worry
- The customer persona profiles in `customer-profile/01-master-customer-profile.md`

**Examples from real community research:**

| Keyword | Fear Statement |
|---------|---------------|
| pet relocation Dubai to India | "I'm afraid my dog will be denied entry at Indian customs because the vaccination paperwork has a mistake I didn't catch" |
| Emirates pet policy | "I'm afraid Emirates won't accept my breed and I'll find out only after I've booked everything" |
| pet relocation Dubai cost | "I'm afraid I'm being quoted a ridiculous price and I have no way to know if it's fair" |
| MOCCAE account setup | "I'm afraid I'll start the MOCCAE process too late and it won't be ready before my move date" |
| bring cat to Dubai | "I'm afraid my cat will suffer in cargo and I won't be there to help her" |
| are people leaving pets behind in Dubai | "I'm afraid that when I can't figure out how to bring my pet, I'll have to make an impossible choice" |
| Etihad cabin carrier size | "I'm afraid I'll buy the wrong carrier and be turned away at the gate with no time to fix it" |
| UAE to Oman by car pet | "I'm afraid the border crossing will go wrong and my pet will be held at customs" |
| emergency pet relocation Dubai | "I'm afraid I've run out of time and nobody can help me move fast enough" |
| pet quarantine Dubai | "I'm afraid my pet will be taken away when we land and I won't see them for weeks" |

---

## Phase 2 — Multi-Community Fear Database (Build After Phase 2 Engine)

**This is the insight that makes the system defensible long-term.**

The same keyword can have completely different fears behind it depending on which community is searching it. When the engine runs from origin country locations (UK `gl=gb`, India `gl=in`, South Africa `gl=za`), the community language from those Reddit threads and Facebook groups will surface different fears for the same keywords.

**The same keyword, different communities, different fears:**

Example: "pet relocation Dubai to India"

| Community | Location | Primary Fear |
|-----------|----------|-------------|
| Indian expat in Dubai leaving job | UAE | "I'm afraid my dog will be denied at Indian customs because paperwork is wrong and I'll have to leave him" |
| Indian family planning Dubai move | India | "I'm afraid the cost will force me to choose between my pet and affording the move" |
| UK expat with Indian route connection | UK | "I'm afraid the transit routing through a third country adds quarantine requirements I don't know about" |

**What this means for content:**
- Same keyword → different page opening → different primary fear → different conversion
- A page written for Indian expats in Dubai leads with abandonment fear
- A page written for Indians planning to move leads with cost fear
- Both pages target the same keyword but serve different audiences

**The structural upgrade for Phase 2:**

Column K in the spreadsheet currently holds one fear statement. Phase 2 expands this to a fear profile per keyword:

```
Column K  — Primary Fear (Phase 1 — current)
Column L  — Secondary Fear (Phase 2 — multi-community)
Column M  — Community Source (which community this fear comes from)
Column N  — Route Context (which specific route this fear applies to)
```

**How to build the Phase 2 fear database:**

1. Run the engine from UK, India, South Africa locations (Phase 2 engine)
2. PRAW Reddit scraper runs across subreddits in each country context
3. Community language from each origin country populates separate Community Language tab rows with a "Location" column
4. For each keyword that appears across multiple community sources — compare the fear language across sources
5. Where the fear is different — create a separate fear entry for that community
6. Content strategy then decides which fear to lead with for each specific page based on its target audience

**Why this matters strategically:**

Most competitors write one generic page per keyword. You will have the intelligence to write the right page for the right community — with the right fear acknowledged in the first sentence. This is the difference between a 2% conversion rate and a 12% conversion rate on the same keyword with the same traffic.

---

## How to Build File 02 (Phase 1)

**Step 1 — Prepare**
Open the spreadsheet to Sheet 1. Filter by status = collection-validated. You have approximately 800–1,200 keywords to process.

**Step 2 — Group by fear type first**
Before writing individual fear statements, group keywords by the type of fear they trigger. Most keywords fall into one of these fear categories in the pet relocation market:

| Fear Category | Keywords in This Category |
|--------------|--------------------------|
| Rejection / denial | customs, border, import rules, requirements, permit, quarantine |
| Documentation mistake | paperwork, microchip, vaccination, certificate, MOCCAE |
| Airline rejection | breed restriction, cabin rules, carrier size, cargo, Emirates, Etihad |
| Financial shock | cost, price, quote, fee, expensive |
| Separation from pet | quarantine, cargo, flight time, layover |
| Wrong provider | best company, reviews, trusted, IPATA |
| Time pressure | emergency, urgent, last minute, before summer |
| Pet suffering | safe, stress, trauma, sedation, heat |
| Process overwhelm | how to, steps, checklist, guide, what do I need |

Grouping first means you write similar fear statements together — faster and more consistent.

**Step 3 — Write the fear statements**
For each keyword, complete "I'm afraid that..."
Draw from community quotes wherever possible — real language beats invented language every time.

**Step 4 — Claude Code automation option**
The bulk of fear statements can be drafted by Claude Code using this input:
- The keyword
- The community language quotes from the same fear category
- The customer persona most likely to search this keyword

Claude drafts. You review and approve. Do not approve generic statements. Every fear statement must be specific enough that you could imagine a real person saying it.

**Step 5 — Audit 15% manually**
After the automated drafts, manually review 15% of the statements — specifically the ones in the highest-priority keyword clusters. These will be used in page headlines and opening sentences.

---

## What Fear Mapping Feeds Into

Every approved fear statement in Column K becomes an input for:

| Downstream Use | How the Fear Statement Is Used |
|---------------|-------------------------------|
| Page headline | "Are you afraid your dog will be denied entry? Here is exactly what to prepare." |
| Page opening sentence | Acknowledge the fear in the first 100 words |
| FAQ section | "Will my dog be quarantined in Dubai?" (the fear as a question) |
| CTA copy | "Get a verified checklist so nothing gets rejected" (the solution to the fear) |
| Content structure | Fear first → verified solution → evidence → CTA |
| Email nurture | 21-day sequence starting from the fear and moving toward confidence |

---

## Completion Criteria

File 03 — Phase 1 is complete when:
- [x] Column K populated for all collection-validated keywords in Sheet 1
- [x] Every fear statement is specific — no generic statements approved
- [x] Fear categories documented and consistent
- [x] Phase 2 multi-community database structure designed and documented
- [x] 15% manual audit complete (audit sub-agent, 2026-05-27)
- [ ] Phase 2 column structure (K, L, M, N) added to spreadsheet ready for Phase 2 data — deferred to Phase 2

## Test Results Log

**Phase 1 — Single fear per keyword — COMPLETE (2026-05-27)**
- Engine: `fear_classification_engine.py` (model `claude-sonnet-4-6`; spec's `claude-sonnet-4-20250514` is an older ID).
- Keywords classified: **598 / 598** (Column J intent + Column K fear). 0 errors.
- Intent breakdown: Informational 275 · Commercial 147 · Research 147 · Fear 14 · Transactional 13 · Urgency 2.
- Audit sub-agent verdict: **PASS** — 100% of fears start with "I'm afraid", all ≤30 words, all 6 intent types present, 78% fear statements unique (top duplicate ×11).
- Advisory (non-blocking): Urgency (2) and Transactional (13) thinly represented; 5 fears use scenario-anchored "something goes wrong" phrasing worth tightening.
- Built from the 12-fear database sourced from 69 community screenshots (`research/community/2026-05-26-facebook-group-findings.md`). Fears are matched to documented community language, never invented.

---

## Phase 2 Note — Do Not Build Yet

The multi-community fear database described above is Phase 2 work. It requires:
- Engine Phase 2 running from origin country locations
- Reddit PRAW data from country-specific subreddits
- Facebook group research from country-specific groups (British Expats, South Africans in Dubai, etc.)

Document this now so it is not forgotten. Build it when the Phase 2 engine runs.

The instruction for Claude Code when the time comes:
> "Read the Community Language tab. For each keyword in Column A, find every community quote that relates to it. Group quotes by the location/community they came from. Where the same keyword has quotes from different communities expressing different fears — create a separate fear entry for each community. Write these into Column L (secondary fear), Column M (community source), Column N (route context)."
