# SKILL 02 — SOURCE RESEARCH ENGINE
## Claude Code prompt — Playwright + Anthropic verification of regulation claims

Read CLAUDE.md, MASTER-SYSTEM.md, and skill-02/README.md before running.
Then read skill-02/files/02-how-to-do-it-manually.md and 04-automation-spec.md.

---

## WHAT THIS DOES

1. Reads every **Pending** claim from `skill-02/data/skill-02-source-bank.xlsx`.
2. Visits each claim's Candidate Official URL with Playwright (headless mobile Chromium).
3. Screenshots the page; extracts visible body text.
4. Sends Claim + page text to the Anthropic API with the verification system prompt.
5. Parses the JSON: status, exact quote, plain English, confidence, notes.
6. Writes the fields back to the spreadsheet; saves a screenshot per claim.
7. Logs every step to `skill-02/source_verification_log.txt`.

Spreadsheet is the source of truth — the engine never overwrites a row whose Status is not `Pending`.

---

## STEP 1 — ENVIRONMENT

Already installed during Skill 01 work:
```
pip install playwright anthropic python-dotenv openpyxl
playwright install chromium
```

Required in `.env` (already present from earlier sessions):
```
ANTHROPIC_API_KEY=
```

Outputs created on first run:
- `skill-02/data/verification-screenshots/`
- `skill-02/source_verification_log.txt`

---

## STEP 2 — RUN MODES

```
py skill-02/engines/source_research_engine.py --test           # 5-claim sample (default test)
py skill-02/engines/source_research_engine.py --only C-001     # single specific claim
py skill-02/engines/source_research_engine.py                  # full run of all Pending rows
```

The 5-claim test is the only mandatory pause point. After it completes, the human reviews the rows; if they look correct, the full run proceeds.

---

## STEP 3 — VERIFICATION SYSTEM PROMPT

Sent as the `system` message to Claude for every claim:

```
You are verifying a regulation/process claim against the live text of an
official source page. You are given:
  CLAIM:        a one-sentence factual statement
  PAGE_TEXT:    the visible text of an official source page

Return ONLY a JSON object — no preamble, no markdown:
{
  "status": "Verified" | "Unverifiable" | "Conflicting",
  "exact_quote": "<verbatim text from PAGE_TEXT that supports the claim, under 50 words>",
  "plain_english": "<one customer-readable sentence saying the same thing as the quote>",
  "confidence": 0.0-1.0,
  "notes": "<one sentence — if Conflicting, what the page says vs what the claim says>"
}

RULES:
- "Verified" only if PAGE_TEXT contains text that supports CLAIM. exact_quote must
  be copy/paste from PAGE_TEXT — no paraphrase, no ellipsis hiding load-bearing words.
- "Conflicting" if PAGE_TEXT addresses the claim but states a different value or
  condition. Put the page's actual value in plain_english; explain the discrepancy
  in notes.
- "Unverifiable" if PAGE_TEXT does not address the claim at all. Leave
  exact_quote empty.
- Never invent a quote. If you cannot find supporting text, status is Unverifiable.
- plain_english must not soften the regulator's language: if the page says
  "shall"/"must," do not write "may."
- confidence below 0.6 -> human must review even if status is Verified.
```

User message per claim:
```
CLAIM: <Claim text from the spreadsheet>

PAGE_TEXT (truncated to ~6000 chars):
<extracted body text>
```

---

## STEP 4 — STATUS POST-PROCESSING

After the API returns, the engine applies these guards before writing:

| Engine condition | Final Status |
|------------------|--------------|
| Playwright load failure (timeout, DNS, 4xx/5xx) | `Pending — load failed` |
| Extracted body text shorter than 200 chars | `Manual review required` (page likely blocked / behind JS) |
| API returned valid JSON, confidence ≥ 0.6 | use API status |
| API returned valid JSON, confidence < 0.6 | `Manual review required` (regardless of API status) |
| API returned invalid JSON | `Pending — parse failed` |

The engine never writes `Verified` on a row with confidence < 0.6.

---

## STEP 5 — TEST PHASE (5 CLAIMS)

`--test` processes the first 5 `Pending` rows in order, prints each result, then exits. The human checks:

- Does the exact_quote appear on the page when opened by hand?
- Does the plain_english change the meaning vs the quote?
- Are statuses sensible (Verified / Unverifiable / Conflicting)?

If any of the 5 fail, fix the prompt or correct the Candidate URL on the failing row before the full run.

---

## STEP 6 — FULL RUN

Removes the test limit. Processes every `Pending` row. Saves the workbook every 5 claims. Prints live progress per claim:

```
[C-001] -> Conflicting (conf 0.82) | "no titer fee published; community says 700-1300 AED"
```

---

## STEP 7 — AUDIT

After the full run, spawn an audit sub-agent. The audit reads CLAIM + Official URL only (NOT the engine's quote or plain English), re-fetches the page, and re-verifies a 20% random sample (minimum 5 rows). Pass threshold: 90% of sampled rows pass all four gates (URL still official, quote still on page, plain English matches the quote, status assignment correct).

Below 90% → halt and re-run manual verification on the failed category before publishing any content.

---

## RATE LIMITS, COST, RUNTIME

| Setting | Value |
|---------|-------|
| Page-load pause | 2 seconds |
| API-call pause  | 0.5 seconds |
| Nav timeout     | 30 seconds |
| Workbook save   | every 5 processed rows |
| Approx cost     | ≈ $0.001–0.003 per claim |
| Approx runtime  | 5–15 min for 18 claims |

---

## RULES

- Never overwrite a row whose Status is not `Pending` / `Pending — *`.
- Save screenshots BEFORE the API call — never lose scraped data on an API failure.
- Log every claim, every URL, every API result.
- Mobile viewport 390x844 (matches Skill 01 File 06 engine).
- Stop and surface any row whose Candidate URL is missing — never invent one.
