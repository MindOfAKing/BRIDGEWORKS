# GEO Audit Report: CEEFM Kft

**Audit Date:** 2026-04-30
**URL:** https://ceefm.eu
**Business Type:** Professional Services / Local Business (B2B facility management, Budapest, serving Hungary and CEE)
**Pages Analyzed:** 2 (/, /hu/) plus llms.txt, robots.txt, sitemap-index.xml, sitemap-0.xml
**Prior Audits:** 2026-03 (16/100), 2026-04-03 (29/100), 2026-04-22 (47/100)
**Prepared by:** BridgeWorks · office@bridgeworks.agency · bridgeworks.agency

---

## Executive Summary

**Overall GEO Score: 61/100 (Fair)**

CEEFM crossed the Poor / Fair threshold this week. The 2026-04-29 deploy closed every Critical issue from the Apr 22 audit: full ProfessionalService schema, Hungarian legal imprint, security headers, server-rendered stat counters, and removal of the false EU Ecolabel `hasCredential` block plus the unsupported aggregateRating. AI crawlers see a fully described, defensible entity for the first time. Technical GEO and Schema both moved into the Good band. The remaining gap is content breadth and entity presence outside the domain. One case study, two indexed URLs, no Wikidata entry, no Google Business Profile, and no named team beyond a footer mention cap how often AI systems will cite CEEFM today.

The path to 75+ runs through three moves: claim Google Business Profile, create a Wikidata Q-item, and ship 3 to 5 service / case study pages. None requires technical rebuild.

**Score progression:**

| Date | Score | Band | Driver |
|---|---|---|---|
| 2026-03 | 16 | Critical | Pre-engagement baseline |
| 2026-04-03 | 29 | Critical | Discovery audit, no fixes yet |
| 2026-04-22 | 47 | Poor | llms.txt, hreflang, partial schema |
| **2026-04-30** | **61** | **Fair** | **Schema completion, imprint, headers, stat fix** |

### Score Breakdown

| Category | Score | Weight | Weighted Score | Δ vs Apr 22 |
|---|---|---|---|---|
| AI Citability | 72/100 | 25% | 18.0 | +14 |
| Brand Authority | 28/100 | 20% | 5.6 | +10 |
| Content E-E-A-T | 57/100 | 20% | 11.4 | +23 |
| Technical GEO | 88/100 | 15% | 13.2 | +10 |
| Schema and Structured Data | 71/100 | 10% | 7.1 | +19 |
| Platform Optimization | 57/100 | 10% | 5.7 | +3 |
| **Overall GEO Score** | | | **61.0** | **+14** |

### Score Interpretation

61 sits in the Fair band (60-74). AI systems can now reach the site, recognise the entity, and pull defensible facts. They will still rarely volunteer CEEFM as a recommendation because external entity signals (Wikidata, Google Business Profile, third-party reviews, additional case studies) are thin or absent.

---

## What Changed Since 2026-04-22

### Critical issues closed (4 of 4)

1. Stat counter regression fixed, homepage now ships "50+ Properties Managed", "98% Client Retention", "10+ Years Experience" in raw HTML. Crawlers and LLMs see real numbers.
2. Hungarian legal imprint live in footer (Cégjegyzékszám 13-09-227045, Adószám 22734015-2-13, registered seat 2724 Újlengyel Petőfi Sándor utca 48, Ügyvezető Victor Danmagaji). Ekertv. compliance and a strong E-E-A-T trust signal.
3. ProfessionalService JSON-LD now complete, telephone, address as PostalAddress, geo coordinates, openingHoursSpecification, sameAs LinkedIn, hasOfferCatalog with 7 offers, contactPoint, knowsLanguage, speakable, numberOfEmployees, foundingDate 2010-05-18, taxID, legalName.
4. Five security headers deployed via .htaccess: HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Content-Security-Policy, Permissions-Policy.

### High-priority items addressed

- Self-declared aggregateRating without Review nodes removed from schema. No Google manual-action risk.
- Full server-side rendering verified for all priority content blocks including the Limehome case study metrics.
- robots.txt expanded to explicitly Allow GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, anthropic-ai, PerplexityBot, Google-Extended, Applebot-Extended, CCBot.

### Items intentionally cancelled

- EU Ecolabel certification claim. CEEFM does not hold the licence (Victor confirmed). False `hasCredential` block removed. Truthful product-use language retained for products supplied where client procurement standards require Ecolabel.
- Brand visual ad package (EUR 625) and solar add-on pitch (EUR 550), declined by client; out of scope for the GEO track.

---

## Critical Issues (Fix Immediately)

None remaining as of 2026-04-30. All four prior Critical items closed.

---

## High Priority Issues

1. **Sitemap content regression.** `/sitemap-index.xml` and `/sitemap-0.xml` return 200 but contain only `/` and `/hu/`. No service pages, no case study pages, no /about, no /contact. This caps every downstream platform score because AI crawlers and search engines have only two passages to choose from. Single biggest drag on the overall score today.

2. **No `<lastmod>` in sitemap.** Bing, Google, and AI crawlers use lastmod to prioritise re-crawls. Without it, the post-Apr 29 deploy will take longer to be reflected in Bing index and Google AI Overviews.

3. **`/sitemap.xml` returns 404.** Some crawlers default to this canonical path and do not follow `Sitemap:` in robots.txt to discover the index. Add an Apache rewrite to redirect to `/sitemap-index.xml`.

4. **No Google Business Profile claimed.** Highest-leverage single move for Brand Authority and Google AI Overviews. The Apr 22 audit flagged this; still open. Verification can take 5 to 10 days for the postcard so this should start now.

5. **No Wikidata entry.** Free, ~30 minutes to create. Every major LLM (Claude, ChatGPT, Gemini, Perplexity) reads Wikidata as ground truth for entity disambiguation. A Q-item with founded date, headquarters, tax ID, official URL, LinkedIn ID is the cheapest possible Brand Authority lift.

6. **Founding year inconsistency across three sources.** Schema says 2010-05-18 (= 16 years). llms.txt says "12 years of operational experience". Homepage stat tile says "10+ Years Experience". AI cross-checks these and flags inconsistencies. Recommended fix: replace all three with "Operating since 2010" or "Founded 2010": one absolute fact, no annual drift.

7. **Single case study (Limehome) is the only proof point.** SolaCare, fire safety, energy audits, student housing all have zero on-page evidence. To break 70+ on Content E-E-A-T, two more named or anonymised case studies are needed across the other service categories.

8. **No Person schema for Victor Danmagaji.** Founder / Managing Director is named only in the footer imprint. AI cannot answer "who runs CEEFM" without an entity. Highest-ROI schema addition. Snippet provided in Schema deep-dive below.

---

## Medium Priority Issues

9. **No FAQPage on homepage or /hu/.** A 6 to 8-question FAQ block with FAQPage schema is the cleanest citability lever still available. Each answer becomes an AI-quotable passage targeting Perplexity and ChatGPT search directly.

10. **`sameAs` only contains LinkedIn.** Should expand to Google Business Profile (once claimed), Facebook page, Wikidata Q-item, Crunchbase. Each platform is a cross-reference signal.

11. **No /about page or leadership section.** Required to surface team credentials and create the link target for Person schema.

12. **`areaServed` says Hungary only.** Marketing positions CEEFM for CEE region. If the case studies support it, expand to add Czech Republic, Slovakia, Romania, Poland.

13. **Service entries in `hasOfferCatalog` are name-only strings.** Add `description` to each Service for semantic depth.

14. **No IndexNow integration and no `msvalidate.01` for Bing Webmaster Tools.** Both are 15-minute jobs that materially help Bing Copilot.

15. **No third-party reviews surfaced.** Three to five real client reviews would unlock proper Review nodes and a defensible aggregateRating.

16. **CSP is minimal (`upgrade-insecure-requests` only).** A directive-based policy (`default-src`, `img-src`, `script-src`, `style-src`) is stronger but the current setup is acceptable for a static marketing site.

---

## Low Priority Issues

17. `image` in JSON-LD reuses `logo.png`. Google prefers a separate hero/storefront image at 1200 x 630 for ProfessionalService.

18. Geo `latitude`/`longitude` are strings. Schema.org spec prefers Number type. Google accepts both.

19. og:image not separately verified in this audit (referenced as `/og-image.jpg`).

20. Privacy policy and cookie/consent posture not re-verified in this sweep. Flag for next pass.

---

## Category Deep Dives

### AI Citability (72/100)

The 2026-04-29 deploy materially improved quotability. Server-side rendering of stats and the Limehome metrics turns the homepage into a fact sheet AI can lift verbatim. Speakable JSON-LD pointing to `h1`, `h2`, `.hero-body` gives Assistant-class crawlers a direct selector for voice answers.

**Highly citable passages now live:**
- Limehome block: "9.2 Booking score, 9.4 Cleanliness, 24 months above 9.0", numeric, attributed, self-contained.
- Homepage stats: "50+ Properties Managed, 98% Client Retention, 10+ Years Experience", three discrete facts, all in raw HTML.
- ProfessionalService entity facts: foundingDate 2010-05-18, taxID 22734015-2-13, full address, 7 services, EN/HU language tags.

**Weakest passages, with rewrite suggestions:**
- Service descriptions read marketing-flat. Rewrite each as one-sentence definition plus one quantitative anchor. Example: "Common Area Maintenance: scheduled inspections, lighting, HVAC checks across lobbies, corridors, and stairwells, billed monthly per square metre."
- No FAQ block. Add 6 to 8 Q&As: pricing model, contract length, response time for emergencies, Budapest district coverage, what is included, languages supported. Each answerable in 1 to 2 sentences.
- Leadership content thin. Two-sentence Victor Danmagaji bio with Person schema closes the "who runs CEEFM" answer.

### Brand Authority (28/100)

Still the weakest category. Every category gain so far has been on-page; Brand Authority lives off-domain.

| Signal | Status |
|---|---|
| Wikipedia / Wikidata | Absent. No entry under any name variant. |
| LinkedIn | Present, active. 146 followers, 11-50 employees, last post 6 days ago, complete profile. Schema `sameAs` references it. |
| Reddit | Not found in any FM-related subreddit. |
| YouTube | No official channel. |
| Hungarian directories | Likely on céginfó / opten via tax ID auto-ingest, not verified, no reviews. |
| Google Business Profile | Not claimed. No Maps reviews surface for the brand. |
| News mentions | None visible. |
| Schema sameAs | LinkedIn only. |

The +10 vs Apr 22 comes from schema `sameAs` disambiguating the entity to LinkedIn plus on-page entity facts (taxID, foundingDate, legalName) giving AI a stable identity to attach future mentions to. Real third-party signal volume has not moved.

### Content E-E-A-T (57/100)

Composite of four pillars (equal-weighted):

- **Experience: 64.** Limehome block carries the weight. Real client, named platform, three hard numbers, measurable timeframe, in raw HTML. Cap is single case study covering one of seven service lines.
- **Expertise: 48.** Correct industry terminology, bilingual delivery is itself an expertise signal. No named team, no credentials, no /about page, no methodology pages.
- **Authoritativeness: 32.** Weakest pillar. No client logo wall, no press mentions, no awards, no trade-association badges, no Wikipedia. Limehome name is the only external entity referenced on the entire site.
- **Trustworthiness: 72.** Big jump. Hungarian legal imprint live, security headers live, false aggregateRating removed, contact info present, HTTPS plus HSTS preload. Drag points: founding-year inconsistency (schema vs llms.txt vs stat tile) and llms.txt Ecolabel wording.

### Technical GEO (88/100)

| Component | Score | Weight | Notes |
|---|---|---|---|
| Server-Side Rendering | 100 | 25% | Astro static, full HTML body, stat counters confirmed in raw HTML |
| Meta Tags and Indexability | 95 | 15% | index, follow + self-canonical + hreflang en/hu/x-default |
| Crawlability | 60 | 15% | Sitemap regression: 2 URLs, no lastmod, /sitemap.xml 404 |
| Security Headers | 100 | 10% | All five headers present and valid |
| Core Web Vitals Risk | 80 | 10% | Hero image preloaded WebP, low INP risk on static Astro, CLS depends on image dimensions |
| Mobile | 90 | 10% | Viewport correct, Astro responsive defaults |
| URL Structure | 95 | 5% | Clean, locale-prefixed |
| Response and Status | 80 | 5% | One 404 (/sitemap.xml) |
| Additional Checks | 80 | 5% | dns-prefetch present for Unsplash, GTM |

### Schema and Structured Data (71/100)

The +19 jump came from removing false claims (which would have triggered Google manual actions) and fully populating the ProfessionalService entity. Validator passes with two minor warnings (image reuses logo, lat/lng as strings).

**Highest-ROI addition: Person schema for Victor Danmagaji as founder + MD.** Drop into BaseLayout.astro:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://ceefm.eu/#victor-danmagaji",
  "name": "Victor Danmagaji",
  "jobTitle": "Managing Director and Founder",
  "worksFor": {"@id": "https://ceefm.eu/#organization"},
  "url": "https://ceefm.eu/about",
  "image": "[REPLACE: https://ceefm.eu/team/victor-danmagaji.jpg]",
  "description": "[REPLACE: 1-2 sentence bio]",
  "knowsAbout": [
    "Facility Management",
    "Hygiene and Sanitization Services",
    "Hospitality Operations",
    "Student Housing Management",
    "Apartment Complex Maintenance"
  ],
  "knowsLanguage": ["hu", "en"],
  "sameAs": ["[REPLACE: https://www.linkedin.com/in/victor-danmagaji]"],
  "nationality": {"@type": "Country", "name": "Hungary"}
}
```

Then add `"founder": {"@id": "https://ceefm.eu/#victor-danmagaji"}` to the existing ProfessionalService block.

### Platform Optimization (57/100)

Per-platform readiness:

| Platform | Score | Single Biggest Miss |
|---|---|---|
| Google AI Overviews | 52 | No Google Business Profile claimed and linked via `sameAs`. AIO will not surface a Hungarian B2B FM provider without GBP confirmation. |
| ChatGPT (web search) | 78 | Only 2 indexable URLs. ChatGPT cites passages, not sites. Needs 6 to 10 distinct service / case-study pages. |
| Perplexity AI | 58 | No third-party validation surface. One Google review or one trade-press mention would shift this materially. |
| Google Gemini | 48 | No Wikidata Q-item. Cheapest entity-graph signal Gemini consumes directly. |
| Bing Copilot | 51 | No IndexNow + no Bing Webmaster Tools verification. Both are 15-minute jobs. |

ChatGPT moved most this period because it weights llms.txt, schema, and crawler access, all three improved. Gemini and AI Overviews barely moved because both depend on Google ecosystem signals (GBP, Wikidata, Knowledge Graph) that the Apr 29 deploy did not touch.

---

## Quick Wins (Implement This Week)

1. **Replace "10+ Years Experience" / "12 years of operational experience" with "Operating since 2010"** in stat tile, llms.txt, and any other surface. One absolute fact, three sources reconciled, no annual drift. Five-minute fix.
2. **Add `.htaccess` rewrite from `/sitemap.xml` to `/sitemap-index.xml`** so crawlers using the canonical path resolve correctly. Under one hour.
3. **Add `msvalidate.01` meta tag and submit sitemap to Bing Webmaster Tools.** Fifteen minutes.
4. **Add IndexNow key file** to `/public/`. Ten minutes.
5. **Submit existing site to Google Search Console** if not already, request indexing for `/` and `/hu/`. Twenty minutes.

## 30-Day Action Plan

### Week 6 (May 4-10): Entity Foundation
- [ ] Claim Google Business Profile for CEEFM Kft (registered seat Újlengyel, ops Budapest). Start postcard verification.
- [ ] Create Wikidata Q-item: instance of facility management company, country Hungary, founded 2010, tax ID, headquarters, official website, LinkedIn ID.
- [ ] Add Person JSON-LD for Victor Danmagaji with `founder` back-reference in ProfessionalService.
- [ ] Reconcile founding-year claim across schema, llms.txt, and homepage stat tile. Default to "Operating since 2010".
- [ ] Add `.htaccess` redirect for `/sitemap.xml`.

### Week 7 (May 11-17): Sitemap and Indexability
- [ ] Build `/about` page in EN + HU with leadership section (Victor + at least one ops lead if available). Add to sitemap with lastmod.
- [ ] Build `/services` index page in EN + HU. Each of the 7 services gets at least 250 words plus a `Service` schema entity with description. Add to sitemap.
- [ ] Verify `@astrojs/sitemap` emits `<lastmod>` for every URL.
- [ ] Add Bing Webmaster Tools verification, IndexNow key file, submit sitemap to Bing.
- [ ] Optimise CEEFM LinkedIn company page end-to-end (banner, description, services, founding posts, regular cadence).

### Week 8 (May 18-24): Content Depth
- [ ] Add FAQPage section to homepage and /hu/ with 6 to 8 Q&As. Wrap in FAQPage schema.
- [ ] Draft and publish second case study (hotel sector preferred, covers a service line beyond Limehome's residential focus).
- [ ] Tighten CSP from `upgrade-insecure-requests` only to a directive-based policy.
- [ ] Replace `image` in JSON-LD with a proper 1200x630 storefront image.

### Week 9 (May 25-31): Authority and Re-Audit
- [ ] Draft and publish third case study covering student housing or fire safety.
- [ ] Collect 3 to 5 real client testimonials and surface as Review schema nodes.
- [ ] Outreach to Hungarian FM trade press for one earned mention.
- [ ] Re-run GEO audit on 2026-05-29 to measure delta. Target: 75/100 (Good band).

---

## Appendix: Pages Analyzed

| URL | Title | Notes |
|---|---|---|
| https://ceefm.eu/ | CEEFM Kft \| Professional Facility Management - Hungary & CEE | Server-rendered, full schema, imprint, 7 services |
| https://ceefm.eu/hu/ | CEEFM Kft \| Professzionális Létesítménygazdálkodás - Magyarország | Mirrors EN structure, HU imprint complete |
| https://ceefm.eu/llms.txt | n/a | Present, 1306 bytes. 12-year claim needs reconciliation |
| https://ceefm.eu/robots.txt | n/a | All major AI crawlers explicit Allow |
| https://ceefm.eu/sitemap-index.xml | n/a | 200, points to sitemap-0 |
| https://ceefm.eu/sitemap-0.xml | n/a | 200, only 2 URLs, no lastmod |
| https://ceefm.eu/sitemap.xml | n/a | **404**: regression flag |

---

office@bridgeworks.agency · bridgeworks.agency
