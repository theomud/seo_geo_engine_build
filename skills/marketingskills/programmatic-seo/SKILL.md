---
name: programmatic-seo
description: When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," "location pages," "[keyword] + [city] pages," "comparison pages," "integration pages," "building many pages for SEO," "pSEO," "generate 100 pages," "data-driven pages," or "templated landing pages." Use this whenever someone wants to create many similar pages targeting different keywords or locations. For auditing existing SEO issues, see seo-audit. For content strategy planning, see content-strategy.
metadata:
  version: 2.0.0
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

## Quality Checks

### Pre-Launch Checklist

**Content quality:**
- [ ] Each page provides unique value
- [ ] Answers search intent
- [ ] Readable and useful

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

## Related Skills

- **seo-audit**: For auditing programmatic pages after launch
- **schema**: For adding structured data
- **site-architecture**: For page hierarchy, URL structure, and internal linking
- **competitors**: For comparison page frameworks
- **copywriting**: For the per-page body content this skill templates
