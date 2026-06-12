# Competitive SEO Teardown — UK & EU Pet-Import Regulatory Queries

**Project:** PawRoute (UAE → UK/EU pet relocation)
**Research date:** 2026-06-09
**Method:** WebSearch for genuine top organic result (ads ignored) → WebFetch page analysis. Domain tenure verified via WebSearch corporate records (Wayback Machine `web.archive.org` was unreachable from this environment, so all Wayback-based tenure is **Estimated**, not Measured).

> **Truth note:** Every "founded" / "tenure" figure below is labelled Measured or Estimated. I did NOT capture first-snapshot dates from the Wayback Machine because the tool could not reach `web.archive.org`. Corporate founding years come from WebSearch of company/About pages and third-party profiles (LinkedIn, Crunchbase, CNBC) — treat as Estimated unless stated.

---

## GOV vs AGGREGATOR — headline finding

| Query | #1 organic result | Type | Gov owns it? |
|---|---|---|---|
| import pet to UK requirements | petrelocation.com (blog) | Competitor-relocator / aggregator | **No** — gov.uk absent from top organic |
| bring dog to UK from abroad rules | gov.uk/bring-pet-to-great-britain | **Government** | **Yes** |
| pet travel to Great Britain | gov.uk/bring-pet-to-great-britain (USDA APHIS also top, US-centric) | **Government** | **Yes** |
| bring pet to EU from non-EU country | food.ec.europa.eu | **Government (EU Commission)** | **Yes** |
| EU pet import rabies titre test | europa.eu/youreurope (Your Europe) | **Government (EU Commission)** | **Yes** |
| Dubai to UK pet relocation | iss-relocations.com (blog) | Competitor-relocator | **No** — gov.uk absent; commercial guides own it |

**Pattern in one line:** Government domains decisively own the *generic regulatory* queries (4 of 6). The two queries gov LOSES are the **transactional / intent-loaded** ones — "import pet to UK **requirements**" and the **route-specific** "Dubai to UK pet relocation" — and that is exactly where a route-specific challenger like PawRoute can win.

---

## 1. "import pet to UK requirements"

**#1 organic:** https://www.petrelocation.com/blog/post/bringing-dogs-and-cats-to-the-uk-a-simple-guide
**Type:** Competitor-relocator / aggregator-content (a US pet-shipping company's blog).
**Gov ownership:** **No.** gov.uk does NOT rank #1 for this phrasing — the word "requirements" pulls a comprehensive guide-style page over the terse official one.

**2. TENURE**
- Company founded **2004** (Estimated — from petrelocation.com "Focus Since 2004" blog + CNBC profile; Crunchbase corroborates). Domain `petrelocation.com` therefore ~22 yrs old.
- Copyright footer: **"Copyright© 2026 PetRelocation, Inc."** (Measured — on page).
- Content "last updated" date: **none shown** (Measured absence).
- Wayback first snapshot: **not captured** (web.archive.org unreachable).

**3. DIFFERENTIATION** — Reads like a human caseworker, not a statute. Covers things gov.uk omits: cost breakdown ("How much does it cost"), crate-training advice, "common mistakes to avoid" (7-bullet list), and the commercial-vs-non-commercial 5-day rule explained in plain English. Soft-sells its done-for-you service via "Get a Quote" CTA.

**4. STRUCTURE**
- H1: *"Everything You Need to Know About Moving Cats and Dogs to The UK"*
- ~1,600–1,800 words; **step-numbered** H2s (Step 1 entry eligibility → Step 2 microchip-then-rabies → Step 3 health certificate), plus 5-day rule, USDA endorsement, tapeworm, approved routes, crate training, cost, commercial fallback, leaving-UK, mistakes.
- Lists yes (cost items, mistakes). **No tables. No FAQ. No JSON-LD** detected. No calculator.
- Internal links: `/country/uk`, `/about`, `/blog`, `/arrange`, `/contact`, author `/blog/author/2`.
- Media: header logo only; no inline photos/video.

**5. TRUST/E-E-A-T** — Author = generic "PetRelocation Team". Cites **USDA-accredited vet** repeatedly but **does NOT link gov.uk / DEFRA** directly. No reviews on-page. Authority is brand-reputation (20-yr-old shipper), not citation.

**6. NOTABLE** — Ranks #1 for a *regulatory* query with **zero official-source links and no schema** — beatable on E-E-A-T by anyone who cites DEFRA and adds FAQ schema.

---

## 2. "bring dog to UK from abroad rules"

**#1 organic:** https://www.gov.uk/bring-pet-to-great-britain
**Type:** **Government** (UK official).
**Gov ownership:** **Yes — total.** This is the canonical DEFRA/APHA page; aggregators rank below it.

**2. TENURE**
- gov.uk domain live since **Oct 2012** (Estimated — gov.uk relaunch is well-documented public record); underlying Pet Travel Scheme (PETS) since **2001**, post-Brexit rules effective **1 Jan 2021** (Estimated — DEFRA history via WebSearch).
- No copyright year / no visible "Last updated" date were returned in the page body (Measured absence in fetch — gov.uk normally carries one lower in metadata; not confirmed here).

**3. DIFFERENTIATION** — Authoritative "step by step" journey hub: each step is its own linked sub-page (microchip, rabies, blood test, tapeworm, documents, banned breeds, quarantine). It is the **source of truth** every aggregator paraphrases.

**4. STRUCTURE**
- H1: *"Bringing your pet dog, cat or ferret to Great Britain"*
- ~1,800–2,000 words incl. nav. H2 "What you need to do" + H3 Step 1–4 (check eligibility → microchip → rabies → travel document); H2 extra-rules, authorising another person.
- Bulleted lists; **5-step sequential nav**. **No FAQ, no tables, no tools.**
- Internal links: deep — travel routes, microchip, rabies vaccination, blood tests for rabies, tapeworm, pet travel documents, pet passports, AHCs, assistance dogs, >5 pets, banned breeds, rabies quarantine. (This dense internal web is its ranking moat.)
- Media: none (GOV.UK app banner only).

**5. TRUST/E-E-A-T** — Maximum institutional authority by domain alone. No named author/department surfaced; no reviews (not applicable). It IS the official source others cite.

**6. NOTABLE** — Terse and link-hubbed by design. It deliberately does NOT cover cost, timelines-in-days, or route logistics — leaving whitespace for commercial guides.

---

## 3. "pet travel to Great Britain"

**#1 organic:** https://www.gov.uk/bring-pet-to-great-britain (same canonical page). USDA **APHIS** (aphis.usda.gov) also ranks at/near the top but is **US-export-specific** and irrelevant to UAE origin.
**Type:** **Government** (UK gov.uk + US APHIS).
**Gov ownership:** **Yes.** Two government bodies split the top; no aggregator owns it.

**2. TENURE** — Same gov.uk page as Query 2 (see above). APHIS = USDA, decades-old `.gov` (Estimated).

**3–6.** Structure/trust identical to Query 2's gov.uk page. The added competitor here is a **government rival (APHIS)**, not an aggregator — reinforcing that gov owns the generic "pet travel to GB" intent. A UAE-origin challenger is not competing with APHIS (wrong origin country) — opportunity is the **UAE→GB origin gap** neither gov page serves.

---

## 4. "bring pet to EU from non-EU country"

**#1 organic:** https://food.ec.europa.eu/animals/live-animal-movements/dogs-cats-and-ferrets/bringing-pet-eu-non-eu-country_en
**Type:** **Government (European Commission, DG SANTE / Food Safety).**
**Gov ownership:** **Yes — total.** The EU Commission's own regulatory page is #1.

**2. TENURE**
- `food.ec.europa.eu` = EU Commission institutional domain (Estimated decades; ec.europa.eu long-established).
- **No last-updated date on page** (Measured absence). Content is current: cites **2026** regulations (see below), so freshly maintained.

**3. DIFFERENTIATION** — Pure regulatory primary source citing the actual legal instruments. Includes a dedicated **"Specific arrangements for United Kingdom"** H3 — directly relevant to post-Brexit GB↔EU moves. Notes the **Finland/Ireland/Malta/Norway/N.Ireland** tapeworm exception.

**4. STRUCTURE**
- H1: *"Bringing a pet into the EU from a non-EU country"*
- ~2,800 words. H2 Conditions / Exceptions / Related links / Posters. H3s: Identification, Health status, Rabies vaccination, **Rabies antibody titration test**, Tapeworm *Echinococcus multilocularis*, Animal Health Certificate + declaration, Travellers' point of entry, UK arrangements.
- Extensive bullets. **No tables, no FAQ, no calculator.** Tools referenced (not embedded): TRACES, designated-laboratory list, points-of-entry directory.
- Legal citations (strong E-E-A-T signal): **Commission Delegated Reg (EU) 2026/131, 2019/2035, 2020/688; Implementing Reg (EU) 2026/705; Decision 2003/803/EC.**
- Media: none embedded (posters listed, not shown).

**5. TRUST/E-E-A-T** — Highest possible: the page IS the law's plain-language gateway, citing the regulations by number. No author needed; institution is the authority.

**6. NOTABLE** — Regulatory depth but **poor UX**: no tables, no FAQ, no per-country selector here (that lives on the Your Europe page, Query 5). Whitespace = digestible tables + route-specific worked examples.

---

## 5. "EU pet import rabies titre test"

**#1 organic:** https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_en.htm (Your Europe — EU Commission citizen portal).
**Type:** **Government (European Commission).**
**Gov ownership:** **Yes.** Your Europe outranks the commercial titre-test guides (petabroad.eu, pets2fly) for this query.

**2. TENURE**
- `europa.eu/youreurope` = EU Commission portal (Estimated long-established institutional domain).
- **"Last checked: 23/04/2026"** (Measured — on page). This is the only one of the six with an explicit, recent freshness date — a real ranking/E-E-A-T asset.

**3. DIFFERENTIATION** — Has an **interactive country selector** ("Choose the country you are travelling from") that dynamically surfaces rules — the closest thing to a tool among all six pages. Most thorough titre-test coverage with exact timings.

**4. STRUCTURE**
- H1: *"Travelling with pets and other animals in the EU"*
- ~3,800–4,200 words (longest of the six). H2s: dogs/cats/ferrets, travel documents, entering the EU, other pets, **FAQs**, EU legislation, assistance services. H3s incl. EU pet passport, EU AHC, **Rabies antibody titration testing**, tapeworm rules, young-animal exceptions.
- **Has FAQs** (linked) + **accordion country-rule sets** + **dropdown selector** = the only page here with genuine interactivity. No tables.
- Titre-test specifics quoted: *"wait 30 days after the primary vaccination"* before testing; *"wait 3 months from the date the blood sample was taken"* before travel; sample taken by authorised vet at a **designated laboratory**; 3-month wait waived for short-stay re-entry.
- Internal links: FAQ page, points-of-entry finder, designated-lab list, assistance-service finder.

**5. TRUST/E-E-A-T** — Institutional authority + **explicit freshness date** + legal citations (EU pet-travel Regulation, EU-UK Withdrawal Agreement). Best-rounded E-E-A-T of the six.

**6. NOTABLE** — This is the **highest bar to beat** on-content: long, fresh, interactive, authoritative. A challenger should NOT try to out-encyclopedia it — win instead on **route specificity** (UAE-origin) and **conversion**, not generic titre depth.

---

## 6. "Dubai to UK pet relocation"

**#1 organic:** https://iss-relocations.com/blog/pet-relocation-dubai-to-uk-guide/
**Type:** Competitor-relocator (a UAE moving company's blog).
**Gov ownership:** **No.** No government page ranks for this route-specific query — it is owned entirely by commercial relocation guides. **This is PawRoute's core battleground.**

**2. TENURE**
- ISS Relocations corporate lineage: origins **1996 (as Mac Movers)** → **ISS Worldwide Movers ~2000** → relocations business sold to CSS Group **2019** (Estimated — from About page + third-party profiles). So the *brand/domain* is old, but the **pet vertical and this blog post are new**.
- Blog post **Published "Apr 01, 2025"** (Measured — on page). ~14 months old.
- Footer **"Copyright © 2026 ISS Relocations"** (Measured). No "updated" date.

**3. DIFFERENTIATION** — Route-specific framing ("Dubai to UK") + door-to-door full-service pitch (home pickup → vet checks → airport drop-off → customs). Strong **trust badges**: FIDI, Worldwide ERC, ISO 9001:2015 & 14001:2015, GEM Network, Euromovers. **30-year history** badge. **No IPATA** visible (gap — IPATA is the pet-relocation industry body).

**4. STRUCTURE**
- H1: *"Smooth Pet Relocation Dubai to UK – Your Ultimate Safety Guide"*
- ~2,100–2,400 words. H2s: Understanding the route, Safe relocation, UK import rules, Dubai-resident guidelines, Quarantine rules & exceptions, Cost breakdown, Talk to experts, Choosing a company, Wrap-up. Rich H3 nesting (PETS explained, pet passport/docs, pre-departure, Dubai exit procedures, when quarantine applies, cost factors, cost-saving tips).
- **Has a 10-question FAQ** (e.g., "What are the requirements for taking a pet from Dubai to the UK?", "How much does it cost?", "Do pets need to quarantine?"). Bulleted doc-requirement lists. **No tables, no calculator.**
- Heavy internal linking to service pages (`/pet-relocation/`, `/moving-to-uk/`, `/customs-clearance/`, related blogs).
- Media: 1 hero image + 8 accreditation badges; no video/infographic.

**5. TRUST/E-E-A-T** — **No author byline** (weakness). Mentions "DEFRA-compliant AHC" and names PETS but **does NOT link gov.uk/DEFRA**. Accreditations are general-mover (FIDI/ISO), **not pet-specific (no IPATA)**. Testimonials linked off-page, none embedded.

**6. NOTABLE** — Ranks #1 on a 14-month-old post with **no author, no official links, no IPATA, no tables, and a generic-mover (not pet-specialist) trust profile.** This is the **weakest #1 of all six** and the clearest win for a focused UAE pet-relocation specialist.

---

## CLUSTER PATTERN SUMMARY

**Gov vs aggregator dominance**
- **Government wins the generic regulatory core (4/6):** "bring dog to UK rules", "pet travel to Great Britain" → gov.uk; "bring pet to EU from non-EU" → food.ec.europa.eu; "EU rabies titre test" → europa.eu Your Europe. These pages win on domain authority + dense internal linking + (for Your Europe) freshness, interactivity and FAQ. **Do not attack these head-on with a generic guide.**
- **Aggregators/relocators win the transactional & route-specific tail (2/6):** "import pet to UK **requirements**" → petrelocation.com; "**Dubai to UK** pet relocation" → iss-relocations.com. The trigger words are *requirements / cost / route-name* — intent that gov pages deliberately under-serve (gov omits cost, day-count timelines, and origin-specific logistics).

**Shared weaknesses across the commercial #1s (the opening for PawRoute):**
1. **No official-source links** — neither petrelocation nor iss-relocations links gov.uk/DEFRA/europa.eu, despite ranking for regulatory queries. A page that *cites and links DEFRA/EC primary law* immediately out-signals them on E-E-A-T.
2. **No JSON-LD / FAQ schema** detected on the commercial winners (ISS has a visible FAQ but no confirmed schema; PetRelocation has neither). Adding `FAQPage` + `HowTo` + `Article`/`author` schema is low-effort, high-leverage.
3. **No tables** anywhere in the cluster — every page is prose+bullets. A clean **requirements/timeline/cost table** (day-count countdown, document checklist) is a differentiated SERP-feature magnet.
4. **No tools/calculators** except Your Europe's country dropdown. A **UAE→UK/EU cost + timeline calculator** would be unique in this entire cluster.
5. **Weak/absent authorship** — PetRelocation = generic "Team"; ISS = no byline. A **named, credentialed author** (vet-reviewed, IPATA-affiliated) beats both.
6. **No pet-specific accreditation** on ISS (no IPATA). PawRoute leading with **IPATA + vet review** is a trust differentiator the route incumbent lacks.

**Where a route-specific challenger (PawRoute) can win — priority order:**
1. **"Dubai to UK pet relocation" (and sibling UAE-origin routes).** No gov page competes; the #1 is a 14-month-old, author-less, badge-only generic-mover post. **Highest-probability win.** Beat it with: named vet-reviewed author + IPATA + gov.uk/DEFRA citations + a day-by-day countdown table + cost calculator + FAQ schema.
2. **"import pet to UK requirements" / "...cost"-style transactional queries.** Out-cite PetRelocation with linked DEFRA sources, add a requirements table and FAQ schema. Winnable.
3. **Do NOT chase** the four gov-owned generic queries with a generic guide. Instead, capture their downstream intent: publish **UAE-origin-specific** derivatives ("UAE rabies titre test for UK", "Dubai pet export to EU AHC") where gov pages are generic and no strong commercial incumbent exists yet.

**Truth/limitations:** Wayback first-snapshot tenure was NOT measured (web.archive.org unreachable); all domain ages are Estimated from corporate/About sources. On-page items (copyright years, ISS "Apr 01 2025" publish date, Your Europe "Last checked 23/04/2026") ARE Measured from the fetched pages.
