# Engine — Email Nurture Sequences
## Spec for the trigger → schedule → personalise → send → route engine (read files/04-automation-spec.md first)

This engine implements the automation in `files/04-automation-spec.md`. Unlike the rest of the
collection, this skill is **Automation 5/5**: once the 7 emails are written and verified, the
engine runs the whole sequence with no further human authoring. It **never writes or edits an
email** — the emails are the human-verified asset; the engine only triggers, schedules,
personalises tokens, sends, and routes replies back to a human.

## What it does (per lead)
1. **Trigger on enquiry** — a new lead-capture record fires the sequence; Email 1 sends
   immediately.
2. **Schedule the rest** — Emails 2–7 are queued on a mid-week (Tue–Thu) cadence across ~21
   days *(P-20)*. If a send lands on a weekend, roll forward to the next Tue–Thu.
3. **Personalise tokens** — fill `{{first_name}}`, `{{origin_country}}`, `{{destination}}`,
   `{{flight_date}}` from the lead record; apply fallbacks where a field is empty (see below).
4. **Send via ESP** — through `ESP_API_KEY`, from `FROM_EMAIL`/`FROM_NAME`, `REPLY_TO_EMAIL`
   set so replies reach a human.
5. **Route replies / stop on conversion** — if the lead replies (the help-first CTA worked) or
   books, pause the automated sequence and hand to a human. Never keep auto-sending at someone
   who has started a conversation.

## Token fallbacks (an email must read correctly with an empty field)
```
{{first_name}}      -> "there"
{{origin_country}}  -> "your current country"
{{destination}}     -> "your destination"
{{flight_date}}     -> "your travel date" (and Email 3 omits the parenthetical)
```

## The schedule core (deterministic)
```python
# Cadence in days from the trigger; Email 1 is immediate (day 0).
SCHEDULE = {1: 0, 2: 3, 3: 6, 4: 9, 5: 12, 6: 16, 7: 21}

def next_midweek(dt):
    # roll a planned send forward to the next Tue/Wed/Thu (weekday 1,2,3)
    while dt.weekday() not in (1, 2, 3):
        dt += ONE_DAY
    return dt
```
Email 1 ignores the mid-week rule (it must arrive while the enquiry is warm); Emails 2–7 are
snapped to the next Tue–Thu.

## A pre-send guard (the one quality check the engine IS allowed to run)
Before sending any email, assert it still satisfies the three threshold gates — a cheap
regression guard so an edited template can't ship broken:
```python
import re
CID = re.compile(r'\bC-\d{3}\b')
def gate_check(email_text, has_named_fear, has_helpfirst_cta):
    return {
        "named_fear": bool(has_named_fear),          # tagged in the template front-matter
        "verified_cid": bool(CID.search(email_text)),# ≥1 Source Bank citation present
        "helpfirst_cta": bool(has_helpfirst_cta),    # CTA tagged help-first, not a quote ask
    }
# all three must be True or the send is blocked and a human is alerted.
```
The engine **flags**, it does not rewrite: a failed gate stops the send and notifies a human.

## Inputs / outputs / guardrails
- **Inputs:** the verified 7-email sequence (`data/email-sequence-dubai-pet-relocation.md`), the
  lead record (name, route, date, email), and the env keys (`ESP_API_KEY`, `FROM_EMAIL`,
  `FROM_NAME`, `REPLY_TO_EMAIL`, `PROJECT_ROOT`).
- **Outputs:** sent emails on the cadence, a per-lead send log (which emails sent, when,
  opened/replied), and a pause/handoff event when the lead replies or books.
- **Never** writes or rewrites an email; **never** invents a fact or a figure (it only sends
  pre-verified, cited copy); **never** manufactures urgency; **never** keeps auto-sending after
  a reply.
- **Hand back to human:** writing/updating the emails; answering replies; the sales
  conversation that follows the help-first CTA; re-verifying a cited fact on the 90-day cycle.
- **Audit:** a sub-agent confirms the sent sequence still meets 7/7 on the three gates and that
  the cadence + reply-handoff behaved (no auto-send after a reply).

## Status
**Spec complete; the 7-email sequence is written, verified, and threshold-counted (the proof).**
`data/email-sequence-dubai-pet-relocation.md` meets the Functional Quality Threshold **7/7** on
all three gates (named fear · verified C-ID · help-first CTA). The sender/scheduler is specified
here; the emails it sends are the human-authored, source-cited asset — the engine never writes
them.

## Library codes
M-02 Fear Hierarchy · M-20 Protection Motivation Theory · M-21 Cialdini's 7 Principles ·
M-32 Hierarchy of Effects · F-22 7-Email Nurture Framework · F-23 AIM Welcome Sequence ·
F-18 AIDA · F-32 Funnel-Stage Copy Matching · P-19 80/20 Value-to-Pitch · P-20 Mid-Week Send
Timing · P-21 One Primary CTA Per Email · P-04 Fear-Acknowledging Not Fear-Exploiting · P-05
One Fear Per Email · P-15 Deliver Then Document. Full citations in `MFP-LIBRARY.md`.
