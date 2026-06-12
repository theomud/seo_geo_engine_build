# Authority Asset Creation — Learner Manual

The one thing AI cannot produce is a resource documented from real work — a real case, a real failure, real evidence. This engine scores whether a page reads as authored from experience: named credentialed author, dense verifiable proof, documented cases, original data, and cited sources — vs generic content any AI could generate.

## How to run the engine
- Score a page: `python skill-engines/authority-assets/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/authority-assets/engine.py --serve 8096`
- These docs: `python skill-engines/authority-assets/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Named, credentialed author

**How we measure it:** We look for a byline, Person schema, and credential language.

**Why it works:** AI content is anonymous; a verifiable expert author is exactly what E-E-A-T and readers trust.

**What to do:** Add a named author with real credentials (+ Person schema).

## Example (what NOT to do -> what to do)
- DON'T: Anonymous page.
- DO: By Jane Doe, IPATA-certified, 8 years' experience.

## 2. Proof density

**How we measure it:** We count verifiable proof items (numbers + citations) per 200 words.

**Why it works:** Authority is proof-dense; the Hormozi test — a basic AI prompt can't reproduce dense real evidence.

**What to do:** Add more verifiable proof (figures, citations) beside claims — aim ≥1 per 200 words.

## Example (what NOT to do -> what to do)
- DON'T: General claims throughout.
- DO: A figure or citation every couple of sentences.

## 3. Documented case / real example

**How we measure it:** We detect case-study / 'we helped' / dated-real-event language.

**Why it works:** A real documented case (with what went wrong) is the un-fakeable core no AI could write.

**What to do:** Document one real case end-to-end, including what went wrong.

## Example (what NOT to do -> what to do)
- DON'T: We help many clients.
- DO: In 2025 we moved a French Bulldog London→Dubai; the titer nearly lapsed — here's what we did.

## 4. Original data / statistics

**How we measure it:** We look for percentages and own-data language.

**Why it works:** Original statistics are the #1 citation lever and can only come from someone who did the work.

**What to do:** Publish an original statistic from your own data.

## Example (what NOT to do -> what to do)
- DON'T: (no data)
- DO: 74% of failed moves were due to incomplete titer docs, per our 450-move dataset.

## 5. Cited sources

**How we measure it:** We count citation signals and authoritative references.

**Why it works:** Citing primary sources is what separates documented expertise from assertion.

**What to do:** Cite the primary/official source for each factual claim.

## Example (what NOT to do -> what to do)
- DON'T: Pets need vaccines.
- DO: Per MOCCAE (moccae.gov.ae).

## 6. Credentials / accreditation

**How we measure it:** We look for licences/accreditations (IPATA/IATA/registered/insured).

**Why it works:** Third-party credentials are trust the reader can verify, not claim.

**What to do:** Show your licences/accreditations (IPATA, IATA, registration).

## Example (what NOT to do -> what to do)
- DON'T: (none shown)
- DO: IPATA member #1234, IATA-certified.

## 7. Un-AI-able specificity

**How we measure it:** We measure named-entity density (concrete, specific detail).

**Why it works:** Specifics a generic prompt can't produce are the signature of real, authored work.

**What to do:** Add specific names, places, figures only someone who did the work would know.

## Example (what NOT to do -> what to do)
- DON'T: We cover international routes.
- DO: Dubai→Heathrow via Emirates cargo; summer embargo Jun–Sep.
