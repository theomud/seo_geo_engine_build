# PawRoute GEO Content Audit — 2026-06-09

Applying the 5-signal GEO scoring model (Answerability, Citation potential, Trust chain, Entity density, Expertise) and the GEO pyramid (regulations → +explained → +examples → +company experience → +proprietary data → +case studies/outcomes) to a representative sample of real PawRoute content.

**Pages sampled**
1. `sites/pawroute/pages/destinations/uae-to-france.yml`
2. `sites/pawroute/pages/destinations/uae-to-uk.yml`
3. `sites/pawroute/pages/blog/pet-taken-at-airport-dubai.yml`
4. `sites/pawroute/pages/blog/dubai-to-eu-pet-rules.yml`
5. `sites/pawroute/content/blogs-to-dubai/pakistan-to-dubai.json`
6. `sites/pawroute/content/blogs-to-dubai/india-to-dubai.json`
7. `sites/pawroute/content/blogs-to-dubai/uk-to-dubai.json`

**Truth policy applied throughout:** No recommendation below asks for an invented statistic, count, success rate, or outcome. Gemini's "47 relocations / 4.2 days" examples are explicitly treated as fabricated illustrations and are NOT carried into the recommendations. Every suggested improvement is achievable from (a) facts already screenshot-verified in the `sourcing` blocks, or (b) genuinely-held process knowledge the team can attest to.

Scoring scale: 0–10 per signal. Pyramid rung is the highest rung the page genuinely reaches.

---

## Page 1 — `destinations/uae-to-france.yml`

| Signal | Score | Evidence / reasoning |
|---|---|---|
| Answerability | 9 | `key_facts.answer` is a clean, self-contained extractable answer; hero card + stats give structured timeline/cost/quarantine/titre. Strong for "Dubai to France pet" queries. |
| Citation potential | 7 | Quotable lines ("no quarantine when paperwork is right", titre 30-days-after / 90-days-before). But several figures are hedged ranges (AED 13,800–18,000) with no attributed basis, weakening verbatim citation. |
| Trust chain | 8 | Named authorities present and linked: European Commission, MOCCAE, IATA, each with a deep URL and a note. `source_authority: European Commission` + `verified: June 2026`. Chain is page→authority→regulation. |
| Entity density | 8 | UAE, France, EU framework, MOCCAE, IATA, rabies, titre test, microchip (ISO 11784/11785), EU animal health certificate, Germany/Netherlands all connected. Missing: Emirates/airline entity, specific EU regulation name (Annex I). |
| Expertise | 6 | Shows sequencing knowledge (chip before rabies), the titre-timing trap, "we confirm listed/non-listed status." Real know-how, but stated as generic best practice, not anchored to PawRoute's own observed cases. |

**Pyramid rung:** *+examples* (regulations + explained + the titre-trap example/story-style callout). Reaches toward *+company experience* via "we confirm…" language but doesn't substantiate it.

**Gap to elite:** No first-party signal. Missing: (a) the precise EU regulation citation the EC page rests on (Reg. (EU) 576/2013 / Annex I listing) to harden the trust chain to traceable-regulation level; (b) any attestable PawRoute process detail (e.g. "we time the EU certificate inside its 10-day entry window backwards from the cargo booking" — already true and stated elsewhere on-site); (c) a named, dated verification of UAE's current listed/non-listed status rather than "we confirm." All achievable truthfully.

---

## Page 2 — `destinations/uae-to-uk.yml`

| Signal | Score | Evidence / reasoning |
|---|---|---|
| Answerability | 10 | Best in sample. `key_facts.answer` directly answers cost (dog vs cat split), timeline, quarantine, the tapeworm gotcha. Hero card, stats, cost-breakdown table, airline table — highly extractable. |
| Citation potential | 9 | Many crisp, attributable claims: tapeworm 1–5 days before arrival; XL Bully banned since 1 Feb 2024; Dangerous Dogs Act 1991 breeds; APHA-approved-vet requirement with named vets (DKC, British Vet Hospital). Line-item cost table is quotable. |
| Trust chain | 9 | Strongest chain: GOV.UK (3 distinct deep links incl. tapeworm + XL Bully), MOCCAE, IATA. Named Act (Dangerous Dogs Act 1991), named regulator (APHA). Page→authority→named law is traceable. |
| Entity density | 9 | UAE, UK, APHA, GOV.UK, MOCCAE, IATA, Emirates/BA/Qatar/Virgin, tapeworm, XL Bully, Pit Bull/Tosa/Dogo/Fila, microchip, rabies — densely interconnected. |
| Expertise | 7 | Real differentiation: which Dubai vets are actually on the APHA list, "wrong paperwork can add AED 5,000+," cost line-items competitors hide. This is genuine company knowledge. Could go further with attestable process specifics. |

**Pyramid rung:** *+company experience* (regulations + explained + examples + named-vet / cost-line knowledge that a government page does not provide). The APHA-vet shortlist and cost breakdown are real expertise rungs.

**Gap to elite:** The two elite rungs (proprietary data, case-study outcomes) are absent — and must stay truthful. Do NOT invent counts. Achievable upgrades: (a) frame the APHA-vet list and tapeworm-window coordination as an explicit, dated "how we do it" method block (process IP, attestable); (b) cite the underlying APHA/Pet Travel legal instrument behind GOV.UK to deepen traceability; (c) date-stamp the AED cost ranges as "as observed June 2026" so they read as first-party pricing data rather than guesses. No fabricated success metric needed.

---

## Page 3 — `blog/pet-taken-at-airport-dubai.yml`

| Signal | Score | Evidence / reasoning |
|---|---|---|
| Answerability | 9 | `key_facts.answer` ("almost never simply taken… nearly always one preventable paperwork problem") is a strong, direct, extractable answer to a high-anxiety query. Stats grid reinforces. |
| Citation potential | 6 | Reassurance-led prose is persuasive but soft for citation — many statements are qualitative ("almost never," "nearly always," "the rare worst case"). The 5-cause checklist is the most quotable element. No hard, attributable figures (correctly, given truth policy). |
| Trust chain | 6 | Sources present (EC, MOCCAE, IATA) but `source_authority` is a vague composite ("the European Commission, IATA and MOCCAE"). Claims like "five known causes" aren't traced to a specific rule — they're framework, not regulation. |
| Entity density | 7 | Rabies titre, microchip/rabies sequence, health certificate, breed/crate, import permit, EC/IATA/MOCCAE, Australia/South Africa/EU as strict-route examples. Good, but the entities are illustrative rather than route-locked. |
| Expertise | 8 | This page IS the expertise layer: the reframe ("the airport is where the outcome is revealed, not decided"), the five-cause taxonomy, the in-good-faith failure pattern. This is what a relocator knows that GOV/MOCCAE never explains. The `story` block is original. |

**Pyramid rung:** *+company experience* (the five-cause taxonomy + "reveal not decide" reframe is held expertise beyond any regulation). The `story` is a constructed-scenario *example*, not a real outcome — so it does not reach case-study rung.

**Gap to elite:** The page leans on qualitative reassurance where an AI engine wants attributable specificity. Truthful upgrades: (a) tie each of the five causes to its governing rule/source (cause → EC titre rule, cause → APHA sequence, etc.) so the taxonomy becomes citable; (b) label the scenario explicitly as a representative/composite scenario (it already says "A common scenario") and, where genuinely true, add the *mechanism* detail the team can attest to (e.g. exactly where in the export check the titre gap surfaces). No invented confiscation rate.

---

## Page 4 — `blog/dubai-to-eu-pet-rules.yml`

| Signal | Score | Evidence / reasoning |
|---|---|---|
| Answerability | 9 | "Short answer" prose + key takeaways are tightly extractable; the titre timing (≥30 days after vaccine, ≥90 days before certificate) and certificate validity (10 days entry / 6 months onward) are precise, answerable facts. |
| Citation potential | 8 | Strongest citation material in the blog set: specific numeric windows, Annex I reference, certificate validity periods. These are verbatim-quotable and attributable to the EC. |
| Trust chain | 8 | EC (deep link), MOCCAE, IATA. Names Annex I to the EU pet-movement regulation as the deciding instrument — good traceability, just stops short of naming Reg. (EU) 576/2013 explicitly. |
| Entity density | 8 | UAE listing status, EU framework, Germany/France/Netherlands, microchip, rabies, titre, EU animal health certificate, Annex I. Cohesive. Missing airline/Emirates and MOCCAE-side specifics. |
| Expertise | 7 | "Sequence beats speed," certificate timed backwards from flight, the listed/non-listed decision as the master variable — genuine explanatory expertise. Story block is a constructed example. |

**Pyramid rung:** *+examples* / edging into *+company experience* (regulation + thorough explanation + the certificate-timing trap example + "sequence beats speed" method framing). Not yet substantiated company-experience because no attestable first-party method/data anchors it.

**Gap to elite:** Closest blog to citable authority but still no first-party layer. Truthful upgrades: (a) name the actual regulation (Reg. (EU) 576/2013 + Annex I) behind the EC page; (b) state, as dated fact, whether the team has confirmed the UAE's current listed/non-listed status (this is knowable and verifiable today — resolves the page's central open variable instead of deferring it); (c) convert "we time the certificate backwards from the flight" into an explicit, attestable method step. No fabricated timelines.

---

## Page 5 — `content/blogs-to-dubai/pakistan-to-dubai.json`

| Signal | Score | Evidence / reasoning |
|---|---|---|
| Answerability | 8 | `key_facts.answer` is clean and direct (microchip, rabies, export health cert, MOCCAE permit, no quarantine if compliant). FAQ answers are tight. |
| Citation potential | 6 | UAE-side facts are citable (permit, no quarantine). But the Pakistan export side is deliberately, heavily hedged ("should be confirmed," "we verify per case") — correct under truth policy, but low for quotable specifics. |
| Trust chain | 7 | MOCCAE, Emirates, IATA linked. UAE side is screenshot-verified (`sourcing.verified_100pct` is excellent — permit 90d, fees, titre high-risk-only, 2-pet limit). Pakistan authority not named/linked, so the origin chain is incomplete. |
| Entity density | 6 | UAE, MOCCAE, Pakistan, Emirates, IATA, rabies, microchip, import permit present — but Pakistan-side entities (the actual quarantine/veterinary authority) are unnamed, leaving the corridor half-connected. |
| Expertise | 6 | Honest "least verified origin detail, most hedged" framing is itself a trust signal. The `sourcing` block shows deep verified MOCCAE knowledge, but that detail is in metadata, not surfaced in the rendered content. |

**Pyramid rung:** *+explained* on the Pakistan side (regulations, lightly explained, heavily hedged); reaches *+company experience* on the UAE side via the verified MOCCAE detail — but that detail lives in `sourcing` metadata, not on the page.

**Gap to elite:** Two concrete, truthful gaps. (1) **The verified MOCCAE facts in `sourcing.verified_100pct` are not surfaced in the visible content** — permit valid 90 days, AED 200 permit / AED 500 dog / AED 250 cat release fees, max 2 pets/person/year, titre only from high-risk countries, parasite doses within 14 days. These are screenshot-verified TODAY and would massively raise answerability + citation. (2) Name the Pakistan animal-quarantine/veterinary authority and link it once confirmed. No invention required — fact (1) is just promotion of already-verified data.

---

## Page 6 — `content/blogs-to-dubai/india-to-dubai.json`

| Signal | Score | Evidence / reasoning |
|---|---|---|
| Answerability | 8 | Clear answer naming the AQCS NOC + MOCCAE permit two-permit structure; FAQ on timing is direct. |
| Citation potential | 7 | Better than Pakistan: names a specific origin instrument (AQCS export NOC) and authority. UAE side citable. NOC lead-time left unquantified (correctly — unverified). |
| Trust chain | 8 | India AQCS (named + linked, aqcsindia.gov.in), MOCCAE, Emirates, IATA. Both ends of the corridor have a named authority — better than Pakistan. UAE side screenshot-verified. |
| Entity density | 8 | UAE, India, AQCS, NOC, MOCCAE, Emirates, IATA, rabies, microchip, import permit — both origin and destination entities present and connected by the "two permits, separate clocks" relationship. |
| Expertise | 7 | The "two permits with separate clocks, start both first" insight is genuine, route-specific expertise. As with Pakistan, the verified MOCCAE detail is buried in `sourcing`, not rendered. |

**Pyramid rung:** *+company experience* (regulation + explained + the two-permit-alignment insight). Held back from elite by the same buried-data issue.

**Gap to elite:** Same dominant gap as Page 5 — the screenshot-verified MOCCAE specifics (90-day permit, fees, 2-pet cap, titre high-risk-only, parasite-dose window) are in metadata but absent from the page. Surface them. Additionally, confirm + state the AQCS NOC lead time once verified (flagged as unverified today — do NOT estimate it). No fabricated figures.

---

## Page 7 — `content/blogs-to-dubai/uk-to-dubai.json`

| Signal | Score | Evidence / reasoning |
|---|---|---|
| Answerability | 9 | Strong, direct answer (microchip, rabies, UK export cert, MOCCAE permit, no quarantine). Three prose sections cover both ends + flight method cleanly. |
| Citation potential | 7 | UK side ("rabies-free country, usually straightforward") + Emirates 17h baggage/cargo rule are citable and verified. Breed restriction kept appropriately general. |
| Trust chain | 8 | GOV.UK, MOCCAE, Emirates, IATA all linked; multiple screenshot-verified facts including the gov.uk rabies-21-day evidence. `truth_rule` explicitly stated in `_meta`. |
| Entity density | 8 | UAE, UK, GOV.UK, MOCCAE, Emirates, IATA, rabies, microchip, export cert, restricted breeds, cabin/baggage/cargo — well connected. |
| Expertise | 7 | "Your end is the easy part — the UAE permit + breed check is the bit to get right" is genuine corridor-direction expertise. Verified MOCCAE detail again sits in `sourcing` only. |

**Pyramid rung:** *+company experience* (regulation + explained + the corridor-direction insight + Emirates flight-method specifics). Same ceiling as the other inbound JSONs.

**Gap to elite:** Identical dominant gap — verified MOCCAE specifics (permit 90d, fees, 2-pet cap, titre high-risk-only, parasite window) are in `sourcing.verified_100pct` but not on the page. Surface them. Also resolve the two `stated_but_unverified` UAE items (exact rabies window / whether a titre is needed from the UK; restricted-breed list) against MOCCAE and state them as dated fact rather than "confirm with MOCCAE." No invention.

---

## Synthesis

### Where the pages sit on the pyramid

| Page | Rung | Notes |
|---|---|---|
| uae-to-uk.yml | **+company experience** (highest) | APHA-vet shortlist + cost line-items = real held knowledge |
| pet-taken-at-airport-dubai.yml | +company experience | 5-cause taxonomy + reframe, but qualitative |
| india-to-dubai.json | +company experience | two-permit insight; verified data buried |
| uk-to-dubai.json | +company experience | corridor insight; verified data buried |
| uae-to-france.yml | +examples (→company) | titre-trap example, "we confirm" not substantiated |
| dubai-to-eu-pet-rules.yml | +examples (→company) | precise EU windows; no first-party anchor |
| pakistan-to-dubai.json | +explained (origin) / +company (UAE, but buried) | most hedged; verified MOCCAE data not surfaced |

**No page reaches the two elite rungs (proprietary data / case-study outcomes).** Crucially, under the truth policy the team should NOT try to reach them by inventing counts or success rates. The realistic ceiling these pages can honestly hit is a *substantiated* +company-experience rung: dated, attestable process method + already-verified first-party regulatory data.

### The common gap across all pages

Two threads, one root:
1. **First-party / proprietary layer is absent or unsubstantiated.** "We confirm," "we verify per case," "we handle both" assert experience without anchoring it. The pyramid's company-experience rung is claimed, not evidenced.
2. **The richest verified data PawRoute already owns is buried in `sourcing` metadata, not in the rendered content.** Every inbound JSON carries a screenshot-verified MOCCAE block (permit valid 90 days; microchip matching cert; rabies ≥21 days; titre only from high-risk countries ≥0.5 IU/ml valid 365d; min age 12wk/15wk; parasite doses within 14 days; max 2 pets/person/year; fees AED 200 permit + AED 500 dog / AED 250 cat release; no quarantine if compliant). None of that precise, attributable, dated detail appears in the visible answer/FAQ/checklist where an AI engine can extract and cite it.

### The single highest-leverage GEO improvement

**Surface the already-verified, screenshot-backed MOCCAE specifics into the visible content of every UAE-import page, presented as dated, source-attributed first-party facts.**

This one move, applied across pages, simultaneously lifts all five signals without inventing anything:
- **Answerability** ↑ — turns "arrange a MOCCAE permit" into "MOCCAE import permit, valid 90 days, AED 200 fee, max 2 pets per person per year" — a precise extractable answer.
- **Citation potential** ↑ — exact numbers + named authority + verification date are exactly what generative engines quote and attribute.
- **Trust chain** ↑ — page → MOCCAE (with the deep link already present) → specific fee/validity rule becomes fully traceable.
- **Entity density** ↑ — connects MOCCAE, UAE, permit, rabies, titre, microchip with concrete numeric relationships.
- **Expertise** ↑ — demonstrates the operator knows the exact fee schedule, pet-count cap, and titre logic that the casual reader and most competitors don't surface.

It is pure truth-policy-safe leverage: the data is already gathered and evidenced (`audit/evidence/uae-import-export/moccae-pets-full.png`, as-of 2026-06-09). The work is presentation (promote metadata → content + add a visible "verified June 2026 against MOCCAE" stamp), not research, and definitely not fabrication.

**Second-order fix (cross-cutting):** Name the underlying legal instruments the linked authority pages rest on — Reg. (EU) 576/2013 + Annex I for EU routes; Dangerous Dogs Act 1991 (already done on UK route) and APHA Pet Travel rules for UK; Federal Law 22/2016 for UAE breed rules. This hardens every trust chain from page→authority to page→authority→named regulation, the level generative engines treat as most authoritative. All are real, citable instruments — no invention.
