# EMAIL NURTURE SEQUENCES
## The automated sequence that turns a frightened enquiry into a booking — one fear at a time

---

## What This Skill Is

Most leads in a high-fear service market do not buy on day one. They arrive afraid, they
research, and the provider who is still **usefully present** three weeks later — not pestering,
helping — wins the booking. Email Nurture Sequences builds that presence as a system: a
**7-email automated sequence** from first enquiry to booking, where each email acknowledges
**one specific fear in the customer's own words**, resolves it with **one verified answer**,
and ends with **one help-first offer** — never a sales push.

The governing idea is **fear-acknowledging, not fear-exploiting**: you name the real fear, then
immediately hand the reader a verified, sourced answer that lowers it. Fear without a credible
way to act produces avoidance, not action — so every email pairs the threat with the coping
step. Once written and wired to the trigger, the sequence runs on its own. It is the only
asset in the collection that compounds without ongoing human involvement.

**Skill Value Score: 21/25**
- Difficulty: 3/5
- Automation Potential: 5/5
- Market Uniqueness: 3/5
- Commercial Value: 5/5
- Teachability: 5/5

**Status:** 🔨 Building (Dubai pet relocation, 2026-06-01)
**Niche-agnostic:** Yes — every high-consideration service market has a fear ladder and verified facts to map onto it

---

## The Sequence Shape

Seven emails across ~21 days. Email 1 sends immediately on enquiry; Emails 2–7 send on a
mid-week (Tue–Thu) rhythm. The arc runs Awareness → Interest → Move (the AIM welcome shape):

| # | Day | The one fear it resolves | The verified answer |
|---|-----|--------------------------|---------------------|
| 1 | 0 | Confiscation at the airport | titer is required (C-019); held-pet fee 500 AED (C-003) |
| 2 | 3 | "Every website says something different" | the exact document chain, MOCCAE-sourced (C-019, C-010) |
| 3 | 6 | "Is there still time?" | the titer-timing-vs-90-day-permit window (C-010) |
| 4 | 9 | "Being quoted endless amounts" | official vs range vs get-in-writing cost split (C-003, C-015, C-001) |
| 5 | 12 | Airline rejection / overcharge | airline is the biggest lever; Etihad fee conflict (C-015) |
| 6 | 16 | The summer embargo nobody warns about | heat window + 90-day permit clock (C-010) |
| 7 | 21 | "Can I trust someone with this?" | help-first offer, no countdown, no pressure |

**Rules baked into every email:** one fear, one primary CTA, value before any ask (the
80/20 value-to-pitch balance), and a real deadline only where one genuinely exists (the summer
embargo) — never a manufactured countdown.

---

## What It Produces

| Output | What it is |
|--------|-----------|
| The 7-email sequence | The complete fear-to-booking sequence, ready to send (`data/`) |
| The threshold count | The table proving 7/7 emails meet all three gates |
| The send schedule | Trigger + mid-week cadence the engine runs automatically |

---

## Functional Quality Threshold (Check 46)

This skill's real output — the email sequence — is **proven** only when **every email** meets
all three gates:

1. **Opens with a named fear in real customer language**, mapped to a Column K fear category.
   Not an invented emotion — a real, attributable community quote.
2. **Cites at least one verified Source Bank entry by C-ID** (or states an official source's
   *absence* honestly and anchors that hedge to a verified C-ID in the same email). The honesty
   is the trust move for this buyer.
3. **Ends with a help-first CTA, not a sales push** — value offered before anything is asked,
   one primary CTA only, and no manufactured urgency.

Measured 7/7 on all three gates in `data/email-sequence-dubai-pet-relocation.md`. An email that
misses any gate is not done. *(Independence — Check 47 — is NOT YET TESTED: only the original
builder has produced the sequence.)*

---

## Inputs and Outputs

| Input | Source | Required |
|-------|--------|----------|
| The fear ladder (one fear per email, real quotes) | the fear database (Column K) | Yes |
| Verified facts with sources (by C-ID) | the verified-source store | Yes |
| The help-first offer per stage | the brand's value assets | Yes |
| The trigger event + lead tokens (route, date) | the lead capture form | Yes (for sending) |

| Output | Format | Contains |
|--------|--------|----------|
| 7-email sequence | Markdown | one fear, one verified answer, one help-first CTA per email |
| Threshold count | table | 7/7 across the three gates, shown |
| Send schedule | trigger + cadence | immediate Email 1, mid-week Emails 2–7 |

---

## Proof

**Status:** 🔨 Building — Dubai pet relocation
**Real output:** the complete 7-email sequence
(`data/email-sequence-dubai-pet-relocation.md`) — confiscation → documentation → timeline →
cost → airline → summer embargo → the help-first booking — each email opening with a real
community fear quote, citing verified MOCCAE/Etihad facts by C-ID (C-019, C-003, C-010, C-015,
C-001) or hedging an absence honestly, and ending help-first.
**Threshold result:** **7/7** emails meet all three gates; 7 of the 9 Column K fear categories
covered.
**Anchor:** the Muze Gu confiscation quote (Facebook) opens Email 1; the verified MOCCAE titer
(C-019) and 500 AED fee (C-003) recur as the spine.
**Skill Value Score (confirmed on completion):** 21/25.

---

## Environment Variables

```
PROJECT_ROOT=        # absolute path to the project root on this machine
ESP_API_KEY=         # email service provider key (sends + schedules the sequence)
FROM_EMAIL=          # the verified sending address
FROM_NAME=           # the advisor / brand name shown as sender
REPLY_TO_EMAIL=      # where help-first replies land (a human reads these)
```

Automation 5/5: once the sequence is written and these are set, the engine triggers on enquiry,
sends Email 1 immediately, schedules Emails 2–7 mid-week, personalises the route/date tokens,
and routes replies to a human. Writing the emails is a one-time human act; sending is fully
automated. See `files/04-automation-spec.md`.

---

## Standalone Test

Someone in any high-consideration service market can use this skill alone: list the customer's
fears in order of depth, attach one verified fact to each, write one email per fear that ends
with a help-first offer, and wire it to the enquiry trigger on a mid-week cadence. The method is
portable; only the fears, the verified facts, and the offers are niche-specific.
