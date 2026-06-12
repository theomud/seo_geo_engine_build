---
Status: verified — tested manually and cross-referenced against documentation
Area: research/api-capabilities
Date: 2026-05-26
Verification method: Manual collection sessions + API documentation review + extended web research
---

# API Capabilities Research — Keyword Collection

## The Core Question

Which APIs can collect which types of Google search data? This was verified manually — not assumed.

## Verification Method

Manual sessions on 2026-05-26 collected:
- Autocomplete data (before pressing enter) — 10 screenshots
- People Also Ask data (after pressing enter, mid-page) — 1 screenshot
- Related Searches data (after pressing enter, bottom of page) — 1 screenshot

These manual results were then cross-referenced against API documentation to confirm which APIs can replicate which data types.

## Complete Capability Matrix

| Data Type | Unofficial Google API | SerpApi | DataForSEO | Reddit API (PRAW) | Facebook API |
|-----------|----------------------|---------|------------|-------------------|-------------|
| Autocomplete | ✅ | ✅ | ✅ | ❌ | ❌ |
| Alphabet expansion | ✅ | ✅ | ✅ | ❌ | ❌ |
| Question prefixes | ✅ | ✅ | ✅ | ❌ | ❌ |
| People Also Ask | ❌ | ✅ | ✅ | ❌ | ❌ |
| Related Searches | ❌ | ✅ | ✅ | ❌ | ❌ |
| Organic results | ❌ | ✅ | ✅ | ❌ | ❌ |
| Featured snippets | ❌ | ✅ | ✅ | ❌ | ❌ |
| Local pack | ❌ | ✅ | ✅ | ❌ | ❌ |
| Ad results | ❌ | ✅ | ✅ | ❌ | ❌ |
| Search volume | ❌ | ❌ separate | ✅ built in | ❌ | ❌ |
| Keyword difficulty | ❌ | ❌ | ✅ | ❌ | ❌ |
| CPC estimate | ❌ | ❌ | ✅ | ❌ | ❌ |
| Full Reddit threads + comments | ❌ | ❌ | ❌ | ✅ | ❌ |
| Upvote counts | ❌ | ❌ | ❌ | ✅ | ❌ |
| Facebook group posts | ❌ | ❌ | ❌ | ❌ | ❌ (no public API) |
| UAE location targeting | ⚠️ best effort | ✅ reliable | ✅ reliable | N/A | N/A |
| Arabic language | ⚠️ limited | ✅ | ✅ | N/A | N/A |
| Reliability | No SLA — unofficial | 99.95% SLA | 99.95% SLA | Official API | No API exists |
| Cost | Free | Monthly plan | $0.0006–$0.002/call | Free (rate limited) | N/A |

## Why Unofficial Google API Is Used Despite Limitations

The unofficial Google API (`suggestqueries.google.com/complete/search`) is free and returns autocomplete data. It is used in parallel with SerpApi for the autocomplete step only — as a cross-check.

The comparison test: run both APIs on the same keyword. If SerpApi returns a keyword and the unofficial API also returns it — double-verified. If only SerpApi returns it — investigate. If only unofficial returns it — flag for manual verification.

The match rate between the two APIs is documented in Sheet 4 of the keyword collection spreadsheet after every engine run. This is a data quality signal unique to this system — no published SEO methodology prescribes this verification step.

## Why PAA and Related Searches Require SerpApi

Verified manually: PAA and Related Searches only appear AFTER pressing enter on the full Google results page. The unofficial Google API only replicates what appears BEFORE pressing enter — the autocomplete dropdown. It has no mechanism to load a full results page.

SerpApi simulates a complete Google search, loads the full results page, and parses every element. One call to `engine=google` returns both PAA and Related Searches simultaneously.

## Why Reddit API (PRAW) Is Not the Same as SerpApi Site:reddit.com

- SerpApi with `site:reddit.com`: returns Google's index of Reddit posts — titles and snippets only
- Reddit API via PRAW: returns full post bodies, every comment, every reply, upvote counts, complete threads

The comments in Reddit threads contain 10–30 people's fears, experiences, and recommendations per thread. This is the data that matters for fear-acknowledging keyword research. SerpApi's Reddit search surfaces the threads. PRAW extracts the conversation inside them.

## Why Facebook Has No API for This Purpose

Facebook's public API (Graph API) does not provide access to group posts or member comments for non-Page entities. Facebook groups are private or closed communities. No tool can access them via API. Manual participation by a real account is the only access method. This makes Facebook group language the only data source in the system that cannot be automated — and also the most underutilised by competitors.

## Phase Timeline

| API | Phase | Status |
|-----|-------|--------|
| SerpApi | Phase 1 — now | Active, key connected |
| Unofficial Google API | Phase 1 — now | Active, free |
| Reddit API (PRAW) | Phase 4 — after engine Phase 3 | Credentials to create |
| DataForSEO | Phase 2 — when scale justifies | Replaces manual Keyword Planner |
| Facebook | Never automated | Manual collection always |
