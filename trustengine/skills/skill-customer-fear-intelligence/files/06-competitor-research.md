---
Status: specced — ready to build
Area: skill-01
Priority: high
Activation: after Files 02-05 complete
Last updated: 2026-05-27
Depends on: skill-01/files/02-intent-classification.md, skill-01/files/03-fear-formula.md
Feeds into: skill-03/content-structure.md, skill-09/conversion-copy.md
Evidence screenshots: research/competitors/screenshots/
---

# Skill 01 — File 06: Competitor Research
## Trust Score every competitor. Find every gap. Build every opportunity.

---

## Purpose

You cannot build the right content until you know exactly what already exists and
how weak it is. File 06 scores all 21 confirmed competitors on the 10-point Trust
Score, annotates what they fail at, extracts every content gap, and converts those
gaps directly into content briefs.

Every red circle on a competitor page is a page you build better.

---

## The 10-Point Trust Score

For every competitor page, answer these 10 questions. One point each.

| # | Question | Yes | No |
|---|----------|-----|----|
| 1 | Fear in first 100 words? | Opens with customer's specific worry | "Professional Pet Relocation Services" |
| 2 | Official source cited? | Links to MOCCAE, airline policy, government | Claims without citations |
| 3 | Specific route named? | "Dubai to UK" with route-specific details | "All international routes" |
| 4 | Step-by-step process? | Numbered steps with what to do and when | Generic bullet points |
| 5 | Timeline included? | "Titer test 2-3 weeks" or "permit valid 90 days" | No time references |
| 6 | Cost ranges shown? | Real numbers with honest disclaimers | "Contact us for a quote" |
| 7 | Common mistakes? | "What if my pet has a tattoo not a microchip?" | No edge cases |
| 8 | Original visuals? | Real staff, branded vehicles, actual pets | Stock photos |
| 9 | CTA feels like help? | "Download checklist" or "Talk to an expert" | "Get a Quote Now" |
| 10 | Would you trust this page? | Yes — you'd send your own pet | No — something feels off |

Score bands: 0-2 dead / 3-4 weak / 5-6 decent / 7-8 strong / 9-10 excellent

---

## Manual Research Results — 3 Scored (2026-05-27)

### Sandy Paws — sandypaws.ae — 5/10
- ✅ Fear adjacent language in tagline
- ✅ Real video testimonials from named people
- ✅ Real photos, branded van
- ✅ Cost page exists (Google Ad sitelink)
- ✅ CTA soft and human
- ❌ No official source (MOCCAE)
- ❌ No step-by-step process
- ❌ No timeline
- ❌ No common mistakes
- ❌ No specific routes named

**Your opportunity:** The document guide they cannot answer

---

### DKC — dkc.ae — 8/10
- ✅ Fear in FAQ structure throughout
- ✅ Official sources linked (import permit source)
- ✅ Routes named (GCC, transit, import/export)
- ✅ Step-by-step via FAQ format
- ✅ Timeline: import permit valid 90 days
- ✅ Cost question exists as FAQ
- ✅ Common mistakes: tattoo vs microchip, sedation, heat
- ✅ Original visuals: branded van, real staff
- ✅ CTA: playful hippo mascot, friendly tone
- ❌ Airport confiscation fear (Muze Gu scenario) never addressed
- ❌ Deepest fear missing entirely

**Your opportunity:** "What happens if your pet is rejected at the Dubai border?"

---

### Pawsome Pets UAE — pawsomepets.ae — 3/10
- ✅ MOCCAE license visible in footer (DXB-AWD-04-1625641)
- ✅ IPATA, PAN, ATA member — strongest credentials in market
- ⚠️ "Looking after your pocket" — acknowledges cost concern but no numbers
- ❌ Opens with "Request A Quote" — no fear, no process
- ❌ No step-by-step
- ❌ No timeline
- ❌ No specific routes
- ❌ No common mistakes
- ❌ CTA is a hard sales push
- ❌ Hand-drawn illustrations only — no real photos
Note: 4.8 stars, 283 Google reviews — strongest external trust. Zero internal trust.

**Your opportunity:** Explain what IPATA/MOCCAE/PAN credentials mean in plain language

---

## Automated Research — 18 Remaining Competitors

Playwright engine visits all remaining competitors automatically.
See: engines/06-competitor-research-engine.md for the Claude Code prompt.

**Remaining 18 to research:**
CarryMyPet.ae, AirPaws, MovingBay.com, Relocate MENA, 9 Lives AE,
Pet Express, Carry My Pet, Snoopy Pets, C&C Pawsome Place, Global Paws,
Fuzzy Friends Pets Services, Dagin Pets Relocation, JetSet Pets Dubai,
Blue Sky Pet Relocation, Relocate Your Pet, K9 Jets, Furry Travel,
uaeanimalcommunity

---

## Content Gap Matrix

After all 21 scored — fill this table:

Completed 2026-05-27. Denominator = **9 scored** competitors (with verifiable websites); the other 12 are social-only/unverified and not scored. Priority: HIGH ≥7 missing.

| Content Gap | Competitors Missing It | Your Priority |
|-------------|----------------------|---------------|
| Airport confiscation fear | 9/9 | HIGH |
| MOCCAE process step-by-step | 7/9 | HIGH |
| Summer embargo warning | 9/9 | HIGH |
| Titer test cost + timeline | 9/9 | HIGH |
| Breed restriction guide | 9/9 | HIGH |
| Airline comparison | 7/9 | HIGH |
| Sharjah vs Dubai vs Abu Dhabi | 9/9 | HIGH |
| Route-specific fears | 7/9 | HIGH |
| Exotic pets | 8/9 | HIGH |
| Cost transparency | 8/9 | HIGH |
| Common mistakes section | 8/9 | HIGH |
| Original visuals (not stock) | 7/9 | HIGH |

**Verdict:** every measured gap is missing from at least 7 of 9 scored competitors. The four universal (9/9) gaps — airport confiscation fear, summer embargo, titer cost+timeline, and the Sharjah/Dubai/Abu Dhabi airport comparison — are the highest-leverage pages to build first. Full data: `research/competitors/CONTENT-GAP-MATRIX.md` + `COMPETITOR-MASTER.html`.

---

## Completion Criteria

- [ ] All 21 competitors scored with Trust Score cards
- [ ] Screenshots saved to research/competitors/screenshots/
- [ ] Content gap matrix complete
- [ ] Top 10 opportunities ranked by gap × keyword volume
- [ ] Each opportunity has a one-line brief:
      "[Fear] + [Keyword] + [What you say that nobody else says]"
- [ ] Results handed to Skill 03 — Content Structure
