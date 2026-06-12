# Official Source Research — Manual Verification Recipe
## The method that converts 47 failed URLs into verified findings
## Discovered during Dubai pet relocation proof run — 2026-05-28

---

## The Core Insight

A failed URL almost never means the information does not exist.
It means you have the wrong address for it.

Government sites constantly:
- Rename domains (Austria moved verbrauchergesundheit.gv.at → bavg.gv.at)
- Retire old portals (India animalquarantineindia.gov.in → aqcsindia.gov.in)
- Bury real content several clicks below the homepage

So instead of trusting the stored link, throw it away.
Re-derive the correct URL from two things that never go stale:
- The name of the authority
- What the page is about

A search engine has already crawled the live site and knows its current
deep URL — even when the old one is dead. That is the leverage.

---

## The Search Formula

One query per authority. Built from four slots:

```
[authority name] + [country] + "bring/import dog cat" + [local-language term] + site:[official domain]
```

**Real examples from the Dubai pet relocation proof run:**

```
Germany BMEL bringing pet dog cat import site:bmel.de
Switzerland FSVO BLV travelling with pets blv.admin.ch
Greece εισαγωγή σκύλου γάτας minagric.gr
```

**Why the site: filter matters:**
Forces an official result instead of a pet relocation blog ranking above the source.

**Why the local-language term matters:**
The real page is often only indexed under the native phrase.
English queries miss it entirely.

Examples of native terms that work:
- German: "Reisen mit Heimtieren" or "Einfuhr Haustier"
- French: "voyager avec animaux domestiques"
- Spanish: "viajar con animales de compañía"
- Greek: "εισαγωγή σκύλου γάτας"
- Arabic: "استيراد الحيوانات الأليفة"

---

## The Verify and Classify Loop

Run on each candidate URL in a **real browser** — not a script.

A real browser distinguishes three outcomes that a headless script blurs together:

### Outcome 1 — Verified ✅
Page loads and contains pet import content.
The URL is correct.
Mark the "official requirements published" claim as Verified.
Copy the exact quote. Note the date.

### Outcome 2 — Wrong page — keep hunting ⚠️
Page loads but shows a 404, homepage, or generic ministry page.
Wrong page, not wrong domain.
Modify the search query and try again.
This is how live Etihad and Flydubai 404s were caught during the proof run.

### Outcome 3 — Domain unreachable — Unverifiable ❌
DNS failure, timeout, SSL block that persists in a real browser.
The domain itself is unreachable — a different problem from a wrong URL.
Examples from proof run: Belgium, Jordan, old South Africa domain.
Mark as Unverifiable. Note the specific failure type.

---

## Why Real Browser Not Script

The original automated engine used a headless fetcher.
This is why 47 rows returned as "Pending — load failed."

Root causes of headless failures:
- JavaScript-rendered pages (Greece looked completely empty to the script)
- HTTP/2 quirks that headless browsers handle differently
- SSL interstitials and certificate errors
- Cookie consent walls that block content loading

A real browser renders the page exactly as a person sees it.
"Empty" pages in headless mode turn out to be full of content in a real browser.

**The price:** screenshots cannot be auto-saved when using a real browser manually.
This is the one gap in the output — noted for future tooling improvement.

---

## Claim Matching — The Simple Test

For each specific claim after finding the page:

**Does the page text actually say this?**

- Yes, explicitly → Verified. Copy exact quote.
- Page is silent on this claim → Unverifiable. The source exists but does not address this.
- Page says something different → Unverifiable + flag the contradiction.

**Real contradictions found during Dubai pet relocation proof run:**

| Claim | Community Said | Official Source Said | Action |
|-------|---------------|---------------------|--------|
| Etihad cabin pet fee | $1,500 USD | $399 USD | Unverifiable + contradiction flagged |
| Air Cairo advance notice | No advance notice needed | Required 48hrs notice | Unverifiable + contradiction flagged |

These contradictions are the most valuable findings in the Source Bank.
They protect customers from acting on wrong community information.

---

## The Screenshot Gap — Known Issue

When verifying manually in a real browser, screenshots must be saved manually.
The automated engine saves them automatically but fails on JS-rendered pages.

**Current workaround:**
- Manual verification: screenshot each page manually, name using convention:
  `[COUNTRY]-[authority]-[claim-id]-[date-verified].png`
- Save to: skill-02/data/source-screenshots/
- Update SOURCE-INDEX.md manually after each session

**Future improvement needed:**
Build a semi-automated tool that opens URLs in a real browser (not headless),
waits for full render, then captures screenshots automatically.
Playwright with headed mode + wait_for_load_state("networkidle") may solve this.

---

## Authority Directory — Useful Starting Points

Built from the Dubai pet relocation proof run.
Use as starting points — always verify the current URL before trusting.

| Country | Authority | Search Term | Domain Hint |
|---------|-----------|-------------|-------------|
| UK | APHA | "APHA pet travel rules" | apha.gov.uk |
| Germany | BMEL | "BMEL Haustier Einfuhr" | bmel.de |
| France | DGAL | "DGAL animaux compagnie" | agriculture.gouv.fr |
| Switzerland | FSVO/BLV | "BLV travelling pets" | blv.admin.ch |
| Austria | BAVG | "BAVG Haustier Einreise" | bavg.gv.at |
| Netherlands | NVWA | "NVWA reizen huisdier" | nvwa.nl |
| Spain | MAPA | "MAPA viajar animales" | mapa.gob.es |
| Italy | Ministero Salute | "animali compagnia viaggio" | salute.gov.it |
| Greece | MinAgric | "εισαγωγή σκύλου" | minagric.gr |
| Sweden | Jordbruksverket | "resa med sällskapsdjur" | jordbruksverket.se |
| Norway | Mattilsynet | "reise kjæledyr" | mattilsynet.no |
| Denmark | Fødevarestyrelsen | "rejse kæledyr" | foedevarestyrelsen.dk |
| Ireland | DAFM | "DAFM pet travel" | gov.ie/dafm |
| US | USDA APHIS | "APHIS bring pet US" | aphis.usda.gov |
| Australia | DAFF | "DAFF import pet" | agriculture.gov.au |
| India | AQCS | "AQCS import dog cat" | aqcsindia.gov.in |
| UAE | MOCCAE | "MOCCAE pet import export" | moccae.gov.ae |

---

## When to Use This Recipe

Use this recipe when:
- The automated engine returns Pending — load failed
- A source URL returns a 404 or homepage instead of the target page
- A government site has recently migrated to a new domain
- Local-language content is needed and English queries return nothing

Do NOT use this recipe to:
- Verify pricing claims — government sites rarely publish these
- Find information that genuinely does not exist online
- Replace automated verification for sources that load cleanly

---

## Time Estimate

Per failed URL: 3-5 minutes
47 failed URLs: approximately 3-4 hours total
Can be batched: 10-15 per session across multiple days

---

## Applying to Other Niches

The formula works for any regulated service market.
The four slots stay the same. Only the content changes:

Immigration law: `[immigration authority] + [country] + "visa application requirements" + [local term] + site:[gov domain]`

Private medical: `[health authority] + [country] + "treatment approval overseas" + [local term] + site:[gov domain]`

Financial services: `[regulator name] + [country] + "licence requirements" + [local term] + site:[gov domain]`

The site: filter and local-language term are the two things most researchers skip.
They are the two things that make the difference.
