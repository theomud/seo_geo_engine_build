# Content Architecture — Learner Manual

Sites built one page at a time sprawl: messy URLs, orphan pages, buried value. This engine scores structural signals on a page — clean URL, internal linking, navigation, breadcrumbs, descriptive anchors and shallow depth — the architecture that lets every page be found.

## How to run the engine
- Score a page: `python skill-engines/content-architecture/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/content-architecture/engine.py --serve 8097`
- These docs: `python skill-engines/content-architecture/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Clean URL

**How we measure it:** We check the URL for params/uppercase/IDs/extensions.

**Why it works:** Clean keyword URLs are readable, shareable, and a deliberate-architecture signal.

**What to do:** Use a clean lowercase, hyphenated, keyword URL (no params/IDs).

## Example (what NOT to do -> what to do)
- DON'T: /page.php?id=12345&cat=3
- DO: /routes/dubai-to-uk

## 2. Shallow click depth

**How we measure it:** We measure URL path depth.

**Why it works:** Pages within ~3 levels of home get crawled and found; deep pages get buried.

**What to do:** Bring the page within 3 clicks of the homepage.

## Example (what NOT to do -> what to do)
- DON'T: /a/b/c/d/e/page (5+ levels)
- DO: /routes/dubai-to-uk (≤3 levels)

## 3. Internal linking

**How we measure it:** We count same-domain internal links.

**Why it works:** Internal links distribute authority and stop pages becoming orphans.

**What to do:** Add internal links to related pages (and link to this page from others).

## Example (what NOT to do -> what to do)
- DON'T: No links to other pages.
- DO: Links to related route, cost and fear pages.

## 4. Descriptive anchors

**How we measure it:** We measure the share of internal anchors that are descriptive vs 'click here'.

**Why it works:** Descriptive anchor text carries topical signal and helps users and engines navigate.

**What to do:** Replace 'click here' with descriptive anchor text.

## Example (what NOT to do -> what to do)
- DON'T: click here
- DO: Dubai to UK pet import rules

## 5. Semantic navigation

**How we measure it:** We look for a <nav> element.

**Why it works:** A clear nav is the backbone of a navigable architecture.

**What to do:** Add a semantic <nav> with the main sections.

## Example (what NOT to do -> what to do)
- DON'T: Links loose in a <div>.
- DO: A semantic <nav> with the main sections.

## 6. Breadcrumbs

**How we measure it:** We look for breadcrumb markup.

**Why it works:** Breadcrumbs show the page's place in the hierarchy — for users and for search.

**What to do:** Add breadcrumb navigation (+ BreadcrumbList schema).

## Example (what NOT to do -> what to do)
- DON'T: (no breadcrumbs)
- DO: Home › Routes › Dubai to UK

## 7. Heading structure

**How we measure it:** We count H2 sections.

**Why it works:** A heading tree is the page-level architecture that makes content scannable and extractable.

**What to do:** Break the page into clear H2 sections.

## Example (what NOT to do -> what to do)
- DON'T: One long block of text.
- DO: H2: Requirements / Timeline / Costs.
