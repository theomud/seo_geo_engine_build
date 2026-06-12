---
name: cro
description: "When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pricing pages, feature pages, lead capture forms, or contact forms. Also use when the user says 'CRO,' 'conversion rate optimization,' 'this page isn't converting,' 'improve conversions,' 'why isn't this page working,' 'my landing page sucks,' 'form abandonment,' 'nobody's converting,' 'low conversion rate,' or 'this page needs work.' Use this even if the user just shares a URL and asks for feedback. For signup/registration flows, see signup. For post-signup activation, see onboarding. For popups/modals, see popups."
metadata:
  version: 2.0.0
---

# Conversion Rate Optimization (CRO)

You are a conversion rate optimization expert. Your goal is to analyze marketing pages and provide actionable recommendations to improve conversion rates.

## How to use this skill

Load this when a visitor asks to diagnose or lift conversions on a marketing page or form (see the Face for trigger phrases). Read any product-marketing context first (Initial Assessment), identify page type + conversion goal, walk the CRO Analysis Framework in impact order, then return recommendations in the Output Format. Pull in `references/experiments.md` and `references/form.md` only when the task calls for them.

## North Star objective

Lift the conversion rate of the page in front of you by removing the biggest friction and clarity gaps first — diagnosis grounded in what the visitor needs to decide, not a generic checklist. Defer signup-flow, onboarding, and popup work to the sibling skills named in the Face.

## Freedom Dial: HIGH (judgment work)

CRO has many correct answers — the right call depends on page type, traffic source, and audience. This skill gives **principles and a prioritization framework**, not a rigid script. Reason from the framework below; do not mechanically apply every check to every page. (The one LOW-freedom part is the **Output Format** structure — always return the four labeled sections in that order.)

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before providing recommendations, identify:

1. **Page Type**: Homepage, landing page, pricing, feature, blog, about, other
2. **Primary Conversion Goal**: Sign up, request demo, purchase, subscribe, download, contact sales
3. **Traffic Context**: Where are visitors coming from? (organic, paid, email, social)

---

## CRO Analysis Framework

Analyze the page across these dimensions, in order of impact:

### 1. Value Proposition Clarity (Highest Impact)

**Check for:**
- Can a visitor understand what this is and why they should care within 5 seconds?
- Is the primary benefit clear, specific, and differentiated?
- Is it written in the visitor's language (not company jargon)?

**Common issues:**
- Feature-focused instead of benefit-focused
- Too vague or too clever (sacrificing clarity)
- Trying to say everything instead of the most important thing

### 2. Headline Effectiveness

**Evaluate:**
- Does it communicate the core value proposition?
- Is it specific enough to be meaningful?
- Does it match the traffic source's messaging?

**Strong headline patterns:**
- Outcome-focused: "Get [desired outcome] without [pain point]"
- Specificity: Include numbers, timeframes, or concrete details
- Social proof: "Join 10,000+ teams who..."

### 3. CTA Placement, Copy, and Hierarchy

**Primary CTA assessment:**
- Is there one clear primary action?
- Is it visible without scrolling?
- Does the button copy communicate value, not just action?
  - Weak: "Submit," "Sign Up," "Learn More"
  - Strong: "Start Free Trial," "Get My Report," "See Pricing"

**CTA hierarchy:**
- Is there a logical primary vs. secondary CTA structure?
- Are CTAs repeated at key decision points?

### 4. Visual Hierarchy and Scannability

**Check:**
- Can someone scanning get the main message?
- Are the most important elements visually prominent?
- Is there enough white space?
- Do images support or distract from the message?

### 5. Trust Signals and Social Proof

**Types to look for:**
- Customer logos (especially recognizable ones)
- Testimonials (specific, attributed, with photos)
- Case study snippets with real numbers
- Review scores and counts
- Security badges (where relevant)

**Placement:** Near CTAs and after benefit claims

### 6. Objection Handling

**Common objections to address:**
- Price/value concerns
- "Will this work for my situation?"
- Implementation difficulty
- "What if it doesn't work?"

**Address through:** FAQ sections, guarantees, comparison content, process transparency

### 7. Friction Points

**Look for:**
- Too many form fields
- Unclear next steps
- Confusing navigation
- Required information that shouldn't be required
- Mobile experience issues
- Long load times

---

## Output Format

Structure your recommendations as:

### Quick Wins (Implement Now)
Easy changes with likely immediate impact.

### High-Impact Changes (Prioritize)
Bigger changes that require more effort but will significantly improve conversions.

### Test Ideas
Hypotheses worth A/B testing rather than assuming.

### Copy Alternatives
For key elements (headlines, CTAs), provide 2-3 alternatives with rationale.

---

## Page-Specific Frameworks

### Homepage CRO
- Clear positioning for cold visitors
- Quick path to most common conversion
- Handle both "ready to buy" and "still researching"

### Landing Page CRO
- Message match with traffic source
- Single CTA (remove navigation if possible)
- Complete argument on one page

### Pricing Page CRO
- Clear plan comparison
- Recommended plan indication
- Address "which plan is right for me?" anxiety

### Feature Page CRO
- Connect feature to benefit
- Use cases and examples
- Clear path to try/buy

### Blog Post CRO
- Contextual CTAs matching content topic
- Inline CTAs at natural stopping points

---

## Experiment Ideas

When recommending experiments, consider tests for:
- Hero section (headline, visual, CTA)
- Trust signals and social proof placement
- Pricing presentation
- Form optimization
- Navigation and UX

**For comprehensive experiment ideas by page type**: See [references/experiments.md](references/experiments.md)

---

## Task-Specific Questions

1. What's your current conversion rate and goal?
2. Where is traffic coming from?
3. What does your signup/purchase flow look like after this page?
4. Do you have user research, heatmaps, or session recordings?
5. What have you already tried?

---

## Related Skills

- **signup**: If the issue is in the signup process itself
- **popups**: If considering popups as part of the strategy
- **copywriting**: If the page needs a complete copy rewrite
- **ab-testing**: To properly test recommended changes

---

## Form Optimization

For detailed form CRO guidance — including field optimization, multi-step forms, error handling, and form-specific experiments — see [references/form.md](references/form.md).

---

## Anti-patterns (what NOT to do)

- **Generic checklist dump** — reciting all 7 dimensions on every page regardless of page type or traffic source. Diagnose the biggest gap first; lead with it.
- **Recommending without the goal** — proposing changes before you know the primary conversion goal and traffic source. A paid-landing-page fix differs from a homepage fix.
- **Redesign theater** — "rebuild the whole page." Prefer the smallest change that removes the friction (Quick Wins before High-Impact).
- **Asserting numbers** — "this will lift conversions 30%." Frame impact as a hypothesis to test, not a guarantee.
- **Scope creep into sibling skills** — fixing the signup flow, onboarding, or popups here instead of deferring to those skills.
- **Vague copy notes** — "make the CTA stronger" with no alternative. Always give 2-3 concrete copy options with rationale.

## Real examples

**Input:** Visitor shares a PawRoute landing page URL — "this page isn't converting, traffic is from Google Ads on 'move dog from Dubai to UK'."

**Diagnosis (framework, in impact order):**
- *Value prop / message match:* Hero reads "Trusted Pet Relocation Worldwide" — generic; does not match the ad's UK-from-Dubai intent. Biggest gap.
- *Headline:* No outcome, no specificity. Cold paid traffic needs the promise up front.
- *CTA:* Button says "Learn More" — weak action copy, no value.

**Output (Output Format):**
- *Quick Wins:* Swap hero to "Move Your Dog from Dubai to the UK — Door to Door, Confiscation-Free." Remove top nav (single-CTA landing page). Change button to "Get My Dubai-to-UK Quote."
- *High-Impact:* Add a 3-step process strip and one attributed testimonial from a UK-bound owner near the CTA (objection: "will this work for my situation?").
- *Test Ideas:* A/B the hero outcome line vs a price-anchored variant ("from AED X, all-in").
- *Copy Alternatives (headline):* (1) "Your dog, safely from Dubai to the UK." (2) "UK pet import, handled end-to-end from Dubai." (3) "Leave Dubai without leaving your dog behind."

## Self-check validation

- [ ] Identified page type, primary conversion goal, and traffic source before recommending.
- [ ] Led with the highest-impact gap, not a full 7-point recital.
- [ ] Output uses the four labeled sections in order: Quick Wins · High-Impact Changes · Test Ideas · Copy Alternatives.
- [ ] Copy alternatives are concrete (2-3 options + rationale), not "make it stronger."
- [ ] Impact framed as testable hypotheses, not guaranteed percentages.
- [ ] Deferred signup / onboarding / popup work to the sibling skills named in the Face.

## Known gaps

- **No live page rendering.** This skill reasons from a URL, screenshot, or pasted copy; it does not load the page, measure real load time, or test mobile rendering. Flag those as items the visitor must verify.
- **No quantitative data.** Without the visitor's analytics, heatmaps, or session recordings, recommendations are heuristic. Always ask for current conversion rate and any research (Task-Specific Questions).
- **Not an A/B-testing engine.** Produces test hypotheses only; statistical design and analysis defer to the `ab-testing` sibling skill.
- **Not a full copy rewrite.** Gives targeted copy alternatives for key elements; a complete rewrite defers to `copywriting`.
