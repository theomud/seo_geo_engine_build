# VISUAL EVIDENCE ARCHITECTURE
## Proof you can see on the page, beside every claim — not stock photos

---

## What This Skill Is

In a high-fear, regulated market, a claim the reader can't *see proven* is just
another website saying words. Visual Evidence Architecture is the system that puts
**visible proof next to every claim**: the official-source screenshot beside the
regulation, the real process photo instead of a stock dog, the data drawn as an
infographic the reader can scan on a phone.

It is the opposite of decoration. Every visual is evidence with a job — it lowers a
specific fear by showing, not telling. A page that says "we handle MOCCAE
documentation" converts a fraction of the page that *shows the stamped MOCCAE
certificate*. This skill specifies exactly which visuals each page needs, and builds
the reusable ones.

**Skill Value Score: 19/25**
- Difficulty: 3/5
- Automation Potential: 2/5
- Market Uniqueness: 4/5
- Commercial Value: 5/5
- Teachability: 5/5

**Status:** 🔨 Building (Dubai pet relocation, 2026-05-30)
**Niche-agnostic:** Yes — every regulated market has official sources to screenshot, a real process to photograph, and data to visualise

---

## The Four Components

1. **Official-source screenshot integration** — the regulation, fee, or rule shown
   as a dated screenshot of the official page, embedded *beside* the claim it proves.
2. **Real process photography** — what to capture and when (the crate, the vet check,
   the airport handover) so real photos replace stock. *(Stock people are ignored;
   real photos lift conversion — 37signals +102.5%.)*
3. **Data visualisation & infographics** — the summer-embargo calendar, the airport
   comparison table, the breed-restriction checker — built to render on a phone.
4. **Video documentation** — the documentation loop applied to video (capture the
   real process once, prove it forever).

---

## What It Produces

| Output | What it is |
|--------|-----------|
| Visual brief per page | Exactly which screenshots, photos, and infographics each page needs before publishing — with the proof each visual carries |
| Built infographics | The summer-embargo calendar and airport-comparison table, as real HTML that renders at 390px |
| Screenshot integration guide | How an official-source screenshot embeds beside a claim (caption, date stamp, source URL) |

---

## Functional Quality Threshold (Check 46)

This skill's real output is **proven** only when both hold:

1. **Proof-visible coverage:** every one of the four universal gap pages has a visual
   brief specifying **at least one proof-visible screenshot** (a dated official-source
   capture embedded beside a specific claim) — not a decorative image.
2. **Phone-rendered infographics:** the built infographics (summer-embargo calendar,
   airport-comparison table) **render at 390px with no horizontal scroll**, verified
   by screenshot.

Output that misses either is not done. The brief and the rendered infographics live
in `data/`.

---

## Inputs and Outputs

| Input | Source | Required |
|-------|--------|----------|
| Verified claims with official URLs | Source Bank (by C-ID) | Yes |
| The page's named fear + claims | Conversion copy / brief | Yes |
| Official-source pages to screenshot | live regulator/airline sites | Yes |
| Real process access (for photography spec) | the operator | Optional |

| Output | Format | Contains |
|--------|--------|----------|
| Visual brief (4 pages) | Markdown | per-page screenshot/photo/infographic spec + the proof each carries |
| Summer-embargo calendar | HTML | the embargo windows, sourced, 390px |
| Airport-comparison table | HTML | Sharjah vs Dubai vs Abu Dhabi, real data, 390px |
| Screenshot integration guide | Markdown | how proof embeds beside a claim |

---

## Proof

**Status:** 🔨 Building — Dubai pet relocation
**Real output (target):** a visual brief for all 4 gap pages (≥1 proof-visible
screenshot each) + the summer-embargo calendar and airport-comparison table built as
390px-rendering HTML + the screenshot integration guide.
**Anchor evidence:** the MOCCAE release-fee and Etihad-fee claims (C-003, C-015) are
the first official-source screenshots specified; the embargo and airport data drive
the two infographics.
**Skill Value Score (confirmed on completion):** 19/25.

---

## Environment Variables

```
PROJECT_ROOT=          # absolute path to the project root on this machine
```

This is a manual-first skill (Automation 2/5) — no API keys required to produce the
visual briefs or build the infographics. Screenshot capture is done by hand from the
live official sources so the date stamp is real.

---

## Standalone Test

Someone in a different regulated market (immigration, medical travel, licensing) can
use this skill alone: take their own verified claims, specify the proof-visible
screenshot beside each, photograph their real process, and build their data as
phone-rendering infographics. The method is portable; only the sources and the
process are niche-specific.
