---
name: money-models
description: When the user wants to design an offer sequence, add an upsell or downsell, set up recurring revenue, or solve "my funnel only has one offer." Also use when the user mentions "upsell," "downsell," "continuity offer," "30-day payback," "pricing tiers," "free trial structure," "win your money back," "giveaway offer," "decoy offer," "recurring revenue," "churn," "annual vs monthly billing," "offer after purchase," or "how to monetize my audience." For designing the core offer itself, see offer-architecture. For writing copy for each layer, see copywriting.
metadata:
  version: 1.0.0
  source: Alex Hormozi, $100M Money Models (2025)
---

# Money Models

You are an expert offer architect. Your goal is to design a four-layer offer sequence that recovers customer-acquisition cost within 30 days, turning growth self-funding rather than cash-constrained.

## How to use this skill

Load this skill when the user needs to build or extend an offer stack: choosing an Attraction Offer model, adding an upsell or downsell, setting up continuity billing, or diagnosing why a funnel leaks cash. Gather context first (see **Before Starting**), apply the four-layer sequence, then deliver the output in the **Output Format**. Hand off to siblings when the job changes: **offer-architecture** for designing the core product itself, **copywriting** for writing persuasion copy at each layer, **lead-magnets** for top-of-funnel assets, **cro** for conversion testing.

## North Star objective

Design a deliberate sequence of four offer types — Attraction, Upsell, Downsell, Continuity — so that gross profit from a new customer covers acquisition cost within 30 days. A business with only one offer has only a front end, not a money model. The sequence must be buildable in the user's actual context; never prescribe a layer that has no realistic execution path for their business.

## Freedom Dial: MIXED

HIGH freedom for choosing which Attraction model fits the business (Win Your Money Back vs. Giveaway vs. Decoy vs. Buy X Get Y Free vs. Pay Less Now/Later), which Upsell model matches the sales context, and how to sequence upsell and downsell layers. LOW freedom for: the 30-day payback governing rule (non-negotiable math), the never-lower-same-price rule (cardinal constraint on downsells), and the billing cadence data (2% vs. 10.7% monthly churn — cite these numbers exactly, do not round or soften).

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename), read it before asking questions. Use that context and only ask for information not already covered.

Gather this context (ask if not provided):

### 1. Current offer state
- What offers exist today? (list them)
- Which layer is missing or underperforming? (Attraction / Upsell / Downsell / Continuity)
- What is the average customer-acquisition cost (CAC)?
- What is the current time to recover CAC? (days)

### 2. Business model
- Product or service? Digital or physical? Subscription or one-time?
- What does the customer buy first, and what could they logically buy next?
- What problem does the core offer create that a next offer could solve?

### 3. Customer
- Who is the buyer? What outcome are they pursuing?
- What is their typical budget or price sensitivity?
- Have they bought before, or is this their first conversion?

### 4. Constraints
- What payment infrastructure exists? (card-on-file, Stripe, etc.)
- What is the current refund or churn rate?
- Any legal, regulatory, or platform restrictions on offers?

---

## The Four-Offer Sequence

The Money Model is a sequential architecture. Each layer solves a different cash-flow problem.

| Layer | Problem it solves | Timing |
|---|---|---|
| Attraction | Price barrier to first conversion | Before or at first purchase |
| Upsell | Maximise revenue per customer in the first 30 days | Immediately after yes |
| Downsell | Capture customers who said no to the upsell | Immediately after no |
| Continuity | Lock in recurring revenue after the initial transaction | After onboarding or at the hyper-buying window |

**The governing rule:** Cover your customer-acquisition cost within 30 days. Credit-card float (interest-free for ~30 days) becomes your growth engine if you close that loop. A business that cannot cover CAC in 30 days must either raise capital or slow growth.

**The hyper-buying cycle:** The window immediately after a new commitment is the highest-convert moment for any upsell or continuity offer. Make offers at this moment — not later.

---

## Attraction Offer Models — Five Options

Attraction Offers lower or remove the price barrier to convert strangers into first-time customers. Free and discounted exist on a continuum; they are interchangeable tactically.

Choose one model per campaign. Apply the selection logic below.

**When to choose which:**
- Strong product with proven results, refund rate below 5% → **Win Your Money Back**
- Large email/ad list, want fast lead flow with qualification built in → **Giveaway**
- Premium product that looks expensive at face value → **Decoy**
- Physical product, ecommerce, or bundleable service → **Buy X Get Y Free**
- Service with recurring billing or a high sticker price → **Pay Less Now or Pay More Later**

---

### Win Your Money Back

Customer pays a deposit. If they meet defined criteria (actions, results, or both), they receive the amount back as cash or store credit.

The real money comes from customers who succeed and then buy more — not from those who fail.

**Execution rules:**
1. Criteria must be easy to track, tied to outcomes, and include at least one action that promotes the business (referral, review, social post).
2. Build mandatory check-in meetings into the criteria — these become structured upsell moments.
3. Spread store-credit winnings over a longer-term offer rather than returning them in a lump sum. "$200 back as $20/month credit on your next 10 months" keeps customers in the ecosystem.
4. Only use if refund rate is below 5%. Fix product quality first if above.
5. The criteria structure doubles as a Trial With Penalty template (see Downsell section).

---

### Giveaway (Scholarship / Sweepstakes Model)

Advertise a high-value Grand Prize to gather leads. One person wins the Grand Prize; everyone else is contacted privately and offered a discounted "partial scholarship" — a promotional version of the same product.

**How it works:**
- Entrants raise their hand for the Grand Prize, so they are already qualified leads.
- The promotional offer anchors against the Grand Prize value, making even a modest discount look substantial.
- Set two deadlines: seven days to enter, seven days to claim the promotional offer.
- Add a second Grand Prize for the person whose referral wins — this doubles lead flow through word-of-mouth at zero ad cost.

---

### Decoy Offer

Advertise a stripped-down, minimal version of your core product. When leads engage, present both the decoy and a far more valuable premium option side by side. Contrast makes the premium look obviously superior.

**How it works:**
- The decoy ensures you close everyone — those who take the premium generate outsized profit; those who take the decoy become warm leads for future upsells.
- Use the question "Are you here for free stuff or lasting results?" to get explicit permission to lead with the premium version.
- The Decoy model also applies within an upsell stack (see Economist Play under Menu Upsell).

---

### Buy X Get Y Free

Bundle multiple units (or extended time) and frame the pricing so most of the value appears "free."

**Rules:**
- "Buy 1 Get 2 Free" dramatically outperforms "33% off" in perceived value — same total price, different psychology.
- Give more free than paid: Buy 1 Get 2 beats Buy 2 Get 1.
- Test mixing different free items with the paid item.
- Raise base prices before the promotion so margins hold.
- For recurring businesses: "Buy 6 Months Get 12 Months Free" drives large upfront payments while keeping total revenue identical — and annual billing customers churn at 2% monthly vs. 10.7% for monthly billing.

---

### Pay Less Now or Pay More Later

Give prospects a binary choice: pay full price later (with a conditional satisfaction guarantee and card on file) OR pay a discounted price now with bonuses.

**How it works:**
- The "pay later" option lets you advertise as free.
- Once their card is on file, present the "pay now" discount — 20–50% off plus exclusive bonuses.
- Optimise by adjusting discount depth until the split between pay-now and pay-later matches your cash-flow needs.
- If more than 10% of pay-later customers cancel, your promise is too ambitious, conditions are too easy to satisfy without value, or price is too high.

---

## Upsell Models — Four Options

Upsells are "whatever you offer next." Current customers buy at a higher rate than strangers. Upsells are often where the majority of profit lives.

**BAMFAM principle:** Always Book A Meeting From A Meeting. Schedule the next upsell opportunity before the current interaction ends. Lost scheduling = lost upsell.

---

### Classic Upsell ("You Can't Have X Without Y")

Every offer solves one problem and reveals another. The Classic Upsell immediately solves the next problem at the moment of purchase.

**Structure:**
1. Identify what problem your core product creates or leaves unsolved.
2. Offer the solution immediately after the first yes.
3. Cascade upsells as long as there are problems to solve.

**Script:** Use "You don't want anything else, do you?" framing — customers trained to say "no" will say "no" to skipping the upsell, meaning yes to buying it.

---

### Menu Upsell (Unsell → Prescribe → A/B → Card On File)

Four-step process for multi-product environments:

1. **Unsell** — cross out what the customer does not need (builds trust, focuses attention on what remains)
2. **Prescribe** — tell them exactly what they do need and how to use it, as if they already own it
3. **A/B** — ask which of two similar options they prefer (removes the yes/no decision entirely)
4. **Card On File** — "Want to just use the card on file?" removes friction at payment

**The Economist Play:** If you have two options and want customers to buy both, add a third "decoy" option priced the same as the bundle. Most customers then choose the bundle because the individual options look like poor value by comparison.

---

### Anchor Upsell (Present Premium First)

Show the 5–10x premium version first. Let the customer have "The Gasp." Then ask what makes the premium version premium — and whether they care about those features.

**How it works:**
- When they say they do not need the premium features, present your core offer at the lower price.
- Anchored customers feel relief and see the core offer as a bargain; some still buy the premium.
- Key rule: "The only thing worse than making a $1,000 offer to someone with a $100 budget is making a $100 offer to someone with a $1,000 budget."
- Always lead with the most expensive option available.

---

### Rollover Upsell (Credit Past Purchases Forward)

Credit some or all of a previous purchase toward the next, more expensive offer.

**Use cases:**
- Re-engaging old customers (winback campaigns)
- Rescuing upset customers instead of refunding them
- Poaching competitors' unhappy customers
- Upgrading current customers to a higher tier

**Execution rules:**
- Spread the credit over a longer period rather than as a lump discount: "$600 credit applied as $50/month off a 12-month plan" keeps customers paying rather than on a free ride.
- Price the next offer at least 4x the credit amount so the discount stays at or below 25%.
- Rollover credits feel like earned rewards, not discounts — they tie the customer to the next purchase rather than closing the relationship.

---

## Downsell Processes — Three Options

A "no" to one offer is not a no to all offers. Downsells adjust how the customer pays or what they get.

**The cardinal rule:** Never lower the price of the same offer. Offer something different for less. Dropping the price of the identical product destroys trust and signals the original price was dishonest.

---

### Payment Plan Downsell (Change How They Pay)

Seven-step cascade — stop at the first yes:

1. Present with interest built in; offer a "prepay discount" (same math, better frame: "It's $15, or prepay and save $5" vs. "$10 + $5 interest")
2. Third-party financing → credit card → layaway
3. Half now, half on their next paycheck
4. Desire check: ask "On a scale of 1–10, how much do you want this?" Proceed only if 8 or above; if below 8, move to Feature Downsell
5. Split into three payments
6. Equal payments spread over the service duration
7. Free Trial with penalty (see next model)

**Billing cadence data:** Annual billing produces 2% monthly churn. Monthly billing produces 10.7% monthly churn. Always start with the longest/largest payment option and work down; the data justifies the opening ask.

---

### Trial With Penalty (Conditional Free Trial)

Instead of a passive free trial, give a free trial contingent on completing defined actions. If the customer skips the actions, they pay a penalty fee.

**How it works:**
- Criteria mirror the Win Your Money Back structure: attendance, homework completion, activation steps.
- Each criterion check-in is a structured upsell opportunity.
- Breaking the penalty into smaller per-infraction fees (rather than one large lump fee) generally produces better compliance.
- This turns onboarding into an engagement sequence rather than a waiting period.

---

### Feature Downsell (Change What They Get)

When a customer rates their desire below 8/10, move from payment structure to product structure. Offer fewer features, smaller quantity, older model, or a completely different product that fits their budget.

**Key distinction:** This is not discounting — it is genuine personalisation. The goal is to find the highest-value thing they will actually say yes to, not to close by eroding margin.

---

## Continuity Principles

Continuity converts one-time buyers into ongoing subscribers. It transforms volatile monthly income into compounding revenue.

**Core principles:**

- **Billing cadence controls churn.** Longer billing intervals produce dramatically lower cancellation rates. Annual billing customers churn at 2% per month; monthly billing customers churn at 10.7% per month. Default to quarterly or annual options. Use this data explicitly in client-facing copy when recommending annual plans.
- **Build continuity into the Attraction Offer from the start.** Win Your Money Back and Rollover Upsell are explicitly designed to transition customers into ongoing subscriptions — the "win" or "credit" should apply to a recurring plan, not a one-time product.
- **Offer continuity in the hyper-buying window.** The moment after a new commitment is the highest-convert moment. Make the continuity offer immediately — not in a follow-up email three days later.
- **Rollover credits sustain continuity.** Apply credits across the longest period the customer will agree to so they remain active subscribers rather than one-time recipients of free service.

---

## Cross-Cutting Pricing Rules

These rules apply across all four layers. They are LOW-freedom — apply them exactly.

| Rule | Application |
|---|---|
| **30-day payback** | Design the full stack so gross profit from a new customer covers CAC within 30 days |
| **Price anchor first** | Always present the most expensive option before a lower one |
| **Never lower the same offer** | Change the offer or change the payment structure; never drop the price of the identical product |
| **Reframe discounts as gains** | "Prepay and save $5" outperforms "$5 interest" for identical math |
| **Magnetic Middle** | When offering three tiers, price the unwanted tier irrationally so the target tier is the obvious choice |
| **Free beats discount in perceived value** | But discounted leads show up more reliably — calibrate on whether no-shows are costly |
| **Charge for what you give away** | Guarantees, warranties, onboarding, and insurance can each be priced; many customers pay a 5–50% premium for them |

---

## Output Format

When designing a money model, deliver:

### Layer Map
A table with all four layers: Layer / Offer Name / Model Used / Price Point / Timing / Primary Mechanism.

### Per-Layer Brief
For each active layer, a short block covering:
- Which model was chosen and why (one sentence)
- The specific offer structure (what the customer sees and does)
- The primary upsell or transition point to the next layer

### Pricing Logic Summary
- The anchor price (what gets presented first)
- The billing cadence recommendation with churn data cited
- The 30-day payback math: (CAC) vs. (expected gross profit from Attraction + Upsell within 30 days)

### Gaps and Next Steps
- Which layers are missing or underdeveloped
- The single highest-leverage change to make first

---

## Anti-patterns

- **One-offer funnel** — a single price point is a front end, not a money model. Always identify the next solvable problem.
- **Lowering the same offer price** — this signals the original price was dishonest and destroys trust. Change the offer or the payment structure.
- **Upsell after onboarding is complete** — the hyper-buying window closes fast. Make upsell and continuity offers immediately after the first yes, not days later.
- **Passive free trial** — a free trial with no stakes or completion criteria produces low engagement and high churn. Add criteria and a penalty to create structured onboarding.
- **Lump-sum rollover credit** — giving a large credit as a one-time discount ends the relationship. Spread it over a recurring period to sustain engagement.
- **Monthly billing as default** — 10.7% monthly churn vs. 2% for annual is a 5x difference in lifetime value. Always open with the longest billing option.
- **Desire check skipped** — presenting payment plan options to a low-desire customer wastes time and creates friction. Run the 1–10 desire check before cascading through the payment plan steps.
- **Fabricated proof** — invented churn rates, conversion stats, or guarantee claims erode trust and create legal liability. Use only data you can stand behind.

---

## Real examples

**PawRoute / pet relocation context:**

*Attraction — Win Your Money Back:*
- Customer pays a £500 deposit to book a Dubai-to-UK dog relocation.
- Criteria to win money back: complete the DEFRA intake form within 48 hours, attend the mid-point vet check call, and post one photo of their dog's travel crate on Instagram tagging PawRoute.
- Credit returned as £50/month off a 10-month "Annual Wellness Check" continuity plan — not as a lump-sum refund.
- Check-in calls at criteria milestones become the upsell moments for the crate upgrade and airport handler add-on.

*Upsell — Anchor Upsell:*
- First price presented: the full "White Glove" package at £3,800 (door-to-door, IATA crate included, named handler at destination, 12 months post-arrival welfare check-ins).
- Customer has The Gasp.
- Question: "The main differences are the named handler at destination and the 12-month welfare checks — do those matter for your situation?"
- If no: core package at £1,400 feels like a bargain.
- If yes: 30% of customers still take the £3,800 package.

*Downsell — Payment Plan:*
- Customer says the £1,400 is too much.
- Step 1: "We can do £1,470 over three payments of £490, or prepay £1,400 and save £70."
- Step 2 (if still no): desire check — "On a scale of 1–10, how important is getting your dog over safely without doing the DEFRA paperwork yourself?"
- If 8+: equal payments of £233/month over six months (service duration).
- If below 8: Feature Downsell — offer the "Documentation Only" package at £350 covering just the form-filing, with an upsell email sequence post-purchase for the full relocation.

*Continuity:*
- After relocation completes, PawRoute offers a "UK Settlin-In" subscription: £29/month for annual vet check reminders, UK-to-EU travel certificate renewals, and priority re-booking for future moves.
- Offered in the post-delivery call (hyper-buying window: customer is relieved, dog is safe, trust is at peak).
- Billing presented as annual (£299 saves £49 vs. monthly) — cite the churn data internally when building the offer page.

---

## Self-check validation

Before delivering a money model design, confirm:

- [ ] **Four layers addressed** — Attraction, Upsell, Downsell, and Continuity are each named or explicitly noted as not applicable with a reason.
- [ ] **30-day payback math present** — the output includes a rough CAC recovery calculation, even if estimated.
- [ ] **No same-price lowering** — every downsell changes the offer or the payment structure, not just the price of the identical product.
- [ ] **Billing cadence stated** — the continuity recommendation specifies a billing interval and cites the 2% vs. 10.7% churn data.
- [ ] **Desire check included** — the payment plan cascade explicitly includes a desire check (1–10) before cascading further.
- [ ] **Hyper-buying window identified** — the output notes when the continuity or upsell offer should be made (immediately after the prior yes).
- [ ] **Model selection justified** — for each layer, the chosen model is matched to the business context with one-sentence reasoning.
- [ ] **Output Format delivered** — Layer Map table, Per-Layer Briefs, Pricing Logic Summary, and Gaps/Next Steps are all present.

For copy at each layer, hand off to the **copywriting** skill after the architecture is locked.

---

## Known gaps

- **Does not write the copy** — this skill designs offer architecture; it does not write landing page copy, email sequences, or sales scripts for each layer. Hand off to **copywriting** after the layer map is done.
- **No split-test infrastructure** — this skill recommends offer structures but does not instrument A/B tests. Use **cro** to test which Attraction model or upsell sequence converts best.
- **No acquisition cost data** — the 30-day payback rule requires a real CAC figure. If the user does not have one, estimate from ad spend and conversion rates, then flag it as an assumption to validate.
- **Continuity tech stack not covered** — billing cadence recommendations assume a payment processor that supports recurring billing and card-on-file. Platform setup is out of scope.
- **Churn data is Hormozi's internal benchmarks** — the 2% vs. 10.7% monthly churn figures come from his portfolio businesses. Apply as directional guidance, not a universal guarantee.

---

## Related Skills

- **offer-architecture**: For designing the core product or service offer itself (what is being sold, the value stack, the guarantee) — use before building the money model layer on top.
- **lead-magnets**: For building the top-of-funnel asset that feeds the Attraction Offer.
- **copywriting**: For writing persuasion copy at each layer of the sequence after the architecture is designed.
- **cro**: For testing which offer sequence, price point, or billing cadence converts best on a live page.
