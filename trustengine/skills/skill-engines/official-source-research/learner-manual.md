# Official Source Research — Learner Manual

In regulated markets, wrong information causes real harm. This engine scores whether a page backs claims with official sources: links to government/authority sites, named regulators, exact quotes, dates, and provenance for figures — instead of unsourced assertions.

## How to run the engine
- Score a page: `python skill-engines/official-source-research/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/official-source-research/engine.py --serve 8098`
- These docs: `python skill-engines/official-source-research/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Official sources linked

**How we measure it:** We count outbound links to government/authority domains.

**Why it works:** A claim with a link to the regulator is provable; an unsourced claim is just an assertion.

**What to do:** Link the official government/authority page for each regulation/fee.

## Example (what NOT to do -> what to do)
- DON'T: Dubai requires documents.
- DO: Dubai requires an import permit — see MOCCAE (moccae.gov.ae).

## 2. Authorities named

**How we measure it:** We detect named regulators/bodies (MOCCAE, DEFRA, IATA…).

**Why it works:** Naming the actual authority signals the writer went to the source, not a competitor's blog.

**What to do:** Name the actual regulator (e.g. MOCCAE, DEFRA) for each rule.

## Example (what NOT to do -> what to do)
- DON'T: the government says…
- DO: MOCCAE (UAE) and DEFRA (UK) require…

## 3. Citation phrasing

**How we measure it:** We look for 'according to / per the / states that' phrasing.

**Why it works:** Explicit attribution makes claims checkable and is what AI engines reward when citing.

**What to do:** Attribute claims explicitly ('according to MOCCAE…').

## Example (what NOT to do -> what to do)
- DON'T: Pets need a titer test.
- DO: According to MOCCAE, pets need a titer test.

## 4. Exact quotes

**How we measure it:** We detect verbatim quoted passages.

**Why it works:** An exact quote of the regulation is the strongest, most-liftable proof.

**What to do:** Quote the exact regulatory wording, then translate it to plain English.

## Example (what NOT to do -> what to do)
- DON'T: valid for about 10 days
- DO: "valid for ten (10) days from the date of issue" (MOCCAE).

## 5. Dates / verification

**How we measure it:** We look for years and 'updated/verified/as of' markers.

**Why it works:** Regulations change; a date tells the reader the fact is current, not stale.

**What to do:** Add the date each fact was verified; re-check every 90 days.

## Example (what NOT to do -> what to do)
- DON'T: (undated claim)
- DO: Verified against MOCCAE, June 2026.

## 6. Figure provenance

**How we measure it:** We compare citation count to the number of figures.

**Why it works:** Every number should trace to a source; lots of figures with no citations is a red flag.

**What to do:** Give every figure a source, or hedge it honestly if none is published.

## Example (what NOT to do -> what to do)
- DON'T: A fee figure with no source.
- DO: 500 AED release fee (MOCCAE, 2026).
