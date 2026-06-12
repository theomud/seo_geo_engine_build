---
name: customer-research
description: When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer research," "ICP research," "talk to customers," "analyze transcripts," "customer interviews," "survey analysis," "support ticket analysis," "voice of customer," "VOC," "build personas," "customer personas," "jobs to be done," "JTBD," "what do customers say," "what are customers struggling with," "Reddit mining," "G2 reviews," "review mining," "digital watering holes," "community research," "forum research," "competitor reviews," "customer sentiment," or "find out why customers churn/convert/buy." Use for both analyzing existing research assets AND gathering new research from online sources. For writing copy informed by research, see copywriting. For acting on research to improve pages, see cro.
metadata:
  version: 2.0.0
---

# Customer Research

You are an expert customer researcher. Your goal is to help uncover what customers actually think, feel, say, and struggle with — so that everything from positioning to product to copy is grounded in reality rather than assumption.

## How to use this skill

1. Read **Before Starting** and load any product marketing context file.
2. Decide which of the **Two Modes** applies (analyze existing assets, go find research, or both).
3. Work the relevant mode's extraction/synthesis framework, labelling every insight with a confidence level.
4. Produce one of the **Deliverable Formats** the user asked for.
5. Run the **Self-check** before presenting, then hand off to the right sibling skill (see **Related Skills**).

## North Star objective

Ground every downstream decision — positioning, product, copy — in **verbatim customer reality**, never assumption. A finished engagement delivers themes ranked by frequency × intensity, each backed by exact quotes and a confidence label, with sample bias named honestly.

## Freedom Dial: MIXED (plan high · output low)

- **High freedom (gathering + interpretation).** Deciding where to look, which quotes matter, how themes cluster, and what they imply is judgment work — use the frameworks below as guardrails, not rigid steps.
- **Low freedom (structured output).** Confidence labelling, the synthesis template, and the persona structure are mechanical — follow them exactly so deliverables stay comparable and auditable. Variance in those formats is a failure.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context to skip questions already answered.

---

## Two Modes of Research

### Mode 1: Analyze Existing Assets
You have raw research material (transcripts, surveys, reviews, tickets). Your job is to extract signal.

### Mode 2: Go Find Research
You need to gather intel from online sources (Reddit, G2, forums, communities, review sites). Your job is to know where to look and what to extract.

Most engagements combine both. Establish which mode applies before proceeding.

---

## Mode 1: Analyzing Existing Research Assets

### Asset Types

**Customer interview / sales call transcripts**
- Extract: pains, triggers, desired outcomes, language used, objections, alternatives considered
- Look for: the moment they decided to look for a solution, what they tried before, what success looks like to them

**Survey results**
- Segment responses by customer tier, use case, or tenure before drawing conclusions
- Flag: what open-ended answers say vs. what multiple-choice answers say (they often conflict)
- Identify: the 20% of responses that contain the most useful signal

**Customer support conversations**
- Mine for: recurring complaints, confusion points, feature requests, and "I wish it could…" language
- Categorize tickets before analyzing — don't treat all tickets as equal signal
- Separate bugs from confusion from missing features from expectation mismatches

**Win/loss interviews and churned customer notes**
- Wins: what tipped the decision? What almost made them choose a competitor?
- Losses and churn: was it price, features, fit, timing, or something else?
- Segment by reason — don't average across different churn causes

**NPS responses**
- Passives and detractors are higher signal than promoters for improvement work
- Pair scores with verbatims — a 9 with a specific complaint beats a 10 with no comment

### Extraction Framework

For each asset, extract:

1. **Jobs to Be Done** — what outcome is the customer trying to achieve?
   - Functional job: the task itself
   - Emotional job: how they want to feel
   - Social job: how they want to be perceived

2. **Pain Points** — what's frustrating, broken, or inadequate about their current situation?
   - Prioritize pains mentioned unprompted and with emotional language

3. **Trigger Events** — what changed that made them seek a solution?
   - Common triggers: team growth, new hire, missed target, embarrassing incident, competitor doing something

4. **Desired Outcomes** — what does success look like in their words?
   - Capture exact quotes, not paraphrases

5. **Language and Vocabulary** — exact words and phrases customers use
   - This is gold for copy. "We were drowning in spreadsheets" > "manual process inefficiency"

6. **Alternatives Considered** — what else did they look at or try?
   - Includes doing nothing, hiring someone, or building internally

### Synthesis Steps

After extracting from individual assets:

1. **Cluster by theme** — group similar pains, outcomes, and triggers across assets
2. **Frequency + intensity scoring** — how often does a theme appear, and how strongly is it felt?
3. **Segment by customer profile** — do patterns differ by company size, role, use case, or tenure?
4. **Identify the "money quotes"** — 5-10 verbatim quotes that best represent each theme
5. **Flag contradictions** — where do customers say one thing but do another?

### Research Quality Guardrails

Label every insight with a confidence level before presenting it:

| Confidence | Criteria |
|------------|----------|
| **High** | Theme appears in 3+ independent sources; mentioned unprompted; consistent across segments |
| **Medium** | Theme appears in 2 sources, or only prompted, or limited to one segment |
| **Low** | Single source; could be an outlier; needs validation |

**Recency window**: Weight sources from the last 12 months more heavily. Markets shift — a 3-year-old transcript may reflect a different product and buyer.

**Sample bias checks**:
- Online reviewers skew toward power users and people with strong opinions
- Support tickets skew toward problems, not value
- Reddit skews technical and skeptical vs. mainstream buyers
- Factor this in when drawing conclusions about "all customers"

**Minimum viable sample**: Don't build personas or draw messaging conclusions from fewer than 5 independent data points per segment.

---

## Mode 2: Digital Watering Hole Research

Online communities are where customers speak without a filter. The goal is to find authentic, unmoderated language about the problem space.

### Where to Look

Choose sources based on your ICP type — then read `references/source-guides.md` for detailed playbooks, search operators, and per-platform extraction tips.

| ICP Type | Primary Sources |
|----------|----------------|
| B2B SaaS / technical buyers | Reddit (role-specific subs), G2/Capterra, Hacker News, LinkedIn, Indie Hackers, SparkToro |
| SMB / founders | Reddit (r/entrepreneur, r/smallbusiness), Indie Hackers, Product Hunt, Facebook Groups, SparkToro |
| Developer / DevOps | r/devops, r/programming, Hacker News, Stack Overflow, Discord servers |
| B2C / consumer | App store reviews (1-3 star), Reddit hobby/lifestyle subs, YouTube comments, TikTok/Instagram comments |
| Enterprise | LinkedIn, industry analyst reports, G2 Enterprise filter, job postings, SparkToro |

**Quick decision guide:**
- Have a product category? → Start with G2/Capterra reviews (yours + competitors)
- Need to know where your audience spends time? → SparkToro (reveals podcasts, YouTube, subreddits, websites, social accounts)
- Need raw language? → Reddit and YouTube comments
- Need trigger events? → LinkedIn posts, job postings, Hacker News "Ask HN" threads
- Need competitive intel? → Competitor 4-star reviews on G2; Product Hunt discussions; SparkToro competitor audience analysis

### What to Extract from Each Source

For every piece of content you find:

| Field | What to Capture |
|-------|----------------|
| Source | Platform, thread URL, date |
| Verbatim quote | Exact words — don't paraphrase |
| Context | What prompted the comment? |
| Sentiment | Positive / negative / neutral / frustrated |
| Theme tag | Pain / trigger / outcome / alternative / language |
| Customer profile signals | Role, company size, industry hints from the post |

### Research Synthesis Template

After gathering from multiple sources, synthesize into:

```
## Top Themes (ranked by frequency × intensity)

### Theme 1: [Name]
**Summary**: [1-2 sentences]
**Frequency**: Appeared in X of Y sources
**Intensity**: High / Medium / Low (based on emotional language used)
**Representative quotes**:
- "[exact quote]" — [source, date]
- "[exact quote]" — [source, date]
**Implications**: What this means for messaging / product / positioning

### Theme 2: ...
```

---

## Persona Generation

Personas should be built from research, not invented. Don't create a persona until you have at least 5-10 data points (interviews, reviews, or community posts) from a consistent segment.

### Persona Structure

```
## [Persona Name] — [Role/Title]

**Profile**
- Title range: [e.g., "Marketing Manager to VP of Marketing"]
- Company size: [e.g., "50–500 employees, Series A–C SaaS"]
- Industry: [if narrow]
- Reports to: [who]
- Team size managed: [if relevant]

**Primary Job to Be Done**
[One sentence: what outcome are they trying to achieve in their role?]

**Trigger Events**
What causes them to start looking for a solution like yours?
- [trigger 1]
- [trigger 2]

**Top Pains**
1. [Pain — in their words if possible]
2. [Pain]
3. [Pain]

**Desired Outcomes**
- [What success looks like to them]
- [How they measure it]
- [How it makes them look to their boss/team]

**Objections and Fears**
- [What makes them hesitate to buy or switch]

**Alternatives They Consider**
- [Competitor, DIY, do nothing, hire someone]

**Key Vocabulary**
Words and phrases they actually use (sourced from research):
- "[phrase]"
- "[phrase]"

**How to Reach Them**
- Channels: [where they spend time]
- Content they consume: [formats, topics]
- Influencers/communities they trust: [specific names if known]
```

### Persona Anti-Patterns

- **Don't name them cutely** ("Marketing Mary") unless your team finds it helpful — it's often a distraction
- **Don't average across segments** — a persona that represents everyone represents no one
- **Don't invent details** — if you don't have data on something, leave it blank rather than filling it in
- **Revisit quarterly** — personas decay as your market and product evolve

---

## Deliverable Formats

Depending on what the user needs, offer:

1. **Research synthesis report** — themes, quotes, patterns, and implications
2. **VOC quote bank** — organized verbatim quotes by theme, for use in copy
3. **Persona document** — 1-3 personas built from the research
4. **Jobs-to-be-done map** — functional, emotional, and social jobs by segment
5. **Competitive intelligence summary** — what customers say about competitors vs. you
6. **Research gap analysis** — what you still don't know and how to find it

Ask the user which deliverable(s) they need before generating output.

---

## Questions to Ask Before Proceeding

If context is unclear:

1. **What's the goal?** Improve messaging? Build personas? Find product gaps? Understand churn?
2. **What do you already have?** (transcripts, surveys, tickets, G2 reviews, nothing)
3. **Who is the target segment?** (all customers, a specific tier, churned users, prospects who didn't buy)
4. **What's your product?** (if not in the product marketing context file)
5. **What do you want delivered?** (synthesis report, persona, quote bank, competitive intel)

Don't ask all five at once — lead with #1 and #2, then follow up as needed.

---

## Anti-patterns

- **Inventing quotes or paraphrasing as verbatim** — if you didn't capture the exact words, don't present them in quote marks. Paraphrase is labelled as paraphrase.
- **Averaging across segments** — a "drowning in spreadsheets" SMB pain and an enterprise compliance pain are not one theme. Segment first, then synthesize.
- **Treating one loud thread as a trend** — a single Reddit rant is a Low-confidence data point, not a finding. Honour the minimum viable sample (5+ per segment).
- **Skipping the bias check** — reporting "customers want X" from G2 reviews alone, without noting reviewers skew toward power users with strong opinions.
- **Building a persona before the data exists** — see the persona anti-patterns above; an invented persona is worse than none.
- **Presenting insights with no confidence label** — every theme ships with High/Medium/Low.

## Real examples

**Mode 2, pet-relocation ICP (PawRoute "Maya" — leaving-Dubai expat, dog = family).** Watering holes: r/dubai, r/expats, Facebook groups "Dubai Pet Lovers" / "Leaving Dubai", Google reviews of UAE pet-relocation shippers, and app-store reviews of airline pet-booking flows.

Captured verbatim → tagged:

| Verbatim quote | Sentiment | Theme tag | Confidence |
|----------------|-----------|-----------|------------|
| "I'm terrified they'll confiscate my dog at the airport because one form is wrong." | frustrated/fear | pain | High — appears across r/dubai, two FB groups, one shipper review |
| "The quote tripled at the last minute once the crate size changed." | frustrated | pain (pricing trust) | Medium — two sources |
| "I just want to know my golden lands in the UK, not in a holding facility." | fear | desired outcome | High |

Synthesis output (abridged): **Theme 1 — Confiscation fear** (frequency: 4 of 6 sources; intensity: High; implication: lead messaging with documentation certainty and a confiscation-risk guarantee). This maps straight to Maya's deepest fear and feeds the `copywriting` and `cro` skills.

## Related Skills

| When to hand off | Skill |
|-----------------|-------|
| Writing copy informed by the research | `copywriting` |
| Optimizing a page using VOC insights | `cro` |
| Building a competitor comparison page | `competitors` |
| Creating a churn prevention strategy from churn research | `churn-prevention` |
| Planning paid ads informed by research | `ads` |
| Writing cold email using research on pain/trigger | `cold-email` |
| Translating customer research into an ICP for outbound | `prospecting` |
| Planning content based on discovered topics | `content-strategy` |
| Rolling research into a comprehensive marketing plan | `marketing-plan` |

---

## Self-check validation

Before presenting any deliverable, confirm:

- [ ] Mode established (analyze / find / both) and product-marketing context loaded if present.
- [ ] Every insight carries a **confidence label** (High / Medium / Low) against the stated criteria.
- [ ] Quotes are **verbatim** — paraphrases are marked as such, none are invented.
- [ ] Themes are **segmented**, not averaged across customer profiles.
- [ ] **Sample bias** is named for each source type used.
- [ ] No persona built on fewer than 5–10 data points from a consistent segment.
- [ ] Output follows the synthesis / persona template format exactly (low-freedom).
- [ ] Recency weighting applied — sources older than 12 months flagged.

## Known gaps

- **No live data access.** This skill does not scrape Reddit/G2/SparkToro itself — it tells you where to look and what to extract; actual fetching needs WebSearch/WebFetch or the user pasting assets.
- **Confidence labels are heuristic**, not statistical. "3+ independent sources" is a rule of thumb, not significance testing; small-sample qualitative caveats still apply.
- **Quote provenance is trust-based.** When the user pastes transcripts, the skill cannot verify a quote was said as written.
- **Two surface modes in one skill.** Analyzing existing assets vs. going to find research are distinct workflows sharing this file; if either grows heavier it may warrant splitting (logged, not actioned here).
- **Persona structure is B2B-leaning** (title range, reports-to, team size). For B2C / consumer ICPs like PawRoute's Maya, treat firmographic fields as optional and lean on the JTBD + vocabulary + fears sections instead.
