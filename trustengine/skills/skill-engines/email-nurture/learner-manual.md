# Email Nurture (capture readiness) — Learner Manual

Most visitors don't buy on the first visit; a nurture sequence keeps you present while they decide. The sequence itself is off-page, but it can only run if the page CAPTURES the lead with a value-first offer. This engine scores that on-page capture readiness; the sequence, cadence and personalisation are shown as Not Measurable.

## How to run the engine
- Score a page: `python skill-engines/email-nurture/engine.py --url <URL> --report out.html`
- Web checker: `python skill-engines/email-nurture/engine.py --serve 8101`
- These docs: `python skill-engines/email-nurture/engine.py --docs`

## The measurements (each one, with why and how)

## 1. Lead-capture form

**How we measure it:** We look for a form with an email field.

**Why it works:** No capture = no nurture; the sequence can't start without an email.

**What to do:** Add a simple email-capture form.

## Example (what NOT to do -> what to do)
- DON'T: No form anywhere.
- DO: A simple email-capture form.

## 2. Lead magnet

**How we measure it:** We look for a downloadable free offer.

**Why it works:** A useful free thing is what makes a worried visitor hand over their email.

**What to do:** Offer a free checklist/guide in exchange for an email.

## Example (what NOT to do -> what to do)
- DON'T: Nothing to download.
- DO: Free Dubai pet-import checklist (email to get it).

## 3. Value-first signup

**How we measure it:** We look for newsletter/updates/tips signups.

**Why it works:** Offering ongoing value (not just 'subscribe') earns the opt-in.

**What to do:** Add a value-first signup ('get the corridor updates').

## Example (what NOT to do -> what to do)
- DON'T: (no signup)
- DO: Join for corridor rule updates.

## 4. Contact options

**How we measure it:** We look for email/phone/WhatsApp/contact.

**Why it works:** A direct line is the simplest nurture entry point for high-intent visitors.

**What to do:** Add clear contact options (email/WhatsApp).

## Example (what NOT to do -> what to do)
- DON'T: (no contact)
- DO: WhatsApp + email shown.

## The nurture sequence itself (human-judged)

Off-page — the 7-email fear-to-booking sequence isn't on the page.

## Send cadence & timing (human-judged)

Off-page — when/how emails send isn't observable here.

## Personalisation tokens (human-judged)

Off-page — handled by the sending system.
