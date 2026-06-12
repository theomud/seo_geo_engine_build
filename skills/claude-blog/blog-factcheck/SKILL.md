---
name: blog-factcheck
description: >
  Verify statistics and claims in blog posts by fetching cited source URLs and
  checking if the claimed data actually appears on the page. Extracts all
  statistical claims (numbers, percentages, named sources), fetches each cited
  URL via WebFetch, and scores match confidence (exact match 1.0, paraphrase
  0.7-0.9, not found 0.0). Flags uncited claims as UNVERIFIED. Use when user
  says "fact check", "verify statistics", "check sources", "validate claims",
  "factcheck", "source verification".
user-invokable: true
argument-hint: "[file]"
license: MIT
---

# Blog Fact-Check

Verify statistics, claims, and source attributions in blog posts. Pure Claude
pipeline with no external NLP dependencies.

## How to use

Run on a finished or draft blog post: `/blog factcheck path/to/post.md`. Walk the
five workflow steps in order, then emit the Verification Report. Use on any post
with numbers, percentages, dollar figures, or named sources — for example a
PawRoute page citing UAE pet-import fees or confiscation statistics.

## North Star objective

Every numeric or sourced claim in the post is either VERIFIED against its cited
page or explicitly flagged so nothing ships unsupported. A reader (and Maya, the
Leaving-Dubai expat whose deepest fear is confiscation) must be able to trust
every "AED 1,200" and "73% of" on the page.

## Freedom Dial: LOW (precision work)

This is mechanical verification, not judgment. There is one correct score per
claim. Follow the steps and the Verification Scoring table exactly — variance is
failure. Do not paraphrase the scoring rubric or skip the report format.

## Workflow

### Step 1: Read the Blog Post

Read the target file and identify all sections containing data claims.

### Step 2: Extract Statistical Claims

Scan the full text for every claim that includes a number, percentage, dollar
amount, or named source. Build a claims list with these fields:

| Field | Description |
|-------|-------------|
| claim_text | The exact sentence or phrase containing the statistic |
| value | The numeric value (e.g., "42%", "$1.2M", "3x") |
| attribution | Named source if present (e.g., "HubSpot", "Gartner 2025") |
| url | Cited URL if present (from markdown link or parenthetical) |
| location | Heading or line number where the claim appears |

### Step 3: Verify Cited Claims

For each claim that includes a URL:

1. Fetch the source page via WebFetch
2. Search the returned content for the specific numeric value
3. If exact value found, check surrounding context matches the claim topic
4. Assign a confidence score (see Verification Scoring below)

Process claims sequentially to avoid rate-limiting source sites.

### Step 4: Flag Uncited Claims

For claims without a URL:

- Mark status as UNVERIFIED
- Suggest a search query the user can run to find a source
- If the attribution names a specific organization, suggest their domain

### Step 5: Generate Verification Report

Output the full results table, summary statistics, and recommended actions.

## Claim Extraction Patterns

Identify claims matching these structures:

**Fully cited** (highest priority):
- `[Number]% [claim] ([Source], [Year])` - parenthetical citation
- `[claim] [Number]% ... [markdown link to source]` - inline link
- `According to [Source], [Number]...` - attribution lead

**Uncited statistics** (flag for sourcing):
- `[Number]% of [noun phrase]` - standalone percentage
- `[Number]x more/less/higher/lower` - multiplier claims
- `$[Number] [claim]` - dollar figures without attribution

**Weak signals** (check context before extracting):
- `studies show`, `research indicates`, `data suggests` + nearby number
- `survey found`, `report reveals`, `analysis shows` + nearby number
- Round numbers in isolation (e.g., "millions of users") - skip unless specific

## Verification Scoring

| Score | Status | Criteria |
|-------|--------|----------|
| 1.0 | VERIFIED | Exact number found on cited page in matching context |
| 0.7-0.9 | PARAPHRASE | Similar data found but with different wording, rounding, or timeframe |
| 0.3-0.6 | WEAK | Source page exists and covers the topic but the specific statistic is not visible |
| 0.0 | NOT FOUND | Cited page does not contain the claimed data anywhere |
| N/A | UNVERIFIED | No source URL provided for the claim |

**Scoring guidance**:
- A claim of "43%" when the source says "nearly half" scores 0.8
- A claim of "2024" data when the source only has "2023" scores 0.7
- A claim citing a homepage when the stat lives on a subpage scores 0.3
- A 404 or unreachable URL scores 0.0

## Anti-patterns

- **Scoring from memory** — never assign VERIFIED without actually fetching the
  URL via WebFetch and finding the value on the page.
- **Trusting attribution alone** — a named source ("Gartner 2025") with no URL is
  UNVERIFIED, not VERIFIED. Names are not proof.
- **Inventing the rubric** — use the Verification Scoring table verbatim; do not
  improvise new confidence bands or round scores arbitrarily.
- **Context-blind matching** — finding "43%" anywhere on the page is not a match;
  the surrounding context must cover the same topic as the claim.
- **Skipping the report** — always emit the full results table and Recommended
  Actions, even when every claim verifies cleanly.

## Real examples

**Verified, exact match** — claim "Dubai charges AED 1,200 per pet import permit
([Ministry of Climate Change](https://example.gov.ae/permits))". WebFetch returns
a fee table listing AED 1,200. Score 1.0, VERIFIED.

**Paraphrase** — claim "nearly half of relocating owners fear confiscation
([source](https://example.com/survey))". Source says "48%". Score 0.8, PARAPHRASE.

**Uncited** — claim "most expat dogs in the UAE are golden retrievers" with no URL.
Status UNVERIFIED. Suggested query: "UAE expat dog breed ownership statistics".

## Output Format

### Verification Report: [Post Title]

**File**: [path]
**Claims found**: [total]
**Verified**: [count] | **Paraphrase**: [count] | **Weak**: [count] | **Not Found**: [count] | **Unverified**: [count]

| # | Claim | Source URL | Score | Status | Notes |
|---|-------|-----------|-------|--------|-------|
| 1 | "73% of marketers..." | https://example.com/report | 1.0 | VERIFIED | Exact match found in section 3 |
| 2 | "5x ROI improvement" | https://example.com/study | 0.8 | PARAPHRASE | Source says "nearly 5x" |
| 3 | "60% prefer video" | (none) | N/A | UNVERIFIED | Try: "video preference statistics 2025" |

### Recommended Actions
- [List claims that need source URLs]
- [List claims with weak or not-found scores that need replacement sources]
- [List claims where the source data may be outdated]

## Integration

This skill can be called from `blog-analyze` as an optional deep-verification step.
When invoked from the analyzer, only claims scoring below 0.7 are flagged in the
analysis report.

Standalone usage: `/blog factcheck path/to/post.md`

## Cross-reference

claude-blog inherits FLOW's evidence triple (year anchor in prose, inline citation with publisher and title, URL with retrieval date). See `skills/blog-flow/references/flow-framework.md` and `/blog flow` for the full framework.

## Self-check validation

- [ ] Every numeric/dollar/percentage/named-source claim was extracted into the
  claims list.
- [ ] Every claim with a URL was fetched via WebFetch — no scores assigned from memory.
- [ ] Each score maps to a row in the Verification Scoring table.
- [ ] Claims without a URL are marked UNVERIFIED with a suggested search query.
- [ ] The Verification Report table and Recommended Actions are both present.

## Known gaps

- **Paywalled content**: WebFetch cannot access content behind login walls. These
  score as WEAK (0.5) with a note about paywall detection.
- **Dynamic pages**: JavaScript-rendered content may not be available via WebFetch.
  If the page returns minimal content, note this in the status.
- **PDF sources**: WebFetch may not extract PDF text reliably. Flag PDF URLs for
  manual verification.
- **Archived pages**: If a URL returns 404, suggest checking web.archive.org.
- **Rate limits**: Process no more than 10 URLs per run to avoid overwhelming
  source servers. If a post has more than 10 cited URLs, verify the first 10 and
  list the remainder as SKIPPED.
- **No truth check**: this skill verifies a claim matches its cited page; it does
  not judge whether the source itself is authoritative or correct. Source quality
  is out of scope — defer to `/blog flow` for evidence-tier guidance.
