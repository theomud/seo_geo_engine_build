---
name: product-marketing
description: "Creates or updates the product marketing context document at `.agents/product-marketing.md` that every other marketing skill reads for product, audience, and positioning context. Always load at the START of any new marketing project, before other marketing skills. Triggers: 'set up context', 'product context', 'marketing context', 'positioning', 'who is my target audience', 'describe my product', 'ICP', 'ideal customer profile', 'I keep repeating my product info'. NOT for writing the actual copy/landing page/ad — once context exists, defer to the sibling copy/cro skills; this skill only captures the foundation they consume."
metadata:
  version: 2.0.0
---

# Product Marketing Context

You help users create and maintain a product marketing context document. This captures foundational positioning and messaging information that other marketing skills reference, so users don't repeat themselves.

The document is stored at `.agents/product-marketing.md`.

## North Star objective

One source of truth for who the product is for, what it does, and why it wins — written in the customer's own words — so every downstream marketing skill produces on-brand, on-audience copy without re-asking the user. Success = a context doc the user confirms is accurate, and that other skills can read and act on with zero clarifying questions.

## How to use this skill

**Freedom Dial: MIXED.** Plan high, output low.
- **Gathering & interview (HIGH freedom):** the questions you ask, the order you probe, how you draft from a codebase, how hard you push for verbatim language — use judgment, follow the principles below, don't read a rigid script.
- **The output file (LOW freedom):** the saved document MUST follow the exact section names, order, and Markdown template in Step 3. Other skills parse these headers, so variance = breakage. Do not rename, reorder, or drop sections.

Walk the workflow in order: check for existing context, gather, write to the template, confirm.

## Workflow

### Step 1: Check for Existing Context

First, check if `.agents/product-marketing.md` already exists. Also check `.claude/product-marketing.md` and the legacy filename `product-marketing-context.md` (in either `.agents/` or `.claude/`) for older setups — if found anywhere other than `.agents/product-marketing.md`, offer to move it to the canonical location.

**If it exists:**
- Read it and summarize what's captured
- Ask which sections they want to update
- Only gather info for those sections

**If it doesn't exist, offer two options:**

1. **Auto-draft from codebase** (recommended): You'll study the repo—README, landing pages, marketing copy, package.json, etc.—and draft a V1 of the context document. The user then reviews, corrects, and fills gaps. This is faster than starting from scratch.

2. **Start from scratch**: Walk through each section conversationally, gathering info one section at a time.

Most users prefer option 1. After presenting the draft, ask: "What needs correcting? What's missing?"

### Step 2: Gather Information

**If auto-drafting:**
1. Read the codebase: README, landing pages, marketing copy, about pages, meta descriptions, package.json, any existing docs
2. Draft all sections based on what you find
3. Present the draft and ask what needs correcting or is missing
4. Iterate until the user is satisfied

**If starting from scratch:**
Walk through each section below conversationally, one at a time. Don't dump all questions at once.

For each section:
1. Briefly explain what you're capturing
2. Ask relevant questions
3. Confirm accuracy
4. Move to the next

Push for verbatim customer language — exact phrases are more valuable than polished descriptions because they reflect how customers actually think and speak, which makes copy more resonant.

---

## Sections to Capture

### 1. Product Overview
- One-line description
- What it does (2-3 sentences)
- Product category (what "shelf" you sit on—how customers search for you)
- Product type (SaaS, marketplace, e-commerce, service, etc.)
- Business model and pricing

### 2. Target Audience
- Target company type (industry, size, stage)
- Target decision-makers (roles, departments)
- Primary use case (the main problem you solve)
- Jobs to be done (2-3 things customers "hire" you for)
- Specific use cases or scenarios

### 3. Personas (B2B only)
If multiple stakeholders are involved in buying, capture for each:
- User, Champion, Decision Maker, Financial Buyer, Technical Influencer
- What each cares about, their challenge, and the value you promise them

### 4. Problems & Pain Points
- Core challenge customers face before finding you
- Why current solutions fall short
- What it costs them (time, money, opportunities)
- Emotional tension (stress, fear, doubt)

### 5. Competitive Landscape
- **Direct competitors**: Same solution, same problem (e.g., Calendly vs SavvyCal)
- **Secondary competitors**: Different solution, same problem (e.g., Calendly vs Superhuman scheduling)
- **Indirect competitors**: Conflicting approach (e.g., Calendly vs personal assistant)
- How each falls short for customers

### 6. Differentiation
- Key differentiators (capabilities alternatives lack)
- How you solve it differently
- Why that's better (benefits)
- Why customers choose you over alternatives

### 7. Objections & Anti-Personas
- Top 3 objections heard in sales and how to address them
- Who is NOT a good fit (anti-persona)

### 8. Switching Dynamics
The JTBD Four Forces:
- **Push**: What frustrations drive them away from current solution
- **Pull**: What attracts them to you
- **Habit**: What keeps them stuck with current approach
- **Anxiety**: What worries them about switching

### 9. Customer Language
- How customers describe the problem (verbatim)
- How they describe your solution (verbatim)
- Words/phrases to use
- Words/phrases to avoid
- Glossary of product-specific terms

### 10. Brand Voice
- Tone (professional, casual, playful, etc.)
- Communication style (direct, conversational, technical)
- Brand personality (3-5 adjectives)

### 11. Proof Points
- Key metrics or results to cite
- Notable customers/logos
- Testimonial snippets
- Main value themes and supporting evidence

### 12. Goals
- Primary business goal
- Key conversion action (what you want people to do)
- Current metrics (if known)

---

## Step 3: Create the Document

After gathering information, create `.agents/product-marketing.md` with this structure:

```markdown
# Product Marketing Context

*Last updated: [date]*

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor] — falls short because...
**Secondary:** [Approach] — falls short because...
**Indirect:** [Alternative] — falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
**Tone:**
**Style:**
**Personality:**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" — [who]
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**
```

---

## Step 4: Confirm and Save

- Show the completed document
- Ask if anything needs adjustment
- Save to `.agents/product-marketing.md`
- Tell them: "Other marketing skills will now use this context automatically. Run `/product-marketing` anytime to update it."

---

## Tips

- **Be specific**: Ask "What's the #1 frustration that brings them to you?" not "What problem do they solve?"
- **Capture exact words**: Customer language beats polished descriptions
- **Ask for examples**: "Can you give me an example?" unlocks better answers
- **Validate as you go**: Summarize each section and confirm before moving on
- **Skip what doesn't apply**: Not every product needs all sections (e.g., Personas for B2C)

---

## Anti-patterns (what NOT to do)

- **Dumping all questions at once.** Section-at-a-time, conversational. A 12-question wall makes users skip and the context goes thin.
- **Polishing over capturing.** Rewriting the customer's "I'm terrified they'll confiscate my dog at the airport" into "addresses customer compliance anxiety" destroys the resonance. Keep verbatim language verbatim.
- **Renaming or reordering the output headers.** Other skills read `## Target Audience`, `## Customer Language`, etc. by name. If you call it "Audience" or move it, downstream skills break.
- **Inventing facts when auto-drafting.** If the codebase doesn't state pricing, competitors, or proof points, leave the field blank and flag it as a gap — never fabricate.
- **Skipping the existing-file check.** Always check `.agents/`, `.claude/`, and the legacy `product-marketing-context.md` first, or you clobber prior work.
- **Term drift.** This skill says "customer" throughout — don't switch to "user," "lead," or "prospect" mid-document.

---

## Real examples

**Trigger → action.** User types "set up context for my pet relocation site" → skill checks for `.agents/product-marketing.md`, finds none, offers to auto-draft from the repo (README, landing copy), then asks "What needs correcting? What's missing?"

**Verbatim capture done right.** For PawRoute's ICP "Maya" (leaving-Dubai expat), the Customer Language section captures the exact fear — `"They'll hold my dog at the airport if my paperwork is wrong"` — not a paraphrase. That sentence later seeds headline copy in the sibling copy skills.

**Update path.** User types "update positioning" on an existing doc → skill reads it, summarizes captured sections, asks which to update, and edits only Differentiation + Competitive Landscape, leaving the rest untouched.

---

## Self-check validation

- [ ] Existing-file check ran across `.agents/`, `.claude/`, and the legacy filename before writing.
- [ ] Saved to the canonical path `.agents/product-marketing.md`.
- [ ] Output uses the exact section names and order from the Step 3 template — none renamed, reordered, or dropped.
- [ ] Customer language is verbatim, in quotes — not paraphrased.
- [ ] No fabricated facts; unknown fields left blank and flagged.
- [ ] One term ("customer") used throughout.
- [ ] User confirmed the document is accurate before save.

---

## Known gaps

- **No validation that downstream skills actually parse the headers.** This skill writes the canonical template, but nothing here verifies a sibling skill (copy, cro) reads it correctly — if a sibling expects a header this skill doesn't emit, the break surfaces there, not here.
- **Auto-draft quality depends entirely on repo content.** A thin README yields a thin draft; the skill cannot research the market, competitors, or pricing on its own. Pair with a research skill for those.
- **B2B/B2C branching is judgment, not enforced.** The skill suggests skipping Personas for B2C, but nothing stops an over-filled or under-filled doc; the user must confirm fit.
- **Date stamping is manual.** The template's `*Last updated: [date]*` is filled by hand at write time and can go stale on partial edits.
