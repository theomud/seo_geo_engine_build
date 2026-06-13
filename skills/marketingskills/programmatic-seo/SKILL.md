---
name: programmatic-seo
description: When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," "location pages," "[keyword] + [city] pages," "comparison pages," "integration pages," "building many pages for SEO," "pSEO," "generate 100 pages," "data-driven pages," or "templated landing pages." Use this whenever someone wants to create many similar pages targeting different keywords or locations. For auditing existing SEO issues, see seo-audit. For content strategy planning, see content-strategy.
metadata:
  version: 2.1.0
---

# Programmatic SEO

You are an expert in programmatic SEO—building SEO-optimized pages at scale using templates and data. Your goal is to create pages that rank, provide value, and avoid thin content penalties.

## How to use this skill

1. Run the **Initial Assessment** to load context and frame the opportunity.
2. **Choose a playbook** (high-freedom judgment — see the dial below).
3. Work the **Implementation Framework** to design pattern, data, template, links, indexation.
4. Gate the build on the **Quality Checks** (low-freedom — variance here = a thin-content penalty).
5. Validate against the **Self-check** before you call the strategy done.

For detailed per-playbook implementation, the pointer is conditional: **if** you have committed to a playbook, see [references/playbooks.md](references/playbooks.md). Otherwise leave it unread.

## North Star objective

Ship the **smallest set of pages that each earn their index slot** — every page answers a real query with value Google can't get cheaper elsewhere. Success is pages that rank and convert without triggering thin-content, doorway, or duplicate-content penalties. 100 pages a user is proud of beats 10,000 that risk a manual action.

## Freedom Dial — MIXED (plan high, output low)

This skill has two phases with two different dials. State which phase you are in:

- **High freedom (planning):** picking the playbook, finding the keyword pattern, deciding what unique value each page carries, choosing data sources. Many right answers — reason from the **Core Principles** and the "Choosing Your Playbook" table; do **not** follow a rigid script.
- **Low freedom (output gate):** the **Quality Checks** checklist, URL/subfolder rules, indexation, schema, internal-linking architecture. One right answer — treat these as a mechanical checklist where variance = failure (a deindexed or penalised page).

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before designing a programmatic SEO strategy, understand:

1. **Business Context**
   - What's the product/service?
   - Who is the target audience?
   - What's the conversion goal for these pages?

2. **Opportunity Assessment**
   - What search patterns exist?
   - How many potential pages?
   - What's the search volume distribution?

3. **Competitive Landscape**
   - Who ranks for these terms now?
   - What do their pages look like?
   - Can you realistically compete?

---

## Core Principles

### 1. Unique Value Per Page
- Every page must provide value specific to that page
- Not just swapped variables in a template
- Maximize unique content—the more differentiated, the better

### 2. Proprietary Data Wins
Hierarchy of data defensibility:
1. Proprietary (you created it)
2. Product-derived (from your users)
3. User-generated (your community)
4. Licensed (exclusive access)
5. Public (anyone can use—weakest)

### 3. Clean URL Structure
**Use subfolders, not subdomains** — subfolders consolidate domain authority while subdomains split it:
- Good: `yoursite.com/templates/resume/`
- Bad: `templates.yoursite.com/resume/`

### 4. Genuine Search Intent Match
Pages must actually answer what people are searching for.

### 5. Quality Over Quantity
Better to have 100 great pages than 10,000 thin ones.

### 6. Avoid Google Penalties
- No doorway pages
- No keyword stuffing
- No duplicate content
- Genuine utility for users

---

## The 12 Playbooks (Overview)

| Playbook | Pattern | Example |
|----------|---------|---------|
| Templates | "[Type] template" | "resume template" |
| Curation | "best [category]" | "best website builders" |
| Conversions | "[X] to [Y]" | "$10 USD to GBP" |
| Comparisons | "[X] vs [Y]" | "webflow vs wordpress" |
| Examples | "[type] examples" | "landing page examples" |
| Locations | "[service] in [location]" | "dentists in austin" |
| Personas | "[product] for [audience]" | "crm for real estate" |
| Integrations | "[product A] [product B] integration" | "slack asana integration" |
| Glossary | "what is [term]" | "what is pSEO" |
| Translations | Content in multiple languages | Localized content |
| Directory | "[category] tools" | "ai copywriting tools" |
| Profiles | "[entity name]" | "stripe ceo" |

**For detailed playbook implementation**: See [references/playbooks.md](references/playbooks.md)

---

## Choosing Your Playbook

| If you have... | Consider... |
|----------------|-------------|
| Proprietary data | Directories, Profiles |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility product | Conversions |
| Content/expertise | Glossary, Curation |
| Competitor landscape | Comparisons |

You can layer multiple playbooks (e.g., "Best coworking spaces in San Diego").

---

## Implementation Framework

### 1. Keyword Pattern Research

**Identify the pattern:**
- What's the repeating structure?
- What are the variables?
- How many unique combinations exist?

**Validate demand:**
- Aggregate search volume
- Volume distribution (head vs. long tail)
- Trend direction

### 2. Data Requirements

**Identify data sources:**
- What data populates each page?
- Is it first-party, scraped, licensed, public?
- How is it updated?

### 3. Template Design

**Page structure:**
- Header with target keyword
- Unique intro (not just variables swapped)
- Data-driven sections
- Related pages / internal links
- CTAs appropriate to intent

**Ensuring uniqueness:**
- Each page needs unique value
- Conditional content based on data
- Original insights/analysis per page

### 4. Internal Linking Architecture

**Hub and spoke model:**
- Hub: Main category page
- Spokes: Individual programmatic pages
- Cross-links between related spokes

**Avoid orphan pages:**
- Every page reachable from main site
- XML sitemap for all pages
- Breadcrumbs with structured data

### 5. Indexation Strategy

- Prioritize high-volume patterns
- Noindex very thin variations
- Manage crawl budget thoughtfully
- Separate sitemaps by page type

---

## pSEO 2.0 — JSON Schema + AI

Modern pSEO treats AI as a structured data transformer, not a freeform writer. The key principle: **never ask AI to write freeform content — ask it to fill a schema.**

### Schema-First Benefits

- **Structurally identical, substantively different pages**: Every page follows the same JSON shape but carries genuinely distinct data. The schema enforces consistency; the data enforces uniqueness.
- **Automated validation**: JSON output can be validated programmatically before it ever reaches a template. Catch hallucinations, missing fields, and duplicates at the pipeline stage — not after publishing.
- **Content/presentation separation**: JSON files own the content; CMS or React templates own the presentation. Swap the template without touching content; update the content without touching the template.

### Niche Context Layer

Roughly **60% of pSEO effectiveness comes from audience-specific context injected into the prompt**, not from the template structure itself. Before generating any page, inject:

- **Audience profile**: who is searching this query, their skill level, their role
- **Pain points**: what problem they are trying to solve right now
- **Monetisation methods**: how this page is expected to convert (affiliate, lead gen, SaaS trial, etc.)

Example prompt structure:
```
You are filling a JSON schema for a page targeting [keyword].
Audience: [profile]. Pain points: [list]. Conversion goal: [method].
Fill every field. Do not invent statistics. Return valid JSON only.
Schema: { ... }
```

### Content vs Presentation

| Layer | Artifact | Owned by |
|-------|----------|----------|
| Content | JSON files (one per page) | Data pipeline / AI |
| Presentation | CMS templates or React components | Engineering / design |

This separation means a design refresh never requires regenerating content, and a content update never breaks the template.

---

## Batch Publishing Strategy

Never publish thousands of pages overnight — this is one of the fastest ways to trigger a manual spam review.

### Staged Rollout

1. **Week 1**: Launch 50–100 pages. This is enough to establish a pattern without triggering algorithmic flags.
2. **Weeks 2–3**: Monitor Search Console. Look at indexation rate, impressions, and any manual action notifications.
3. **If positive signals**: Expand to 500+ pages. Repeat the monitor step before scaling further.
4. **Never skip the monitor step** between tiers regardless of how confident you are in the content quality.

### Automated Quality Gates

Run these checks on every page before it enters the publish queue:

- Minimum word count met (set per playbook — e.g., 400 words for glossary, 600 for location pages)
- All required schema fields populated (no empty or null values)
- No hallucinated data (cross-reference numeric claims against source data)
- No near-duplicate pages (similarity check against already-published set)

### Manual Spot-Check

Review **10% of each batch** manually before the batch goes live. Rotate which 10% so the full set gets reviewed over time. If manual review finds issues, halt the batch, fix the pipeline, and re-run automated checks before re-queuing.

---

## Tech Stacks

Choose the stack that matches your page volume and team capability. Do not over-engineer for a 200-page site or under-engineer for a 50,000-page site.

### No-Code ($150–300/month)

Best for: 100–5,000 pages, non-technical teams.

| Tool | Role |
|------|------|
| Airtable | Data source / CMS backbone |
| Webflow CMS | Template rendering and hosting |
| Whalesync | Airtable → Webflow sync |
| Make.com | Automation glue / AI enrichment |

### WordPress (~$200 one-time)

Best for: 500–20,000 pages, existing WordPress sites.

| Tool | Role |
|------|------|
| Google Sheets | Data source |
| WP All Import Pro | Bulk page import from CSV/XML |
| ACF (Advanced Custom Fields) | Custom field schema per template |

### Developer Stack (10,000+ pages)

Best for: 10K–1M+ pages, engineering team available.

| Tool | Role |
|------|------|
| Next.js ISR | Static generation with incremental refresh |
| Gemini Flash | AI content generation at scale |
| PostgreSQL | Structured data store |
| Python | Data pipeline, validation, batch orchestration |
| IndexNow | Instant index submission to Bing/Yandex (speeds Google discovery) |

**API cost at scale**: approximately **$5–15 per 10,000 pages** with Gemini Flash (as of mid-2026). Budget accordingly — a 100K-page project costs roughly $50–150 in API calls alone before infrastructure.

---

## Quality Checks

### Pre-Launch Checklist

**Content quality:**
- [ ] Each page provides unique value
- [ ] Answers search intent
- [ ] Readable and useful
- [ ] Would this page be useful without search engines? (If the honest answer is no, do not publish it — see Google penalty guidance below.)

**Technical SEO:**
- [ ] Unique titles and meta descriptions
- [ ] Proper heading structure
- [ ] Schema markup implemented
- [ ] Page speed acceptable

**Internal linking:**
- [ ] Connected to site architecture
- [ ] Related pages linked
- [ ] No orphan pages

**Indexation:**
- [ ] In XML sitemap
- [ ] Crawlable
- [ ] No conflicting noindex

### "Would this page be useful without search engines?" Test

Google's quality rater guidelines and algorithmic signals penalise:

- **Keyword-swapped duplicates**: pages that differ only by a variable substitution with no substantive content difference
- **Content existing only to rank**: pages that serve no purpose a real user would recognise
- **Fabricated data**: statistics, prices, or facts invented or hallucinated by AI

Acceptable at scale: large sets of pages that address **genuinely distinct user intent** (different location, different integration, different persona) backed by **unique data** (proprietary, product-derived, or licensed). The test is whether a human arriving from that specific query would find the page genuinely useful — not just technically present.

### Post-Launch Monitoring

Track: Indexation rate, Rankings, Traffic, Engagement, Conversion

Watch for: Thin content warnings, Ranking drops, Manual actions, Crawl errors

---

## Anti-patterns (common mistakes)

- **Thin content**: Just swapping city names in identical content
- **Keyword cannibalization**: Multiple pages targeting same keyword
- **Over-generation**: Creating pages with no search demand
- **Poor data quality**: Outdated or incorrect information
- **Ignoring UX**: Pages exist for Google, not users
- **Subdomain split**: Putting pages on a subdomain and splitting domain authority
- **No Feedback Loop**: Launching pages and then ignoring Search Console. Fix: set up weekly monitoring cadence — double down on niches that are gaining impressions and clicks, prune or noindex underperformers after 90 days with no traction.

---

## Output Format

### Strategy Document
- Opportunity analysis
- Implementation plan
- Content guidelines

### Page Template
- URL structure
- Title/meta templates
- Content outline
- Schema markup

---

## Task-Specific Questions

1. What keyword patterns are you targeting?
2. What data do you have (or can acquire)?
3. How many pages are you planning?
4. What does your site authority look like?
5. Who currently ranks for these terms?
6. What's your technical stack?

---

## Real examples

**Locations playbook (pet relocation, this repo).** Pattern: `[service] in [location]` →
"pet relocation from Dubai to London", "import a dog to the UK from the UAE". Variables: origin
emirate × destination country × species. Unique value per page is **proprietary**: live-validated
cost tables, the destination's exact import rules (rabies titre wait, microchip standard, approved
airlines), and confiscation-risk notes for that corridor — not a city name swapped into one
template. URL: `pawroute.com/relocate/dubai-to-london/` (subfolder, not a subdomain). Hub = the
destination-country page; spokes = each origin corridor; cross-link sibling corridors. Pages with
no real search demand (tiny origin emirate × rare destination) are noindexed rather than shipped.

**Glossary playbook (same site).** Pattern: `what is [term]` → "what is a pet passport", "what is a
rabies titre test". One concept per page, each linking up to the relevant corridor pages.

**Zapier — Integrations playbook.** Pattern: `connect [App A] to [App B]`. Scale: **70,000+ pages**, **16.2M monthly visitors**, **1.3M+ keywords ranked**. Success factor: each page contains a real, working setup guide for that specific integration pair — not a template with app names swapped in. Users can actually follow the instructions to connect their tools. The depth of per-page utility is what separates it from a thin integration directory.

**Flyhomes — Locations playbook.** Pattern: `cost of living in [City]`. Scale: grew from **10,000 to 425,000 pages in 3 months**, reaching **1.1M visits**. Success factor: relocation intent mapped directly to product (Flyhomes helps people buy homes). Each page answers the specific cost question (rent, groceries, utilities for that city) and naturally leads to the core product. Intent alignment between the query and the conversion path is the critical variable.

**KrispCall — Locations + Product playbook.** Pattern: `[US area code] phone numbers`. Scale: drives **82% of KrispCall's US traffic**, with **1,969% year-over-year growth**. Success factor: highly specific geographic intent (people looking for a phone number with a particular area code) combined with unique carrier data per page (which providers serve that area, porting rules, local number availability). Specificity of intent plus proprietary data is the formula.

**Jake Ward / Byword — Niche context injection.** Pattern: `[Number] [content type] for [niche]` (e.g., "50 Instagram captions for coffee shops"). Scale: **13,000 pages generated in 3 hours**, growing from **971 to 5,500 weekly clicks (+466%) in 60 days**. Success factor: niche context injected into every prompt. The pages are not generic "50 Instagram captions" — each is tuned to a specific audience (coffee shop owners, yoga instructors, real estate agents). This is a direct demonstration that the Niche Context Layer is responsible for most of the SEO effectiveness, not the template structure itself.

## Self-check validation

- [ ] Each page carries **unique value** (proprietary/product/user data), not swapped variables
- [ ] A real **keyword pattern** with validated demand backs the page set
- [ ] **Subfolders, not subdomains**; titles + meta are unique per page
- [ ] **Hub-and-spoke** internal links present; no orphan pages; XML sitemap covers the set
- [ ] **Indexation** managed — thin/zero-demand variations noindexed, crawl budget respected
- [ ] Schema markup + heading structure in place; page speed acceptable
- [ ] No cannibalization (two pages chasing the same keyword)
- [ ] Planning phase reasoned from principles; output phase passed the Quality Checks checklist

## Known gaps

- This skill **plans and templates**; it does not write the per-page prose or build the site.
  Hand off body copy to **copywriting** and the actual Jinja/page generation to the SEO+GEO engine.
- No keyword-volume data source is bundled — "validate demand" assumes the user supplies volumes
  (Search Console, a keyword tool). The skill cannot pull search volumes itself.
- Penalty thresholds (how thin is "thin", crawl-budget limits) are judgment calls, not hard rules;
  Google does not publish them, so the Quality Checks are a best-effort guard, not a guarantee.
- GEO / AI-answer optimization (getting cited in AI Overviews / AI Mode) is out of scope here —
  that lives with the GEO work, not this pSEO skill.
- **Indexing timeline**: expect **3–6 months** for new domains to see meaningful indexation of pSEO pages. Established domains index faster but still rarely see full coverage in under 4 weeks for large batches.
- **Success rate**: roughly **40% of pSEO projects succeed** at meaningful scale. The 60% failure rate is almost entirely attributable to thin content — insufficient unique value per page, no proprietary data, or no niche context in AI generation. The technique works; the execution is the variable.
- **AI generation cost**: Gemini Flash at scale costs approximately **$5–15 per 10,000 pages** (mid-2026 pricing). Factor this into project economics before committing to large-scale generation. Costs will shift as model pricing changes.

## Related Skills

- **seo-audit**: For auditing programmatic pages after launch
- **schema**: For adding structured data
- **site-architecture**: For page hierarchy, URL structure, and internal linking
- **competitors**: For comparison page frameworks
- **copywriting**: For the per-page body content this skill templates
