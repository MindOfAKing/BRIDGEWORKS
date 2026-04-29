# Council Review: Oliviks Service Agreement

**Mode:** Deep (5 reviewers)
**Content type:** Engagement contract (legal-grade)
**Document:** CONTRACT-OLIVIKS-2026-04-29.md
**Date:** 2026-04-29

## Verdicts

| Reviewer | Role | Verdict |
|---|---|---|
| 1 | Hungarian small-business legal reviewer | Maybe (2 fixes) |
| 2 | Founder protection reviewer | Maybe (3 fixes) |
| 3 | Olivia (client perspective) | Yes (2 small tweaks) |
| 4 | Brand voice enforcer | Revisions-needed (2 fixes) |
| 5 | Past-burned-client reviewer | Mostly |

**Council consensus:** **Revise** — no fatal issues, but multiple convergent gaps. Do not send as-is.

---

## Key Problems (ranked by severity, by how many reviewers flagged each)

### 1. No revision rounds, no acceptance criteria, no deemed-acceptance clause
**Flagged by:** Legal, Founder Protection, Olivia, Past-Burned (4 of 5)
**Impact:** Highest-severity gap. Without acceptance criteria the Client can withhold the second 136,305 HUF indefinitely by claiming dissatisfaction. Without revision rounds the scope is "unlimited." Without deemed-acceptance Emmanuel is locked in (§11.1 ties termination to "final handover and full payment").
**Fix (add to §2 or §5):**
> "Each workstream includes two rounds of revisions per deliverable. Further rounds quoted at 15,000 HUF/hour. The Client has 5 working days from BridgeWorks' written handover notice to submit specific written objections referencing deliverables in Annex A. Silence past 5 working days constitutes deemed acceptance, and payment 2 is invoiced immediately."

### 2. Section 7.4 portfolio case-study clause is opt-out, not opt-in
**Flagged by:** Legal, Founder Protection, Olivia (3 of 5)
**Impact:** Olivia's words: "I would prefer it the other way around. Ask me first, then use it." A small KFT signing this without negotiation is fine; a savvier client will redline. Either way it invites a "we never agreed" dispute later.
**Fix:** Change 7.4 to opt-in. Either:
> "BridgeWorks may reference the engagement and use Oliviks Kitchen's name and logo as a portfolio case study only with the Client's prior written consent. Consent will not be unreasonably withheld."
OR remove 7.4 entirely and request consent separately at handover.

### 3. Pro-rata termination math undefined
**Flagged by:** Past-Burned, Founder Protection (2 of 5)
**Impact:** §11.3 says "pro-rata percentage of the total fee against the milestones reached" but no milestone schedule exists. The non-refundable first payment combined with undefined math leaves Olivia paying for work she may never receive if she terminates at week 2.
**Fix:** Add a milestone breakdown to §11.3:
> "Milestone weights for pro-rata calculation: Week 1 kickoff and access setup = 20%, Week 2 GBP and Email/WhatsApp delivered = 50%, Week 3 Website Upgrade delivered + final handover = 30%."

### 4. Section 10.2 "Estimates in the Proposal are illustrative"
**Flagged by:** Brand voice, Past-Burned (2 of 5)
**Impact:** Past-burned reviewer: "the trap door" — agency wriggle-room language. Brand voice: vague, soft.
**Fix:** Cut the sentence entirely. The no-guarantee-of-outcomes line in 10.2 is enough.

### 5. Liability cap carve-out (10.4) too vague under Hungarian law
**Flagged by:** Legal (1 of 5, but legally important)
**Impact:** Hungarian Ptk. 6:152 § voids limitations for damages caused by intentional conduct or to life/health. The current 10.4 gestures at this but is too vague to be safe.
**Fix:** Replace 10.4 with:
> "Section 10.3 does not apply to damages caused intentionally or by gross negligence (szándékosság vagy súlyos gondatlanság), or to harm caused to life, bodily integrity, or health."

### 6. Force majeure clause missing
**Flagged by:** Legal (1 of 5)
**Impact:** Hungarian Ptk. 6:142 § gives statutory relief but is narrow. Missing for a contract with platform dependencies (WordPress, Google, MailerLite).
**Fix:** Add new section 12.7:
> "Force majeure: neither Party is liable for delay or failure caused by events outside reasonable control, including pandemics, infrastructure outages, or third-party platform shutdowns. The affected Party will notify the other within 5 working days and propose mitigation."

### 7. Subcontractor clause missing
**Flagged by:** Founder Protection (1 of 5)
**Impact:** Marci is doing social work nowhere named in the contract. If Marci breaches confidentiality or causes harm, BridgeWorks' liability is uncovered.
**Fix:** Add to §8 or as new sub-clause:
> "BridgeWorks may engage subcontractors and remains fully responsible for their work, including obligations under sections 8 (Confidentiality) and 9 (Data Protection)."

### 8. Section 6 client-access window may be tight (5 working days for everything)
**Flagged by:** Olivia (1 of 5, client perspective)
**Impact:** Olivia: "I run a kitchen. Some weeks I barely sit at my computer. 5 days feels tight."
**Fix (founder decision):** Either extend to 10 working days, OR keep at 5 and rely on the day-for-day extension clause to absorb realistic delays. Recommend extending to 10 — costs nothing and reduces friction.

### 9. Section 5.4 statutory interest is vague to a non-lawyer client
**Flagged by:** Olivia (1 of 5)
**Impact:** Olivia: "I do not know what that number is. Either tell me the percentage or just say 'we will agree the late fee in writing if it happens.'"
**Fix:** Replace "Statutory late-payment interest under Hungarian law applies" with the specific rate (Hungarian central bank base rate + 8% as of 2026) OR a plain-language explanation.

### 10. 14-day post-handover defects window missing
**Flagged by:** Past-Burned (1 of 5)
**Impact:** Past-burned reviewer: "Without it, 'handover' becomes the agency's finish line and mine."
**Fix:** Add to §4 or §10:
> "BridgeWorks will fix in-scope defects (broken pages, schema errors, opt-in failures) reported in writing within 14 days of handover at no additional charge."

### 11. Brand voice: long sentences on lines 40 and 43
**Flagged by:** Brand voice (1 of 5)
**Impact:** Sentences doing more than one job. Violates short-sentence brand rule. Easy fix.
**Fix:** Split the GBP paragraph (line 40) after "one-page handover document." Split the Email/WhatsApp paragraph (line 43) after "GDPR compliance (...privacy-policy update)."

### 12. Change Control clause missing
**Flagged by:** Legal (1 of 5)
**Impact:** "Foundation only" is descriptive, not exclusionary. Without an explicit Change Control clause the Client could later argue items not in Annex A are "implied."
**Fix:** Add new §3.2:
> "Anything not listed in Annex A Part A is a Change Request. Change Requests are quoted separately and signed by both Parties before work begins."

---

## Strengths to Preserve (multi-reviewer consensus)

- **Section 4 kickoff trigger** (later of payment + access) — Legal: "enforceable and protects against Client-caused drift." Founder Protection: "the right shape." Past-Burned: "fair, day-for-day extension is honest."
- **Section 5.3 invoicing block** — Legal: "tight: cites §188 AAM exemption, names szamlazz.hu, sets 8-day terms, confirms NAV submission. No ambiguity for an AAM EV."
- **Section 7.1 IP transfer tied to full payment** — Legal: "correctly conditions IP transfer on payment, which is the Hungarian Ptk. default position done right." Olivia: "That part is written plainly."
- **Section 11.4 BridgeWorks-without-cause termination obligations** — Past-Burned: "actually obliges the agency to refund and hand over WIP if they walk. My old contract had nothing like that."
- **Concrete deliverable details** (23 dish descriptions, 5 named platforms for NAP) — Past-Burned: "the opposite of fluff." Olivia: "honest. I can see exactly what would cost extra later."
- **Section 3 explicit out-of-scope list** — Past-Burned: "no surprise upsells dressed as 'discovered scope.'"

---

## Cut List

- Section 10.2 second sentence: `"Estimates in the Proposal are illustrative."` — cut entirely
- Section 7.4 — cut OR convert to opt-in (founder decision)

---

## Brand Voice Sweep

- **Em dashes:** zero. Confirmed clean by brand voice reviewer (post-fix).
- **AI slop terms:** zero (none of: world-class, innovative, seamless, ecosystem, game-changing, transformative, robust, cutting-edge, passionate about, leverage, synergize).
- **Footer format:** `*BridgeWorks · office@bridgeworks.agency · bridgeworks.agency*` is the canonical long-form closing line per CLIENT-FACING-OUTPUT-CHECKLIST.md. Approved.
- **Long sentences:** 2 flagged (lines 40, 43) — see fix #11 above.
- **Voice drift:** "one-time digital foundation rebuild" reads soft (line 28), "Estimates are illustrative" already in cut list.

---

## Recommended fix order

**Tier 1 — must fix before sending (safe to auto-apply):**
1. Add revision rounds + deemed-acceptance clause (Problem #1)
2. Cut "Estimates are illustrative" sentence (Problem #4)
3. Add 14-day post-handover defects window (Problem #10)
4. Split long sentences on lines 40 + 43 (Problem #11)
5. Add force majeure clause (Problem #6)
6. Add subcontractor clause (Problem #7)
7. Strengthen liability carve-out with Hungarian Ptk. citation (Problem #5)
8. Add Change Control clause (Problem #12)

**Tier 2 — founder decision required:**
9. §7.4 case-study: keep opt-out, change to opt-in, or remove entirely (Problem #2)
10. Pro-rata milestone breakdown: 20/50/30 split or different weighting (Problem #3)
11. §6 client-access window: 5 working days vs 10 working days (Problem #8)
12. §5.4 statutory interest: name the rate vs plain-language vs leave as-is (Problem #9)

---

## Council recommendation

Apply Tier 1 fixes immediately (no business decisions required). Make Tier 2 decisions before sending. Once both tiers are addressed, contract is ready for Olivia.

---

*Council review by 5 independent agents. Synthesised by Chairman. Stored at bridgeworks-workspace/clients/oliviks/council-review-2026-04-29.md.*
