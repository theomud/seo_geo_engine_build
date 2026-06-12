# ENGINE — Independence Test (Check 47)
## The replication harness that flips a skill from NOT YET TESTED → TESTED
## Sub-protocol of engine-skill-auditor.md (v2.0, Check 47). Built 2026-06-01.

---

## WHY THIS EXISTS

All 14 proven skills pass 47/47 **but every one carries Check 47 = NOT YET TESTED** — only the
original builder has produced each output. Per the auditor, a skill **cannot be COMMERCIALLY READY
until Check 47 = TESTED**, and TESTED means: *a second party, working only from the skill's
documentation, independently reproduced output that meets the skill's Functional Quality Threshold.*

This engine is the repeatable way to run that test. It does **not** assert a skill is TESTED — it
**produces the evidence** that lets the flag be set honestly.

---

## THE INDEPENDENCE RULE (what makes it a real test)

A replication only counts if the replicator is genuinely independent of the build:

- **The replicator MAY read:** the skill's `README.md`, `files/01–04` + `files/06`, and
  `engines/engine-*.md` (the published documentation) — and the bounded input given in the manifest.
- **The replicator MUST NOT read:** `data/` (the existing real output), `SKILL-COMPLETION.md`,
  `SKILL-AUDIT-REPORT.md`, the customer-profile snapshot's worked answers, or any build notes. If it
  sees the answer, it isn't reproducing it.
- **The scorer is a third party** — independent of both builder and replicator — and scores the
  replicated output against the README's Functional Quality Threshold, blind to the replicator's
  self-assessment.

A pass = the replicated output **meets the threshold** and the scorer can trace each pass to evidence.

---

## THE TEST IS HUMAN (and why an agent can't substitute)

**Check 47 is satisfied by one thing only: a real second person — e.g. Greig or David — given a
skill's README and File 02 (and nothing else), producing output that meets the Functional Quality
Threshold.** That is the whole test. The flag it sets is the only valid one:

> `TESTED — human replication (name, date)`

**An agent instance is NOT a valid second party.** A fresh sub-agent shares this builder's training
and reasoning patterns; an agent reproducing another agent's output proves only that the documentation
is *machine-readable*, not that a *human* can follow it independently. So:

| | What it actually proves | Flag it sets |
|---|---|---|
| **Human replication** | a person can follow the docs to a threshold-meeting result — the real test | `TESTED — human` (the only TESTED flag) |
| **Agent pre-check** (optional) | the docs are internally complete/unambiguous enough to be parsed — a machine-readability smoke test | **none — sets no flag, does not count toward Check 47** |

A skill stays **NOT YET TESTED** until a human runs it. The optional agent pre-check (below) is only a
cheap way to catch obvious documentation holes *before* spending a human's time — it never flips the flag.

---

## THE OPTIONAL AGENT PRE-CHECK (machine-readability only — does NOT satisfy Check 47)

Before spending a person's time, you *may* run a cheap smoke test to catch obvious documentation holes.
It is not the independence test and sets no flag — treat a pass as "worth handing to a human", nothing more.

```
STEP 1 — a fresh sub-agent, given ONLY the docs (README + files/01-04,06 + engine spec) + the bounded
         input, forbidden from data/ / completion / audit docs, attempts the replication task.
STEP 2 — a second fresh sub-agent scores it against the README threshold.
VERDICT
  PASS -> the docs are at least machine-parseable. NO flag set; Check 47 STILL requires a human run.
  FAIL -> a DOCUMENTATION defect: the docs left out something the builder knew. Log exactly what was
          missing, fix the docs, and re-check — BEFORE the human pilot, so you don't waste their time.
```

The FAIL path is the whole value of the pre-check: a failure is almost never "the skill is wrong" — it
is "the documentation assumed knowledge the builder had." Fixing that is what makes the skill followable.

---

## THE HUMAN REPLICATION RUN (the actual Check 47 test)

This is the test that counts. For each skill, assemble a one-file replication packet for a human
(Greig, David, or any capable second person who did not build the skill):
1. The skill's published docs (README + files + engine spec), with `data/` and completion/audit docs **removed**.
2. The bounded input from the manifest.
3. The replication task (one paragraph: "produce X").
4. A blank score sheet = the README's Functional Quality Threshold gates, one row each, PASS/FAIL + evidence.
5. A sign-off line: name · date · result.

The human works from the packet alone; a second person (or this engine's scorer) scores it.

---

## THE 14-SKILL MANIFEST

Each row gives the **bounded replication task** (small enough to run in one pass, real enough to test
the method) and the **pass threshold** (the skill's own Functional Quality Threshold). Status starts
at NOT YET TESTED for all 14.

| # | Skill | Bounded replication task (from docs only) | Pass threshold (FQT) | Status |
|---|-------|-------------------------------------------|----------------------|--------|
| 1 | Prompt Engineering | Given one page type + a short fact set, write a 9-element prompt and generate a draft | Draft is 70%+ usable (light edits only); all 9 elements present | NOT YET TESTED |
| 2 | Content Structure for Trust | Given one fear + 3 facts, produce a page brief on the 5-layer structure | Clears all 5 layers; 100% of asserted facts cited or hedged | NOT YET TESTED |
| 3 | Website Audit | Audit **a fresh URL** (NOT dkc.ae) on the 13 dimensions | 13/13 scored with on-site quotes; gaps RICE'd; 1 brief; client-ready | NOT YET TESTED |
| 4 | Customer Fear Intelligence | Classify a fixed set of 20 keywords by intent (J) + fear (K) | 100% classified; fears open "I'm afraid", ≤30w, grounded | NOT YET TESTED |
| 5 | Editorial Judgment | Score one supplied draft page on the 10 criteria | Scores within ±4 of the hidden reference; correct publish/hold | NOT YET TESTED |
| 6 | Conversion Copy | Rewrite headline + opening + CTA for one supplied fear+fact | Voice 4+/5; editorial 40+/50; help-first CTA passes the test | NOT YET TESTED |
| 7 | AI Citation & GEO | Optimise one supplied page (answer box + FAQ schema + entity link) | 4/4 on-page GEO gates | NOT YET TESTED |
| 8 | Email Nurture | Write 2 emails of the sequence from the fear ladder | Each: named fear + ≥1 verified C-ID/hedge + help-first CTA | NOT YET TESTED |
| 9 | Trust Gap Analysis | Score 3 supplied competitor pages on the 10-point trust score | 3 scored on 10 dims w/ evidence; ≥1 gap named per page | NOT YET TESTED |
| 10 | Content Intelligence Monitoring | Run `engine-monitoring-system.py` and read the report | Report regenerates; ≥3 RICE-scored items, ≥1 regulatory | NOT YET TESTED |
| 11 | Official Source Research | Verify 5 supplied claims against live official sources + screenshot | 100% with C-ID + URL + date; Verified rows screenshot-backed | NOT YET TESTED |
| 12 | Visual Evidence Architecture | Produce a visual brief for one supplied page | ≥1 proof-visible screenshot spec; infographic renders at 390px | NOT YET TESTED |
| 13 | Authority Asset Creation | Document one supplied real mini-case as a case study | Proof density ≥1 verifiable item / 200 words; Hormozi test passes | NOT YET TESTED |
| 14 | Content Architecture | Produce a sitemap for a supplied 12-page set + run `validate()` | ≤3 clicks · 0 orphans · 100% URL-consistent | NOT YET TESTED |

**Bounded inputs** (the fixed test inputs) live in `data/independence-inputs/` per skill, added when the
pass is run, so every replicator gets the identical, builder-blind input.

---

## RECOMMENDED ORDER (highest commercial value first)

Run the pass in this order so the most sellable skills are validated first:
**Website Audit → Conversion Copy → AI Citation → Prompt Engineering → Editorial Judgment →
Authority Assets → Trust Gap Analysis →** then the remaining seven.

Pilot one skill first with a real person (recommended: Website Audit — the lead deliverable): hand
them the packet, let them work from it alone, score the result, review, then proceed to the rest.

---

## HOW STATUS IS RECORDED (so the system stays honest)

On a human PASS, update three places:
1. This manifest (status → `TESTED — human (name, date)`).
2. The skill's `SKILL-AUDIT-REPORT.md` Check-47 line.
3. `SYSTEM-AUDIT-REPORT.md` (the Check-47 column) and `SKILL-COMPLETE-LIST.md` commercial-ready status.

A skill flips to **COMMERCIALLY READY** only when its Check 47 = `TESTED — human`. The optional agent
pre-check never changes status — at most it records "docs pre-checked (date)" as a build note.

---

## STATUS (this engine)

**Spec complete; not yet run — and it is not run by an agent.** Setup is ready: the protocol, the
independence rule, the human packet, the optional agent pre-check, and the 14-skill manifest are
defined. **The test itself is run by a real second person (Greig/David), not in this session** — that
is the point of an independence test. Next action (human, offline): hand the pilot skill's packet
(Website Audit recommended) to a capable person who didn't build it, let them work from it alone,
score the result, record the verdict here. No skill's Check 47 has been flipped — all 14 remain
NOT YET TESTED until a human pass runs.

## Library codes
P-07 Independent Verification · P-12 Each Skill Stands Alone (the docs must be self-sufficient) ·
P-01 Manual Before Automated · F-11 Forty-Five/Forty-Seven-Check Audit · P-13 Hormozi Test. Full
citations in `MFP-LIBRARY.md`.
