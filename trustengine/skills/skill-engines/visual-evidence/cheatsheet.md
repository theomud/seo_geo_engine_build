# Visual Evidence Architecture — Cheatsheet

*Does the page SHOW proof — real photos, dated screenshots, data visuals — beside its claims?*

| # | Measurement | What to do | Example (don't &rarr; do) |
|---|---|---|---|
| 1 | Images present | Add real images that show the work/proof. | DON'T: A wall of text, no images. &rarr; DO: Real photos of the crate prep, vet check and airport handover. |
| 2 | Alt text coverage | Add descriptive alt text to every image. | DON'T: <img> with no alt attribute. &rarr; DO: alt="MOCCAE import-fee page, captured 2026-06". |
| 3 | Real (non-stock) images | Replace stock photos with real photos of the actual work. | DON'T: A stock smiling-dog photo. &rarr; DO: Your own photo of the actual handover. |
| 4 | Data visuals (tables/charts) | Turn key numbers into a table or simple chart/infographic. | DON'T: Costs written in a paragraph. &rarr; DO: A cost table or a simple bar chart. |
| 5 | Video / rich media | Add a short video (process/explainer) or transcript-backed embed. | DON'T: No video. &rarr; DO: A 60-second process video with its transcript on the page. |
| 6 | Captions / figure context | Wrap images in <figure> with a <figcaption> explaining what it proves. | DON'T: A bare image. &rarr; DO: <figure><figcaption>MOCCAE 500 AED release fee, 2026</figcaption></figure>. |
| 7 | Visual density | Add a proof image beside each major claim, not just one at the top. | DON'T: One hero image only. &rarr; DO: A proof image beside each major claim. |


**Run:** `python skill-engines/visual-evidence/engine.py --url <URL>` or `--serve 8094` (web checker).
