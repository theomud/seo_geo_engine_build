---
Status: draft — built 2026-05-28
Area: skill-02
Depends on: skill-02/README.md (PENDING CLAIMS list)
Feeds into: skill-02/files/04-automation-spec.md
---

# Skill 02 · File 02 — How To Do It Manually
## The verification process step by step — always do this first

---

## Why manual first

Every automated verification step is built from a manual one. Until a human has visited the official source, found the exact quote, and recorded the row by hand for at least five claims, the automation spec is guessing. **Document the manual process with screenshots before any code is written.**

Time required: 4–8 hours for the initial Source Bank in a regulated niche, then ~30 minutes per month to re-verify dated rows.

---

## Step 1 — Build the claim list

Open every input source and list every regulation claim, one row per claim. Inputs (in priority order):

1. **Community research output** — every claim made by a customer in `research/community/2026-05-26-facebook-group-findings.md` and the 69 community screenshots (`research/community/screenshots/`).
2. **Competitor research output** — every claim made on a competitor page in `research/competitors/COMPETITOR-MASTER.html` and the 31 manual screenshots (`research/competitors/screenshots/`).
3. **Conflicts already known** — start with the items already enumerated in `skill-02/README.md` under PENDING CLAIMS (pricing discrepancies, timeline conflicts, process questions, airline-specific).

Each claim row in the spreadsheet (skeleton built in `skill-02/data/skill-02-source-bank.xlsx`):

| Column | Example value |
|--------|--------------|
| ID | C-001 |
| Category | Timeline · Pricing · Process · Airline · Restriction |
| Claim | "Rabies titer test results take 2–3 weeks in the UAE" |
| Community source | IrbisKat, Reddit r/dubai (Batch 5) |
| Official URL | _to be filled_ |
| Date checked | _to be filled_ |
| Exact quote | _to be filled_ |
| Plain English | _to be filled_ |
| Status | Pending |
| Notes | "Conflicts with Sammy12xyz quote (1 week, 700 AED)" |

Pending = nothing verified yet. The whole spreadsheet starts in Pending.

---

## Step 2 — Identify the official source for each claim

The hierarchy of acceptable sources, strictest first:

1. **The regulating government body.** For UAE pet import/export: **MOCCAE** (`moccae.gov.ae`). Specifically: `site.moccae.gov.ae/en/services/export-import-services/animal-health-certificate-for-export-re-export-of-live-animals.aspx`.
2. **The destination country's authority.** UK: `apha.gov.uk`. India: `dahd.gov.in`. Australia: `agriculture.gov.au`. EU: relevant member-state agriculture ministry.
3. **The airline operating the route.** Emirates: `emirates.com/.../travelling-with-pets`. Etihad: `etihad.com/.../pets`. Turkish: `turkishairlines.com`. Royal Jordanian: `rj.com`. Air Cairo: official policy page.
4. **A recognised industry body**, only when no government source exists. **IPATA** (`ipata.com`) for industry standards.
5. **Mark as Unverifiable** if none of the above publishes the claim. Do not substitute a competitor or a forum post.

If a claim falls between authorities (e.g. titer-test labs in the UAE), the regulator is the source of truth; an operator's published price is acceptable only if the operator is listed on the regulator's page.

---

## Step 3 — Visit the URL and find the exact quote

Open the page in a real browser. Search the visible text for the relevant phrase. **Copy the quote verbatim — do not paraphrase, do not edit punctuation.** If the page is a PDF, open it, copy the quote, record the page number.

Acceptable: "The Animal Health Certificate for export of live animals is valid for ten (10) days from the date of issue." — verbatim, with the page reference.

Not acceptable: "MOCCAE says the certificate is valid for 10 days." — paraphrased, no quote.

Take a screenshot of the page with the relevant text visible and save it to `skill-02/data/verification-screenshots/C-001-moccae-cert.png`. Screenshots are the only defence when an official page changes its text later.

---

## Step 4 — Write the plain-English translation

The exact quote is rarely customer-readable. Translate it into one sentence a confused pet owner would understand. Keep the meaning identical; remove the legal/regulatory texture.

Example:
- Quote: "The Animal Health Certificate for export of live animals is valid for ten (10) days from the date of issue."
- Plain English: "Your Cargo Village export certificate is only valid for 10 days — get it within 10 days of your flight."

The plain-English line is what content writers paste into pages. The quote is what the audit checks against.

---

## Step 5 — Record date checked + status

Date checked = the date the URL was visited and the quote re-verified. This is the most important field for maintenance — a date older than 90 days flags the row for re-check.

Status options:
- **Verified** — official source visited, quote recorded, plain English written.
- **Unverifiable** — searched the regulator, the destination authority, and at least one operator; no official statement of this claim exists. Flag the row for content writers — they will hedge the language.
- **Conflicting** — community says X, official says Y. Record **both**: keep the community quote in Notes, record the official quote in the Quote field, write the Plain English from the official version, set Status = Conflicting.

Never delete a claim row. Even Unverifiable rows are useful — they tell writers what *not* to assert.

---

## Step 6 — Repeat for every pending claim

The PENDING CLAIMS list in `skill-02/README.md` gives the priority order for the Dubai pet relocation niche. Work through it top-down. After the pricing discrepancies and timeline conflicts are resolved, the process and airline-specific claims tend to verify faster because the answers cluster on a small number of official pages.

---

## Step 7 — Hand off to writing

When every PENDING claim is non-Pending, the Source Bank is ready. Any content writer pulling claims for a page uses two columns: **Plain English** (the sentence to use) and **Official URL** (the citation to link). The writer should not need to read the regulator's PDF to produce a page.

This is the moment the skill pays back: an entire content team can write confidently for a regulated market because someone did the source work once, recorded it cleanly, and committed to keeping it current.

---

## What you must not do

- **Do not paraphrase the quote.** Verbatim or it didn't happen.
- **Do not cite a competitor.** A competitor citing MOCCAE doesn't make their page an official source.
- **Do not accept "MOCCAE says…" without a URL.** If you can't link it, it's hearsay.
- **Do not let a date checked exceed 90 days** for any active row.
- **Do not delete community quotes that conflict with the official version.** Conflicts are the most valuable rows — they show the customer where the market is wrong.

---

## Output of this manual phase

When manual verification is complete for the first 5–10 claims, you have:

1. A populated Source Bank spreadsheet with rows in Verified / Unverifiable / Conflicting status.
2. Screenshots saved in `skill-02/data/verification-screenshots/`.
3. A confident answer to: *"For this niche, what are the regulators that matter, and what do they actually say?"*

That answer is what makes File 04 (the automation spec) implementable. Without it, automation just looks up keywords on websites.
