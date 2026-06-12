# Regulatory Services — Governance Principles

> For regulated domains (pet relocation, immigration, visas, customs, tax, licensing) the firm
> operates like a **compliance firm, not a logistics/marketing firm**. Regulations are legal
> requirements, not opinions. This doctrine governs how the engine researches, writes, and verifies.
> Companion to `feedback_claim-verification` (memory) and the `audit/verify_claims.py` evidence system.

## The 15 principles
1. **The source is the truth.** Trust only government authorities, official agencies, legislation, regulatory databases, official notices — **and the operator's own site** (e.g. the airline). Never blogs, forums, Reddit, Facebook, competitors, or AI. *If the source is not official, it is not the source.*
2. **Always trace back to origin.** Every statement → "According to DEFRA…", "According to MOCCAE…". Never "Google says" / "a blog says".
3. **Never guess.** A wrong answer can kill an animal, cause quarantine, deportation, refusal of entry, or loss. If uncertain: **"I do not know"** → investigate.
4. **Never assume rules are universal.** UK ≠ EU. UAE ≠ Saudi. Dog ≠ cat. Every route is unique.
5. **Country-pair logic.** It's Origin **+** Destination = **four systems**: export rules · airline rules · transit rules · import rules. Not one.
6. **Airline rules matter — verify them separately.** Government approval ≠ airline approval (crate specs, brachycephalic limits, temperature embargoes, seasonal/route restrictions).
7. **Regulations change constantly.** Never "Updated 2024" forever. Track **effective date · revision date · last-verified date · version**. Every rule carries: `Source · Source URL · Date verified · Version · Reviewer`.
8. **Escalation over confidence.** Unclear cases (hybrid wolfdog, service animal, multi-country transit, rescue, commercial shipment) → escalate, don't guess.
9. **Compliance before convenience.** "Can we skip the blood test / backdate docs / reuse another pet's record?" → **No.**
10. **Document-driven decisions.** Rely on certificates, permits, licences, official records — not conversation. Undocumented = unverified.
11. **Build checklists, not memory.** Every route has an Entry / Exit / Arrival checklist.
12. **One rule per step.** Microchip → rabies → blood test → wait → permit. Not one giant paragraph.
13. **Auditability.** A regulator could ask "why did you tell the client this?" → show Source · Date · Regulation · decision path, instantly.
14. **Separate facts from advice.** Fact: "DEFRA requires X." Advice: "We recommend doing X 30 days earlier." Never mix them.
15. **Never let AI be the final authority.** AI may summarise/organise/explain. Workflow: **Official Source → Verification → Human Review → Client.** Never AI → Client.

## Golden rules
**Always:** official gov sources · verify every route individually · verify airline requirements · record verification dates · use checklists · escalate uncertainty · document every decision · separate facts from advice.
**Never:** guess · use Reddit/blogs as authority · assume countries are alike · assume rules unchanged · promise approval · skip required docs · let AI make the final compliance call · prioritise convenience over compliance.

## How the engine enforces this (status)
- ✅ **Official sources only + screenshots** — `audit/verify_claims.py` (gov/standards/operator domains; blogs rejected).
- ✅ **Never guess / hedge** — TRUTH_POLICY; un-confirmable specifics flagged "confirm with [authority]".
- ✅ **Route-specific** — page-type profiles + per-route briefs + per-route blogs (no universal assumptions).
- ✅ **Auditability** — `CLAIMS-AUDIT.md` + evidence ledgers (source, URL, date, screenshot).
- 🔜 **To add:** (A) full **verification metadata** on every regulatory claim (`Source · URL · Date verified · Version · Reviewer`) in a route **regulatory register**; (B) explicit **facts-vs-advice** separation in content; (C) **airline rules verified as a separate source** per route; (D) **escalation list** for edge cases; (E) **staleness/last-verified** tracking with re-verify dates.
