---
name: competitors
description: "When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when the user mentions 'alternative page,' 'vs page,' 'competitor comparison,' 'comparison page,' '[Product] vs [Product],' '[Product] alternative,' 'competitive landing pages,' 'how do we compare to X,' 'battle card,' or 'competitor teardown.' Use this for any content that positions your product against competitors. Covers four formats: singular alternative, plural alternatives, you vs competitor, and competitor vs competitor. For sales-specific competitor docs, see sales-enablement."
metadata:
  version: 2.0.0
---

# Competitor & Alternative Pages

You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search terms, provide genuine value to evaluators, and position your product effectively.

## How to use this skill

1. Read the **Initial Assessment** and gather product + competitive-landscape context (pull from `.agents/product-marketing.md` if it exists — don't re-ask).
2. Pick one of the **four Page Formats** based on search intent.
3. Build to the **Core Principles** and **Essential Sections**, pulling heavy templates from Memory only when you actually draft a page.
4. Run the **Self-check** before handing back.

## North Star objective

A competitor page that ranks for the competitive query AND earns the evaluator's trust by being genuinely, verifiably honest — so a real switcher converts. A page that wins the ranking but reads as biased fails the North Star. Honesty is the moat: readers are comparing and will verify every claim.

## Freedom Dial: MIXED (plan high, output low)

- **High freedom — positioning & honesty judgment.** How you frame differentiators, who-it's-for calls, and which competitor strengths to concede are judgment work. Reason from the Core Principles; do not mechanise.
- **Low freedom — page structure & SEO mechanics.** Once a Format is chosen, follow its **Page structure** section order, URL pattern, and keyword targeting exactly. Variance here = lost rankings and broken internal-link hubs.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before creating competitor pages, understand:

1. **Your Product**
   - Core value proposition
   - Key differentiators
   - Ideal customer profile
   - Pricing model
   - Strengths and honest weaknesses

2. **Competitive Landscape**
   - Direct competitors
   - Indirect/adjacent competitors
   - Market positioning of each
   - Search volume for competitor terms

3. **Goals**
   - SEO traffic capture
   - Sales enablement
   - Conversion from competitor users
   - Brand positioning

---

## Core Principles

### 1. Honesty Builds Trust
- Acknowledge competitor strengths
- Be accurate about your limitations
- Don't misrepresent competitor features
- Readers are comparing—they'll verify claims

### 2. Depth Over Surface
- Go beyond feature checklists
- Explain *why* differences matter
- Include use cases and scenarios
- Show, don't just tell

### 3. Help Them Decide
- Different tools fit different needs
- Be clear about who you're best for
- Be clear about who competitor is best for
- Reduce evaluation friction

### 4. Modular Content Architecture
- Competitor data should be centralized
- Updates propagate to all pages
- Single source of truth per competitor

---

## Page Formats

### Format 1: [Competitor] Alternative (Singular)

**Search intent**: User is actively looking to switch from a specific competitor

**URL pattern**: `/alternatives/[competitor]` or `/[competitor]-alternative`

**Target keywords**: "[Competitor] alternative", "alternative to [Competitor]", "switch from [Competitor]"

**Page structure**:
1. Why people look for alternatives (validate their pain)
2. Summary: You as the alternative (quick positioning)
3. Detailed comparison (features, service, pricing)
4. Who should switch (and who shouldn't)
5. Migration path
6. Social proof from switchers
7. CTA

---

### Format 2: [Competitor] Alternatives (Plural)

**Search intent**: User is researching options, earlier in journey

**URL pattern**: `/alternatives/[competitor]-alternatives`

**Target keywords**: "[Competitor] alternatives", "best [Competitor] alternatives", "tools like [Competitor]"

**Page structure**:
1. Why people look for alternatives (common pain points)
2. What to look for in an alternative (criteria framework)
3. List of alternatives (you first, but include real options)
4. Comparison table (summary)
5. Detailed breakdown of each alternative
6. Recommendation by use case
7. CTA

**Important**: Include 4-7 real alternatives. Being genuinely helpful builds trust and ranks better.

---

### Format 3: You vs [Competitor]

**Search intent**: User is directly comparing you to a specific competitor

**URL pattern**: `/vs/[competitor]` or `/compare/[you]-vs-[competitor]`

**Target keywords**: "[You] vs [Competitor]", "[Competitor] vs [You]"

**Page structure**:
1. TL;DR summary (key differences in 2-3 sentences)
2. At-a-glance comparison table
3. Detailed comparison by category (Features, Pricing, Support, Ease of use, Integrations)
4. Who [You] is best for
5. Who [Competitor] is best for (be honest)
6. What customers say (testimonials from switchers)
7. Migration support
8. CTA

---

### Format 4: [Competitor A] vs [Competitor B]

**Search intent**: User comparing two competitors (not you directly)

**URL pattern**: `/compare/[competitor-a]-vs-[competitor-b]`

**Page structure**:
1. Overview of both products
2. Comparison by category
3. Who each is best for
4. The third option (introduce yourself)
5. Comparison table (all three)
6. CTA

**Why this works**: Captures search traffic for competitor terms, positions you as knowledgeable.

---

## Essential Sections

### TL;DR Summary
Start every page with a quick summary for scanners—key differences in 2-3 sentences.

### Paragraph Comparisons
Go beyond tables. For each dimension, write a paragraph explaining the differences and when each matters.

### Feature Comparison
For each category: describe how each handles it, list strengths and limitations, give bottom line recommendation.

### Pricing Comparison
Include tier-by-tier comparison, what's included, hidden costs, and total cost calculation for sample team size.

### Who It's For
Be explicit about ideal customer for each option. Honest recommendations build trust.

### Migration Section
Cover what transfers, what needs reconfiguration, support offered, and quotes from customers who switched.

**For detailed templates**: See [references/templates.md](references/templates.md)

---

## Content Architecture

### Centralized Competitor Data
Create a single source of truth for each competitor with:
- Positioning and target audience
- Pricing (all tiers)
- Feature ratings
- Strengths and weaknesses
- Best for / not ideal for
- Common complaints (from reviews)
- Migration notes

**For data structure and examples**: See [references/content-architecture.md](references/content-architecture.md)

---

## Research Process

### Deep Competitor Research

For each competitor, gather:

1. **Product research**: Sign up, use it, document features/UX/limitations
2. **Pricing research**: Current pricing, what's included, hidden costs
3. **Review mining**: G2, Capterra, TrustRadius for common praise/complaint themes
4. **Customer feedback**: Talk to customers who switched (both directions)
5. **Content research**: Their positioning, their comparison pages, their changelog

### Ongoing Updates

- **Quarterly**: Verify pricing, check for major feature changes
- **When notified**: Customer mentions competitor change
- **Annually**: Full refresh of all competitor data

---

## SEO Considerations

### Keyword Targeting

| Format | Primary Keywords |
|--------|-----------------|
| Alternative (singular) | [Competitor] alternative, alternative to [Competitor] |
| Alternatives (plural) | [Competitor] alternatives, best [Competitor] alternatives |
| You vs Competitor | [You] vs [Competitor], [Competitor] vs [You] |
| Competitor vs Competitor | [A] vs [B], [B] vs [A] |

### Internal Linking
- Link between related competitor pages
- Link from feature pages to relevant comparisons
- Create hub page linking to all competitor content

### Schema Markup
Consider FAQ schema for common questions like "What is the best alternative to [Competitor]?"

---

## Output Format

### Competitor Data File
Complete competitor profile in YAML format for use across all comparison pages.

### Page Content
For each page: URL, meta tags, full page copy organized by section, comparison tables, CTAs.

### Page Set Plan
Recommended pages to create with priority order based on search volume.

---

## Task-Specific Questions

1. What are common reasons people switch to you?
2. Do you have customer quotes about switching?
3. What's your pricing vs. competitors?
4. Do you offer migration support?

---

## Anti-patterns

- **Hype with no concessions.** A page that lists only your wins reads as an ad and loses trust (and rankings). Concede at least one real competitor strength.
- **Feature-checklist only.** Tables without paragraphs explaining *why* a difference matters. Depth over surface.
- **Fabricated or stale competitor data.** Misrepresenting a competitor's features/pricing — readers verify. Re-check pricing quarterly.
- **Wrong format for intent.** Using "You vs Competitor" when the searcher typed "[Competitor] alternatives" (plural research intent). Match format to intent.
- **Skipping who-it's-for honesty.** Refusing to name who the competitor is genuinely better for. The honest call is what converts the right switcher.
- **Drifting the structure.** Reordering a Format's prescribed section order — breaks the SEO-tuned hub and internal-link plan.

## Real examples

- **Format 1 (singular alternative)** — user prompt: *"Make us a PetRelocate alternative page."* → URL `/alternatives/petrelocate`, target `PetRelocate alternative` / `switch from PetRelocate`, structure opens with "Why people leave PetRelocate" (validate the confiscation fear) → your positioning → honest comparison → migration path for an in-flight relocation → switcher proof → CTA.
- **Format 4 (competitor vs competitor)** — user prompt: *"PetRelocate vs DubaiPaws, where do we fit?"* → URL `/compare/petrelocate-vs-dubaipaws`, neutral overview of both, comparison by category, who-each-is-best-for, then introduce yourself as the third option with the three-way table.

## Self-check validation

- [ ] Format chosen matches the searcher's intent (singular switch / plural research / direct vs / A-vs-B).
- [ ] Page follows that Format's exact section order, URL pattern, and target keywords.
- [ ] At least one genuine competitor strength is conceded; no fabricated claims.
- [ ] TL;DR summary present; comparison goes beyond tables with explanatory paragraphs.
- [ ] "Who it's for" stated honestly for every option.
- [ ] Competitor data sourced to a single source of truth; pricing verified current.
- [ ] Heavy templates pulled from `references/` only when drafting — not inlined.

## Known gaps

- No live SEO data: search-volume and SERP-difficulty calls are left to the user or `programmatic-seo`; this skill assumes the competitor set and priorities are supplied.
- Does not generate sales-internal collateral (battle cards, objection decks) beyond the public page — that is **sales-enablement's** job; this skill only positions public competitor/alternative pages.
- Review-mining and customer-switch interviews (Research Process) are manual; the skill prescribes the method but cannot fetch G2/Capterra data itself.

## Related Skills

- **programmatic-seo**: For building competitor pages at scale
- **copywriting**: For writing compelling comparison copy
- **seo-audit**: For optimizing competitor pages
- **schema**: For FAQ and comparison schema
- **sales-enablement**: For internal sales collateral, decks, and objection docs
