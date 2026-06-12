---
name: emails
description: When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email program. Also use when the user mentions "email sequence," "drip campaign," "nurture sequence," "onboarding emails," "welcome sequence," "re-engagement emails," "email automation," "lifecycle emails," "trigger-based emails," "email funnel," "email workflow," "what emails should I send," "welcome series," or "email cadence." Use this for any multi-email automated flow. For cold outreach emails, see cold-email. For in-app onboarding, see onboarding.
metadata:
  version: 2.0.0
---

# Email Sequence Design

You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, and move people toward conversion.

## How to use this skill

Use it to plan and draft any multi-email automated flow (welcome, nurture, onboarding, re-engagement, post-purchase). Run the **Initial Assessment** first, design the sequence against the **Core Principles** and **Sequence Types**, then deliver in the exact **Output Format**. Pull heavy detail from the reference files only when the task calls for it.

## North Star objective

Ship a sequence where every email has one job and earns the next open — fewer, more relevant emails that move the reader toward one conversion goal, never volume for its own sake.

## Freedom Dial: MIXED (plan high · output low)

- **Design phase = HIGH freedom.** Sequence strategy, email count, angle, and copy are judgment work with many right answers. The principles and type templates below are guardrails, not rigid steps — reason from the audience and goal, don't paint by numbers.
- **Output phase = LOW freedom.** Once designed, deliver in the **Output Format** block exactly: every email must carry Send timing, Subject, Preview, Body, CTA, and Segment/Conditions. Missing fields = failure.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before creating a sequence, understand:

1. **Sequence Type**
   - Welcome/onboarding sequence
   - Lead nurture sequence
   - Re-engagement sequence
   - Post-purchase sequence
   - Event-based sequence
   - Educational sequence
   - Sales sequence

2. **Audience Context**
   - Who are they?
   - What triggered them into this sequence?
   - What do they already know/believe?
   - What's their current relationship with you?

3. **Goals**
   - Primary conversion goal
   - Relationship-building goals
   - Segmentation goals
   - What defines success?

---

## Core Principles

### 1. One Email, One Job
- Each email has one primary purpose
- One main CTA per email
- Don't try to do everything

### 2. Value Before Ask
- Lead with usefulness
- Build trust through content
- Earn the right to sell

### 3. Relevance Over Volume
- Fewer, better emails win
- Segment for relevance
- Quality > frequency

### 4. Clear Path Forward
- Every email moves them somewhere
- Links should do something useful
- Make next steps obvious

---

## Email Sequence Strategy

### Sequence Length
- Welcome: 3-7 emails
- Lead nurture: 5-10 emails
- Onboarding: 5-10 emails
- Re-engagement: 3-5 emails

Depends on:
- Sales cycle length
- Product complexity
- Relationship stage

### Timing/Delays
- Welcome email: Immediately
- Early sequence: 1-2 days apart
- Nurture: 2-4 days apart
- Long-term: Weekly or bi-weekly

Consider:
- B2B: Avoid weekends
- B2C: Test weekends
- Time zones: Send at local time

### Subject Line Strategy
- Clear > Clever
- Specific > Vague
- Benefit or curiosity-driven
- 40-60 characters ideal
- Test emoji (they're polarizing)

**Patterns that work:**
- Question: "Still struggling with X?"
- How-to: "How to [achieve outcome] in [timeframe]"
- Number: "3 ways to [benefit]"
- Direct: "[First name], your [thing] is ready"
- Story tease: "The mistake I made with [topic]"

### Preview Text
- Extends the subject line
- ~90-140 characters
- Don't repeat subject line
- Complete the thought or add intrigue

---

## Sequence Types Overview

### Welcome Sequence (Post-Signup)
**Length**: 5-7 emails over 12-14 days
**Goal**: Activate, build trust, convert

Key emails:
1. Welcome + deliver promised value (immediate)
2. Quick win (day 1-2)
3. Story/Why (day 3-4)
4. Social proof (day 5-6)
5. Overcome objection (day 7-8)
6. Core feature highlight (day 9-11)
7. Conversion (day 12-14)

### Lead Nurture Sequence (Pre-Sale)
**Length**: 6-8 emails over 2-3 weeks
**Goal**: Build trust, demonstrate expertise, convert

Key emails:
1. Deliver lead magnet + intro (immediate)
2. Expand on topic (day 2-3)
3. Problem deep-dive (day 4-5)
4. Solution framework (day 6-8)
5. Case study (day 9-11)
6. Differentiation (day 12-14)
7. Objection handler (day 15-18)
8. Direct offer (day 19-21)

### Re-Engagement Sequence
**Length**: 3-4 emails over 2 weeks
**Trigger**: 30-60 days of inactivity
**Goal**: Win back or clean list

Key emails:
1. Check-in (genuine concern)
2. Value reminder (what's new)
3. Incentive (special offer)
4. Last chance (stay or unsubscribe)

### Onboarding Sequence (Product Users)
**Length**: 5-7 emails over 14 days
**Goal**: Activate, drive to aha moment, upgrade
**Note**: Coordinate with in-app onboarding—email supports, doesn't duplicate

Key emails:
1. Welcome + first step (immediate)
2. Getting started help (day 1)
3. Feature highlight (day 2-3)
4. Success story (day 4-5)
5. Check-in (day 7)
6. Advanced tip (day 10-12)
7. Upgrade/expand (day 14+)

**For detailed templates**: See [references/sequence-templates.md](references/sequence-templates.md)

---

## Email Types by Category

### Onboarding Emails
- New users series
- New customers series
- Key onboarding step reminders
- New user invites

### Retention Emails
- Upgrade to paid
- Upgrade to higher plan
- Ask for review
- Proactive support offers
- Product usage reports
- NPS survey
- Referral program

### Billing Emails
- Switch to annual
- Failed payment recovery
- Cancellation survey
- Upcoming renewal reminders

### Usage Emails
- Daily/weekly/monthly summaries
- Key event notifications
- Milestone celebrations

### Win-Back Emails
- Expired trials
- Cancelled customers

### Campaign Emails
- Monthly roundup / newsletter
- Seasonal promotions
- Product updates
- Industry news roundup
- Pricing updates

**For detailed email type reference**: See [references/email-types.md](references/email-types.md)

---

## Email Copy Guidelines

### Structure
1. **Hook**: First line grabs attention
2. **Context**: Why this matters to them
3. **Value**: The useful content
4. **CTA**: What to do next
5. **Sign-off**: Human, warm close

### Formatting
- Short paragraphs (1-3 sentences)
- White space between sections
- Bullet points for scanability
- Bold for emphasis (sparingly)
- Mobile-first (most read on phone)

### Tone
- Conversational, not formal
- First-person (I/we) and second-person (you)
- Active voice
- Read it out loud—does it sound human?

### Length
- 50-125 words for transactional
- 150-300 words for educational
- 300-500 words for story-driven

### CTA Guidelines
- Buttons for primary actions
- Links for secondary actions
- One clear primary CTA per email
- Button text: Action + outcome

**For detailed copy, personalization, and testing guidelines**: See [references/copy-guidelines.md](references/copy-guidelines.md)

---

## Output Format

### Sequence Overview
```
Sequence Name: [Name]
Trigger: [What starts the sequence]
Goal: [Primary conversion goal]
Length: [Number of emails]
Timing: [Delay between emails]
Exit Conditions: [When they leave the sequence]
```

### For Each Email
```
Email [#]: [Name/Purpose]
Send: [Timing]
Subject: [Subject line]
Preview: [Preview text]
Body: [Full copy]
CTA: [Button text] → [Link destination]
Segment/Conditions: [If applicable]
```

### Metrics Plan
What to measure and benchmarks

---

## Task-Specific Questions

1. What triggers entry to this sequence?
2. What's the primary goal/conversion action?
3. What do they already know about you?
4. What other emails are they receiving?
5. What's your current email performance?

---

## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md). Key email tools:

| Tool | Best For | MCP | Guide |
|------|----------|:---:|-------|
| **Customer.io** | Behavior-based automation | - | [customer-io.md](../../tools/integrations/customer-io.md) |
| **Mailchimp** | SMB email marketing | ✓ | [mailchimp.md](../../tools/integrations/mailchimp.md) |
| **Nitrosend** | AI-native email (sequences via prompts) | ✓ | [nitrosend.md](../../tools/integrations/nitrosend.md) |
| **Resend** | Developer-friendly transactional | ✓ | [resend.md](../../tools/integrations/resend.md) |
| **SendGrid** | Transactional email at scale | - | [sendgrid.md](../../tools/integrations/sendgrid.md) |
| **Kit** | Creator/newsletter focused | - | [kit.md](../../tools/integrations/kit.md) |

---

## Anti-patterns (what NOT to do)

- **Two jobs in one email** — bundling a feature highlight, a testimonial, and a hard sell in the same send. One email, one CTA.
- **Volume over relevance** — padding a sequence to hit an arbitrary email count. Cut any email that doesn't move the reader forward.
- **Ask before value** — selling in email 1 before earning trust. Lead with usefulness.
- **Duplicating in-app onboarding** — email should support the product's onboarding, not repeat it. Defer to the onboarding skill.
- **Skipping the Output Format** — handing back prose without per-email Send/Subject/Preview/Body/CTA/Conditions fields.
- **Subject-line cleverness over clarity** — clever that obscures the benefit loses to clear. Clear > clever.

## Real examples

**Input:** "What welcome emails should I send to people who download our 'Leaving Dubai with your dog' checklist on PawRoute?"

**Output (excerpt — full delivery uses the Output Format block):**

```
Sequence Name: Leaving-Dubai Checklist Welcome
Trigger: Lead magnet download ("Leaving Dubai with your dog" checklist)
Goal: Book a free relocation consult call
Length: 5 emails over 12 days
Timing: Immediate, then days 2, 4, 7, 12
Exit Conditions: Books a call

Email 1: Deliver the checklist (immediate)
Subject: Your Dubai-exit checklist (+ the one date that trips people up)
Preview: Most owners start the export paperwork too late. Here's the timeline.
Body: [Deliver checklist link. Name the single biggest fear — confiscation at
      destination customs — and promise the sequence will defuse it.]
CTA: Open your checklist → [link]
Segment/Conditions: All downloaders

Email 3: Story / Why (day 4)
Subject: The owner who almost lost her rescue at the airport
Preview: One missing rabies-titer date. Here's how we caught it.
Body: [Concrete near-miss; how PawRoute's pre-flight audit prevents it.]
CTA: See how the audit works → [link]
Segment/Conditions: Opened email 1 OR 2
```

This keeps one job per email, leads with the checklist (value before ask), and aims the whole flow at one conversion: the consult call.

## Self-check validation

- [ ] Initial Assessment answered (sequence type, audience trigger, goal) before drafting.
- [ ] Each email has exactly one job and one primary CTA.
- [ ] Sequence leads with value; the ask arrives only after trust is built.
- [ ] Email count is justified by sales cycle / relationship stage — no padding.
- [ ] Output delivered in the exact Output Format (Send · Subject · Preview · Body · CTA · Segment/Conditions per email, plus the Sequence Overview and Metrics Plan).
- [ ] Onboarding/cold-outreach/cancel-flow work has been deferred to the correct sibling skill, not duplicated here.

## Known gaps

- **No deliverability or technical setup.** This skill designs sequences; it does not configure SPF/DKIM/DMARC, warm-up, or sending domains — see the tool integration guides.
- **No live performance data.** Benchmarks and timing here are starting points; real open/click/conversion rates must come from the user's account, then feed back into ab-testing.
- **Strategy, not implementation.** It produces the copy and structure, not the automation built inside Customer.io/Mailchimp/etc. — hand the output to the relevant tool integration.
- **Cold outreach and dunning are out of scope by design** (one skill, one job) — defer to cold-email and churn-prevention.

## Related Skills

- **lead-magnets**: For planning lead magnets that feed into nurture sequences
- **churn-prevention**: For cancel flows, save offers, and dunning strategy (email supports this)
- **onboarding**: For in-app onboarding (email supports this)
- **copywriting**: For landing pages emails link to
- **ab-testing**: For testing email elements
- **popups**: For email capture popups
- **revops**: For lifecycle stages that trigger email sequences
