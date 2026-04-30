# Google Ads Video Script and Beat Sheet

**Client:** CEEFM Kft
**Date:** 2026-04-30
**Prepared by:** BridgeWorks · office@bridgeworks.agency
**Purpose:** Video assets for the Google Ads campaign to lift Ad Strength rating from Weak to Good or Excellent. Performance Max, Demand Gen, and YouTube formats all favour multiple aspect ratios and durations.
**For:** Codex Remotion job at `clients/ceefm/remotion/`

---

## Output specs

Render two durations (15s and 30s) in three aspect ratios each. Twelve files total (2 durations × 3 aspects × 2 languages = 12).

| Aspect | Resolution | Use case |
|---|---|---|
| 16:9 horizontal | 1920 × 1080 px | YouTube in-stream, Google Ads landscape placements |
| 1:1 square | 1080 × 1080 px | Demand Gen feed, mobile placements |
| 9:16 vertical | 1080 × 1920 px | Shorts, Performance Max vertical inventory |

**Format:** MP4, H.264, AAC audio (or no audio if music-free), 30 fps, 8-12 Mbps bitrate.
**Audio approach:** music bed only, no voiceover. CEEFM does not have a brand audio identity yet and synthetic VO would feel inauthentic on a B2B premium ad. Text-on-motion carries the message.
**Music recommendation:** instrumental ambient/cinematic at 70-90 BPM. Royalty-free. Suggested sources: Artlist, Epidemic Sound, Uppbeat. Track suggestions in Section 6 below.

---

## Brand and visual specs (Codex consumes these in Remotion components)

```js
const BRAND = {
  green: '#1C3D2A',         // primary background
  greenLight: '#2D5942',    // gradient tail
  navy: '#0F1A2E',           // alternative background
  gold: '#B8860B',           // accent rule, key numbers
  ivory: '#F5F0E8',          // text on dark
  white: '#FFFFFF',
  muted: '#E2DDD3',          // secondary text
};

const FONTS = {
  serif: 'Cormorant Garamond',  // tagline, hero numbers
  sans: 'Inter',                 // smaller copy, CTA
};

const LOGO_PATH = '/c/Users/ELITEX21012G2/Projects/bridgeworks-workspace/clients/ceefm/brand-visuals/logo/ceefm-logo.png';
```

Logo placement: bottom-right or top-right small (max 80px on the long axis). Never centred or full-screen. The brand recedes; the message leads.

Background: deep green gradient `#1C3D2A → #2D5942` with subtle architectural texture overlay (light diagonal lines at 18% opacity, same pattern as the LinkedIn banner). No stock footage. No B-roll. Text-on-motion only.

---

## 15-second cut (primary, for Bumper / Shorts / mobile placements)

### Structure

| Time | Beat | Visual | On-screen text (EN) | On-screen text (HU) |
|---|---|---|---|---|
| 0.0 - 1.5s | Hook: brand entrance | Background fades in, logo appears top-right, gold rule animates left-to-right at the bottom | `9.4 cleanliness score.` (large, serif, white) | `9.4-es tisztasági pontszám.` |
| 1.5 - 3.5s | Proof | Hold the number; below it animate in a smaller line | `Sustained 24 months at Limehome Budapest.` (sans, muted ivory) | `24 hónapja a Limehome Budapesten.` |
| 3.5 - 6.0s | Category cue | Number fades; H1 fades in, centered | `Premium facility management.` (large serif, white) | `Prémium létesítménygazdálkodás.` |
| 6.0 - 9.0s | Service breadth | Three text lines stagger in vertically | `Hotels.` `Aparthotels.` `Residential.` (each on its own line, sans, ivory) | `Szállodák.` `Apartmanhotelek.` `Lakóparkok.` |
| 9.0 - 12.0s | Differentiator | Lines clear; single line slides in | `Contract-based. KPI-led. Operating since 2010.` (sans, white, with gold rule under) | `Szerződés alapú. KPI-vezérelt. 2010 óta.` |
| 12.0 - 14.5s | CTA | Background darkens slightly; CTA card with arrow | `Request a site assessment →` `ceefm.eu/contact` (sans, white, with gold rule above) | `Kérjen helyszíni felmérést →` `ceefm.eu/hu/kapcsolat` |
| 14.5 - 15.0s | Hold | Logo top-right pulses subtly; text holds | (CTA persists) | (CTA persists) |

### Total on-screen words

EN: 26 words. HU: 22 words. Both well within the 30-word ceiling for legibility at the 15-second pace.

---

## 30-second cut (long-form, for in-stream and tutorial-style placements)

### Structure

| Time | Beat | Visual | On-screen text (EN) | On-screen text (HU) |
|---|---|---|---|---|
| 0.0 - 2.0s | Hook | Brand entrance; logo top-right; gold rule animates | `9.4 cleanliness score.` | `9.4-es tisztasági pontszám.` |
| 2.0 - 4.5s | Proof anchor | Below the number, smaller line | `Sustained 24 months at Limehome Budapest.` | `24 hónapja a Limehome Budapesten.` |
| 4.5 - 7.0s | Pivot to category | Number clears, H1 fades in | `Premium facility management for Hungary.` | `Prémium létesítménygazdálkodás Magyarországon.` |
| 7.0 - 11.0s | Three sectors | Three lines stagger | `Hotels and aparthotels.` `Residential portfolios.` `Student housing.` | `Szállodák és apartmanhotelek.` `Lakossági portfóliók.` `Diákszállások.` |
| 11.0 - 14.5s | Differentiator 1 | Lines clear; single line + animated bullet stack | `Contract-based.` `Dedicated account manager.` `Monthly KPI reporting.` (each on own line, sans, white) | `Szerződés alapú.` `Dedikált ügyfélmenedzser.` `Havi KPI-jelentés.` |
| 14.5 - 18.0s | Differentiator 2 | Single line slides in; gold rule beneath | `EU-compliant audit trails. Same teams every visit.` | `EU-megfelelő audit nyomvonal. Ugyanaz a csapat minden látogatáskor.` |
| 18.0 - 22.0s | Trust block | Three big numbers, sequential reveal | `50+` `98%` `15 years` (each labelled below: `properties managed` `client retention` `operating since 2010`) | `50+` `98%` `15 év` (`kezelt ingatlan` `ügyfélmegtartás` `2010 óta működünk`) |
| 22.0 - 26.0s | Pivot to action | Numbers clear; H1 reads | `Property managers, hotel GMs, condo boards.` (sans, ivory) | `Társasházak, szállodák, ingatlankezelők.` |
| 26.0 - 29.0s | CTA | CTA card with arrow + URL | `Request a free site assessment →` `ceefm.eu/contact` | `Kérjen ingyenes helyszíni felmérést →` `ceefm.eu/hu/kapcsolat` |
| 29.0 - 30.0s | Hold | Logo pulses subtly | (CTA persists) | (CTA persists) |

### Total on-screen words

EN: 51 words. HU: 45 words. Pace allows 1.7s per word average; comfortable read.

---

## Animation principles (Codex Remotion notes)

- **Easing:** use `Easing.out(Easing.cubic)` for entrances, `Easing.in(Easing.cubic)` for exits. Never linear; never bouncy.
- **Cuts vs fades:** prefer cross-fades at scene transitions (300-400ms). Hard cuts only on the gold rule animation (250ms left-to-right wipe).
- **Text entry:** stagger word-by-word with 60ms offset for serif H1s. Fade-in only for sans-serif body lines.
- **Numbers:** count-up animation for the "50+", "98%", "15 years" block in the 30s cut. 800ms each, sequential.
- **No flashing or strobe:** Google Ads policy.
- **Subtle parallax allowed:** the architectural texture overlay can drift 4-8 pixels left-to-right across the duration for slight depth.
- **No motion exceeds 1.2s per element:** otherwise the eye gets tired before the next beat.

---

## On-screen text rendering rules

- All text rendered at its native font (Cormorant Garamond for serif, Inter for sans). No outlines, no drop shadows other than 1-2px subtle for legibility on light areas of the gradient.
- Maximum 3 lines on screen at any moment. Anything more reads as cluttered at mobile sizes.
- Key numbers (9.4, 24, 50+, 98%) get the gold accent treatment: gold underline rule directly beneath, animated in 250ms.
- Hungarian text: Cormorant Garamond renders á é ó ú í ő ű correctly. Verify at render time. Inter same.
- The CTA URL is rendered as text (not as a clickable link in the video; YouTube ad placements don't support that anyway). The companion CTA button comes from the Google Ads ad group settings.

---

## Audio brief

**No voiceover.** Music bed only. Two track moods to test:

| Mood | Source examples | Use |
|---|---|---|
| Cinematic ambient | Artlist: "Ascension" by Stanley Gurvich; Epidemic: "Slow Build" by Edward Karl Hanson | Premium / hospitality angle |
| Modern minimalist | Uppbeat: "Sunrise" by Yarin Primak; Artlist: "Quietude" by Tristan Barton | Operational / B2B rational angle |

Test both moods with the 15s cut first, pick the higher CTR variant for the 30s cut. Codex can render both moods as separate files or leave music selection to a final pass.

**Audio mix:** music bed at -18 LUFS integrated. Room for subtle audio sting at the CTA (-12 LUFS, 200ms duration).

---

## Output files Codex should produce

```
clients/ceefm/remotion/out/
  ceefm-ad-15s-16x9-EN.mp4
  ceefm-ad-15s-16x9-HU.mp4
  ceefm-ad-15s-1x1-EN.mp4
  ceefm-ad-15s-1x1-HU.mp4
  ceefm-ad-15s-9x16-EN.mp4
  ceefm-ad-15s-9x16-HU.mp4
  ceefm-ad-30s-16x9-EN.mp4
  ceefm-ad-30s-16x9-HU.mp4
  ceefm-ad-30s-1x1-EN.mp4
  ceefm-ad-30s-1x1-HU.mp4
  ceefm-ad-30s-9x16-EN.mp4
  ceefm-ad-30s-9x16-HU.mp4
```

Total 12 renders. Each under 5 MB (well below YouTube and Google Ads limits).

---

## How these get into Google Ads

1. Upload all 12 to a private (or unlisted) YouTube channel under CEEFM's Google account
2. In Google Ads, go to the campaign → Assets → Add video asset
3. Paste the YouTube URL for each variant. Google auto-detects aspect ratio
4. Apply to ad groups. Performance Max accepts all aspects. RSA campaigns accept the 16:9 only as a "Video extension" surface.
5. Save. Ad Strength meter should re-evaluate within 24 hours.

If the YouTube channel is not yet set up, Codex can either:
- Use Emmanuel's existing personal YouTube channel temporarily (quick path)
- Set up a CEEFM Kft channel (10 minutes; better for brand consistency long-term)

The videos do not need to be public. Unlisted is sufficient for ads.

---

## Acceptance check

When Codex returns the renders, verify:

- All 12 files exist and play
- Each duration is correct (15.0s ± 0.2s, 30.0s ± 0.2s)
- All text spelled correctly (especially HU diacritics)
- Logo visible top-right on all aspects
- Gold accent visible
- No text bleeds off-screen at the smallest aspect (9:16 mobile portrait)
- Music plays uninterrupted, no sync issues
- File size each under 10 MB

---

## Companion deliverables

This script pairs with:
- `clients/ceefm/deliverables/GOOGLE-ADS-RSA-COPY-EN-HU.md` (text ad copy already shipped)
- `clients/ceefm/deliverables/GBP-BUSINESS-DESCRIPTION-EN-HU.md` (Google Business Profile)
- The brand guidelines panel values provided to Emmanuel via the Google Ads admin

Once all video renders + RSA copy + brand guidelines are in place, Ad Strength should hit Good or Excellent.

---

office@bridgeworks.agency · bridgeworks.agency
