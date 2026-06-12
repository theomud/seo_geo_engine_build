# Fact-check — Gemini's Pakistan→UAE claims (2026-06-09)

Source: Gemini analysis of the Pakistan→Dubai pet-relocation page.
Scored against our screenshot-verified MOCCAE data (`sites/pawroute/content/blogs-to-dubai/pakistan-to-dubai.json`,
evidence verified 2026-06-09) and the [truth policy](../../GOVERNANCE/TRUTH_POLICY.md).

**These are facts, not bets — resolved now.** Verdicts: ✅ correct · ❌ incorrect · ◐ partial · ⚠️ unverified (→ claim-audit).

| # | Gemini's claim | Our verified data | Verdict |
|---|---|---|---|
| F01 | Import permit **200 AED/head** | AED 200 permit (screenshot-verified) | ✅ correct |
| F02 | Permit valid **90 days**, must precede travel | valid 90 days | ✅ correct |
| F03 | Titer **≥0.5 IU/ml**, valid **365 days** | ≥0.5 IU/ml, valid 365d | ✅ correct |
| F04 | Rabies **≥21 days** before travel | rabies ≥21 days (first/lapsed; none for valid booster) | ✅ correct (Gemini omits the booster nuance) |
| F05 | Max **2 pets/person/year** | max 2 pets/person/year | ✅ correct |
| F06 | Min age **≥12 weeks** | **15 weeks (high-risk origin)**; 12wk is low-risk only | ❌ **incorrect** — Pakistan is high-risk → 15wk |
| F07 | **Manifested Cargo only; cannot travel as checked baggage** | Emirates: **checked baggage on journeys <17h** OR cargo | ❌ **incorrect / conflicts verified evidence** |
| F08 | Titer release fee **500 AED** | AED **500/dog & 250/cat** release | ◐ partial — right for dogs, omits the cat rate |
| F09 | **Immediate deportation** if no valid titer | not asserted by us; consequence unverified | ⚠️ unverified → claim-audit (do NOT publish) |
| F10 | Banned breeds via **Federal Law 22/2016** (Pit Bull, Am Staff, Tosa, Fila, Dogo, Mastiff) | our banned-breed list is "still to confirm" | ⚠️ unverified lead → claim-audit (promising, screenshot before use) |

## Tally (checkable items only: F01–F08)

- **Correct:** 5 (F01–F05)
- **Incorrect:** 2 (F06 min-age, F07 cabin/baggage)
- **Partial:** 1 (F08)
- **Unverified (not scored):** F09, F10 → routed to claim-audit.

**Accuracy on checkable claims ≈ 5.5 / 8 (69%).** Genuinely strong on MOCCAE specifics — but the
two misses (F06, F07) are exactly the kind of confident error that would have shipped a falsehood
without the screenshot firewall. **Net lesson: Gemini is a high-value *lead generator* for facts,
not a *source of record*. Every figure still goes through the official-source screenshot.**

## Actions

- [ ] F09, F10 → add to `audit/` claim-audit queue; screenshot the official MOCCAE/Federal-Law source before any use.
- [ ] If F10 verifies, it fills the known gap ("UAE specific banned-breed list" — flagged across all to-Dubai content).
- [ ] Do not change F06/F07 in our copy — our data is already correct; Gemini's version is the error.
