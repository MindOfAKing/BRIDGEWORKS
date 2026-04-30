# 16-Week Digital Growth Campaign Roadmap

**Client:** CEEFM Kft
**Engagement:** CEEFM-PROP-001
**Engagement period:** Late March 2026 to mid-July 2026
**Date issued:** 2026-04-30 (end of Week 5)
**Prepared by:** BridgeWorks · office@bridgeworks.agency
**Proposal reference:** CEEFM-PROP-001 · Setup deliverable (16-week campaign roadmap)

---

## Purpose of this document

The proposal committed to a 16-week campaign roadmap. This is that document. It does three things:

1. States the original 5-phase plan from CEEFM-PROP-001 for reference
2. Documents the Week 5 joint decision to re-sequence the plan, and why
3. Lays out the actual week-by-week plan being executed, with current progress

If the roadmap and the proposal disagree, the roadmap is the live operational truth. The proposal is the original commitment frame.

---

## Original proposal plan (CEEFM-PROP-001, March 2026)

The proposal structured the engagement across five phases:

| Phase | Weeks | Focus | Key milestones |
|---|---|---|---|
| 1. Build and Launch | 1-2 | Foundation | Website complete, LinkedIn live, cold email sequence ready, ad creatives built |
| 2. Test and Learn | 3-4 | Ads and Outreach | Ad campaigns live, cold emails sent to first 50 targets, social media posting begins |
| 3. Optimise | 5-8 | Performance | Ad variants optimised based on data, outreach expanded to 150 targets, 2 leads targeted |
| 4. Scale | 9-12 | Growth | Best-performing ads scaled, SEO improvements live, 5+ qualified leads targeted |
| 5. Compound | 13-16 | Momentum | Full system running, case study documented, retainer continuation reviewed |

The plan assumed a stable digital foundation existed at Week 1. In practice, the discovery audit at Week 1 measured the GEO/AI visibility score at 16/100 (Critical band).

## Why the plan was re-sequenced (Week 5 joint decision)

By Week 4, the GEO baseline was at 29/100, still in the Critical band, and a deeper structural audit (commissioned mid-engagement) revealed that the website would not convert ad traffic at the rates the proposal assumed. Specific findings:

- Stat counters rendered as 0+ Properties, 0% Retention, 0+ Years to crawlers and pre-JS visitors
- Hungarian legal imprint missing (Ekertv. compliance gap)
- ProfessionalService schema skeleton, no telephone, address, geo, sameAs, opening hours
- No security headers. Perplexity and Gemini downgrade trust signals on bare HTTPS
- False EU Ecolabel hasCredential block in schema (CEEFM does not hold the licence)
- Self-declared aggregateRating with no Review nodes. Google manual-action risk

Spending ad budget against a site in this state would have inflated cost-per-lead, surfaced the credibility gaps to every prospect who clicked through, and risked triggering a Google manual action. The honest call was to redirect Phase 3 retainer effort into closing the foundation gap before paid acquisition launched.

The re-sequenced plan was agreed jointly between BridgeWorks and CEEFM in mid-April. Original Phase 3 ad and outreach work moved to Wk 9-12. Wk 5-8 became a content, schema, and entity foundation sprint targeting GEO score 70 or higher.

---

## Executed plan (live truth, week-by-week)

### Phase 1: Foundation Build (Weeks 1-2, ~Mar 27 to Apr 9)

| Week | Activities | Status |
|---|---|---|
| 1 | Discovery audit, baseline GEO score 16/100, content inventory, scope confirmation | Complete |
| 2 | Website completion: contact form wired, mobile QA, initial brand assets | Complete |

### Phase 2: Foundation Build, continued (Weeks 3-4, ~Apr 10 to Apr 23)

| Week | Activities | Status |
|---|---|---|
| 3 | LinkedIn company page created, initial posts, Limehome partnership featured | Complete |
| 3 | April content calendar planned and approved (12 posts) | Complete |
| 4 | Brand visual ad-samples produced (4 ads, 4 final EN/HU videos, voiceover audio) | Complete (package later cancelled by client) |
| 4 | GEO audit run, baseline measured at 47/100 after Wk 1-3 fixes | Complete |
| 4 | Joint decision: defer Phase 3 ads and outreach until GEO score reaches 70 | Documented |

### Phase 3 (re-sequenced): Truth and Trust Foundations (Weeks 5-8, Apr 24 to May 21)

This phase is what the original Phase 3 ad-and-outreach work was reallocated to. Each item targets a specific structural failure that would have eroded ad performance.

| Week | Activities | Status |
|---|---|---|
| 5 | Hungarian legal imprint live in footer (Cégjegyzékszám, Adószám, registered seat, Ügyvezető) | Complete (deployed 2026-04-29) |
| 5 | Full ProfessionalService JSON-LD schema (telephone, address, geo, hours, sameAs, hasOfferCatalog, speakable, knowsLanguage) | Complete |
| 5 | Security headers deployed via .htaccess (HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, CSP, Permissions-Policy) | Complete |
| 5 | Stat counters rebuilt to render server-side (50+/98%/10+ now in raw HTML) | Complete |
| 5 | False EU Ecolabel hasCredential block removed from schema | Complete |
| 5 | Self-declared aggregateRating removed (manual action risk closed) | Complete |
| 5 | SolaCare added as 7th service tile with provider relationship in schema | Complete |
| 5 | GEO audit re-run measures score at 61/100 (+14 points in 8 days) | Complete |
| 6 | Standalone /contact page (EN) and /hu/kapcsolat (HU) with ContactPage and BreadcrumbList schema | In progress |
| 6 | LinkedIn company page full optimisation (banner, About copy EN+HU, services keywords, hashtags, custom button) | In progress |
| 6 | Google Business Profile claim and verification (postcard, ~10 days) | Scheduled to start |
| 6 | Wikidata Q-item creation for entity recognition by Gemini, Claude, Perplexity | Scheduled |
| 6 | Top-20 SEO keyword research deliverable | Complete |
| 6 | 3-email cold outreach sequence drafted in EN and HU (launch deferred) | Complete |
| 6 | Founding-year inconsistency reconciled (schema, llms.txt, on-page stat tile) | Open |
| 7 | First two Tier 1 service pages live (`/services/facility-management-budapest/` + `/hu/szolgaltatasok/aparthotel-takaritas/`) | Scheduled |
| 7 | Limehome case study page live (`/case-studies/limehome/`) | Scheduled |
| 7 | Bing Webmaster Tools verification + IndexNow integration | Scheduled |
| 8 | Two more Tier 1 service pages live | Scheduled |
| 8 | FAQPage section + schema on homepage and /hu/ | Scheduled |
| 8 | Re-run GEO audit (target: 75 or higher) | Scheduled |

### Phase 4: Outreach and Paid Activation (Weeks 9-12, May 22 to June 18)

This is when the original Phase 3 work resumes, on a foundation that can convert. Trigger conditions: GEO score above 70, at least 4 indexed service or case study pages, Google Business Profile verified, mailbox warmed.

| Week | Activities | Status |
|---|---|---|
| 9 | Cold outreach sequence launches to first 50 prospects (aparthotel, PM, boutique hotel segments) | Pending |
| 9 | Google Ads test campaign live (3 variants A/B tested, HUF 150-250k/month budget) | Pending; needs Victor budget confirmation |
| 9 | Weekly performance reports begin (LinkedIn analytics, ad campaign metrics, SEO rankings, form submissions) | Pending |
| 10 | Outreach list expanded to 100 prospects | Pending |
| 11 | Best-performing ad variants scaled, weakest variants paused | Pending |
| 12 | Mid-campaign review with Victor: cost per lead, conversion rate, signed contracts | Pending |

### Phase 5: Scale and Compound (Weeks 13-16, June 19 to July 16)

| Week | Activities | Status |
|---|---|---|
| 13 | Outreach list expanded to 150 prospects | Pending |
| 13 | Second case study published (target: hotel sector) | Pending |
| 14 | Tier 2 SEO keywords targeted (CSRD, ESG, ISO themes) | Pending |
| 15 | Final ad campaign optimisations | Pending |
| 16 | End-of-engagement review: signed contracts, cost per acquisition, retainer continuation conversation | Pending |

---

## What changed from the proposal

| Original commitment | Re-sequenced version | Reason |
|---|---|---|
| Phase 3 ads live Wk 5 | Phase 3 ads live Wk 9 | GEO score below conversion threshold |
| Cold outreach to 50 prospects Wk 3-4 | Cold outreach to 50 prospects Wk 9 | Same |
| Cold outreach 150 by Wk 8 | Cold outreach 150 by Wk 13 | Same |
| Brand visual design package | Cancelled | Declined by client (Apr 12) |
| Solar add-on pitch | Cancelled | Declined by client (Apr 16) |
| 16-week campaign roadmap delivered Wk 1-2 | Delivered Wk 6 (this document) | Original Wk 1-2 version was an inline proposal section, not a standalone client deliverable |

## What stayed the same

- Total engagement length (16 weeks)
- Total contracted investment (EUR 2,650 plus performance bonuses)
- All six deliverable categories from the proposal
- Monthly performance review cadence
- Performance bonus structure (EUR 200 per signed client, EUR 350 if contract value exceeds EUR 2,000/month)

## What is added beyond the original proposal

The Wk 5 re-sequence introduced foundation work that was not in the original proposal but became necessary on inspection:

- ProfessionalService JSON-LD schema build-out
- Security headers via .htaccess
- Hungarian legal imprint compliance with Ekertv.
- llms.txt for AI crawler discoverability
- ContactPage + BreadcrumbList schema for the standalone contact page
- Wikidata entity creation
- Google Business Profile claim and full optimisation
- speakable JSON-LD for voice-AI surfaces

This work was funded by re-deploying the Wk 5-8 retainer effort. No additional charge to CEEFM.

---

## Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| GEO score does not reach 70 by Wk 8 | Medium | Phase 4 launch gates on the score, not the date. Roadmap holds. |
| Google Ads launch blocked on budget confirmation | Low-Medium | Confirm with Victor in early May. Backup: organic-only Phase 4 with reduced lead targets. |
| Outreach reply rate below 6% | Medium | A/B test subject lines across the 3 segments. Tighten target list quality. |
| Limehome partnership concentration risk (single anchor reference) | Medium | Phase 5 publishes second case study. Aim for 3 references by Wk 16. |
| Postcard verification for Google Business Profile delays | Medium | Start Wk 6, build in 10-day buffer. |

---

## What CEEFM should track week-to-week

To stay aligned with the roadmap, the simplest rhythm is a weekly review of these five metrics:

1. **GEO score** (target trajectory: 61 → 75 → 80+ across Wk 6-16)
2. **Followers on the LinkedIn company page** (target +50 by 2026-05-30)
3. **Indexed pages on ceefm.eu** (target: 12 to 15 by Wk 12)
4. **Site assessment requests via /contact** (target: 5 in May, 10 in June, 15 in July)
5. **Signed contracts originating from this engagement** (target: 1-2 by Wk 12, 3-5 by Wk 16)

These metrics appear in the monthly client report and form the basis of the end-of-engagement retainer continuation conversation.

---

office@bridgeworks.agency · bridgeworks.agency
