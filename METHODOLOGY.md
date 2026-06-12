# PawRoute Content Engine — Writing, SEO/GEO & Imagery Methodology

*How we write, how we audit, what we're certain of, what we still have to prove, and why the
images look the way they do. This is the operating manual behind every page the engine produces.*

> **Scope.** This engine does two things only: it **writes** (SEO/GEO content) and **renders pictures**.
> It does not design the website — that's handed off downstream. Everything here is about producing
> *content and imagery* that is accurate, trusted, citable, and built to convert a stranger into a lead.
>
> **Objective.** `lead_generation`. Success = qualified enquiries and cost-per-lead, **not pageviews**.
> A post with 400 reads and 12 quotes beats one with 50,000 reads and none.

---

## PART 1 — How we write (and why)

### The core belief
People searching pet relocation are **not browsing — they're scared**. A wrong move can mean a
delayed, refused or quarantined pet. So we don't write "content marketing." We build a **search-based
trust machine**: understand the fear → answer it better than anyone → prove it with official sources →
make the next step feel like help.

The scientific basis for every writing rule in this engine lives in two places:
- **`skills/copy_and_image_sciences/MASTER_FRAMEWORK.md`** — 3,800+ line framework covering
  cognitive load theory (Sweller), dual coding, fluency→trust (Reber & Schwarz), Cialdini's
  persuasion principles, loss aversion, fear appeals (Tannenbaum 2015 meta-analysis), image
  psychology (Kindchenschema, gaze direction), and sector-specific writing styles.
- **`skills/copy_and_image_sciences/THE_WRITING_SYSTEM.md`** — 20 enforceable writing principles
  derived from that science (sentence caps, inverted pyramid, specificity, cognitive fluency, etc.)

The claim bank (`skills/copy_and_image_sciences/claim_bank.csv`) is the live, Admiralty-graded
source of every statistic the AI writer is allowed to use. (Sources: NN/G reading research,
Schwartz, Cialdini, our validated `KNOWLEDGE-BASE.md`, and the Numini-verified frameworks.)

### The writing pipeline (every page)
1. **Read the prospect's mind** — current state → desired state → obstacles → false beliefs →
   emotional driver (fear/frustration/hope). Write to *one* person.
2. **Use their words (Voice-of-Customer)** — pull real phrasing from `voc-bank.md` (mined from
   forums/reviews). Their questions become our FAQ headings.
3. **Set an angle** — a specific, slightly contrarian position only an expert would hold
   (e.g. *"distance isn't the cost driver — rules are"*). No angle = not enough understanding yet.
4. **Research official sources** — government, standards bodies (IATA), and the operator's own site.
   Never blogs/forums/AI as the source of a fact.
5. **Outline, then draft section by section** — hook → answer → evidence → explanation →
   story/example → FAQ → action.
6. **Humanize** — strip AI clichés ("in today's world", "delve", "seamless"), add a real example,
   a warning, varied sentence rhythm.
7. **Separate facts from advice** — *"DEFRA requires X"* (fact, sourced) is rendered distinctly from
   *"we recommend X"* (advice). See the `compliance` block.
8. **Self-check the 7-category QA** (below) before output.

### The page anatomy (the 2026 article)
Headline (curiosity/result) → **answer-first** opening (the liftable answer in the first lines) →
**key takeaways** box → **table of contents** → scannable H2/H3 sections → a **visual** (data table or
flow) → **original insight / a story** → **FAQ** (with schema) → **official sources** → a single
**help-first CTA**. Different page *jobs* re-weight this (reassurance, trust-comparison, guide, service,
hub, blog) — the auditor scores each against its job, not one flat rubric.

### The truth policy (non-negotiable)
- Cite the official source or hedge — **never invent**.
- Never guarantee airline delivery dates; never give veterinary advice.
- Verify every route individually (UK ≠ EU, dog ≠ cat); verify the **airline separately** from the government.
- If uncertain: say so and flag it, don't guess. AI drafts; a human approves before publish.

---

## PART 2 — How we audit (SEO/GEO)

### The auditor (`audit/audit.py`) — 5 lenses, 7-category QA, ~39 checks
| Lens | What it scores |
|---|---|
| 🌐 Website | title/meta/H1, hierarchy, scannability, alt, schema, canonical, internal links, weight |
| 🔍 SEO | intent match, topical depth, descriptive anchors, named-author E-E-A-T, outbound authority, freshness, FAQ |
| 🤖 GEO | answer-first, statistics, cited sources, quotable facts, entity coverage, definition, FAQ schema |
| 💛 Lead-gen/Trust | fear-first, cost transparency, help-first CTA, single CTA, social proof, objections, original visuals |
| ✨ Quality | human voice, original insight, helpful/actionable, outcome focus, reader-focus, storytelling, headline hook |

These map to the doctrine's **7-category QA**: Helpful · Human · Original (Quality) · Trustworthy
(sources) · SEO · GEO · Conversion (Trust).

### How scoring stays honest
- **Page-type profiles** re-weight lenses by the page's job + name the *critical* checks for it.
- **Evidence tier** on every check (T1 sworn → T6 practitioner) + **verified-vs-heuristic** tag.
- **Coverage → confidence** (High/Moderate/Limited/Low). **Not-measurable checks are excluded, never zeroed.**
- **Risk caps** (thin content, keyword stuffing, fake schema, no-CTA) cap the final score.
- **Brief-alignment** checks a page against its intended strategy (fear, page type, CTA).
- **Claim verification** (`verify_claims.py`): every regulatory claim is screenshotted against its
  official source; **official domains only**. The **regulatory register** logs source · URL · date
  verified · version · reviewer · re-verify-by — auditable, with a human-sign-off gate.

### What the score *is* (and isn't)
The audit score is a **structured on-page quality judgment** — not a measured ranking or citation.
A high score means "we did the controllable on-page things right," nothing more.

---

## PART 3 — What we're sure of vs what we must still prove (to be 100%)

**HIGH confidence — done & controllable (on-page):**
- The content is accurate, official-sourced, answer-first, citable, fear-led, and genuinely
  best-in-niche (competitors hide pricing, show no dates, no original data, are anonymous).
- Structured data, breadcrumbs, sitemap/robots, internal linking — all in place.

**MODERATE confidence — plausible but unproven (GEO citation):**
- Our content is exactly what AI engines favour (answer-first, cited stats, quotable, structured,
  entity-consistent). GEO levers add ~25–28% (the "40%" is a benchmark ceiling, not a promise).
- Citation is decoupled from ranking (66% of AI-Overview citations come from outside the top-20),
  so this is our best near-term shot — **but it requires being indexed and is volatile.**

**LOW confidence (short-term) — depends on off-page we haven't built (SEO ranking):**
- A new domain with no backlinks, no domain authority, no Google Business Profile, no reviews and an
  anonymous author **will not rank quickly, however good the pages are.** On-page is necessary, not sufficient.

**What we must still do to be "100% sure" (the measurement + authority gap):**
1. **Deploy + index** (submit sitemap to Search Console) — nothing ranks unindexed.
2. **Measure**: connect GSC (impressions/position/CTR); run `audit/ai_citation.py` for a real
   AI-citation baseline, then monthly; measure real Core Web Vitals (PageSpeed/CrUX).
3. **Build authority**: a real **named author + credentials**, **Google Business Profile + NAP + reviews**,
   and **backlinks** (pitch the calculators + a real cost-data report — they're built as link magnets).
4. **Calibrate the auditor** against that live data — until then, scores are *advisory*.

Bottom line: we are confident in the **craft**; we will not claim **results** until they're measured.
Anyone promising GEO/SEO results from on-page work alone is guessing.

---

## PART 4 — The images (why they look this way, and how they work on the reader)

### What and how
Images are AI-rendered with **BFL FLUX** (`engine/render_images.py`) into a dedicated `images/` folder,
then referenced by pages. Currently **low-resolution to save credits**; bumped to full-res once a
concept is approved. Every image has descriptive **alt text** (accessibility + an SEO/GEO signal).

### Why AI-rendered, original images (not stock)
- The auditor rewards **original (non-stock) visuals** and penalises stock — original imagery signals a
  real operator, and Google/raters treat generic stock as a low-effort signal.
- We can render the **exact emotional moment** we want, on brand, for any route — impossible with stock.

### The psychology — how each image is designed to appeal
This is a **trust + fear market**, so imagery does emotional work the words can't:
- **Hero images sell the *outcome*, not the service** — the *relief* the reader wants: an owner hugging
  a calm pet beside a labelled IATA crate at a bright airport. The reader sees the happy ending they're
  afraid they won't get. (Principle 12: sell the destination, not the vehicle.)
- **Warmth + calm, photorealistic** — soft natural light, relaxed pets, caring handlers. The fear is
  "my pet will suffer in cargo"; the image answers it visually with safety and care.
- **Supporting images show the *process* honestly** — e.g. a vet scanning a microchip — which builds
  competence/trust ("they know the steps") without a wall of text.
- **Calm, not chaotic; specific, not generic** — a real-feeling scene (a Labrador, a world map, a
  suitcase) is concrete and believable; concreteness builds credibility (Ogilvy).
- **No fear-mongering imagery** — we name fears in *words* and resolve them; the pictures stay
  reassuring. We never use distressing images to manufacture anxiety (no dark patterns).

### Rules for image prompts
Photorealistic · warm/reassuring mood · soft natural light · calm pet + caring human · on-brand,
non-stock · no text in image · 3:2 hero crop. Every prompt + alt text is stored in the page's content
JSON so the brief is auditable and reproducible.

---

## In one line
**Understand the fear → answer it better than anyone, in their words, from official sources →
prove it and show the relief in the image → make the next step feel like help → measure the result,
and never claim what we haven't verified.**
