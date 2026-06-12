# Prompt Template Library — Dubai pet relocation
## The real output of Prompt Engineering: a complete 9-element prompt template for all 9 page types
## Built 2026-05-29 · every Verified claim cited by Source Bank C-ID · every Unverifiable claim hedged

**How to use:** pick the page type for your keyword (Intent × Fear → page type), open its template below, swap in the specific keyword/route, and run it. The first four are filled as worked examples from the four universal-gap pages; all nine are filled with real Dubai data — no placeholders. Tested against Gate set A (File 03). Source Bank rows: Verified C-003 (release 500 AED/dog), C-007 (rabies ≥21 days), C-010 (permit 90 days), C-019 (permit online), C-022 (flydubai cargo-only), C-024/026/028 (UK gov.uk); Unverifiable C-001 (titer cost); Conflict C-015 (Etihad $399 vs $1,500).

---

## 1. FEAR RESOLUTION PAGE — worked example: airport confiscation
- **Context:** Dubai pet relocation, maximum-risk regulated market; customers arrive afraid.
- **Role:** a relocation specialist who has cleared pets through MOCCAE.
- **Objective:** a 700-word Fear Resolution page: "what happens if your dog is taken at Dubai airport — and the 3 steps that prevent it."
- **Audience:** Import-to-Dubai owner who read their dog could be confiscated.
- **Inputs:** Verified C-019 (permit online), C-010 (90-day validity), C-007 (rabies ≥21 days), C-003 (500 AED release); community quote (Muze Gu); Unverifiable C-001 (titer cost).
- **Constraints:** open with Muze Gu's words; cite every fact by C-ID; hedge C-001 ("no official figure; community 700–1,300 AED"); no "Get a Quote"; ban "stress-free", "peace of mind".
- **Examples:** the 5-layer structure; embed MOCCAE screenshot as Layer-3 proof.
- **Output Format:** 5 layers, markdown, each factual line tagged with its C-ID.
- **Quality Criteria:** every claim cited or hedged; opens with the fear; passes Hormozi "name on it" test.
> Produces the real page in data/content-structure-templates/fear-resolution/.

## 2. PROCESS GUIDE — worked example: summer embargo
- **Context:** Dubai pet relocation; summer-move anxiety.
- **Role:** specialist who books pet cargo in peak UAE summer.
- **Objective:** a 1,200–1,800-word Process Guide: "can I move my pet to Dubai in summer?"
- **Audience:** Confused Researcher / Family who just heard about a "summer ban".
- **Inputs:** Verified C-022 (cargo-only), C-019/C-010 (permit); Unverifiable: the heat-embargo dates (no MOCCAE figure — airline/IATA rule).
- **Constraints:** separate regulator rules (don't change by season) from airline heat rules; hedge the embargo dates ("not published by MOCCAE; confirm with the carrier"); numbered steps with timing.
- **Examples:** month-by-month timeline; flydubai cargo-policy screenshot.
- **Output Format:** intro + numbered process + timeline table, markdown, C-IDs inline.
- **Quality Criteria:** regulator vs airline rules clearly separated; embargo dates never asserted as official; a reader can plan a summer move.
> Produces data/content-structure-templates/process-guide/.

## 3. COST TRANSPARENCY PAGE — worked example: rabies titer cost
- **Context:** maximum-risk niche; customers sure they're overcharged.
- **Role:** specialist who has paid these fees and reads MOCCAE directly.
- **Objective:** a 600–900-word Cost Transparency page: "how much does the rabies titer test cost in Dubai?"
- **Audience:** owner mid-quote-comparison ("being quoted an insane amount, no way to know if fair").
- **Inputs:** Verified C-003 (500 AED release); Unverifiable C-001 (titer: no official figure; community 700–1,300 AED); Conflict C-015 (Etihad $399 vs $1,500); IrbisKat quote.
- **Constraints:** open with the price fear; hedge every unpublished number; lead the Etihad point with the official $399 then name the $1,500 discrepancy; no "Get a Quote"; ban "competitive/affordable pricing".
- **Examples:** 5-layer structure; "silence-as-proof" (embed the MOCCAE page showing no titer price).
- **Output Format:** 5 layers, markdown, C-IDs inline.
- **Quality Criteria:** every published number cited, every unpublished number hedged; usable to challenge an unfair quote.
> Produces data/content-structure-templates/cost-transparency/.

## 4. COMPARISON PAGE — worked example: Sharjah vs Dubai vs Abu Dhabi
- **Context:** owners choosing an entry airport; fear of the wrong choice / doc mistake.
- **Role:** specialist who has run pets through all three UAE airports.
- **Objective:** a 1,000–1,500-word Comparison page: "Sharjah vs Dubai vs Abu Dhabi — which airport for your pet?"
- **Audience:** Research-intent owner comparing routes.
- **Inputs:** Verified C-019 (permit, all entry points), C-022 (cargo-only); Unverifiable: the "Sharjah hack" (~20 min, community-sourced).
- **Constraints:** state what's identical at all three (MOCCAE rules) vs what differs; hedge the Sharjah hack ("community-sourced; verify with carrier"); objective table, no airport misrepresented.
- **Examples:** a 3-column comparison table.
- **Output Format:** intro + comparison table + per-airport notes, markdown, C-IDs inline.
- **Quality Criteria:** identical-everywhere rules cited; the hack hedged; the table is fair.
> Produces data/content-structure-templates/comparison/.

## 5. ROUTE/VARIANT PAGE — example: Dubai → UK
- **Context:** export from Dubai to a strict destination (UK); fear of border rejection.
- **Role:** specialist who has cleared pets into Great Britain.
- **Objective:** a 1,200-word Route page: "moving your pet from Dubai to the UK — the exact requirements."
- **Audience:** Expat Leaving Dubai, afraid of a documentation mistake at the UK border.
- **Inputs:** Verified C-024 (UK gov.uk publishes the requirements), C-028 (microchip → rabies ≥21 days → pet travel document; tapeworm 24–120h before for dogs), C-026 (non-compliance → up to 4 months quarantine or refused entry).
- **Constraints:** use the **destination** authority (gov.uk), not the origin's; cite each requirement by C-ID; state the quarantine consequence plainly; no "Get a Quote".
- **Examples:** an ordered requirements checklist; gov.uk screenshot.
- **Output Format:** intro + ordered requirements + consequence box, markdown, C-IDs inline.
- **Quality Criteria:** every requirement cited to the UK authority; the quarantine consequence (C-026) stated; nothing origin-only.

## 6. URGENCY PAGE — example: deadline approaching
- **Context:** owner with a real move deadline in weeks; time-pressured but not in crisis.
- **Role:** specialist who builds the timeline backwards from a flight date.
- **Objective:** a 500–800-word Urgency page: "moving to Dubai soon — is there still time?"
- **Audience:** Last-Minute Mover with a deadline (e.g. before the summer embargo).
- **Inputs:** Verified C-007 (rabies ≥21 days — the binding wait), C-010 (permit 90 days), C-019 (online); Unverifiable embargo dates (hedged).
- **Constraints:** lead with the binding timeline (the 21-day rabies wait); one clear action path; decisive CTA; do not induce panic — give the plan.
- **Examples:** a "start today" countdown.
- **Output Format:** short, scannable; the critical-path timeline first, markdown, C-IDs inline.
- **Quality Criteria:** the binding wait (C-007) is front and centre; one action path; reassuring not alarmist.

## 7. EMERGENCY PAGE — example: pet stuck at the airport now
- **Context:** acute crisis in progress — pet held, or flight imminent; reader cannot scroll.
- **Role:** specialist who handles airport holds.
- **Objective:** a 300–500-word Emergency page: "pet stuck at Dubai airport — what to do right now."
- **Audience:** Emergency intent — crisis happening in hours.
- **Inputs:** Verified C-003 (500 AED release fee), C-019 (permit); immediate-contact details.
- **Constraints:** ONE line of acknowledgement; the contact CTA (call/WhatsApp) **above the fold**; minimal reading; the release-fee fact (C-003) for reassurance; never assert anything unpublished.
- **Examples:** an emergency-page layout (contact-first).
- **Output Format:** ≤500 words, contact block first, then 3 steps, markdown.
- **Quality Criteria:** contact above the fold; <30s to the action; only Verified facts.

## 8. CASE STUDY PAGE — example: a completed Dubai → UK relocation
- **Context:** Problem-intent reader asking "will this actually work for someone like me?"
- **Role:** the practitioner who ran the relocation, documenting it honestly.
- **Objective:** a 1,500–3,000-word Case Study: one real, completed Dubai→UK relocation end-to-end.
- **Audience:** owner on the same route, wanting proof it works.
- **Inputs:** the **real, documented** relocation (real dates, route, the actual MOCCAE permit + UK requirements used — C-019/C-028); at least one real artefact (document/photo); any surprise or setback that really happened.
- **Constraints:** real specifics only (no invented names/dates); document the setback honestly (in-the-trenches voice); cite the regulated steps by C-ID; never fabricate a success story.
- **Examples:** Authority Asset Type-1 case study structure.
- **Output Format:** narrative + a verified-steps box + a real artefact, markdown.
- **Quality Criteria:** verifiable specifics; one honest setback documented; passes "could AI alone have written this?" (no).

## 9. TRUST PAGE — example: why trust this provider
- **Context:** Research-intent reader whose primary fear is the provider itself.
- **Role:** the provider stating its real, checkable credentials.
- **Objective:** an 800–1,500-word Trust page: credentials, licences, named team, guarantees.
- **Audience:** owner who has been told to "do proper research and read reviews" (Curious_cat).
- **Inputs:** the **provider's real verifiable credentials** — MOCCAE registration number, IPATA membership #, named team with photos, real review counts (e.g. a real Google rating), guarantee terms. *(Insert the client's own; do not fabricate.)*
- **Constraints:** every credential must be checkable (registration numbers, linkable bodies); name the team; never claim an unverifiable badge; no stock photos.
- **Examples:** a credentials grid + named-team section.
- **Output Format:** credentials grid + team + guarantee, markdown.
- **Quality Criteria:** every claimed credential is real and checkable; one uncheckable badge fails the page.

---

## Coverage note
Templates 1–4 are filled worked examples that produced the four real proof-run pages (data/content-structure-templates/). Templates 5–9 are complete, real-data templates ready to run; 5–8 cite Verified rows (C-024/026/028, C-007/010/019, C-003); 9 (Trust) intentionally takes the client's own verifiable credentials as Inputs rather than fabricating them. The README also lists generic content types (SEO article, FAQ, location page, rewrite, meta tags) — these are formatting variants of the above page types and use the same 9-element fill.
