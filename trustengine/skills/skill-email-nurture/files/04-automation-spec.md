---
Status: draft — built 2026-06-01
Area: skill-email-nurture
Depends on: skill-email-nurture/files/02-how-to-do-it-manually.md, skill-email-nurture/files/03-how-to-verify-it.md
Feeds into: skill-email-nurture/engines/engine-email-nurture.md
---

# Skill · File 04 — Automation Spec
## What the nurture engine does end-to-end, and what stays irreducibly human

---

## Automation target

**~90% of the work can be automated** — the **highest ceiling in the collection.** Writing the
seven emails is a one-time human act; everything after — triggering, scheduling, personalising,
sending, tracking, and routing replies — runs with no further human authoring. This is the only
skill that *compounds without ongoing human involvement*: set it once, and every new enquiry is
nurtured automatically. *(Library: P-20 Mid-Week Send Timing; F-22 7-Email Nurture Framework;
P-21 One Primary CTA Per Email.)*

What gets automated (the 90%):
- **Trigger** — a new lead-capture record fires the sequence; Email 1 sends immediately.
- **Schedule** — Emails 2–7 queue on a mid-week (Tue–Thu) cadence across ~21 days.
- **Personalise** — fill `{{first_name}}`, `{{origin_country}}`, `{{destination}}`,
  `{{flight_date}}` from the lead record, with safe fallbacks.
- **Send & track** — deliver via the ESP; log sends, opens, and replies.
- **Route** — on a reply or a booking, pause the sequence and hand to a human.
- **Pre-send gate guard** — assert each email still meets the three gates before it ships (a
  regression check; it blocks and alerts, it never rewrites).

What stays manual (the 10%):
- **Writing the emails** — the fear, the verified answer, the offer. Always human.
- **Verifying the facts** — the C-IDs come from the source store; the engine cites, it does not
  decide truth.
- **Answering replies** — the help-first CTA starts a human conversation; a human finishes it.
- **Updating copy** — when a fact changes on the 90-day re-verify cycle, a human edits the email.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| The verified 7-email sequence | Markdown (this skill's `data/`) | the human writer |
| The lead record (name, route, date, email) | row / JSON | the lead-capture form |
| ESP credentials | env | `.env` (`ESP_API_KEY`, `FROM_EMAIL`, `FROM_NAME`, `REPLY_TO_EMAIL`) |
| `PROJECT_ROOT` | env | `.env` |

The engine is **forbidden** from writing or rewriting an email — it sends only the
human-authored, source-cited copy.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Sent emails on the cadence (Email 1 immediate, 2–7 mid-week) | the lead's inbox |
| Per-lead send log (sent/opened/replied, timestamps) | build report / CRM |
| Pause/handoff event (on reply or booking) | the human queue |
| Gate-guard result per send (pass/blocked) | build report |

The engine never declares a lead "converted" or writes a word of copy — it sends the verified
sequence, tracks it, and hands replies to a human.

---

## Engine flow per lead

```
on new enquiry (lead record created):
    1. send Email 1 immediately (gate-guard first)
    2. for n in 2..7:
         planned = trigger_date + SCHEDULE[n]      # 3,6,9,12,16,21 days
         send_date = next_midweek(planned)         # snap to Tue/Wed/Thu
         personalise tokens (with fallbacks)
         gate-guard; if pass -> queue send; else -> block + alert human
    3. on reply or booking at any point -> pause remaining sends, hand to human
```

---

## The schedule core (deterministic)

```python
SCHEDULE = {1: 0, 2: 3, 3: 6, 4: 9, 5: 12, 6: 16, 7: 21}   # days from trigger
def next_midweek(dt):
    while dt.weekday() not in (1, 2, 3):   # Tue, Wed, Thu
        dt += ONE_DAY
    return dt
```
Email 1 ignores the mid-week snap (it must arrive while the enquiry is warm); Emails 2–7 are
snapped forward to the next Tue–Thu. *(P-20.)*

---

## The pre-send gate guard (the one check the engine runs)

```python
import re
CID = re.compile(r'\bC-\d{3}\b')
def gate_ok(email_text, named_fear_tag, helpfirst_tag):
    return (bool(named_fear_tag)            # template front-matter tags the Column K fear
            and bool(CID.search(email_text))# ≥1 Source Bank citation present in the body
            and bool(helpfirst_tag))        # CTA tagged help-first, not a quote-grab
```
A failed gate **blocks the send and alerts a human** — the engine flags, it never rewrites. This
catches a template edited into a broken state before it can reach a lead.

---

## Worked example (the proof-niche sequence)

Fed the 7-email sequence and a lead (Sarah, UK → Dubai, flight 2026-07-15): Email 1 sends on
enquiry day with `{{first_name}}=Sarah`, `{{destination}}=Dubai`; the gate guard confirms the
Muze Gu fear tag, the `C-019`/`C-003` citations, and the help-first checklist CTA → passes.
Emails 2–7 queue on the next Tue–Thu after days 3/6/9/12/16/21; each gate-guards green (every
email carries a C-ID). On day 8 Sarah replies "checklist" — the engine pauses Emails 4–7 and
hands her to a human advisor. No email was rewritten; nothing auto-sent after her reply.

---

## Test phase (one lead through the full sequence, then PAUSE)

Run one test lead end-to-end against a sandbox inbox: confirm Email 1 fires immediately, Emails
2–7 land on Tue–Thu at the right intervals, tokens fill (and fall back when blank), the gate
guard passes all 7, and a simulated reply pauses the remainder and raises a handoff. Only after
that passes is the sequence wired to live enquiries.

---

## Audit (after a build)

A sub-agent confirms the sent sequence still meets **7/7** on the three gates, the cadence and
mid-week snapping behaved, and the reply-handoff fired (no auto-send after a reply). A broken
gate that still sent, or an auto-send after a reply, is a **hard fail**. *(Library: P-07
Independent Verification.)*

---

## When automation must hand back to humans

- **Writing / updating the emails** — always human; the engine never authors copy.
- **Verifying a cited fact** — the engine sees a citation, not whether it is still true (re-verify
  on the 90-day cycle).
- **Answering a reply** — the help-first CTA opens a human conversation.
- **Any gate-guard block** — a human fixes the copy; the engine does not.

---

## Cost & runtime

| Metric | Value |
|--------|-------|
| Trigger + schedule + personalise + gate guard | milliseconds per lead (local) |
| Send | the ESP's per-email cost (fractions of a cent) |
| Human cost after setup | ~zero until a lead replies — then a normal sales conversation |

---

## Files in this skill (created by the build)

```
skill-email-nurture/
├── README.md
├── .env.example
├── customer-profile/customer-profile-snapshot.md
├── files/ (01-04 + 06)
├── guides/ (study-manual + cheatsheet)
├── data/
│   └── email-sequence-dubai-pet-relocation.md   ← the 7-email sequence (real output)
└── engines/
    └── engine-email-nurture.md
```
