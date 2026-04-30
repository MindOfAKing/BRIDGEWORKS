# Delivery Appendix: April 2026

This appendix proves what shipped in Month 1 of the 16-week engagement. It complements the Executive Report by enumerating the full delivery roster, with file references for each deliverable.

All amounts in HUF. The CEEFM-PROP-001 contract is denominated in EUR; the HUF figures here use the actual rate from the April 2026 invoices issued via szamlazz: 363.68 HUF/EUR.

---

## Proposal Commitments Closed in Month 1

These map to the original CEEFM-PROP-001 proposal scope. All shipped during Wk 1-5.

### Website completion

- Contact form wired to office@ceefm.eu, verified live
- Placeholder stat counters fixed: homepage now ships "50+ Properties Managed", "98% Client Retention", "10+ Years Experience" in raw HTML (was 0+/0%/0+ before Wk 5 fix; AI crawlers now see real numbers)
- Mobile optimisation review (today's marketing audit: Mobile 90/100)
- Standalone /contact page (EN) and /hu/kapcsolat (HU) with focused conversion design, ContactPage and BreadcrumbList JSON-LD schema. Sitemap expanded from 2 to 4 URLs.
- Three Hungarian production typos in homepage copy fixed: márkareputáció, szabványait, szabványainak

### LinkedIn company page

- Page created with Limehome partnership featured
- Banner uploaded (green variant, on-brand gradient)
- About copy applied EN + HU (~1,900 chars)
- 20 specialty tags applied including Hungarian "letesitmenygazdalkodas"
- Custom button set to "Visit website" → https://ceefm.eu/contact
- Tagline applied EN + HU
- Hashtags followed: #facilitymanagement, #ingatlankezelés, #propertymanagement
- Founding posts queued (3 posts: Limehome partnership pin, service depth, solar angle)
- April content cadence: 12 of 12 calendar posts published Apr 1-24

### AI-Powered Advertising (assets ready, campaign launch in Phase 4)

- 4 ad creatives + 4 final EN/HU videos + voiceover audio produced
- 12 Remotion-generated video assets rendered locally for Google Ads (15s + 30s × 3 aspects × EN+HU): output at `clients/ceefm/brand-visuals/remotion-video/out/`
- Google Ads RSA copy: 15 headlines + 4 descriptions per language, 7 distinct angles, all within Google Ads character limits (`clients/ceefm/deliverables/GOOGLE-ADS-RSA-COPY-EN-HU.md`)
- Google Ads brand guidelines populated: business name CEEFM Kft, main color #1C3D2A, accent color #8FBF7A, font preference Inter / Roboto / Arial, logo uploaded
- 16-week campaign roadmap as polished client document (`clients/ceefm/deliverables/16-WEEK-CAMPAIGN-ROADMAP.md`)

### Cold Email Outreach System

- 3-email cold outreach sequence drafted in EN and HU (intro / value / soft close), with 3 subject-line A/B options each, preheaders, and personalisation tokens (`clients/ceefm/deliverables/COLD-OUTREACH-SEQUENCE-EN-HU.md`)
- Recommended sending platform identified (Apollo or Smartlead)
- Pre-flight checklist for SPF, DKIM, DMARC, mailbox warm-up
- Launch deferred per Wk 5 joint decision until GEO score crosses 80

### Social Media

- April content calendar (12 posts published Apr 1-24, 3.4 posts/week, exceeds proposal commitment of 3/week)
- LinkedIn-primary content cadence sustained
- Facebook secondary page: parked for Wk 7 build

### SEO Foundations

- On-page optimisation across all pages (meta titles, descriptions, hreflang en/hu/x-default)
- llms.txt at /llms.txt for AI crawler discoverability
- robots.txt with explicit Allow for all major AI crawlers (GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, anthropic-ai, PerplexityBot, Google-Extended, Applebot-Extended, CCBot, plus Bingbot, DuckDuckBot, YandexBot)
- speakable JSON-LD selectors (h1, h2, .hero-body) for voice-AI surfaces
- Top-20 SEO keyword research deliverable: three tiers, Hungarian-primary, target page mapping (`clients/ceefm/deliverables/SEO-KEYWORD-RESEARCH-TOP-20.md`)
- Google Business Profile claimed; postcard verification window 2026-05-07 to 2026-05-14
- GBP business descriptions drafted EN + HU, GBP-policy compliant, under 750 chars (`clients/ceefm/deliverables/GBP-BUSINESS-DESCRIPTION-EN-HU.md`)

---

## Platform Foundation Shipped (2026-04-30)

These were not in the original proposal scope as discrete line items but became necessary to lift CEEFM's entity recognition for AI search and Google Ads readiness. Funded by the Wk 5 retainer redirection.

### Schema and structured data

- Full ProfessionalService JSON-LD with 14 fields: legalName, taxID, foundingDate (2010-05-18), telephone, email, address (PostalAddress), geo (GeoCoordinates), areaServed, openingHoursSpecification (Mon-Sun 08:00-17:00), contactPoint, knowsLanguage, hasOfferCatalog with 7 Service offers, numberOfEmployees (QuantitativeValue 11-50), speakable
- ContactPage and BreadcrumbList schema deployed on /contact and /hu/kapcsolat
- Schema completeness verified: see Sitemap before/after, Schema completeness, Stat counters, HU production typo composites

### Sitemap before/after

Before and after view of sitemap expansion.

### Wikidata entity (Q139592822)

- Q-item published with EN and HU labels ("CEEFM Kft" / "CEEFM Kft")
- Seven claims live: instance of (facility management company), country (Hungary), headquarters location (Újlengyel), inception (2010-05-18), official website (https://ceefm.eu), industry (facility management), LinkedIn company ID
- Cited bidirectionally in ProfessionalService schema as `identifier.value`, `identifier.url`, and `sameAs`
- Wikidata is the canonical entity layer Google, ChatGPT, Claude, and Perplexity consume as ground truth; this is the single highest-leverage move for a sub-1000-employee firm

### Bing Webmaster Tools verification

- `msvalidate.01` meta tag deployed in BaseLayout.astro with token `BA08FF5FB45EA54364C56B7D914AB85D`
- BWT property verified
- Sitemap (https://ceefm.eu/sitemap-index.xml) submitted; processing in progress

### IndexNow integration

- Key file deployed at https://ceefm.eu/d9916e6c1f394ddd97bf35b81cfa2e7f.txt (32-character hex key, file content matches filename)
- Bing Copilot can now do near-realtime recrawl on URL update

### Hungarian legal imprint (Ekertv. compliance)

- Cégjegyzékszám 13-09-227045
- Adószám 22734015-2-13
- Registered seat 2724 Újlengyel, Petőfi Sándor utca 48
- Ügyvezető: Victor Danmagaji
- Live in footer on all pages
- Trust signal that Google, Gemini, and Perplexity downgrade authority on without

### Security headers

- HSTS: max-age=31536000; includeSubDomains; preload
- X-Content-Type-Options: nosniff
- X-Frame-Options: SAMEORIGIN
- Referrer-Policy: strict-origin-when-cross-origin
- Content-Security-Policy: upgrade-insecure-requests
- Permissions-Policy: camera=(), microphone=(), geolocation=()

All five headers deployed via Apache .htaccess. Live verified.

### Performance patch

Deployed 2026-04-30 against the mobile LCP issue identified by PageSpeed Insights:

- Font subset reduction: dropped Cyrillic and Vietnamese subsets, retained latin and latin-ext only. Total woff2 files: 24+ → 12.
- Hero stats counter: React island → static Astro markup
- Cookie banner: React island → static HTML with inline script
- Contact form hydration: `client:load` → `client:visible`
- Unsplash images: `q=80&w=800` → `q=60&w=640`
- Unsplash resource hint: `dns-prefetch` → `preconnect`

Mobile re-test queued.

### Google Rich Results Test

- 1 valid Local Business item detected (CEEFM Kft) on https://ceefm.eu/
- Eligible for Google Search rich results
- Earlier optional warning on numberOfEmployees missing maxValue closed by adding `{minValue: 11, maxValue: 50}` (matches LinkedIn 11-50 employee range)

---

## Truth and Trust Corrections (Named, Not Buried)

| Item | Decision | Date | Effect |
|---|---|---|---|
| Brand visual design package | Declined by client | 2026-04-12 | 227,300 HUF not invoiced. Existing brand assets used as-is. |
| Solar add-on pitch | Declined by Victor | 2026-04-16 | 200,024 HUF not invoiced. SolaCare retained as 7th service tile under CEEFM, not as separate brand build. |
| EU Ecolabel `hasCredential` schema block | Removed | 2026-04-29 | Verified via the public ECAT registry: CEEFM does not hold the licence. The claim could not stand. Truthful product-use language retained where applicable. |
| `aggregateRating` 9.5/10 in schema | Removed | 2026-04-29 | No Review nodes existed to support the rating. Self-declared aggregateRating without reviews is a Google manual action trigger. Removed entirely. |
| HU production typos: márkareputáció, szabványait, szabványainak | Corrected | 2026-04-30 | Three Hungarian-language errors live since site launch. Fixed in source `content.ts`, deployed. Trust signal in bilingual market. |

These five corrections improved trust signals across every AI platform that reads structured data. The audit-critical fix was simply not making claims we cannot defend.

---

## Engagement Progress (16 Weeks)

| Week | Focus | Status |
|---|---|---|
| 1 | Discovery + audit (GEO 16/100 baseline) | Complete |
| 2 | Website completion (form, mobile, basic SEO) | Complete |
| 3 | LinkedIn build, April content calendar planning | Complete |
| 4 | Brand visual production, GEO audit Wk 1-3 fixes (47/100) | Complete |
| 5 | Truth and trust foundations: schema, imprint, headers, GEO 74/100, /contact pages, LinkedIn fully optimised, Wikidata Q139592822, Bing verified, GBP claimed, Rich Results passing, Google Ads RSA + brand guidelines + 12 video assets prepared, performance patch deployed | Complete |
| 6 | GBP postcard verification, founding year reconciliation, brand voice spec, PageSpeed re-test, video upload to YouTube, ad activation prep | In progress |
| 7 | Sitemap and content depth: /about page, services pages, case study sub-page, FAQPage schema | Scheduled |
| 8 | Funnel split + Aparthotel Operating Standard draft + GEO re-audit + Google Ads campaign activation | Scheduled |
| 9 | Phase 4 launch: cold outreach, ad optimisation, weekly reports | Scheduled |
| 10 | Outreach list expansion to 100; first ad optimisation cycle | Pending |
| 11 | Scale best-performing ads; Aparthotel Standard ship | Pending |
| 12 | Mid-engagement review with Victor; cost-per-lead analysis | Pending |
| 13 | Outreach list to 150; second case study published | Pending |
| 14 | Tier 2 SEO keywords; first contract conversions tracked | Pending |
| 15 | Final ad optimisation; portfolio dashboard live for first client | Pending |
| 16 | End-of-engagement review; retainer continuation conversation | Pending |

---

## Investment Summary (Month 1)

| Line | HUF | EUR equivalent | Status |
|---|---|---|---|
| Setup fee (one-time) | **381,864 HUF** | 1,050 EUR | Invoice E-EO-2026-1 issued 2026-04-28, due 2026-05-01 |
| April retainer (Month 1 of 4) | **145,472 HUF** | 400 EUR | Invoice E-EO-2026-2 issued 2026-04-28, due 2026-05-01 |
| Brand visual package | 0 HUF | 0 EUR | Declined by client; not invoiced |
| Solar add-on pitch | 0 HUF | 0 EUR | Declined by Victor; not invoiced |
| **Month 1 invoiced total** | **527,336 HUF** | **1,450 EUR** | |
| Performance bonuses (Month 1) | 0 HUF | 0 EUR | No new client contracts signed yet (Phase 4 deferred) |

Programme-level totals for reference: 16-week setup + retainer total **963,752 HUF** (2,650 EUR). Performance bonuses: 73,000 HUF per signed client, 127,000 HUF for clients with monthly value above ~728,000 HUF (2,000 EUR/month).

---

## File and Source References

All deliverables saved under `clients/ceefm/`:

| Deliverable | Path |
|---|---|
| Standalone /contact page (EN + HU) | `ceefm-astro/src/pages/contact.astro` and `ceefm-astro/src/pages/hu/kapcsolat.astro` |
| LinkedIn optimisation pack | `clients/ceefm/deliverables/LINKEDIN-COMPANY-PAGE-OPTIMISATION.md` |
| Top-20 SEO keyword research | `clients/ceefm/deliverables/SEO-KEYWORD-RESEARCH-TOP-20.md` |
| 3-email cold outreach sequence (EN + HU) | `clients/ceefm/deliverables/COLD-OUTREACH-SEQUENCE-EN-HU.md` |
| 16-week campaign roadmap | `clients/ceefm/deliverables/16-WEEK-CAMPAIGN-ROADMAP.md` |
| GBP business descriptions (EN + HU) | `clients/ceefm/deliverables/GBP-BUSINESS-DESCRIPTION-EN-HU.md` |
| Google Ads RSA copy (EN + HU) | `clients/ceefm/deliverables/GOOGLE-ADS-RSA-COPY-EN-HU.md` |
| Video script and beat sheet | `clients/ceefm/deliverables/VIDEO-SCRIPT-GOOGLE-ADS-EN-HU.md` |
| 12 Remotion video assets | `clients/ceefm/brand-visuals/remotion-video/out/` |
| LinkedIn banner | `clients/ceefm/brand-visuals/linkedin/ceefm-linkedin-banner-green-1128x191.png` |
| GEO audit report (evening, 74/100) | `clients/ceefm/reports/GEO-AUDIT-REPORT-2026-04-30-evening.md` |
| Marketing audit report (67.6/100) | `clients/ceefm/reports/MARKETING-AUDIT-2026-04-30.md` |
| Site source code changes | `ceefm-astro/src/layouts/BaseLayout.astro` (Wikidata + msvalidate.01 + maxValue), `ceefm-astro/src/data/content.ts` (HU typo fixes + contactPage block), `ceefm-astro/public/d9916e6c1f394ddd97bf35b81cfa2e7f.txt` (IndexNow key), `ceefm-astro/src/styles/global.css` (font subset reduction) |
| Issued invoices | `clients/ceefm/invoices/E-EO-2026-1_Setup-fee.pdf`, `clients/ceefm/invoices/E-EO-2026-2_April-retainer-(Month-1).pdf` |
