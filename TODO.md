# BridgeWorks To-Do List
*Last updated: 2026-04-26*

## Completed

### CEE FM Site Fixes
- [x] Fix stats counter bug
- [x] Fix schema data (ratingCount 50, removed Romania/Slovakia)
- [x] Fix llms.txt (50+ projects, Hungary only)
- [ ] Add visible phone number with click-to-call — ON HOLD (owners prefer no personal line)

### BridgeWorks Launch Content
- [x] Blog: GEO explainer
- [x] Blog: SEO vs GEO comparison
- [x] Blog: CEE FM case study (real audit data)
- [x] Build /geo-audit lead magnet page on bridgeworks.agency
- [x] Update homepage FreeAudit CTA to link to /geo-audit
- [x] Fix false "competitor comparison" claim across all audit references
- [x] Add competitive analysis upsell hook on /geo-audit page

### CEE FM Apr Delivery (Weeks 1-4 of 16)
- [x] Brand visual design package — cancelled by client (Apr 12, EUR 625 declined)
- [x] Solar add-on pitch — declined by Victor (Apr 16, EUR 550, do not re-pitch)
- [x] April content calendar published: 12/12 posts (Apr 1-24)
- [x] Brand visual ad-samples produced (4 ads + 4 final HU/EN videos + VO audio)
- [x] AI visibility 16/100 → 82/100 (per Sat Apr 25 BridgeWorks post)
- [x] Week 1 diagnosis, Week 2 system layer, Week 3 content arch, Week 4 handover docs

### Launch Prep (drafted; launch postponed from Apr 18)
- [x] LinkedIn countdown sequence drafted (16 posts in personal-brand-workspace)
- [x] The Bridge Issue 002 newsletter drafted
- [x] Sunday auto-refresh routine scheduled (trig_01HPBodf1RzMLpyWsmQXisze, runs Sun 18:00 Budapest)

---

## This Week (Mon Apr 27 - Sun May 3) — Week 5/16 of CEE FM, Backend Build Week 2

### BridgeWorks backend (the launch blocker)
- [ ] Invoicing template via szamlazz.hu (NAV-compliant, EN+HU)
- [ ] VAT handling for EU clients (HU + reverse charge logic)
- [ ] Contract template EN/HU + signing flow
- [ ] Onboarding doc / week-1 client handbook
- [ ] Payment flow for NGN clients (avoid 4% card fee)

### CEE FM (Week 5/16 — Foundation-first, ads deferred)
Strategic decision (Apr): defer paid ads + cold outreach until content/GEO/SEO foundation is solid. Current GEO score 47/100 (target 70+). Working from GEO-AUDIT-REPORT.md 30-day action plan, not proposal Phase 3 ad work.

**This week (GEO 30-day Week 1: Truth & Trust):**
- [ ] **URGENT: Draft CEE FM May content calendar** (12 posts, first Tue May 5)
- [ ] Add Hungarian legal imprint to footer (Cégjegyzékszám 13-09-227045, Adószám 22734015-2-13, registered seat 2724 Újlengyel Petőfi Sándor utca 48). Fulfils GEO audit Critical Issue #2 + Quick Win #2. **Confirm with Victor whether to also publish a Budapest telephely.**
- [ ] Fix founding year in llms.txt + schema + homepage stat: 2010 not 2012 (~15 years, not 12+)
- [ ] Audit "50+" claims in content/llms.txt — clarify as projects/properties not employees (actual headcount: 8)
- [x] Replace JS stat counters with server-rendered text (50+, 95%, 12+) — done Apr
- [ ] Surface EU Ecolabel cert block on homepage with logo + cert number
- [ ] Replace LocalBusiness JSON-LD with full ProfessionalService block per GEO audit Appendix A
- [ ] Add security headers via public/_headers (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy)

### BridgeWorks site
- [ ] Add client logo bar to homepage (Limehome anchor + anonymized references)
- [ ] Set up The Bridge Issue 002 in Beehiiv (overdue from launch week)

### Content this week (per CONTENT-WEEK-2026-04-27.md)
- [ ] Personal LinkedIn x4 (Mon, Wed, Fri, Sun)
- [ ] BridgeWorks LinkedIn x2 (Thu method, Sat results)
- [ ] Twitter/X x3 (Mon, Wed, Fri)
- [ ] Generate visuals via /generate-social-visual

---

## Backlog

### CEE FM 16-week Roadmap (re-sequenced; ads deferred until foundation ready)
Original proposal CEEFM-PROP-001 had ads + outreach launching Wk 1-4. Joint decision with Victor: invest Wk 5-8 in foundation per GEO audit, then run ads on a converting site Wk 9-12.

**Wk 5 (GEO 30-day Wk 1) — Truth & Trust Foundations:**
- [ ] Hungarian legal imprint live (céginformáció from Victor)
- [ ] Complete ProfessionalService JSON-LD per GEO audit Appendix A
- [ ] EU Ecolabel surfaced on homepage with logo + cert number
- [ ] Security headers added via public/_headers
- [ ] May calendar published for CEE FM (12 posts)

**Wk 6 (GEO 30-day Wk 2) — Entity & Platform Signals:**
- [ ] Google Business Profile claimed, 10+ photos, services, hours
- [ ] LinkedIn company page completion (description, banner, services, founding posts)
- [ ] Wikidata item created for CEEFM Kft
- [ ] List on IFMA Hungary, Budapest Chamber of Commerce, facility-management.hu
- [ ] Bing Webmaster Tools verified, IndexNow key file, sitemap submitted
- [ ] llms.txt updated with Limehome metrics + Hungarian section + /llms-full.txt published

**Wk 7 (GEO 30-day Wk 3) — Content Breadth & Case Studies:**
- [ ] /case-studies/limehome dated full page with metrics
- [ ] 3 additional case studies from existing 50+ projects
- [ ] Single-page site split into 6 dedicated service pages
- [ ] /about page with named leadership, photos, credentials, bios
- [ ] FAQPage JSON-LD wrapping existing FAQ
- [ ] Replace Unsplash stock with real CEEFM photography

**Wk 8 (GEO 30-day Wk 4) — Topical Authority & Freshness:**
- [ ] /insights launched with 4 pillar articles (HU FM compliance, hotel turnover SOPs, apartment maintenance, green cleaning)
- [ ] Sitemap lastmod dates via @astrojs/sitemap config
- [ ] HU translations for all new pages via scripts/translate.mjs
- [ ] First monthly operations note on LinkedIn linking to a dedicated site page
- [ ] **Re-run GEO audit. Target: 70+/100 (from 47).** Decision gate: if score < 65, extend foundation work by 2 weeks. If 65+, proceed to ads.

**Wk 9-12 — Paid acquisition (originally proposal Phase 2):**
- [ ] Ad creatives produced (already drafted in brand-visuals/ad-samples/)
- [ ] Google Ads or Meta selected based on Wk 8 audience analysis
- [ ] Initial 2-week test campaign with 3+ variants
- [ ] Cold email sequence (3 emails EN/HU) drafted and first 50 targets contacted
- [ ] Weekly ad performance report to Victor
- [ ] Phase target: 2-5 qualified leads booked

**Wk 13-16 — Compound:**
- [ ] Winning ads scaled, losing variants killed
- [ ] Cold outreach expanded based on Wk 9-12 reply data
- [ ] Full system running end-to-end
- [ ] Case study documented for BridgeWorks portfolio + CEE FM site
- [ ] Retainer continuation conversation with Victor

**Recurring across all weeks:**
- [ ] LinkedIn 3x/week (Tue/Wed/Thu) bilingual EN/HU
- [ ] Monthly performance review call with Victor
- [ ] CEE FM June calendar drafted by end of May

### Open proposals
- [ ] CEE FM Ops Platform — Apr 17 proposal sent (3 tiers: 1.2K / 4.5K / 12K EUR). Awaiting Victor's answers to 8 scoping questions.

### Internal systems
- [ ] Set up pipeline cron schedules (daily 7:03, weekly Mon 9:07, monthly 1st 10:13)
- [ ] Fix youtube-analytics script for v1.2.4 API compatibility
- [ ] Scope command center (Notion vs dashboard vs Sheets expansion)

### New leads / pipeline
- [ ] Oliviks: marketing audit drafted, no engagement scoped. Decide: pursue, drop, or repurpose.
