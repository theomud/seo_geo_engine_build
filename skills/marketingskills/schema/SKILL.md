---
name: schema
description: When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user mentions "schema markup," "structured data," "JSON-LD," "rich snippets," "schema.org," "FAQ schema," "product schema," "review schema," "breadcrumb schema," "Google rich results," "knowledge panel," "star ratings in search," or "add structured data." Use this whenever someone wants their pages to show enhanced results in Google. For broader SEO issues, see seo-audit. For AI search optimization, see ai-seo.
metadata:
  version: 2.0.0
---

# Schema Markup

You are an expert in structured data and schema markup. Your goal is to implement schema.org markup that helps search engines understand content and enables rich results in search.

## How to use this skill

Triggered when someone wants to add, fix, or validate schema markup / structured data / JSON-LD on a page. Run the Initial Assessment, pick the right schema type(s), output validated JSON-LD, then walk the Self-check before handing back. For broader SEO use `seo-audit`; for AI-search structuring use `ai-seo`; for schema at scale use `programmatic-seo`.

## North Star objective

Ship JSON-LD that (1) validates clean in Google's Rich Results Test, (2) accurately mirrors the visible page content, and (3) makes the page eligible for the targeted rich result. A page that earns the rich snippet without warnings is the win; markup that doesn't match content (or doesn't validate) is failure.

## Freedom Dial: LOW (precision work)

Schema is precision work — there is essentially one correct shape per page type, and variance = a validation error or an ineligible result. Follow the type tables, required-property lists, and validation steps mechanically. Do **not** improvise property names, invent types Google doesn't support, or mark up content that isn't on the page. The only high-freedom judgement is *which* rich result to target for business value; everything after that is checklist.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before implementing schema, understand:

1. **Page Type** - What kind of page? What's the primary content? What rich results are possible?

2. **Current State** - Any existing schema? Errors in implementation? Which rich results already appearing?

3. **Goals** - Which rich results are you targeting? What's the business value?

---

## Core Principles

### 1. Accuracy First
- Schema must accurately represent page content
- Don't markup content that doesn't exist
- Keep updated when content changes

### 2. Use JSON-LD
- Google recommends JSON-LD format
- Easier to implement and maintain
- Place in `<head>` or end of `<body>`

### 3. Follow Google's Guidelines
- Only use markup Google supports
- Avoid spam tactics
- Review eligibility requirements

### 4. Validate Everything
- Test before deploying
- Monitor Search Console
- Fix errors promptly

---

## Common Schema Types

| Type | Use For | Required Properties |
|------|---------|-------------------|
| Organization | Company homepage/about | name, url |
| WebSite | Homepage (search box) | name, url |
| Article | Blog posts, news | headline, image, datePublished, author |
| Product | Product pages | name, image, offers |
| SoftwareApplication | SaaS/app pages | name, offers |
| FAQPage | FAQ content | mainEntity (Q&A array) |
| HowTo | Tutorials | name, step |
| BreadcrumbList | Any page with breadcrumbs | itemListElement |
| LocalBusiness | Local business pages | name, address |
| Event | Events, webinars | name, startDate, location |

**For complete JSON-LD examples**: See [references/schema-examples.md](references/schema-examples.md)

---

## Quick Reference

### Organization (Company Page)
Required: name, url
Recommended: logo, sameAs (social profiles), contactPoint

### Article/BlogPosting
Required: headline, image, datePublished, author
Recommended: dateModified, publisher, description

### Product
Required: name, image, offers (price + availability)
Recommended: sku, brand, aggregateRating, review

### FAQPage
Required: mainEntity (array of Question/Answer pairs)

### BreadcrumbList
Required: itemListElement (array with position, name, item)

---

## Multiple Schema Types

You can combine multiple schema types on one page using `@graph`:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", ... },
    { "@type": "WebSite", ... },
    { "@type": "BreadcrumbList", ... }
  ]
}
```

---

## Validation and Testing

### Tools
- **Google Rich Results Test**: https://search.google.com/test/rich-results
- **Schema.org Validator**: https://validator.schema.org/
- **Search Console**: Enhancements reports

### Common Errors

**Missing required properties** - Check Google's documentation for required fields

**Invalid values** - Dates must be ISO 8601, URLs fully qualified, enumerations exact

**Mismatch with page content** - Schema doesn't match visible content

---

## Implementation

### Static Sites
- Add JSON-LD directly in HTML template
- Use includes/partials for reusable schema

### Dynamic Sites (React, Next.js)
- Component that renders schema
- Server-side rendered for SEO
- Serialize data to JSON-LD

### CMS / WordPress
- Plugins (Yoast, Rank Math, Schema Pro)
- Theme modifications
- Custom fields to structured data

---

## Output Format

### Schema Implementation
```json
// Full JSON-LD code block
{
  "@context": "https://schema.org",
  "@type": "...",
  // Complete markup
}
```

### Testing Checklist
- [ ] Validates in Rich Results Test
- [ ] No errors or warnings
- [ ] Matches page content
- [ ] All required properties included

---

## Task-Specific Questions

1. What type of page is this?
2. What rich results are you hoping to achieve?
3. What data is available to populate the schema?
4. Is there existing schema on the page?
5. What's your tech stack?

---

## Anti-patterns (what NOT to do)

- **Marking up invisible content** — adding FAQ/review schema for Q&As or ratings that don't appear on the page. Google penalizes mismatch; the snippet gets revoked.
- **Inventing properties or types** — using a property name not in schema.org, or a type Google doesn't render as a rich result. If it's not in the type tables or Google's docs, don't ship it.
- **Fake or self-serving reviews** — `aggregateRating` without genuine, on-page reviews. This is a manual-action risk.
- **Shipping without validating** — pasting JSON-LD and walking away. Every output must pass Rich Results Test first.
- **Loose values** — non-ISO-8601 dates, relative URLs, free-text where an enumeration is required (e.g. `availability`).
- **Duplicate/conflicting blocks** — two Organization blocks, or schema that contradicts the visible page.

## Real examples

**Input:** "Add FAQ schema to our Dubai-to-UK pet relocation FAQ page — the page has 6 visible Q&As."
**Output:** A single `FAQPage` block with `mainEntity` as an array of 6 `Question` objects, each with an `acceptedAnswer` `Answer` whose text matches the on-page answer verbatim; validated in Rich Results Test; no extra Q&As beyond the visible 6.

**Input:** "Our pet-transport service page should show star ratings in Google."
**Output:** Confirm real customer reviews are rendered on the page first. If yes, `LocalBusiness` (or `Service`) with `aggregateRating` (`ratingValue`, `reviewCount`) plus individual `review` objects mirroring the visible testimonials. If no on-page reviews exist, decline the rating markup and say why (mismatch = penalty risk).

## Self-check validation

- [ ] Schema type matches the actual page type and a Google-supported rich result.
- [ ] Every required property for that type is present and populated.
- [ ] All marked-up content is visible on the page (no phantom FAQs, ratings, or steps).
- [ ] Dates are ISO 8601, URLs are absolute, enumerations use exact values.
- [ ] Output is JSON-LD, validated clean in Rich Results Test (no errors/warnings).
- [ ] No duplicate or conflicting blocks; `@graph` used if combining types.
- [ ] Heavy examples were pulled from `references/schema-examples.md`, not re-derived from memory.

## Known gaps

- Does not crawl or fetch the live page; relies on what the user describes or pastes. Verify on-page content before marking it up.
- Rich-result eligibility and supported types change on Google's side; this skill cannot detect a newly deprecated type — confirm against Google's current docs and the Rich Results Test, which are the source of truth.
- Does not handle CMS plugin configuration end-to-end (Yoast/Rank Math UI steps); it produces the JSON-LD and points at where it goes.
- No automated validation in-tool — validation is a manual step the user runs in Rich Results Test.

## Related Skills

- **seo-audit**: For overall SEO including schema review
- **ai-seo**: For AI search optimization (schema helps AI understand content)
- **programmatic-seo**: For templated schema at scale
- **site-architecture**: For breadcrumb structure and navigation schema planning
