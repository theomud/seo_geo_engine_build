---
Status: draft — built 2026-06-01
Area: skill-email-nurture
Depends on: skill-email-nurture/files/01-what-is-this-skill.md, skill-email-nurture/README.md
Feeds into: skill-email-nurture/files/03-how-to-verify-it.md, skill-email-nurture/files/04-automation-spec.md
---

# Skill · File 02 — How To Do It Manually
## Writing the seven emails by hand — one fear, one verified answer, one help-first offer each

---

## Why manual first

Sending is fully automatable; **writing is not.** The emails are the human-verified asset — the
fear in real words, the cited fact, the offer that lowers the fear — and the engine only sends
what a human wrote and verified. Write all seven by hand first; automation comes after the
sequence passes its gates. *(Library: P-01 Manual Before Automated; P-15 Deliver Then
Document — every factual line is documented from a cited source.)*

Three things on the desk before you start:
1. **The fear ladder** — the customer's fears, in their own words, ranked by depth (from the
   fear database / customer profile snapshot).
2. **The verified facts** — the C-IDs from the source store that answer each fear, plus the
   honest hedges where no official source exists.
3. **The help-first offers** — one useful thing you can give per fear (a checklist, a timeline,
   a cost sheet) that lowers the fear *before* asking for anything.

---

## Step 1 — Rank the fears, one per email

List the customer's real fears and order them by depth — deepest first. *(Library: M-02 Fear
Hierarchy.)* Assign exactly one fear to each of the seven emails; never stack two fears in one
email *(P-05)*. For the proof niche the ladder is: confiscation → documentation → timeline →
cost → airline → summer embargo → trust. The opening fear is the one that wakes them at 3am;
the closing "fear" is the trust question that gates the booking.

---

## Step 2 — Open each email with the fear in real words

The first lines must sound like the customer's situation, not a brochure. Use a **real,
attributable quote** wherever you have one (a community post, a verbatim enquiry). *(Library:
P-04 Fear-Acknowledging; P-11 Real Examples Mandatory.)* Email 1 opens on Muze Gu's *"taken
away in airport… I crying"*; Email 4 on *"being quoted endless amounts."* An invented emotion
("Are you worried about your move?") fails — it is the brochure voice the reader distrusts.

---

## Step 3 — Resolve the fear with a verified answer (cite by C-ID)

Immediately after naming the fear, hand over the verified fact that lowers it, cited by C-ID.
*(Library: M-20 Protection Motivation Theory — pair the threat with response efficacy; M-01
Verified Fact Model.)* The titer is required (C-019); the held-pet fee is 500 AED (C-003); the
permit is valid 90 days (C-010). Where **no official source exists**, say so and give the
community range — *the hedge is the trust move:* "there's no official titer price (C-001);
owners report 700–1,300 AED — get it in writing." A confident invented number would lose this
buyer; the honest absence wins them.

---

## Step 4 — End with one help-first CTA (not a sales push)

Close every email by **offering** the useful thing, not asking for the sale. *(Library: P-19
80/20 Value-to-Pitch; P-21 One Primary CTA Per Email.)* One CTA only — "reply 'checklist' and
I'll send the one-pager," "send your flight date and I'll map the backward timeline." The CTA
gives before it asks. Only Email 7 makes the booking ask, and even then with no countdown
("reply 'manage it' *when you're ready* — the checklist doesn't expire"). A second CTA, or a
manufactured deadline, breaks the help-first contract.

---

## Step 5 — Set the cadence (immediate, then mid-week)

Email 1 sends immediately on enquiry, while the worry is warm. Emails 2–7 send on a **mid-week
(Tue–Thu)** rhythm across ~21 days. *(Library: P-20 Mid-Week Send Timing; F-22.)* Mid-week
because that is when this audience opens and reads; spacing because a fear resolved needs a few
days to settle before the next is raised. The only **real** deadline allowed anywhere is a
genuine external one (the summer embargo + 90-day permit) — never a fake countdown.

---

## Step 6 — Personalise with tokens that fail safely

Write in `{{first_name}}`, `{{origin_country}}`, `{{destination}}`, `{{flight_date}}` so each
email speaks to the lead's actual move. Every sentence must still read correctly if a token is
empty (the engine supplies fallbacks — "there", "your destination"). Personalisation is
relevance, not a gimmick: it tells the reader this was written for *their* route.

---

## Worked example — the seven emails of the proof niche

| # | Fear named (real quote) | Verified answer | Help-first CTA |
|---|--------------------------|-----------------|----------------|
| 1 | Confiscation — Muze Gu | titer required (C-019); 500 AED fee (C-003) | route → airport-day checklist |
| 2 | "every website says different" | the MOCCAE document chain (C-019, C-010) | "checklist" → printable one-pager |
| 3 | "is there still time?" | titer-timing vs 90-day permit (C-010) | flight date → backward timeline |
| 4 | "endless amounts" (Reddit) | official/range/get-in-writing split (C-003, C-015, C-001) | "costs" → itemised cost sheet |
| 5 | "Etihad… took advantage" | airline is the lever; Etihad fee conflict (C-015) | breed+route → which airlines take that dog |
| 6 | "couldn't fly in summer" | heat window + 90-day clock (C-010 + hedge) | "summer" → current embargo check |
| 7 | "can I trust someone?" | help-first offer, recap (C-019, C-003) | "manage it" *when ready*, no countdown |

Threshold: every row names a real fear, cites a verified C-ID, ends help-first → **7/7.**

---

## What you must not do

- **Do not invent the fear or the quote.** A made-up emotion is the brochure voice; use real,
  attributable customer language.
- **Do not let a claim float.** Every factual line carries a C-ID or an honest hedge, or it is
  cut.
- **Do not assert an unverified figure.** Cite it or hedge it ("no official price — get it in
  writing"); the hedge converts this buyer better than a confident guess.
- **Do not stack fears or CTAs.** One fear, one primary CTA per email.
- **Do not manufacture urgency.** The only deadline allowed is a real external one (the
  embargo); a fake countdown confirms the reader's distrust.
- **Do not lead with the sale.** Six emails give before the seventh asks.

---

## Output of this manual phase

The complete 7-email sequence exists (`data/email-sequence-dubai-pet-relocation.md`): each email
opens with a named fear in real words, resolves it with a C-ID-cited answer (or honest hedge),
ends with one help-first CTA, and is tagged with its send day. The threshold count shows 7/7.
That sequence is the real output and the input to File 04 — automation sends and schedules it;
the writing stays human.
