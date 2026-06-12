# E-E-A-T & Authority Checklist — the off-page layer that drives results

> Our on-page content is strong, but **on-page is necessary, not sufficient**. Real SEO/GEO results
> are driven by **trust + authority + links + local signals** — most of which are *off-page* and not
> yet built. This is the gap between a high audit score and an actual ranking/citation.
> Status for PawRoute: ✅ done · ⚠️ partial · ❌ missing. Most "results" levers are ❌ today.
> (E-E-A-T is a rater/quality framework, not a direct ranking dial — but it's how Google + AI engines
> decide who to trust. Trust is its most important component.)

## 1. Experience & Expertise — *who is behind this?*
- ❌ **Named author** on every guide (real person, photo, role) — currently "the PawRoute team" (anonymous).
- ❌ **Author bio page** with credentials + history (IPATA cert, years in pet relocation).
- ❌ **Named expert reviewer** ("Reviewed by [Name], IPATA-certified / veterinarian") — currently generic.
- ⚠️ **First-hand experience** signals (real cases, "we've moved X pets") — implied, not evidenced.
- ✅ Genuine subject depth + official sourcing (already strong).
> *Why it matters:* in a YMYL-adjacent, trust-heavy niche, anonymous content underperforms; raters and AI both look for identifiable expertise. **Highest-leverage on-page-ish fix.**

## 2. Authoritativeness — *is the brand real and recognised?*
- ❌ **About page** — real story, team, photos, physical UAE address.
- ❌ **Verifiable credentials/badges** — IPATA / IATA membership, UAE trade licence number.
- ❌ **Press / mentions / citations** from other sites.
- ⚠️ Consistent brand entity (name, logo, description) across the site — partial.

## 3. Trust — *the most important component*
- ✅ **Transparent pricing** (real ranges, no "get a quote" wall) — a genuine differentiator.
- ✅ **Honest disclaimers** + no dark patterns + "we don't guarantee dates".
- ✅ **Official-source citations** + screenshot evidence trail (regulatory register).
- ❌ **Real reviews / testimonials** with names, + `Review` / `AggregateRating` schema.
- ⚠️ **Clear contact** — WhatsApp/email present; ❌ physical address + landline + map.
- ❌ **Privacy policy / terms** pages.
- ✅ HTTPS assumed on deploy.

## 4. Local SEO — *materially affects a service business*
- ❌ **Google Business Profile** (complete, categorised, photos).
- ❌ **Consistent NAP** (Name/Address/Phone) across the site + directories.
- ❌ **Reviews on GBP** (volume + recency + responses).
- ❌ **LocalBusiness / Service schema** with address + areaServed (we emit Organization/Service — add LocalBusiness + address).
- ❌ Local citations / directory listings (UAE business directories, expat sites).

## 5. Off-page authority / link-earning — *the SEO bottleneck*
- ❌ **Backlinks** from relevant sites (the single biggest ranking lever we have none of).
- 🎯 **Digital PR with what we built**: pitch the **cost/timeline calculators**, the **decision tool**, and the **2026 cost data** to expat sites, pet blogs, UAE media — these are *designed* as link magnets.
- ❌ **Partnerships** (vets, airlines, expat/relocation communities) for links + referrals.
- ❌ **Original proprietary data** worth citing — our cost figures are a model estimate; a real annual "UAE Pet Relocation Report" (survey/operational data) would earn links + AI citations.

## 6. Technical trust signals
- ⚠️ **Core Web Vitals** — measured by proxy only; run PageSpeed Insights/CrUX on the live site (LCP ≤2.5s, INP ≤200ms, CLS ≤0.1).
- ✅ **Structured data** (Organization, Service, FAQPage, WebPage, BreadcrumbList) — validate with Rich Results Test on deploy.
- ❌ **Sitemap.xml + robots.txt** + Search Console verification + indexing.
- ✅ Mobile-responsive + accessible structure (headings/alt/contrast).

## 7. Freshness & governance
- ✅ **Visible review dates** (`dateModified` in JSON-LD + "updated June 2026").
- ⚠️ **Named reviewer** per page (see §1).
- ✅ **Re-verify-by dates** on regulatory claims (the register).
- ❌ **Update cadence** owner + schedule for when regulations change.

---

## Priority order (do these for results, in order)
1. **Deploy + index** (sitemap, robots, Search Console) — nothing ranks unindexed.
2. **Named author + expert reviewer + About page** (real E-E-A-T) — fixes the biggest credibility gap.
3. **Google Business Profile + NAP + LocalBusiness schema + first reviews** — the local-service multiplier.
4. **Link-earning push** with the calculators/tools + a real cost-data report — the off-page lever.
5. **Run the AI-citation harness** (`audit/ai_citation.py`) for a baseline, then monthly.
6. **Measure CWV** on the live site; fix anything below threshold.

## What our auditor already covers vs not
- **On-page proxies it checks:** author signal (heuristic), schema, freshness, internal links, scannability, CWV-by-weight.
- **It cannot check (off-page / live):** real backlinks, domain authority, GBP/reviews, indexing, actual CWV, real AI-citation. **Those decide results — and they live here, not in the page score.**
