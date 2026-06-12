# Competitor SEO Teardown — USA / Canada / India Pet-Import Regulatory Queries

Research date: 2026-06-09. For PawRoute (UAE pet relocation).
Method: WebSearch for the genuine #1 organic result (ads ignored), WebFetch to analyze, Wayback CDX/availability API for domain tenure.
Truth labels: **[Measured]** = observed directly (page text, Wayback API, page source). **[Estimated]** = inferred/approximate.

> Data note: APHIS (aphis.usda.gov) pages are heavy Drupal/JS and repeatedly timed out in WebFetch; their content is reconstructed from search snippets + the print-PDF node and is labelled accordingly. Wayback's CDX endpoint rate-limited (503/504) on some queries, so a few gov first-snapshot dates are **[Estimated]**.

---

## 1. QUERY: "bring dog to USA CDC rules 2026"

**Winner:** https://www.cdc.gov/importation/dogs/index.html — "Bringing a Dog into the U.S."
**TYPE:** Government (CDC / NCEZID).

- A worldcarepet.com competitor page ("Returning to the U.S. With a Dog: 2026 Travel Requirements") ranks #2 — the only non-gov result with traction (see Challenger section).

**2. TENURE**
- Domain cdc.gov first Wayback capture **1996-12-22**. **[Measured]**
- The `/importation/dogs/` path first captured **2024-07-17** — i.e. the page in its current form was published with the new rule regime, NOT older content reskinned. **[Measured]**
- Content "Aug. 1, 2024" date stamp at top and bottom of page. Image asset path references "2026/02" (Feb 2026 CMS touch). **[Measured]**
- No copyright year; no separate "last reviewed" line. **[Measured]**

**3. DIFFERENTIATION**
- It is the regulatory primary source — the rule itself. Authoritative by definition.
- "Dog Importation Navigator" interactive decision tool (linked) that branches by the dog's situation. **[Measured]**

**4. STRUCTURE**
- H1: "Bringing a Dog into the U.S."
- H2: Background · Requirements are based on your dog's situation · Additional information
- H3: High-risk countries for dog rabies · Dog Importation Navigator · "In the 6 months prior to entering the U.S., your dog has been…" · Questions?
- Length ~800–1,000 words (deliberately short, hub-and-spoke). **[Estimated]**
- 1 decision matrix table (three dog scenarios → requirement links); ~3 bulleted lists; FAQ NOT embedded (links to separate /faqs.html). **[Measured]**
- ~6 internal links (high-risk country list, Navigator tool, vet docs, airline info, FAQ, laws) + outbound to USDA. **[Measured]**
- No JSON-LD quoted in source; gov templates typically emit minimal/GovernmentOrganization schema only. **[Estimated]**

**5. TRUST / E-E-A-T**
- Reviewing body: National Center for Emerging and Zoonotic Infectious Diseases (NCEZID). **[Measured]**
- CDC-INFO phone (800) 232-4636. No author byline, no reviews (not needed — it's the regulator). **[Measured]**

**6. FRESHNESS handling (the key lever for this rules-changed query)**
- Explicit "Aug. 1, 2024" date — the date the new rule took effect — shown top and bottom. **[Measured]**
- Per CDC's own messaging, the **Feb 5, 2026 update** to the Dog Import Form web system is called out as "new look… no changes to importation requirements" — they actively suppress freshness churn anxiety. **[Measured, from search snippet]**
- Lesson: the gov page wins the "2026" query without stuffing "2026" — it owns the canonical rule + recent dated stamp. The dated authority beats keyword-matching.

---

## 2. QUERY: "import dog to United States requirements"

**Winner:** Top organic = CDC pages (`/importation/dogs/dog-import-form-instructions.html` and `/importation/dogs/index.html`); first non-CDC gov result is APHIS:
https://www.aphis.usda.gov/pet-travel/another-country-to-us-import/dogs — "Bring a Pet Dog into the United States"
**TYPE:** Government (USDA APHIS). CDC owns the SERP head; APHIS owns the USDA/agriculture angle.

**2. TENURE**
- aphis.usda.gov first Wayback capture **1997-07-02**. **[Measured]**
- No on-page "last updated" date captured (WebFetch timed out). **[Estimated]**

**3. DIFFERENTIATION**
- USDA-side of the dual-agency split: covers the USDA endorsement / agriculture inspection angle CDC doesn't, and links country-by-country.
- Part of a large `/pet-travel/` hub covering every country pair (import + export).

**4. STRUCTURE [Estimated — reconstructed from snippets]**
- Country-risk branching (high-risk vs low-risk/rabies-free), microchip-before-vaccination ordering, CDC-registered facility reservation requirement for foreign-vaccinated dogs from high-risk countries.
- Hub page linking to forms (Certification of Foreign Rabies Vaccination and Microchip; Certification of U.S.-issued Rabies Vaccination).

**5. TRUST / E-E-A-T**
- USDA APHIS as authority; very old, high-authority gov domain. **[Measured tenure]**

**6. FRESHNESS**
- APHIS leans on domain authority + cross-links to CDC's dated rule rather than its own date stamping. **[Estimated]**

> Note: aggregator pettravel.com and a vet-clinic blog (animalvetsfairfield.com) appear lower — proof that non-gov content can rank on this exact-match query, but only below the two agencies.

---

## 3. QUERY: "import pet to Canada CFIA requirements"

**Winner:** https://inspection.canada.ca/en/importing-food-plants-animals/pets — "Bringing animals to Canada: Importing and travelling with pets"
**TYPE:** Government (CFIA / Government of Canada).

**2. TENURE**
- inspection.canada.ca is the CFIA's domain; CFIA established 1997. Wayback CDX rate-limited on retries; domain age **[Estimated: 1997-era, 25+ yrs]**.
- On-page **"Date modified: 2024-07-22"**. No copyright year. **[Measured]**

**3. DIFFERENTIATION**
- Interactive cascading decision-tree tool (select animal type → import purpose → origin) that routes the user to exact requirements — strongest interactive UX of the three regulators. **[Measured]**
- Bilingual (English/Français). The separate AIRS (Automated Import Reference System) is the deep lookup engine it feeds into. **[Measured]**

**4. STRUCTURE**
- H1: "Bringing animals to Canada: Importing and travelling with pets"
- H2: "What type of animal are you importing or travelling with?" + Government-of-Canada chrome (Feedback / CFIA / Themes / About this site)
- H3: nested per-animal categories (Dog, Cat, Ferret, Bird, Rabbit…)
- Length ~2,000–2,500 words incl. nav/footer. **[Estimated]**
- No data tables, no embedded FAQ; the tool replaces them. Bulleted category lists. **[Measured]**
- Breadcrumb to Canada.ca; internal cross-refs only, no external citations. **[Measured]**
- Schema: likely GovernmentOrganization; none visibly quoted. **[Estimated]**

**5. TRUST / E-E-A-T**
- CFIA + Government of Canada branding throughout; no author/reviews (regulator). **[Measured]**

**6. FRESHNESS**
- "Date modified: 2024-07-22" is the freshness signal — a single visible modified date, no year keywords. Same pattern as CDC: dated authority, not keyword stuffing. **[Measured]**

> Aggregators chasing this cluster with year-stamped titles: yourdogbutler.com ("Ultimate Guide For 2025"), petuniapets.com (multiple 2025 + 2026 dated checklist posts). They rank below the gov page but are clearly targeting the freshness/year angle the gov page deliberately ignores.

---

## 4. QUERY: "bring pet to India requirements" / "returning to India with a dog NOC"

**Winner:** https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-india — "Pet Travel From the United States to India"
**TYPE:** Government (USDA APHIS, export side). Notable that for the *NOC* query the US gov export page outranks Indian gov sources.

- Indian government alternatives present: cgisf.gov.in (Consulate General SF), aqcsindia.gov.in (AQCS — the actual NOC issuer). Competitor-relocators tailwindglobalpet.com and furryflyers.com also rank.

**2. TENURE**
- aphis.usda.gov first capture **1997-07-02**. **[Measured]**
- No on-page date captured (WebFetch timed out). **[Estimated]**

**3. DIFFERENTIATION**
- Hosts downloadable **Standard Operating Procedure PDFs** as primary assets: `india-dogs-guidance.pdf`, `india-cats-guidance.pdf`, `ind-live-poul-gd.pdf` — step-by-step SOPs no competitor replicates with equal authority. **[Measured, from search]**
- Spells out the full bureaucratic chain competitors gloss over: **DGFT license (form ANF-2M, specific columns 2(i)/(ii), 3(ii), 4, 5, 7, 8, 9; ~1 month processing) → NOC from AQCS (~5 working days, by mail/fax/in person) → USDA-endorsed health cert → microchip + rabies**. **[Measured, from search]**

**4. STRUCTURE [Estimated — reconstructed]**
- Export-checklist format: documents, NOC, DGFT, health certificate, microchip, rabies; links out to the SOP PDFs.

**5. TRUST / E-E-A-T**
- USDA APHIS authority + links to Indian regulatory specifics. The PDF SOPs are the E-E-A-T moat. **[Measured]**

**6. FRESHNESS**
- Relies on domain authority + the SOP documents; not a date-led page. **[Estimated]**

> The "returning to India with a dog NOC" intent (resident returnees) is **under-served by the gov pages**, which are framed as US→India *export*. The CGI consulate page and AQCS handle the NOC mechanics but read as dense bureaucracy — a clear content gap (see Challenger).

---

## 5. QUERY: "Dubai to USA pet relocation"

**Winner:** https://www.carrymypet.ae/destination/usa — "International Pet Transportation to the U.S.A" (Carry My Pet)
**TYPE:** Competitor-relocator (direct PawRoute rival, UAE-based).

- Other competitors on page 1: sandypaws.ae, dkc.ae (claims "30+ years"), thepetshop.com, universalrelocations.com, relocateyourpet.com; plus petrelocation.com (US giant) and Emirates SkyCargo (airline).

**2. TENURE**
- carrymypet.ae first-ever Wayback capture **2023-10-17** — entire domain history is < ~2.5 years. **Young domain.** **[Measured]**
- No copyright year or last-updated date on the page; blog posts show **June 2024** dates. **[Measured]**

**3. DIFFERENTIATION**
- Covers BOTH directions on one page: USA import requirements + UAE export requirements. **[Measured]**
- In-house ancillary services: IATA-accredited crates, microchipping, rabies titer testing, pet-taxi. **[Measured]**
- Multi-destination footprint (9+ country landing pages, same template). **[Measured]**

**4. STRUCTURE**
- H1: "International Pet Transportation to the U.S.A"
- H2: Pet Microchip · Rabies Titer Test Results · Vaccination & Certification · Parasite Inspection (Dogs Only) · Documentation & Permits · Export Requirements
- H3: For Dogs / For Cats subsections
- Length ~2,000–2,500 words. **[Estimated]**
- Lists for vaccination/document requirements; **FAQ of 5 Qs — but they're about INDIA relocation, not USA** (template not localized — a real defect). **[Measured]**
- No pricing table, no timeline graphic, no calculator. "GET QUOTE" form/CTA is the only tool. **[Measured]**
- No JSON-LD/microdata visible. **[Estimated → weakness]**

**5. TRUST / E-E-A-T**
- IATA + IPATA logos in footer (accreditation). **[Measured]**
- No author byline, no testimonials/reviews on the page, no clickable CDC/USDA citations (names them but doesn't link). **[Measured — significant E-E-A-T weakness]**

**6. FRESHNESS — and how it handles the changed CDC rules**
- Weak. No 2024/2025/2026 references; content is static. **Does NOT address the Aug 2024 CDC rule change** (new Dog Import Form, high-risk facility rules). **[Measured]**
- This is the single biggest exploitable gap in the commercial SERP: the #1 commercial result is silent on the very rule change the query year ("2026") implies.

---

## CLUSTER PATTERN SUMMARY

1. **Regulators own the regulatory queries.** CDC, APHIS, and CFIA take the #1 organic slot for every pure-info query (USA, Canada, India-export). On extremely old, high-authority gov domains (cdc.gov 1996, aphis.usda.gov 1997, CFIA ~1997). A challenger should not try to outrank the regulator for "[country] dog import requirements" head terms.

2. **Freshness is signalled by a dated authority, not keyword stuffing.** The winners use a single visible date — CDC "Aug. 1, 2024", CFIA "Date modified: 2024-07-22" — and notably do NOT cram "2026" into titles/body. Yet they win "...2026" queries. The ranking lever is: canonical rule + recent honest modified-date + suppression of churn anxiety (CDC explicitly says the Feb 2026 form update "does not change requirements").

3. **Tools beat prose.** Both CDC (Dog Importation Navigator) and CFIA (cascading decision tree → AIRS) replace long text with interactive branching by the pet's situation. Length is modest (~800–2,500 words); structure and a decision tool do the work.

4. **The agency split is itself a content gap.** USA rules are split across CDC (rabies/health) AND USDA APHIS (endorsement/ag), and India across USDA-export + Indian DGFT/AQCS. No single gov page unifies the end-to-end journey for a real traveler. Aggregators (worldcarepet, petuniapets, yourdogbutler, pettravel) live in exactly this gap with year-stamped "ultimate guide / checklist" pages.

5. **Commercial SERP is weak and exploitable.** The #1 commercial result for "Dubai to USA" (carrymypet.ae) is a < 2.5-yr-old domain, no schema, no clickable gov citations, an un-localized India FAQ on a USA page, and zero coverage of the 2024 CDC rule change. The relocator field competes on services/accreditation logos, not content quality or freshness.

---

## WHERE A CHALLENGER (PawRoute) CAN WIN

- **Own the journey, not the rule.** Build the unified "Dubai/UAE → USA" (and → Canada, → India-return) page the regulators structurally can't: combine CDC + USDA-APHIS + airline + UAE-export steps into one timeline. UAE is low-risk/rabies-free — lead with that simplification advantage.
- **Win freshness honestly.** Add a visible "Last updated" date + a short "What changed: Aug 2024 CDC rule + Feb 2026 form" changelog block. carrymypet.ae and peers are silent here; the query carries a "2026" expectation the gov pages satisfy and the commercial pages do not.
- **Beat carrymypet.ae on E-E-A-T basics it's missing:** clickable citations to cdc.gov/aphis/CFIA, named author/vet reviewer, testimonials/reviews, and JSON-LD (FAQPage + HowTo + Organization/LocalBusiness + breadcrumbs). These are cheap wins it's leaving on the table.
- **Build the tool.** A UAE-origin "what does my pet need" decision widget (mirroring CDC Navigator / CFIA tree) plus a cost + timeline estimator — relocator competitors only offer a "Get Quote" form.
- **Target the under-served "returning to India with a dog NOC" intent.** Gov pages frame it as US-export; nobody owns the resident-returnee NOC walkthrough (DGFT ANF-2M → AQCS NOC → timelines). High-intent, low-quality competition.
- **Localize templates.** carrymypet.ae shows an India FAQ on its USA page — a per-country PawRoute template that's actually localized immediately out-quality-signals the incumbent.

---

### Tenure evidence log (Wayback / availability API)
- cdc.gov — first capture **1996-12-22** [Measured]; `/importation/dogs/` path first capture **2024-07-17** [Measured]
- aphis.usda.gov — first capture **1997-07-02** [Measured]
- inspection.canada.ca — CDX rate-limited; CFIA est. 1997 [Estimated]
- carrymypet.ae — first capture **2023-10-17** [Measured]
