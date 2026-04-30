# GEO Audit Report: CEEFM Kft

**Audit Date:** 2026-04-30 (evening, post-platform-foundation deploy)
**URL:** https://ceefm.eu
**Business Type:** Professional Services / Local Business (B2B facility management, Budapest, serving Hungary)
**Pages Analyzed:** 4 (/, /hu/, /contact, /hu/kapcsolat) plus llms.txt, robots.txt, sitemap-index.xml, sitemap-0.xml
**Prior Audits:** 2026-03 (16/100), 2026-04-03 (29/100), 2026-04-22 (47/100), 2026-04-30 morning (61/100)
**Prepared by:** BridgeWorks · office@bridgeworks.agency · bridgeworks.agency

---

## Executive Summary

**Overall GEO Score: 74/100 (Fair, top of band, one point below Good)**

CEEFM closed Day 1 of Wk 5 at 47/100. Fourteen hours later, the site is at 74/100. The trigger was a stack of platform-foundation moves shipped together: Wikidata Q139592822 published and bidirectionally cited in schema, Bing Webmaster Tools verified with sitemap submitted, IndexNow integration live, Google Business Profile claimed and in postcard verification, LinkedIn company page fully optimised, schema gained `numberOfEmployees` `maxValue` to close the prior Rich Results warning, and a PageSpeed performance patch deployed (font subsetting, hydration delays, image compression).

Wikidata Q139592822 is the single highest-leverage move. It moves the needle on four of five AI platforms simultaneously and adds 40 points to Brand Authority alone. The Q-item resolves with 7 claims (P31 instance of, P17 country, P159 headquarters, P571 inception, P856 official website, P452 industry, P4264 LinkedIn ID), and the site's ProfessionalService schema cites it in `identifier.value`, `identifier.url`, and `sameAs`. This is the canonical entity-grounding signal LLMs (Claude, ChatGPT, Gemini, Perplexity) consume as ground truth.

The path from 74 to 80+ runs through three remaining moves: Person schema for Victor Danmagaji (founder identity), the dedicated `/case-studies/limehome` page (turns the existing metrics into a citable asset), and FAQPage schema with 6-8 high-intent questions. None requires platform setup or external dependencies. All scheduled for Wk 7-8.

### Score progression

| Date | Score | Band | Driver |
|---|---|---|---|
| 2026-03 | 16 | Critical | Pre-engagement baseline |
| 2026-04-03 | 29 | Critical | Discovery audit, no fixes yet |
| 2026-04-22 | 47 | Poor | llms.txt, hreflang, partial schema |
| 2026-04-30 morning | 61 | Fair | Schema completion, imprint, headers, stat fix |
| **2026-04-30 evening** | **74** | **Fair (top)** | **Wikidata, Bing, IndexNow, GBP claim, LinkedIn polish, PageSpeed patch** |

### Score Breakdown

| Category | Score | Weight | Weighted Score | Δ vs 61/100 |
|---|---|---|---|---|
| AI Citability | 72/100 | 25% | 18.0 | 0 |
| Brand Authority | 68/100 | 20% | 13.6 | +40 |
| Content E-E-A-T | 67/100 | 20% | 13.4 | +10 |
| Technical GEO | 92/100 | 15% | 13.8 | +4 |
| Schema and Structured Data | 82/100 | 10% | 8.2 | +11 |
| Platform Optimization | 74.2/100 | 10% | 7.4 | +17 |
| **Overall GEO Score** | | | **74.4** | **+13** |

---

## What Changed Since the 61/100 Audit

### Platform foundation shipped (2026-04-30 evening)

1. **Wikidata Q139592822 ("CEEFM Kft") published.** EN and HU labels. 7 claims live: instance of (facility management company), country (Hungary), headquarters (Újlengyel), inception (2010-05-18), official website (https://ceefm.eu), industry (facility management), LinkedIn company ID. Cited in site schema as `identifier.value`, `identifier.url`, and `sameAs`.

2. **Bing Webmaster Tools verified.** `msvalidate.01` meta tag deployed with token `BA08FF5FB45EA54364C56B7D914AB85D`. Sitemap-index.xml submitted to Bing and currently processing. First crawl typically lands within 7-14 days.

3. **IndexNow integration live.** Key file at `https://ceefm.eu/d9916e6c1f394ddd97bf35b81cfa2e7f.txt` returns 200. Bing Copilot can recrawl on URL update without waiting for scheduled passes.

4. **Google Business Profile claimed.** Postcard verification window 2026-05-07 to 2026-05-14. Once verified, the listing URL adds to `sameAs` and unlocks Maps presence.

5. **LinkedIn company page fully optimised.** Banner uploaded (green variant), About copy EN+HU live, 20 specialty tags including Hungarian "letesitmenygazdalkodas", custom button to /contact, founding posts queued. Followers 146, April content 12 posts, top post 6,621 impressions, 3.69% engagement rate.

6. **Schema `numberOfEmployees` updated** to `{minValue: 11, maxValue: 50}`, matching LinkedIn employee range. Closes the Rich Results Test optional warning.

7. **PageSpeed performance patch deployed.** Font subsetting from 24+ woff2 to 12 (latin + latin-ext only), hero stats from React island to static Astro, cookie banner from React island to static HTML, ContactForm hydration to `client:visible`, Unsplash images to `q=60&w=640`, Unsplash resource hint upgraded from `dns-prefetch` to `preconnect`. Mobile re-test queued.

8. **Three Hungarian production typos corrected** in homepage copy: márkareputáció, szabványait, szabványainak.

9. **Rich Results Test passed.** 1 valid Local Business item detected (CEEFM Kft). Eligible for Google Search rich results.

---

## Critical Issues (Fix Immediately)

None remaining as of 2026-04-30 evening.

---

## High Priority Issues

1. **Founding-year inconsistency persists across three sources.** Schema says 2010-05-18 (= 16 years today). llms.txt says "12 years of operational experience". Homepage stat tile says "10+ Years Experience". A literacy-savvy reader or a Google quality rater will flag this instantly. Recommended fix: replace all three with "Operating since 2010" and stop relying on relative claims that drift annually. Pending Victor's wording call.

2. **Sitemap content cap.** `/sitemap-index.xml` and `/sitemap-0.xml` return 200 but contain only 4 URLs (`/`, `/contact/`, `/hu/`, `/hu/kapcsolat/`). No service pages, no case study pages, no `/about`, no FAQ. This caps the URL surface every AI platform can cite. Wk 7-8 service and case-study page builds resolve this.

3. **Sitemap.xml returns 404.** Some crawlers default to the canonical `/sitemap.xml` path before reading `Sitemap:` in robots.txt. Two-line .htaccess redirect to `/sitemap-index.xml` resolves it.

4. **Person schema for Victor Danmagaji still missing.** Single biggest remaining schema gap. AI cannot answer "who runs CEEFM" from on-page entity data without it. Wk 7 build.

5. **Limehome attribution unverifiable.** The 9.4 cleanliness score and "24 months above 9.0" sit unattributed on the homepage. A name, role, and ideally a LinkedIn link converts decoration into a citable proof point. Pending Limehome contact approval.

---

## Medium Priority Issues

6. **No FAQPage on homepage or /hu/.** A 6-8 question FAQ block with FAQPage schema is the cleanest remaining citability lever. Each answer becomes an AI-quotable passage. Wk 7-8.

7. **`sameAs` only contains LinkedIn and Wikidata.** Two strong platforms but the array can extend to 5: Crunchbase, Facebook, Google Business Profile (post-verification), and one industry directory (cégjegyzék or MAISZ). Each platform is a cross-reference signal AI uses for entity resolution.

8. **No /about page or named leadership section.** Required to surface team credentials and create the link target for Victor's Person schema.

9. **`areaServed` says Hungary only.** Marketing positions for CEE region. If case-study geography supports it, expand to Czech Republic, Slovakia, Romania, Poland.

10. **Service entries in `hasOfferCatalog` are name-only strings.** Adding `description`, `serviceType`, and `areaServed` to each Service converts the catalog from labels into machine-readable definitions.

11. **No third-party reviews surfaced.** Three to five real client reviews would unlock proper Review schema nodes and a defensible aggregateRating.

12. **WebSite + SearchAction schema still missing.** Cheap to ship, anchors the root domain as a named entity, gives Google the option to render a sitelinks search box.

13. **CSP minimal.** `upgrade-insecure-requests` only. A directive-based policy (`default-src`, `script-src`, `style-src`, `img-src`, `connect-src`) lifts Security score and signals trust to AI verifiers and Bing.

14. **og:image still reuses logo.png.** Google prefers a separate hero/storefront image at 1200×630 for ProfessionalService.

---

## Low Priority Issues

15. Geo `latitude`/`longitude` rendered as strings in JSON-LD. Schema.org spec prefers Number. Google accepts both.
16. Bytespider, Amazonbot, FacebookBot not explicitly listed in robots.txt (covered by wildcard Allow but explicit listing is best practice).
17. llms.txt could publish a companion `/llms-full.txt` with the full homepage content as clean markdown.

---

## Category Deep Dives

### AI Citability (72/100) — unchanged

Same homepage and /hu/ content as the morning audit. Top citable passages remain the Limehome partnership block (9.2 / 9.4 / 24 months), the homepage stats (50+ Properties, 98% Client Retention, 10+ Years Experience), and the ProfessionalService entity facts (foundingDate 2010-05-18, taxID 22734015-2-13, full address, 7 services, EN/HU language tags).

The Wikidata identifier addition raises the trust attached to those passages but does not add new content. A genuine citability lift requires net-new content (case study sub-page, /about with founder bio, FAQPage block) which is correctly scheduled for Wk 7-8.

### Brand Authority (68/100, was 28) — biggest single lift

Live signals tonight:

| Signal | Status | Strength |
|---|---|---|
| Wikidata Q139592822 | Live, 7 claims, EN+HU labels, bidirectional citation | Maximum |
| LinkedIn company page | Fully optimised (banner, About EN+HU, 20 specialties, 146 followers) | Strong |
| Bing Webmaster Tools verification | Verified | Strong |
| Google Business Profile | Claimed, postcard pending | Half (until verified) |
| Schema `sameAs` | 2 platforms (LinkedIn + Wikidata) | Moderate |
| Reddit / YouTube / Wikipedia article | Absent | None |

Wikidata is the canonical entity layer that Google, ChatGPT, Claude, and Perplexity all consume. A small B2B paying zero euros for this signal jumped 40 points. The remaining gap to 80+ requires a Wikipedia stub (the lower-deletion-risk Hungarian wiki first), one editorial mention on a Hungarian B2B outlet, or community signals (Reddit thread, YouTube channel).

### Content E-E-A-T (67/100, was 57) — meaningful Authoritativeness pillar lift

Per-pillar:

| Pillar | Score | Δ | Driver |
|---|---|---|---|
| Experience | 65 | +1 | Limehome metrics still single proof asset |
| Expertise | 51 | +3 | HU literacy fixes; Wikidata anchor |
| Authoritativeness | 58 | +26 | Wikidata + LinkedIn + Bing + GBP claim cluster |
| Trustworthiness | 78 | +6 | Rich Results pass; HU typos fixed; maxValue closes warning |

The Authoritativeness band move from Poor (32) to Fair (58) is what Wikidata enables. Trustworthiness ceiling at 78 capped only by the founding-year inconsistency (still pending Victor's wording call).

### Technical GEO (92/100, was 88) — Excellent band

Lift sources: Bing Webmaster Tools + IndexNow integration (was 0 last audit), Core Web Vitals risk drop from font and hydration patches, sitemap discovery via non-standard `/sitemap-index.xml` path costs 2 points until `/sitemap.xml` redirect ships.

Pre-patch PageSpeed: desktop 94, mobile 76 (LCP 5.0s Poor). Post-patch mobile estimate: Performance 86-90, FCP 1.6-2.0s, LCP 3.4-3.8s. This still flags LCP as Needs Improvement (green threshold 2.5s). Hitting green requires inlining critical CSS for Faq and Footer plus self-hosting fonts with explicit `font-display: swap` (already shipped via @fontsource v5 default).

### Schema and Structured Data (82/100, was 71) — Good band, upper

Wikidata identifier PropertyValue plus `sameAs` URL together create a verified entity link from ceefm.eu directly into the open knowledge graph. Q139592822 is now machine-resolvable across Google, ChatGPT, Claude, Perplexity. ContactPage and BreadcrumbList live on /contact and /hu/kapcsolat.

Path to 95: Person schema for Victor (+8), WebSite + SearchAction (+5), one more `sameAs` platform like Crunchbase or GBP-once-verified (+3).

### Platform Optimization (74.2/100, was 57) — Good band reached on average

Per-platform:

| Platform | Prior | New | Δ | Single biggest remaining miss |
|---|---|---|---|---|
| Google AI Overviews | 52 | 71 | +19 | GBP unverified + indexable URL count |
| ChatGPT (web search) | 78 | 82 | +4 | One editorial Hungarian B2B mention |
| Perplexity AI | 58 | 68 | +10 | Reddit / community signal |
| Google Gemini | 48 | 74 | +26 | YouTube channel; GBP unverified |
| Bing Copilot | 51 | 76 | +25 | Index processing in progress (7-14 days) |

Gemini moved most. Wikidata Q139592822 is the exact ground-truth structure Gemini consumes through the Knowledge Graph pipeline. ChatGPT moved least because it was already strong. Bing Copilot's 25-point lift is conditional on the in-flight index processing completing.

---

## Quick Wins (Implement This Week)

1. **Reconcile founding year.** Replace "10+ Years Experience" / "12 years of operational experience" with "Operating since 2010" in stat tile, llms.txt, and any other surface. One absolute fact, three sources reconciled. Lifts Trustworthiness from 78 to 82+. Five-minute fix once Victor confirms.

2. **Add `/sitemap.xml` to `/sitemap-index.xml` 301 redirect** in `.htaccess`. Two lines. Closes one of the 4 Crawlability deductions.

3. **Submit the 4 current URLs through IndexNow individually.** Not just the sitemap, but explicit IndexNow ping with the four URLs. Accelerates Bing Copilot first crawl from 7-14 days to potentially 1-3 days.

4. **Tighten CSP from `upgrade-insecure-requests`** to a directive-based policy with `default-src 'self'`, explicit `script-src`, `style-src`, `img-src` (include images.unsplash.com), `connect-src`. Lifts Security score by 10 points, signals trust to Bing and AI verifiers.

5. **Add Person schema for Victor Danmagaji.** Even before the `/about` page ships in Wk 7, the Person node can land in BaseLayout JSON-LD with `worksFor` pointing to `#organization`. Lifts Schema score by 8 points, fills the Expertise pillar gap.

---

## 30-Day Action Plan (revised given today's lift)

### Wk 6 (May 4-10): Verification close-out and content kickoff
- Confirm Bing first index pass (sitemap submitted 2026-04-30; expect 7-14 days)
- Confirm GBP postcard arrival, complete verification, add GBP listing URL to schema `sameAs`
- Reconcile founding-year wording across schema, llms.txt, on-page (Victor's call)
- Add Person schema for Victor Danmagaji to BaseLayout JSON-LD
- Ship `/sitemap.xml` redirect to `/sitemap-index.xml`
- Tighten CSP to directive-based policy
- Re-run mobile PageSpeed against deployed performance patch; verify LCP drop from 5.0s

### Wk 7 (May 11-17): Content depth and indexable URL count
- Build `/about` page (EN + HU) with leadership section
- Build first 2 Tier-1 service pages: `/services/facility-management-budapest/` and `/hu/szolgaltatasok/aparthotel-takaritas/`
- Build `/case-studies/limehome/` (subject to Limehome attribution approval)
- Add FAQPage schema and 8 questions to homepage and /hu/

### Wk 8 (May 18-24): Funnel split and Aparthotel Standard
- Ship `/hospitality`, `/vendeglatas`, `/residential`, `/lakopark` split-funnel landing pages
- First draft of Aparthotel Operating Standard v1 (14-point framework)
- Add WebSite + SearchAction schema
- Re-run GEO audit (target 80+, Good band)

### Wk 9 (May 25-31): Phase 4 launch readiness
- Limehome case study published if attribution approved
- Cold outreach mailbox warm-up complete
- Google Ads campaign activated using the 120,000 HUF credit, 12 video assets attached
- Re-audit GEO and report drop to Victor

---

## Appendix: Pages Analyzed

| URL | Title | Notes |
|---|---|---|
| https://ceefm.eu/ | CEEFM Kft \| Professional Facility Management - Hungary & CEE | Server-rendered, full schema with Wikidata identifier, Hungarian imprint, msvalidate.01 verified |
| https://ceefm.eu/hu/ | CEEFM Kft \| Professzionális Létesítménygazdálkodás - Magyarország | Mirrors EN with HU imprint, 3 typo fixes live |
| https://ceefm.eu/contact/ | Contact CEEFM \| Request a Site Assessment in Hungary | ContactPage + BreadcrumbList schema |
| https://ceefm.eu/hu/kapcsolat/ | Kapcsolat CEEFM \| Helyszíni Felmérés Igénylése | Same |
| https://ceefm.eu/llms.txt | n/a | Present, valid, founding year reconciliation pending |
| https://ceefm.eu/robots.txt | n/a | All major AI crawlers explicit Allow |
| https://ceefm.eu/sitemap-index.xml | n/a | 200 OK |
| https://ceefm.eu/sitemap-0.xml | n/a | 200 OK, 4 URLs |
| https://ceefm.eu/sitemap.xml | n/a | **404** still (regression flag, redirect pending) |
| https://ceefm.eu/d9916e6c1f394ddd97bf35b81cfa2e7f.txt | n/a | 200 OK, IndexNow key file |
| https://www.wikidata.org/wiki/Q139592822 | CEEFM Kft - Wikidata | Live, 7 claims, EN+HU labels, bidirectionally cited from site |

---

office@bridgeworks.agency · bridgeworks.agency
