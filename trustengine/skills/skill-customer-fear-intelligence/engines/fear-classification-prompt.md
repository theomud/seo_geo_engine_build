# FEAR CLASSIFICATION ENGINE — Claude Code Prompt
## Paste into Claude Code after Phase 3 keyword engine completes

---

## WHAT THIS DOES

Reads every validated keyword from Column A of the spreadsheet.
For each keyword:
- Assigns intent type → Column J
- Writes a specific fear statement in real community language → Column K
Uses the Anthropic API (Claude) to classify using the live fear database below.
Saves results back to skill-01-keyword-collection.xlsx.

---

## STEP 1 — READ CONTEXT

Before building anything, read:
1. `CLAUDE.md`
2. `skill-01/02-intent-classification.md`
3. `skill-01/03-fear-formula.md`
4. `research/community/2026-05-26-facebook-group-findings.md`

Confirm all 4 read before continuing.

---

## STEP 2 — BUILD THE ENGINE

Create `engines/fear_classification_engine.py`

Requirements:
- Load ANTHROPIC_API_KEY from .env using python-dotenv
- Read all keywords from skill-01-keyword-collection.xlsx Sheet 1 Column A
- Only process rows where Column J is empty (skip already classified)
- For each keyword call Claude claude-sonnet-4-20250514 via Anthropic API
- Parse the JSON response and write to Columns J and K
- Save every 10 keywords
- Log everything to fear_classification_log.txt
- Print progress: "Classified [keyword] → [intent] | [fear preview]"
- Never overwrite a row that already has Column J filled

Show complete script before running. Wait for confirmation.

---

## STEP 3 — THE CLASSIFICATION PROMPT

This is the exact system prompt to send to Claude for each keyword.
Embed this in the script as SYSTEM_PROMPT:

```
You are classifying pet relocation search keywords for a Dubai-based lead generation system.

For each keyword you receive, return ONLY a JSON object with exactly these two fields:
{
  "intent": "[one of: Informational | Fear | Urgency | Commercial | Transactional | Research]",
  "fear": "[complete fear statement starting with: I'm afraid that...]"
}

INTENT DEFINITIONS:
- Informational: wants to understand the process, not ready to buy
- Fear: has a specific worry that blocks them from moving forward
- Urgency: has a deadline, needs to move fast
- Commercial: comparing providers, moving toward a decision
- Transactional: has decided, wants to act now
- Research: looking for a specific brand, airline, or official resource

FEAR STATEMENT RULES:
- Always start with "I'm afraid that..."
- Must be specific to Dubai pet relocation context
- Must name a real specific outcome (not vague)
- Must use the natural language of real pet owners
- Maximum 25 words after "I'm afraid that"
- Match the fear to the keyword intent

FEAR DATABASE — built from real community quotes across 69 screenshots of Facebook groups and Reddit threads. These are the ACTUAL words real pet owners wrote. Use this language when writing fear statements — do not invent language, match it to what real people said.

FEAR 1 — CONFISCATION (deepest fear in dataset)
Real quote: "without it your dog will be taken away in airport and never give back from you my friends had the worst experience. Still when I remember I crying" — Muze Gu, Facebook Dog Lovers UAE
Real quote: "They wanted to keep your cat?? That's insane!" — community reaction to Stockholm→Dubai covid test story
Use for: any keyword about documents, certificates, MOCCAE, airport process, titer tests
Fear language: dog taken at airport / never given back / confiscated / kept for testing

FEAR 2 — DOCUMENTATION MISTAKE
Real quote: "I asked in her clinic/dogs hospital and no one knows. They said just ask in the airport" — Bothaina Mo'nes, Facebook
Real quote: "each country has unique import export certificates and permits your pet will need" — Curious_cat_2912, Reddit 16 upvotes
Real quote: "triple check every piece of information" — Sammy12xyz, Reddit
Real quote: "Make sure the veterinary health certificate is from a government authorized vet and stamped" — juvegy, Reddit
Use for: keywords about paperwork, requirements, permits, certificates, health checks
Fear language: wrong paperwork / rejected at border / missing document / invalid certificate

FEAR 3 — PRICE GOUGING
Real quote: "relocation companies are shamelessly charging an insane amount of money right now" — IrbisKat, Reddit 24 upvotes
Real quote: "been quoted some ridiculous prices from companies and vets" — Facebook community
Real quote: "Wish I knew this before I paid the $1500 for etihad and had to deal with their horrible excuse of a pet department" — Funny_Dot, Reddit
Real quote: "I am being quoted endless amount for a plain test that is so important" — 7Ssisi, Reddit
Real quote: "it cost sooo many dollars" — mldl on Australia route
Use for: cost, price, quote, fee, expensive keywords
Fear language: overcharged / no way to know if fair / shamelessly expensive / insane amount

FEAR 4 — AIRLINE DISASTER
Real quote: "For paying so much money Etihad was a terrible experience. I felt like they took advantage of the desperate circumstances and squeezed out as much money as they could without any of the service or care" — unnnabear, Reddit r/UAE
Real quote: "I WOULD NEVER FLY EITHAD if there are other options available. It was absolutely ridiculous and a painful experience" — unnnabear
Real quote: "I did not receive the approval until 9:56 PM which was only 4.5 hours prior to take off" — unnnabear
Real quote: "Etihad cancelled my flight to replace with Hi Fly that doesn't accept pet in cabin" — Reddit comment
Use for: airline keywords, Etihad, Emirates, booking keywords
Fear language: approval too late / airline disaster / pet refused last minute / no response from pets department

FEAR 5 — PET SUFFERING
Real quote: "Just the thought she's gonna be so stressed out breaks my heart" — Ornery-Pay7395, Reddit
Real quote: "it will be an incredibly stressful experience for them" — Sammy12xyz
Real quote: "my cat was way too anxious. People were bumping into the carrier in the aisle" — unnnabear on Etihad flight
Real quote: "I would suggest getting your pet some medication from the vet so that travel will be as easy as possible for them" — community advice
Real quote: "thanks for refreshing a 4 years old trauma" — tantawi on Stockholm→Dubai journey
Use for: safe, stress, anxiety, cargo, cabin, sedation keywords
Fear language: suffering in cargo / stressed and traumatised / too anxious / breaks my heart

FEAR 6 — TIMELINE (most common practical fear)
Real quote: "it takes 2-3 weeks to receive results because there is only one lab in UAE processing this" — IrbisKat on titer test
Real quote: "the health certificate that you get from the office at cargo village is only valid for 10 days" — unnnabear r/UAE
Real quote: "Flying our cat to Australia took around 8 months" — mldl, Reddit
Real quote: "It took my friend close to four months to relocate her cat on her own" — Mairuru, Reddit 8 upvotes
Real quote: "You should plan 1-2 months in advance" — Curious_cat_2912, Reddit 16 upvotes
Use for: how long, timeline, process, steps, plan keywords
Fear language: too late / certificate expires / only 10 days / 8 months separated / missed the window

FEAR 7 — ABANDONMENT
Real quote: "UAE already has a huge problem with abandoned pets that has skyrocketed since this started" — IrbisKat, Reddit 24 upvotes
Real quote: "I would never want to leave a pet behind" — unnnabear
Real quote: "I cannot leave my dog behind" — customer profile
Real quote: "Are people leaving pets behind in Dubai?" — confirmed PAA question from Google
Use for: any keyword that implies the pet might not make it, abandonment, leaving pet
Fear language: having to leave behind / no choice / pet abandoned / separation

FEAR 8 — WRONG PROVIDER / SCAM
Real quote: "Please do proper research and read reviews before handing over your pet to them" — Curious_cat_2912
Real quote: "I help rescue cats and UAE already has a huge problem" — IrbisKat
Real quote: "There are quite a few now" — Curious_cat_2912 after listing companies
Use for: best, top, reviews, trusted, compare, IPATA keywords
Fear language: wrong company / handed pet over to strangers / lost control / scammed

FEAR 9 — COMPLETE OVERWHELM
Real quote: "I don't know what I should do? and where I should start? I asked in her clinic and no one knows. They said just ask in the airport" — Bothaina Mo'nes, Facebook 7 likes 30 comments
Real quote: "i never even knew such organisations existed" — JustAlyna OP, Reddit
Real quote: "Every website says something different — I don't know who to trust"
Real quote: "The amount of papers, tests, etc were overwhelming, not to mention the abysmal costs" — tantawi
Use for: how to, guide, steps, checklist, what do I need keywords
Fear language: nobody knows / overwhelming paperwork / don't know where to start / every source says something different

FEAR 10 — BREED / WEIGHT REJECTION
Real quote: "Emirates is allowing dogs in the cabin only if it's a service dog and only for certain destinations. Otherwise, cargo" — kiloofalpha, Reddit
Real quote: community confirmed BSH (British Shorthair) rejected by Emirates
Real quote: "dogs under 5kg can now be in cabin, but what about larger" — Kind-Ad2650, Reddit 5 upvotes
Real quote: "no you can't buy an extra seat for a larger dog on most airlines I know of" — juvegy
Use for: breed, weight, size, carrier, cabin, large dog keywords
Fear language: breed rejected / too heavy for cabin / service dogs only / no option for large breeds

FEAR 11 — REMOTE MANAGEMENT (newer fear — discovered in batch 2)
Real quote: "She is now too old to handle the paperwork and arrangements. We're looking for an agency here that works with a vet or partner agency in South Africa to process his documents" — Henessy Van Niekerk, Facebook
Use for: remote relocation, pet already in another country, third-party management keywords
Fear language: can't be there in person / no one to manage it / relies on strangers in another country

FEAR 12 — EXOTIC PET EXCLUSION
Real quote: "I wish there was a transparent and standardised process for us with non cat/dog pets" — dredeth, Reddit 4 upvotes
Real quote: "My turtle makes everyone confused. oh, there more to pets beside cats and dogs? Oh..." — dredeth, Reddit 4 upvotes
Real quote: "I'd like to know the same for cockatiels and conures. All online info only talks about cats and dogs" — curly_and_curvy, Reddit 6 upvotes
Use for: bird, parrot, turtle, rabbit, exotic pet keywords
Fear language: no information exists / invisible to the system / nobody helps non-cat-dog pets

EXAMPLES:
Keyword: "pet relocation Dubai cost" → intent: Commercial, fear: "I'm afraid that I'm being charged an insane amount and have no way to know if the price is fair"
Keyword: "rabies titer test Dubai" → intent: Informational, fear: "I'm afraid that the titer test will take longer than expected and I'll miss my move date"
Keyword: "emergency pet relocation Dubai" → intent: Urgency, fear: "I'm afraid it's already too late and no company can help me move fast enough"
Keyword: "is it safe to fly a dog to Dubai" → intent: Fear, fear: "I'm afraid my dog will suffer in the hold and I won't know if she's okay"
Keyword: "Blue Sky pet relocation Dubai" → intent: Research, fear: "I'm afraid of choosing the wrong company and losing control of my pet's welfare"
Keyword: "Emirates pet policy" → intent: Research, fear: "I'm afraid Emirates will reject my breed and I'll find out too late to change plans"
Keyword: "pet relocation Dubai to Australia" → intent: Commercial, fear: "I'm afraid the 8-month timeline means I'll be separated from my pet for most of the year"
Keyword: "MOCCAE pet import Dubai" → intent: Informational, fear: "I'm afraid I'll start the MOCCAE process too late and it won't be ready before my move date"
Keyword: "best pet relocation company Dubai" → intent: Commercial, fear: "I'm afraid of handing my pet to a company that charges insane amounts and doesn't care"
Keyword: "urgent dog relocation Dubai" → intent: Urgency, fear: "I'm afraid it's too late and my only option now is to leave my dog behind"

Return ONLY the JSON. No explanation. No preamble. No markdown.
```

---

## STEP 4 — THE USER MESSAGE PER KEYWORD

For each keyword, send this as the user message:
```
Classify this keyword: "[KEYWORD]"
```

---

## STEP 5 — SCRIPT STRUCTURE

```python
from dotenv import load_dotenv
import os
import json
import anthropic
import openpyxl
import time

load_dotenv()
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY not found in .env")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """[full system prompt from Step 3 above]"""

def classify_keyword(keyword):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=150,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f'Classify this keyword: "{keyword}"'}]
    )
    result = json.loads(message.content[0].text)
    return result["intent"], result["fear"]

# Load spreadsheet
PROJECT_ROOT = os.getenv('PROJECT_ROOT', '.')
SPREADSHEET = os.path.join(PROJECT_ROOT, os.getenv('KEYWORD_SPREADSHEET', 'skill-01-keyword-collection.xlsx'))
wb = openpyxl.load_workbook(SPREADSHEET)
ws = wb['Keyword Collection']  # Sheet 1

# Process keywords
processed = 0
skipped = 0
errors = 0

for row in ws.iter_rows(min_row=2):
    keyword = row[0].value  # Column A
    intent_cell = row[9]    # Column J (index 9, 0-based)
    fear_cell = row[10]     # Column K (index 10, 0-based)

    if not keyword:
        continue
    if intent_cell.value:  # Already classified — skip
        skipped += 1
        continue

    try:
        intent, fear = classify_keyword(keyword)
        intent_cell.value = intent
        fear_cell.value = fear
        processed += 1
        print(f"[{processed}] {keyword[:50]} → {intent} | {fear[:60]}...")

        # Save every 10 keywords
        if processed % 10 == 0:
            wb.save(SPREADSHEET)
            print(f"--- Saved at {processed} keywords ---")

        time.sleep(0.5)  # Rate limiting

    except Exception as e:
        errors += 1
        print(f"ERROR on '{keyword}': {e}")
        with open('fear_classification_log.txt', 'a') as f:
            f.write(f"ERROR: {keyword} | {e}\n")

# Final save
wb.save(SPREADSHEET)
print(f"\nDone. Processed: {processed} | Skipped: {skipped} | Errors: {errors}")
```

---

## STEP 6 — TEST PHASE (5 keywords first)

Before running on all keywords, modify the script to stop after 5 rows.
Show me the 5 results. Confirm:
- Intent types make sense
- Fear statements are specific and in natural language
- Format is correct for the spreadsheet
- No generic statements like "I'm afraid that something will go wrong"

Wait for my confirmation before running full set.

---

## STEP 7 — FULL RUN

After I confirm the test:
Remove the 5-row limit. Run on all keywords.
Show live progress every keyword.
Final report:
- Total keywords classified
- Intent type breakdown (how many of each)
- Any errors
- Sample of 10 fear statements — one per intent type

---

## STEP 8 — AUDIT

After full run, spawn audit sub-agent:
- Read 20 random keywords from Column A
- Check Column J and K are populated
- Verify no generic fear statements (flag any that say "something might go wrong" or similar)
- Verify no duplicates in Column K (every fear should be specific to its keyword)
- Check all 6 intent types are represented
- Report PASS/FAIL per check

---

## STEP 9 — UPDATE DOCUMENTATION

After audit passes:
1. Update skill-01/03-fear-formula.md — mark Phase 1 as complete
2. Update README.md — mark File 03 as done
3. Print final status:
   "Fear Formula complete.
   [X] keywords classified
   Intent breakdown: [counts]
   Ready for: File 04 — 4-Second Sorting Funnel"

---

## COST ESTIMATE

Roughly 800-1,200 keywords × ~200 tokens per call = 160,000-240,000 tokens
At claude-sonnet-4-20250514 rates: approximately $0.60-$0.90 total
Runtime: approximately 10-15 minutes with 0.5s rate limiting
