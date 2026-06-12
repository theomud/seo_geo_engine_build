---
Status: draft — built 2026-05-28
Area: skill-02
Depends on: skill-02/files/02-how-to-do-it-manually.md
Feeds into: skill-02/files/04-automation-spec.md
---

# Skill 02 · File 03 — How To Verify The Verification
## Auditing the Source Bank itself

---

## Why verify the verifier

Every other skill depends on the Source Bank being correct. If a regulation in the bank is wrong, every page that cites it is wrong, every email is wrong, every quote a writer gives a customer is wrong. The cost of one bad row compounds across the whole content estate.

This file defines the standards a row must meet to be called Verified, the audit mechanism that catches drift, and the schedule that keeps the bank current.

---

## The five gates a row must pass before it is marked Verified

1. **Source authority gate.** The Official URL is a `.gov` site, the destination country's regulator, the airline that flies the route, or a recognised industry body. A blog, agency, news outlet, or competitor does not pass this gate.
2. **Verbatim quote gate.** The Exact Quote field contains text copied directly from the page, with original punctuation. No paraphrase, no ellipsis hiding load-bearing words.
3. **Plain-English fidelity gate.** The Plain English sentence says the same thing as the quote. A claim cannot get easier than the source intended. If the regulator says "may," the Plain English does not say "will."
4. **Date gate.** Date checked is within the last 90 days for active rows, or within the last 12 months for stable rows that explicitly state a long validity (e.g. statutory law unlikely to change).
5. **Screenshot gate.** A screenshot of the page showing the quote in context is saved to `skill-02/data/verification-screenshots/` with the claim ID in the filename.

A row that fails any gate is downgraded to Pending and re-verified.

---

## The audit sub-agent

After every automation run, an audit sub-agent samples 20% of the rows (minimum 5) and re-verifies them independently. It is not allowed to read the existing Quote or Plain English fields — only the Claim and the Official URL. It re-fetches the URL, extracts the relevant text on its own, and compares.

Audit checks per sampled row:

- **URL resolves and matches authority gate** — does the URL still 200, and is it still on an official domain?
- **Quote present on page** — can the recorded Exact Quote be found verbatim in the live page text?
- **Plain English matches quote** — does the Plain English convey the same fact, with no softening of "may/must/required"?
- **Status assignment correct** — given the quote, is `Verified` the right status, or should it be `Conflicting` (because the community-stated value differs) or `Unverifiable` (because the quote no longer says what was claimed)?

Pass threshold: 90% of sampled rows pass all four checks. Below 90% → halt content writing on those categories until rows are re-verified.

---

## Handling the three statuses correctly

**Verified.** All five gates passed. Content writers may use the Plain English sentence and link the Official URL. This is the default published state.

**Conflicting.** A community-stated value and an official value differ. The bank records both. Content strategy:
- Lead the page with the *official* value (Plain English from the official quote).
- In a side note or FAQ, explicitly address the discrepancy: *"You may see the figure quoted as 1,300 AED in online communities — the officially published rate is X AED, last verified on [date]."*
- Conflicting rows are some of the most valuable pages a writer can produce — they are where competitor pages are silently wrong and yours is loudly right.

**Unverifiable.** Searched the regulator, the destination authority, and at least one operator. No official publication of the claim. Content strategy:
- Hedge the language: *"Community reports consistently put the cost in the 700–1,300 AED range. No officially published figure currently exists."*
- Link to the bank row so a customer can see the work.
- Re-check Unverifiable rows every 90 days — authorities publish new pages constantly.

---

## What the audit cannot catch — human-only checks

Three things the sub-agent cannot evaluate; these stay manual:

1. **Interpretation of legal language.** When a regulation reads "may require additional documentation depending on circumstances," a human decides whether the Plain English should commit to "will" or "might."
2. **Conflicting authorities.** Two government pages disagree (e.g. MOCCAE and a customs annex). A human reads both, decides which governs, and records the reasoning in Notes.
3. **Regulator-implied but un-stated facts.** The regulator publishes Form A and Form B but never explicitly says "use Form A for cats over 8 kg." A human reads the field labels on both forms, infers the rule, and marks the row Conflicting until the regulator publishes a clarification.

These three categories are exactly the rows worth most to content. They are also the rows most likely to slip past an automated audit.

---

## Maintenance schedule

| Trigger | Action |
|---------|--------|
| Date checked > 90 days | Re-verify row; if quote still present, refresh Date checked; if changed, downgrade to Pending and re-verify. |
| Regulator publishes a press release or rule change (manual subscription) | Re-verify all rows in the affected category within 7 days. |
| Audit sub-agent pass rate < 90% | Halt content on affected categories; re-run manual verification on every failed row. |
| New niche launched | Run the full skill from scratch — sources change per market. |

---

## Output of the verification phase

When File 03 is satisfied, the Source Bank can be defended in front of a regulator, a journalist, or an unhappy customer who followed a page and had something go wrong. That defensibility is the whole point of the skill.
