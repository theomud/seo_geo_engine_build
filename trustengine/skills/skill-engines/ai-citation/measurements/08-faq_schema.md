# FAQ structured data

*Measurement 8 of AI Citation Readiness.*

## What it measures (how)
We check the page's machine-readable code for FAQPage / Question schema (the data engines read directly), and count the Q&A pairs.

## Why it works
FAQ schema hands the engine clean question→answer pairs in a format it parses natively — the easiest possible thing to cite.

## What to do (the fix)
Add 5+ FAQ Q&A as FAQPage JSON-LD (validate with Rich Results Test).

## Example (what NOT to do -> what to do)
- DON'T: (no FAQ on the page)
- DO: Add FAQPage schema with 5 Q&A, e.g. “Can pets fly to Dubai in summer?”
