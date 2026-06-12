# Content Architecture — Cheatsheet

*Is the site's structure deliberate — clean URLs, internal links, navigable, no dead ends?*

| # | Measurement | What to do | Example (don't &rarr; do) |
|---|---|---|---|
| 1 | Clean URL | Use a clean lowercase, hyphenated, keyword URL (no params/IDs). | DON'T: /page.php?id=12345&cat=3 &rarr; DO: /routes/dubai-to-uk |
| 2 | Shallow click depth | Bring the page within 3 clicks of the homepage. | DON'T: /a/b/c/d/e/page (5+ levels) &rarr; DO: /routes/dubai-to-uk (≤3 levels) |
| 3 | Internal linking | Add internal links to related pages (and link to this page from others). | DON'T: No links to other pages. &rarr; DO: Links to related route, cost and fear pages. |
| 4 | Descriptive anchors | Replace 'click here' with descriptive anchor text. | DON'T: click here &rarr; DO: Dubai to UK pet import rules |
| 5 | Semantic navigation | Add a semantic <nav> with the main sections. | DON'T: Links loose in a <div>. &rarr; DO: A semantic <nav> with the main sections. |
| 6 | Breadcrumbs | Add breadcrumb navigation (+ BreadcrumbList schema). | DON'T: (no breadcrumbs) &rarr; DO: Home › Routes › Dubai to UK |
| 7 | Heading structure | Break the page into clear H2 sections. | DON'T: One long block of text. &rarr; DO: H2: Requirements / Timeline / Costs. |


**Run:** `python skill-engines/content-architecture/engine.py --url <URL>` or `--serve 8097` (web checker).
