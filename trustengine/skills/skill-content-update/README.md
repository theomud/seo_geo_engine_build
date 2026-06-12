# CONTENT UPDATE & REFRESH STRATEGY
## The system for deciding when to update, how to update, and when to remove

---

## What This Skill Is

Most content systems build new pages and ignore what they already have.
This is a mistake.

Updating existing content is often more valuable than creating new content.
A page ranking on page 2 may need only small improvements to reach page 1.
A declining page needs refreshing before a competitor takes the ranking.
A page that attracts traffic but does not convert needs a different fix.

Content Update & Refresh Strategy is the decision system for:
- When a page needs updating (and when to leave it alone)
- How to update it (what to change and what to keep)
- When to remove or consolidate it
- How to measure whether the update worked

**Skill Value Score: 16/25**
- Difficulty: 3/5
- Automation Potential: 3/5
- Market Uniqueness: 3/5
- Commercial Value: 4/5
- Teachability: 3/5

**Status:** 📋 Planned
**Niche-agnostic:** Yes — all content-driven businesses need this

---

## The Update Priority Matrix

Use this to decide what to update first:

| Situation | Action | Priority |
|-----------|--------|---------|
| High traffic + declining | Update immediately | 🔴 First |
| High potential + weak content | Update immediately | 🔴 First |
| Position 11-20 + good content | Small improvements | 🟡 Second |
| Low traffic + old | Low priority | 🟢 Third |
| High traffic + strong | Monitor only | ⬜ Hold |
| Competitor just improved | Respond within 30 days | 🔴 First |

---

## When To Update

Update a page when:
- Content is factually outdated (regulations changed, prices changed)
- Rankings are declining month-on-month
- A competitor has published better content on the same topic
- New verified information is available for the Source Bank
- Page has traffic but low conversions
- Page ranks on page 2 (small improvements can push to page 1)

Do NOT update a page when:
- It is performing well and rankings are stable
- The update would remove content that earns links
- You have more urgent priorities

---

## The 7-Step Update Process

**Step 1: Audit the current page**
What is working (keep), what is outdated (update), what is missing (add),
what competitors have that you do not (match or exceed).

**Step 2: Refresh and expand**
Update facts and figures from the Source Bank.
Add new sections for gaps competitors have.
Expand thin sections with verified information.
Improve headers to be more descriptive.

**Step 3: Optimise for search**
Improve title and meta description based on GSC CTR data.
Add internal links to newer pages.
Add schema markup if not already present.
Optimise for featured snippets with direct Q&A format.

**Step 4: Republish and promote**
Update the publish date.
Add internal links from related pages.
Share in communities if appropriate.

**Step 5: Monitor results**
Wait 4 weeks before judging the impact.
Track: ranking changes, traffic changes, conversion changes.

---

## When To Remove Content

Remove a page when:
- Gets zero traffic and has never had any
- Targets a keyword with no search volume
- Is factually incorrect and cannot be corrected
- Competes with a stronger page on the same topic (cannibalisation)
- Is too thin to be useful and cannot be expanded

---

## When To Consolidate

Consolidate when:
- Multiple thin pages on the same topic
- Individual pages do not rank but together they might
- Pages compete with each other for the same keyword

Consolidation process:
1. Merge best content from all pages into one
2. Set up 301 redirects from old URLs to new URL
3. Update all internal links to point to the new page
4. Remove old pages from sitemap

---

## The Re-verification Rule

Every verified fact in the Source Bank has a 90-day re-verification date.
Government regulations change. Airline policies change. Prices change.

When a Source Bank entry expires:
1. Visit the official source URL
2. Confirm the information is still accurate
3. Update the verified date
4. If changed — update the Source Bank and the page immediately

---

## Environment Variables

```
ANTHROPIC_API_KEY=
SOURCE_BANK_SPREADSHEET=    # Path to Official Source Research output
PROJECT_ROOT=
```

---

## Proof

**Status:** Planned
**Success metric:** No page older than 90 days without a review decision
**Skill Value Score (estimated):** 16/25
