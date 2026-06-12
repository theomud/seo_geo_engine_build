# Visual Evidence Architecture — Learner Manual

A frightened, high-stakes visitor believes what they can see proven, not what the text asserts. This engine scores whether a page backs its claims with visible evidence: real photos (not stock), official-source screenshots, captions, and phone-readable data visuals — instead of decoration.

## How to run the engine
- Score a page: `python skill-engines/visual-evidence/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/visual-evidence/engine.py --serve 8094`
- These docs: `python skill-engines/visual-evidence/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Images present

**How we measure it:** We count images on the page.

**Why it works:** A page of pure text gives a wary visitor nothing to believe; visuals carry proof.

**What to do:** Add real images that show the work/proof.

## Example (what NOT to do -> what to do)
- DON'T: A wall of text, no images.
- DO: Real photos of the crate prep, vet check and airport handover.

## 2. Alt text coverage

**How we measure it:** We measure the share of images with alt text.

**Why it works:** Alt text makes images accessible and machine-readable — and signals real, described evidence.

**What to do:** Add descriptive alt text to every image.

## Example (what NOT to do -> what to do)
- DON'T: <img> with no alt attribute.
- DO: alt="MOCCAE import-fee page, captured 2026-06".

## 3. Real (non-stock) images

**How we measure it:** We flag images whose source looks like a stock library.

**Why it works:** Stock 'happy customer' photos are tuned out; a real photo of the actual work is proof.

**What to do:** Replace stock photos with real photos of the actual work.

## Example (what NOT to do -> what to do)
- DON'T: A stock smiling-dog photo.
- DO: Your own photo of the actual handover.

## 4. Data visuals (tables/charts)

**How we measure it:** We count tables, SVG/canvas, and infographic terms.

**Why it works:** Numbers shown as a table or chart are lifted and believed more than numbers buried in prose.

**What to do:** Turn key numbers into a table or simple chart/infographic.

## Example (what NOT to do -> what to do)
- DON'T: Costs written in a paragraph.
- DO: A cost table or a simple bar chart.

## 5. Video / rich media

**How we measure it:** We detect video tags and YouTube/Vimeo embeds.

**Why it works:** Video is a strong trust + citation surface, especially for process/how-to content.

**What to do:** Add a short video (process/explainer) or transcript-backed embed.

## Example (what NOT to do -> what to do)
- DON'T: No video.
- DO: A 60-second process video with its transcript on the page.

## 6. Captions / figure context

**How we measure it:** We count figure/figcaption elements.

**Why it works:** A caption tells the reader what they're looking at and why it proves the claim.

**What to do:** Wrap images in <figure> with a <figcaption> explaining what it proves.

## Example (what NOT to do -> what to do)
- DON'T: A bare image.
- DO: <figure><figcaption>MOCCAE 500 AED release fee, 2026</figcaption></figure>.

## 7. Visual density

**How we measure it:** We compute images per 500 words.

**Why it works:** Proof should sit beside claims throughout, not appear once — density signals evidence-led content.

**What to do:** Add a proof image beside each major claim, not just one at the top.

## Example (what NOT to do -> what to do)
- DON'T: One hero image only.
- DO: A proof image beside each major claim.
