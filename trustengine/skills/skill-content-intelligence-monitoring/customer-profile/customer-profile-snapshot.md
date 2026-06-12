# Customer Profile Snapshot — Content Intelligence Monitoring
## Only the excerpts needed to decide what to monitor and how to score it
## Full profile: ../../customer-profile/01-master-customer-profile.md

---

## Why this matters for monitoring

This customer makes a **high-stakes, time-boxed decision under fear**: they are moving a pet
internationally, the rules are unforgiving, and a single wrong fact — an out-of-date fee, a lapsed
permit window, a missed airline embargo — can mean their pet is denied entry or held at the border.
They are *"researching regulations"* in a *"confusion → clarity"* state, and they trust whatever
source looks most current and most specific. That is exactly why monitoring is a YMYL obligation
here, not hygiene: the moment a published fact decays, the most-prepared provider is now handing the
customer a landmine. The profile tells us three things the monitor needs: **which facts decay (and
how badly being wrong hurts), which fears recur (so community signals are scoreable), and where the
competitors leave gaps (so content signals are real opportunities).**

---

## The facts that decay → what to monitor, and the Impact of being wrong

Every figure below is a monitored signal: it has a verified source (a C-ID) and a half-life. When
the re-verification clock runs out (P-08, 90 days) or a stream detects a change, it re-enters the
queue — and its **Impact** is set by how badly being wrong hurts the pet or the customer's money
(P-02). This table is the calibration key for the regulatory and search streams.

| Fact | Status | Impact if wrong | Stream |
|------|--------|-----------------|--------|
| Import permit applied for online before travel | Verified (C-019) | 3 — pet denied entry | 1 (MOCCAE) |
| Import permit valid **90 days** | Verified (C-010) | 3 — travel outside window = refused | 1, 3 |
| Rabies vaccination valid ≥**21 days** after first dose | Verified (C-007) | 3 — refused at border | 1, 2 |
| Held-pet release fee **500 AED/dog** (250/cat) | Verified (C-003) | 2 — unexpected cost / distress | 1 |
| Etihad fee **USD 399** official vs **~USD 1,500** community | Verified conflict (C-015) | 2 — price shock | 7 |
| flydubai **cargo-only** (no cabin) | Verified (C-022) | 2 — wrong booking | 3 |
| Rabies titer price | **No official figure** (C-001); community 700–1,300 AED | 1 — but honesty is the asset | 7, 10 |
| Summer heat-embargo window (airline-set, ≈Jun–Sep) | No single official date | 3 — timeline failure | 3 |

The pattern: **regulatory facts carry Impact 3** (real harm) and run on the fastest cadence;
cost/booking facts carry Impact 2; the honest "no official figure" carries low Impact but high value
because disclosing it is itself a trust signal.

---

## The fears that recur → why community signals are scoreable

The profile's fear inventory (Column K) is what makes a community thread a *signal* and not noise:
when Reddit or a Facebook group surfaces one of these, it's a confirmed live fear, so its Confidence
is real (~0.8 — community pattern, not official). The recurring ones the monitor watches:

| Fear | Verbatim community signal | Stream |
|------|---------------------------|--------|
| Price gouging on the titer / process | *"being quoted endless amounts"* — 7Ssisi; *"shamelessly charging an insane amount"* — IrbisKat | 10 |
| Being exploited in a crisis | *"took advantage of the desperate circumstances"* — unnnabear (Etihad fee) | 7, 10 |
| Confiscation at the airport | the deepest fear in the market — paperwork-incomplete hold | 5, 10 |
| Breed rejection | BSH rejected by Emirates (a confirmed real case) | 10 |

Community-only signals are **capped at ~0.8 Confidence** (P-07) — loud doesn't mean verified — but a
recurring, quoted pattern is a genuine signal worth scoring.

---

## Where the competitors leave gaps → why content signals are real opportunities

The content-gap matrix (9 scored competitors) is the source for the competitor and content streams.
The gaps that recur as signals:

- **Confiscation page** — missing on 9/9, *including the market leader DKC (Trust Score 8.0/10)*.
  The deepest fear, unanswered by anyone → a high-RICE content signal (stream 6).
- **AI-citation gap** — 9/9 omit citeable answers to the four universal gap queries → the
  AI-citation stream (9) scores publishing the GEO pages as a real opportunity.
- **Breed-restriction guide** — missing on 9/9, but lower urgency → a genuine but deferable signal
  that correctly lands in the monthly cycle (RICE 3.15).

A gap on 9/9 competitors is what makes a content signal a real opportunity rather than a guess — the
Reach and Confidence are evidenced by the matrix, not assumed.

---

## How to use this snapshot

Scoring a new signal: find the fact or fear it touches in the tables above → its **Impact** comes
from the harm column (3 = real harm), its **Confidence** from the source type (official C-ID ~1.0;
community pattern ~0.8; single report ~0.5), its **Reach** from how many customers/pages it affects
(the gap matrix evidences this for content signals). Then `(R × I × C) ÷ E` and `route()`. Everything
else in the master profile is unnecessary for this skill.
