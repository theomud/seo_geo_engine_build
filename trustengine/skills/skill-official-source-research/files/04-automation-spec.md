---
Status: draft — built 2026-05-28
Area: skill-02
Depends on: skill-02/files/02-how-to-do-it-manually.md, skill-02/files/03-how-to-verify-it.md
Feeds into: skill-02/engines/engine-source-research.md, skill-02/engines/source_research_engine.py
---

# Skill 02 · File 04 — Automation Spec
## What the verification engine does, and what stays manual

---

## Automation target

**~70% of the verification work can be automated** after the manual process is documented for at least 5 claims and the source authorities for the niche are identified.

What gets automated:
- Visiting official source URLs (Playwright headless Chromium).
- Extracting visible page text (and/or PDF text where the source is a PDF).
- Matching the page text against each pending claim (Anthropic API — judgment call).
- Proposing a verbatim quote, a Plain English translation, and a Status.
- Writing the result back to the Source Bank spreadsheet (Verified / Unverifiable / Conflicting).
- Saving a screenshot of each page visited.
- Logging every URL, every claim, every API call.

What stays manual:
- Initial mapping of claim → candidate source URL (humans know the regulator hierarchy in their niche).
- Interpretation of legally ambiguous language.
- Resolving conflicts between two official authorities.
- Approving the Plain English line before it ships to content writers.
- Adding new claims to the bank when community or competitor research surfaces them.

---

## Inputs

| Input | Format | Source |
|-------|--------|--------|
| Source Bank spreadsheet (Pending rows) | `.xlsx` | `skill-02/data/skill-02-source-bank.xlsx` |
| Per-claim candidate URL | column on each Pending row | filled by humans during manual mapping |
| Anthropic API key | env | `ANTHROPIC_API_KEY` in `.env` |

The engine does not auto-discover URLs. URL discovery is manual on purpose — auto-discovery resolves to the wrong site in niche markets (see Skill 01's File 06 outcome: Bing first-result returned 9gag.com for "9 Lives AE"). Humans map the URL once; the engine verifies forever.

---

## Outputs

| Output | Destination |
|--------|-------------|
| Verified / Unverifiable / Conflicting status per row | Source Bank, in place |
| Exact quote (verbatim from page) | Source Bank, in place |
| Plain English translation (for human approval) | Source Bank, in place |
| Date checked | Source Bank, in place |
| Page screenshot | `skill-02/data/verification-screenshots/<ID>-<authority>.png` |
| Verification log | `skill-02/source_verification_log.txt` |

The engine never deletes a row. Failed verifications downgrade Status to `Pending — verification failed` with the failure reason in Notes.

---

## Engine flow per claim

```
for each Pending row in Source Bank:
    1. read Claim, Category, Candidate Official URL
    2. Playwright: goto(URL) headless mobile viewport 390x844
       - wait for network idle
       - screenshot full page → save with claim ID + authority slug
       - extract inner_text("body")
       - on failure: log, set Status = "Pending — load failed", continue
    3. Anthropic API:
       - system prompt = the Step 4 verification system prompt (below)
       - user message: Claim text + page text (truncated to ~6000 chars)
       - parse JSON response: { status, exact_quote, plain_english, confidence, notes }
    4. write fields back to row; mark Date checked = today
    5. rate limit: 2s between page loads, 0.5s between API calls
```

---

## The verification system prompt

```
You are verifying a regulation/process claim against the live text of an
official source page. You are given:
  CLAIM:        a one-sentence factual statement
  PAGE_TEXT:    the visible text of an official source page

Return ONLY a JSON object — no preamble, no markdown:
{
  "status": "Verified" | "Unverifiable" | "Conflicting",
  "exact_quote": "<verbatim text from PAGE_TEXT that supports the claim, under 50 words>",
  "plain_english": "<one customer-readable sentence that says the same thing as the quote>",
  "confidence": 0.0-1.0,
  "notes": "<one sentence — if Conflicting, state what the page says vs what the claim says>"
}

RULES:
- "Verified" only if the page contains text that supports the claim. exact_quote
  must be copy/paste from PAGE_TEXT — no paraphrase, no ellipsis hiding words.
- "Conflicting" if the page addresses the claim but states a different value
  or condition. Put the page's actual value in plain_english and the
  discrepancy in notes.
- "Unverifiable" if the page does not address the claim at all. Leave
  exact_quote empty.
- Never invent a quote. If you cannot find supporting text, status is
  Unverifiable.
- plain_english must not soften the regulator's language: if the page says
  "shall" or "must," do not write "may."
- confidence below 0.6 -> human must review even if status is Verified.
```

---

## Test phase (5 claims, then PAUSE)

Before the full run, the engine processes 5 claims and stops. The human reviews:

- Does the exact_quote appear on the page when you check by hand?
- Does the plain_english change the meaning?
- Does the status make sense?

If any of the 5 fail, fix the prompt or the URL mapping; do not run the full set on a flawed engine.

---

## Audit (Step 7 of the build)

After the full run, a sub-agent samples 20% of Verified rows and re-checks them per the four gates in File 03:
- URL resolves and is still official
- Exact quote is still on the page
- Plain English matches the quote
- Status assignment is correct

Pass threshold: 90% of sampled rows pass all four. Below 90% → halt and re-run manual verification on the failed category.

---

## Rate limits, costs, runtime

| Metric | Value |
|--------|-------|
| Page-load pause | 2 seconds |
| API-call pause | 0.5 seconds |
| Claims processed per hour | ~600 |
| Anthropic cost per claim | ≈ $0.001–0.003 |
| Typical Source Bank size (Dubai pet relocation) | 30–80 rows |
| Cost of a full re-verification run | <$0.30 |
| Wall-clock of a full re-verification run | 5–15 minutes |

---

## When automation must hand back to humans

The engine sets `status = "Manual review required"` (a fifth status reserved for the engine, never written by a human directly) whenever:

- The API confidence is below 0.6.
- The page loaded but `extract_text` returned fewer than 200 characters.
- The page text contains "may," "in certain circumstances," or "depending on" near the matched fact.
- Two pages have been checked for the same claim and they disagree.

These rows go to a human queue in the spreadsheet, sorted by date. The human resolves them, sets the final status, and records the reasoning in Notes. This is non-negotiable: regulated-market content has no acceptable "guess" status.

---

## Files in this skill (created by the build)

```
skill-02/
├── README.md
├── .env.example
├── customer-profile/
│   └── customer-profile-snapshot.md
├── files/
│   ├── 01-what-is-this-skill.md
│   ├── 02-how-to-do-it-manually.md
│   ├── 03-how-to-verify-it.md
│   └── 04-automation-spec.md        ← this file
├── guides/
│   ├── skill-02-study-manual.html   ← built after engine is proven
│   └── skill-02-cheatsheet.html     ← built after engine is proven
├── data/
│   ├── skill-02-source-bank.xlsx
│   └── verification-screenshots/
└── engines/
    ├── engine-source-research.md
    └── source_research_engine.py
```
