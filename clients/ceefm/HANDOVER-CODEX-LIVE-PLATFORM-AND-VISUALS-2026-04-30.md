# Handover

**Repo:** `bridgeworks-workspace` (and ceefm.eu live site, plus external platforms)
**From:** Claude Code (session 2026-04-30 afternoon)
**To:** Codex (live-platform action lane per `business-brain/AGENT-HANDOVER.md`)
**Date:** 2026-04-30
**Trigger:** Per protocol, Codex owns implementation, frontend changes, and live-website actions. Two workstreams here: (1) execute live-platform actions that BridgeWorks committed to in the April monthly report and (2) generate or capture every visual proof asset required for the April monthly report PDF.

---

## Current task

Two workstreams, both feeding the April monthly report deliverable to Victor:

1. **Live-platform actions:** apply or claim what is currently a "claim pending" or "apply pending" status across LinkedIn, Wikidata, Bing Webmaster Tools, IndexNow, and (post-authorisation) Google Business Profile.
2. **Visual asset generation and capture:** produce every chart and screenshot listed in Section B below. Save to the conventional output path so the PDF generator can pick them up automatically.

## Business goal

Bring the April monthly report to a state where it can ship to Victor as a branded PDF with verifiable proof of the work done. CEEFM is the active commercial center. The report is the Month 1 of 16 deliverable. Charts and screenshots are the difference between "Emmanuel says we improved your GEO score" and "here is the audit screenshot, the schema validator pass, the live security headers grade, the LinkedIn analytics dashboard."

## Files to avoid

- `clients/ceefm/CEEFM digital growth proposal.docx`, `clients/ceefm/invoices/`, the published case study and results tracker PDFs — read only.
- `clients/ceefm/reports/MONTHLY-REPORT-CEEFM-2026-04.md` — owned by Claude Code in this session; do not edit unless review-gate process surfaces a defect (in which case use the report-review handover at `HANDOVER-CODEX-REPORT-REVIEW-2026-04-30.md`).
- `clients/ceefm/deliverables/*.md` — same as above. These are document deliverables in Claude Code's lane.
- `ceefm-astro/dist/` — frontend deploy, separate handover at `ceefm-astro/HANDOVER-CODEX-FRONTEND-REVIEW-2026-04-30.md`.

---

## Section A: Live-platform actions

### A1. LinkedIn company page full optimisation (Wk 6 priority)

**Source:** `clients/ceefm/deliverables/LINKEDIN-COMPANY-PAGE-OPTIMISATION.md`
**Target:** https://www.linkedin.com/company/cee-facility-management/
**Auth needed:** LinkedIn admin access for the CEEFM page. Confirm with Emmanuel before starting if access is not already provisioned.

Apply each section of the optimisation pack in this order:
1. Industry → Facilities Services
2. Tagline EN, then HU translation
3. About EN, then HU translation (full text in deliverable Sections 3.EN and 3.HU)
4. Specialties (20 tags listed in deliverable Section 4)
5. Headquarters, Year founded (2010), Company size (11-50)
6. Website https://ceefm.eu, Phone +36 30 600 5400
7. Custom button → "Visit website" → https://ceefm.eu/contact (or HU equivalent based on visitor language)
8. Hashtags followed: #facilitymanagement, #ingatlankezelés, #propertymanagement
9. Banner image upload (after Canva produced per the brief in deliverable Section 1; optionally Codex generates the banner directly using Kie.ai or similar)
10. Schedule the three founding posts from deliverable Section 8 (one immediately, two queued for staggered ship over the next week)

**Output expected:** confirmation note in `clients/ceefm/sessions/codex-2026-04-30-linkedin-applied.md` with timestamps and any field that LinkedIn would not accept verbatim.

### A2. Wikidata Q-item creation

**Auth needed:** none for creation; Wikidata account recommended for attribution.

Create a Q-item for "CEEFM Kft" with these properties (P-codes provided so Codex can draft the wikitext directly):

- `instance of` (P31) → facility management company (Q3056789) or similar appropriate class
- `country` (P17) → Hungary (Q28)
- `headquarters location` (P159) → Újlengyel (Q1116017) or Budapest (Q1781) for operations base
- `inception` (P571) → 2010-05-18
- `official website` (P856) → https://ceefm.eu
- `tax identification number` (P11329) → 22734015-2-13
- `industry` (P452) → facility management (Q1418601)
- `LinkedIn company ID` (P4264) → cee-facility-management (the slug from the URL)
- `language of work or name` (P407) → English, Hungarian
- aliases (en) → "CEE Facility Management", "CEEFM"
- aliases (hu) → "CEEFM Ingatlanüzemeltető Kft."
- description (en) → "Hungarian facility management company"
- description (hu) → "magyar létesítménygazdálkodási vállalat"

Any properties not on this list that Codex judges relevant can be added with cited references where Wikidata requires them.

**Output expected:** the Q-ID assigned. Note in `clients/ceefm/sessions/codex-2026-04-30-wikidata-applied.md`. Update the live `ceefm-astro/src/layouts/BaseLayout.astro` schema `sameAs` array to add the Wikidata entity URL `https://www.wikidata.org/wiki/Q[ID]` once the ID is known.

### A3. Bing Webmaster Tools verification + IndexNow integration

**Auth needed:** Bing Webmaster Tools account.

1. Sign in to https://www.bing.com/webmasters/, add property `https://ceefm.eu/`.
2. Use Meta Tag verification method. Bing returns a `msvalidate.01` content value.
3. Add the meta tag to `ceefm-astro/src/layouts/BaseLayout.astro` head section: `<meta name="msvalidate.01" content="[VALUE]" />`.
4. Submit `https://ceefm.eu/sitemap-index.xml` in the Sitemaps section.
5. Generate an IndexNow key (any random hex string, 32+ chars). Save to `ceefm-astro/public/[KEY].txt` containing the same key as the file content.
6. Add IndexNow `<meta name="indexnow" content="[KEY]" />` to BaseLayout if Bing Webmaster Tools requires that flow (check current Bing UX before committing).
7. Trigger the IndexNow ping for the four current URLs (`https://ceefm.eu/`, `/hu/`, `/contact`, `/hu/kapcsolat`).

**Output expected:** confirmation note in `clients/ceefm/sessions/codex-2026-04-30-bing-indexnow-applied.md` with verification status and the key used.

### A4. Google Business Profile claim and setup

**Auth needed:** Victor's authorisation to claim. The postcard verification will be sent to the registered seat (2724 Újlengyel, Petőfi Sándor utca 48). Postcard delivery and code entry typically takes 7-10 days.

**Hold this action** until Emmanuel confirms Victor has authorised it. The April monthly report Section 12 lists this as a decision needed at the May call. Once confirmed:

1. Claim CEEFM Kft on https://business.google.com/.
2. Use the registered seat address. Mark service area as "Hungary" if Victor agrees to a service-area business model (no public address) or use the registered address as a public location.
3. Categories (primary): Facility Management. Secondary: Commercial Cleaning, Property Management, Hygiene Services.
4. Hours: Mon-Sun 08:00-17:00 (matches the schema OpeningHoursSpecification).
5. Phone +36 30 600 5400. Website https://ceefm.eu/.
6. Trigger postcard verification.
7. Once verified: upload at least 10 photos (Codex can request these from Victor or generate brand-consistent placeholders), add the 7 services, write a 750-character business description (lift from LinkedIn About copy).
8. Update the live schema `sameAs` array with the GBP URL once GBP listing is live.

**Output expected:** running log in `clients/ceefm/sessions/codex-gbp-progress.md` updated as each step completes.

### A5. Post-deploy verification of /contact pages

**Trigger:** after Emmanuel approves the ceefm-astro deploy package and Hostinger upload completes.

1. Verify `https://ceefm.eu/contact` returns 200 with full body content rendered.
2. Verify `https://ceefm.eu/hu/kapcsolat` returns 200.
3. Verify `https://ceefm.eu/sitemap-0.xml` contains 4 URLs (`/`, `/contact/`, `/hu/`, `/hu/kapcsolat/`).
4. Verify the ContactPage and BreadcrumbList JSON-LD on both new pages via Google Rich Results Test.
5. Submit the form on /contact with a test payload. Confirm office@ceefm.eu receives the test message. Note: form posts to web3forms.com client-side. The web3forms key is in client source.
6. Verify the three HU typo fixes are live by reading the rendered text on https://ceefm.eu/hu/ Why CEEFM section, Industries section (Hotels block), and FAQ.

**Output expected:** verification note in `clients/ceefm/sessions/codex-2026-04-30-deploy-verified.md` with screenshots E and F (see Section B below) captured during this verification step.

---

## Section B: Visuals to generate or capture

All visuals save to `clients/ceefm/reports/charts/2026-04/` with the file naming convention specified per item. The PDF generator (built in Section D below) loads from this directory automatically.

### B1. Analytical charts (data sources are local files, generate via matplotlib or equivalent)

Output format: PNG, 1200 × 800 px, transparent background or white. Use BridgeWorks brand palette: navy `#0F1A2E`, gold `#B8860B`, ivory `#F5F0E8`, sage `#4A6741`. Inter font (or Helvetica fallback). No em dashes in any chart label.

| Filename | What | Data source |
|---|---|---|
| `01-geo-score-progression.png` | Line chart, 4 points: Mar (16), Apr 3 (29), Apr 22 (47), Apr 30 (61). Y-axis 0-100 with band annotations (Critical 0-39, Poor 40-59, Fair 60-74, Good 75-89, Excellent 90-100). | `clients/ceefm/reports/GEO-AUDIT-REPORT-2026-04-30.md` Score progression table; older audits in same folder |
| `02-geo-categories-delta.png` | Grouped bar chart, 6 categories x 2 dates (Apr 22 vs Apr 30). Show delta as a label above each bar pair. | Same audit reports |
| `03-marketing-audit-radar.png` | Radar chart, 6 axes: Content, Conversion, SEO, Competitive, Brand, Growth. Single polygon for current scores. | `clients/ceefm/reports/MARKETING-AUDIT-2026-04-30.md` Score table |
| `04-linkedin-impressions-april.png` | Daily impressions line chart, x-axis Apr 1-28, y-axis impressions. | `clients/ceefm/reports/linkedin-analytics/2026-04/cee-facility-management_content_*.xls` |
| `05-linkedin-followers-cumulative.png` | Cumulative follower growth line, x-axis Mar 30-Apr 28, y-axis follower count. | `_followers_*.xls` |
| `06-linkedin-visitor-demographics.png` | Three small horizontal bar charts in a single image: top 5 job functions, top 5 industries, top 5 locations. | `_visitors_*.xls` |
| `07-sitemap-before-after.png` | Visual diff: left panel "Before" with 2 URL boxes, right panel "After" with 4 URL boxes. Text labels for each URL. | This session's audit |
| `08-funnel-diagram.png` | Six-stage funnel (Awareness, Visit, Engaged, Form Submit, Walkthrough, Contract) with conversion rate band labels and leak-point markers between stages. | `MARKETING-AUDIT-2026-04-30.md` Section: Conversion Optimization Analysis |

### B2. Live-platform screenshots

Output format: PNG, full-resolution browser capture. Use a 1440 × 900 viewport. Crop to the relevant area when the full page is too long.

| Filename | What | URL or platform |
|---|---|---|
| `A-schema-validator-pass.png` | Google Rich Results Test screenshot showing valid ProfessionalService entity, valid ContactPage on /contact, valid BreadcrumbList. | https://search.google.com/test/rich-results?url=https://ceefm.eu and same for /contact |
| `B-security-headers-grade.png` | securityheaders.com result for ceefm.eu showing the grade and the 5 headers present. | https://securityheaders.com/?q=ceefm.eu&followRedirects=on |
| `C-pagespeed-mobile-desktop.png` | PageSpeed Insights summary, mobile + desktop scores side by side. | https://pagespeed.web.dev/?url=https%3A%2F%2Fceefm.eu |
| `D-homepage-rendered.png` | Live https://ceefm.eu/ homepage hero + Limehome metrics + footer imprint visible. May need stitched scroll capture. | https://ceefm.eu/ |
| `E-contact-page-rendered.png` | Live /contact page after deploy. Full page or hero + form + trust strip. | https://ceefm.eu/contact (post-deploy only) |
| `F-hu-kapcsolat-rendered.png` | Live /hu/kapcsolat page after deploy. | https://ceefm.eu/hu/kapcsolat (post-deploy only) |
| `G-linkedin-page-current.png` | LinkedIn company page as it currently appears (pre-optimisation pack apply). Captures baseline. | https://www.linkedin.com/company/cee-facility-management/ |
| `H-llms-and-robots.png` | Combined image: top half rendered https://ceefm.eu/llms.txt, bottom half https://ceefm.eu/robots.txt. | Both URLs |
| `I-linkedin-top-post.png` | LinkedIn analytics admin view showing the top April post ("Hotel housekeeping standards guests notice", 6,621 impressions, 196 clicks). | LinkedIn admin → Analytics → Content |

### B3. Composite before/after panels

Output format: PNG, 1600 × 800 px, two columns labelled "Before" and "After".

| Filename | Composition |
|---|---|
| `X1-schema-completeness.png` | Left: skeleton schema (just `@type` and `name`). Right: full ProfessionalService schema fields list (legalName, taxID, foundingDate, address, geo, openingHours, contactPoint, knowsLanguage, sameAs, hasOfferCatalog with 7 offers, speakable, numberOfEmployees). |
| `X2-stat-counters.png` | Left: raw HTML view showing `0+ Properties / 0% Retention / 0+ Years`. Right: raw HTML view showing `50+ Properties / 98% Retention / 10+ Years`. |
| `X3-hu-typos.png` | Three rows. Each row: "Before" cell with the typo (`márkareputaéció`, `szabányait`, `szabányainak`) underlined red, "After" cell with the corrected word. |

---

## Section C: Output conventions

- **Charts directory:** `clients/ceefm/reports/charts/2026-04/`
- **Filenames:** as listed above. Lowercase, dashes, descriptive.
- **PNG only.** No SVG (PDF generator path needs raster).
- **Brand palette enforced:** navy #0F1A2E, gold #B8860B, ivory #F5F0E8, sage #4A6741.
- **No em dashes** in any chart label, axis title, legend, or annotation.
- **No AI slop** in chart titles or descriptions.
- **Screenshots include the URL bar** when relevant (D, E, F, G) so the proof is verifiable.
- **Each visual gets a 1-2 sentence caption** in `clients/ceefm/reports/charts/2026-04/captions.md` so the PDF generator can pull captions automatically.

---

## Section D: PDF generator

Claude Code will build the PDF generator at `clients/ceefm/reports/generate-monthly-report-pdf.py`. It:

1. Reads `clients/ceefm/reports/MONTHLY-REPORT-CEEFM-2026-04.md`
2. Loads all `.png` files from `clients/ceefm/reports/charts/2026-04/`
3. Loads `captions.md` if present
4. Renders to `clients/ceefm/reports/MONTHLY-REPORT-CEEFM-2026-04.pdf` with BridgeWorks branded chrome (navy header band + gold accent + ivory background + footer "office@bridgeworks.agency · bridgeworks.agency")
5. Embeds visuals at section anchors based on filename prefix (`01-`, `02-`, ... `09-` analytical charts → Section 2 "Headline Metrics"; `A-` to `I-` screenshots → distributed across sections; `X1-X3` before-after panels → Section 5 or 6)

The PDF generator runs once Codex has produced the visuals and committed them to the charts directory. Claude Code triggers it; output is the deliverable PDF.

---

## Verification needed

- LinkedIn admin access to CEEFM page is provisioned for Codex
- Wikidata account is set up (or one is created) before A2 starts
- All three before/after composite panels (X1-X3) accurately represent the actual states (verify against `ceefm-astro/src/data/content.ts` git history for HU typos and the schema diff in `BaseLayout.astro`)
- Every screenshot is from the live site, not a cached or staged version
- All visuals pass the brand palette and no-em-dash check before save

## Companion handovers

- Frontend code review for /contact deploy: `ceefm-astro/HANDOVER-CODEX-FRONTEND-REVIEW-2026-04-30.md`
- Document review (Claude-drafted client artifacts): `clients/ceefm/HANDOVER-CODEX-REPORT-REVIEW-2026-04-30.md`

This handover is the third leg of the Codex review and execution loop for the April delivery.

---

Claude Code · session 2026-04-30 afternoon
