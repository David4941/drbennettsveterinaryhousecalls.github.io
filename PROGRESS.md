# Bennett Vet new-site — progress notes

Updated: 2026-05-22. Resume in next session by reading this file first.

## 🔀 BRAND PIVOT (2026-05-22)

Site repositioned from euthanasia-leaning to general veterinary practice
positioning. Per Google's one-brand-per-website guidance, bennettvet.com
now represents the GENERAL PRACTICE brand (Bennett Veterinary Service),
while euthanasia services live at the separate brand Petsforangels.com
(a Wix site, already live).

What changed across the new (preview) site:
- Homepage rewritten: hero, content, schema all general-practice
- 15 city pages: titles changed from "In-Home Pet Euthanasia in X" to
  "House-Call Veterinarian in X"; body content rewritten with per-city
  neighborhood snippets; service schema updated
- Services page: euthanasia section replaced with a subtle link to
  petsforangels.com; OfferCatalog no longer lists euthanasia
- About page intro: euthanasia mention removed
- Footer Quick Links across all 24 HTML pages: "In-Home Pet Euthanasia"
  → "Pet Euthanasia Services" linking out to petsforangels.com
- /in-home-pet-euthanasia/ directory: DELETED
- netlify.toml: all /in-home-pet-euthanasia/* (and the old iMatrix
  /pet-euthanasia and /what-to-expect inbound redirects) now 301 to
  https://petsforangels.com/

Old saved feedback "Petsforangles cannot appear on this site" is
SUPERSEDED by this strategy. See memory project_brand_split.md.

## 🔔 ACTIVE: Domain transfer in flight (2026-05-21 → ~2026-05-28)

iMatrix released the auth code on 2026-05-21 (4 days earlier than projected).
David initiated the transfer at GoDaddy the same day.

- Auth code (DO NOT share): stored only in David's email. After transfer
  completes, the code becomes useless and should be discarded.
- No further DNS-change requests to iMatrix during the transfer window —
  keep things simple until registration is fully under David's control.
- Email MX flip: deferred until transfer completes. Then we set up David's
  own Cloudflare zone, change nameservers at GoDaddy, and flip MX there.
- Expected completion: 2026-05-26 to 2026-05-28.

Watch for these emails (one goes to davidbennett@bennettvet.com via iMatrix,
others to GoDaddy signup email):
- GoDaddy "Verify your domain transfer" — MUST CLICK or transfer auto-cancels
- register.com release notification — clicking approval link speeds it up
- GoDaddy "Welcome — transfer complete" — signals next phase

## ✅ LIVE PREVIEW

**https://bennettvet-preview.netlify.app**

Last redeployed 2026-05-10 via `netlify deploy --prod --dir=.` from
`c:\Users\Vetpe\OneDrive\Documents\Bennettvet-newsite`.

David is logged in to Netlify as davidbvet@icloud.com on team
"Dr. Bennett's Veterinary house Calls". Project is linked locally (`.netlify` folder).
To redeploy after changes, just run: `netlify deploy --prod --dir=.`

**The existing live bennettvet.com (iMatrix) is UNTOUCHED.** Domain at register.com
unchanged. The Netlify preview is on a separate subdomain.

## What changed 2026-05-10

- Phone number corrected to **(925) 519-2316** everywhere (was 519-2315). 23 HTML files updated, 0 stragglers.
- Nav label changed from "Other Veterinary Services" → **"Wellness & Medical Care"**, including footer Quick Links and the services page `<title>`.
- Re-deployed to Netlify preview.

## What's built

**Top-level pages (8):**
- `/` — Home (with city sidebar, Dr. Bennett callout, schema markup)
- `/in-home-pet-euthanasia/` — Cornerstone SEO page (rainbow-bridge hero)
- `/services/` — Wellness & Medical Care
- `/about/` — About Dr. Bennett (with portrait)
- `/contact/` — Contact form (Formspree placeholder — see below)
- `/privacy/` — Privacy policy
- `/thank-you/` — Form-submit redirect target
- `/404.html` — Friendly not-found page

**All 15 city pages BUILT** (with consistent template, intro copy, SEO schema, and varied per-city body content to avoid Google duplicate-content flags — see 2026-05-17 rewrite below):
- Walnut Creek, Lafayette, Orinda, Alamo, Martinez, Pleasant Hill, Concord, Clayton, Moraga, El Sobrante, Pinole, Hercules, Piedmont, Oakland Hills, Berkeley Hills.

Photos in place on **13 of 15 city pages**: Walnut Creek (bridges), Orinda (theater), Pleasant Hill (War Memorial — floated portrait inset), Concord (Mt. Diablo), Clayton (downtown park / dancing children sculpture, 16:9 hero), Piedmont (Piedmont Park Exedra, 16:9 hero), Hercules (Refugio Valley Park fountains and dome, 16:9 hero), Lafayette (Mt. Diablo from Lamorinda hills, 16:9 hero), Martinez (Martinez Marina along Carquinez Strait, 16:9 hero), Pinole (Welcome to Pinole city sign — square floated inset), El Sobrante (grazing herd and guardian dog on hillside, 16:9 hero), Moraga (Rheem Theatre, 16:9 hero), Berkeley Hills (panoramic vista with eucalyptus and SF skyline, 16:9 hero).

Photos also on About (Dr. Bennett portrait) and Contact (a friend of Dr. Bennett with two dogs at home — figcaption: "Every pet, a family member"; the man is NOT Dr. Bennett and alt text reflects that).

Still text-only: **Alamo, Oakland Hills** (city pages) and **Home page hero, Services page** (top-level pages).

**Optimized photos in `/images/`:**
- `dr-bennett.jpg` — 659x800, 130 KB
- `rainbow-bridge.png` — 184 KB
- `cities/walnut-creek-bridges.jpg` — 1600x900, 440 KB
- `cities/mt-diablo.jpg` — 1600x721, 183 KB
- `cities/orinda-theater.jpg` — 1200x1237, 132 KB

**Infrastructure:**
- `sitemap.xml` (lists all planned URLs)
- `robots.txt`, `netlify.toml`, `.gitignore`
- `.claude/settings.json` — auto-allow list for routine file ops
- `css/style.css` — full design system

## What changed 2026-05-14 through 2026-05-17 (major work)

- **All 24 pages: rebrand visible + structured** — "Formerly Dr. Bennett's Veterinary House Calls" line added to homepage (above first H2), footer of every page (under business name), and About page intro paragraph. Schema.org `alternateName: "Dr. Bennett's Veterinary House Calls"` added to homepage VeterinaryCare schema and to the provider object on all 16 city/service pages. `.rebrand-note` CSS class introduced.
- **Site rebrand complete on the new (preview) site.** David has not yet updated the old iMatrix bennettvet.com — plans to do so before cutover (early next week).
- **Security + regulatory pass**: HSTS, CSP, Cross-Origin-Opener-Policy, Cross-Origin-Resource-Policy added to netlify.toml. CCPA section in privacy policy enhanced (explicit Know/Delete/Correct/Opt-out rights, 45-day response). New /accessibility/ page (WCAG 2.1 AA statement) linked from every footer. Prescription disclaimer added to every footer regulatory block (CA Bus. & Prof. Code §4170 compliance).
- **Auto-generating sitemap.xml** via `scripts/build-sitemap.py`, runs on every Netlify deploy AND via local `deploy.ps1`. Auto-detects og:image and adds image:image entries. Excludes noindex pages.
- **Formspree wired** to `xlgajjyz`. Autoresponder still needs configuring in David's Formspree dashboard.
- **City-page deduplication** — rewrote "What to Expect" and "Other House-Call Services" sections across all 15 city pages with 5 rotating variants each, so no two cities share identical paragraphs (eliminated previous duplicate-content concern).
- **Logo** — placed in header of every page; favicon + apple-touch-icon set; schema.org `logo` field added.
- **Contact form data accuracy fix**: the photo on the contact page is a friend of Dr. Bennett (not him). Filename, alt text, and figcaption corrected on 2026-05-17.

## Open items / decisions David still needs to provide

1. **Public contact email** — placeholder `[email TBD]` on privacy page. Pending Google Workspace setup (resumes Monday 2026-05-18 with Cloudflare creds).
2. **Hospital permit #** — placeholder `[TO BE ADDED]` in every footer.
3. **Privacy + Accessibility effective dates** — currently `[TO BE SET ON LAUNCH]`.
4. ~~**Formspree form ID**~~ ✅ Done — wired to `xlgajjyz`. Autoresponder config still pending in David's Formspree dashboard (subject + body documented in HTML comments above the form).
5. **City photos still to swap in** — Alamo, Oakland Hills (2 city pages); Home page hero; Services page (4 total). David has been delivering photos as he takes them.
6. **HEIC photo conversions** — bennettvet-pictures folder has HEIC files (Pleasant Hill, more Orinda, more Walnut Creek) that need "Save as JPEG" in Windows Photos before re-running the optimizer.
7. **CA VMB regulatory disclosure verification** — email vmb@dca.ca.gov to confirm exact wording required.
8. **DNS cutover** at launch — change A/CNAME records when David is ready. ⚠️ 2026-05-21: David doesn't have direct Cloudflare access (iMatrix owns the zone). Plan: after domain transfer completes (~May 28), set up David's own Cloudflare zone with all records pre-staged, change nameservers at GoDaddy to point to his Cloudflare, then flip A/MX records there.
9. **Email migration (Google Workspace)** — Workspace account `davidbennett@bennettvet.com` exists and outbound mail works. Inbound still flows to iMatrix because MX still points there. ⚠️ 2026-05-21 update: David doesn't have direct Cloudflare access (iMatrix owns the zone). MX flip is now blocked until domain transfer to GoDaddy completes (~May 28) and we set up David's own Cloudflare zone. iMatrix forwarding for `davidbennett@bennettvet.com → bennettvet@gmail.com` was set up 2026-05-21 as interim safety net.
10. **Google Business Profile rename** in progress — David requested change from "Dr. Bennett's Veterinary House Calls" to "Bennett Veterinary Service" on 2026-05-17. Google's review pending over the weekend. ⚠️ He initially put descriptors in the name field (keyword stuffing); needs to edit to just `Bennett Veterinary Service` (singular, no extra text). Descriptors go in Description field, not name.
11. **Yelp rename + add "formerly" note** — old Yelp listing has 89 reviews and 16 photos under "Dr. Bennett's Veterinary House Calls." ⚠️ 2026-05-20: Yelp Support confirmed they will NOT change the business name until the website at `bennettvet.com` displays the new name. This means the Yelp rename has to wait for DNS cutover (when the new Netlify site replaces the iMatrix site at `bennettvet.com`). Once cutover happens, request rename via biz.yelp.com — Yelp will verify by re-crawling the site.
12. **Facebook pages — two-brand split needed**. Each brand gets its own page with its own phone:
    - Bennett Veterinary Service page: rename if old branding still on it; phone = (925) 519-2316
    - Pets for Angels page (may need to create new): phone = (510) 758-7921
    - The previously-noted "wrong phone (510-758-7921)" on the BVS page was actually the Pets for Angels number on the wrong listing; not "wrong" per se, just misplaced. Per Google's E-E-A-T guidance, each brand needs separate listing + separate phone everywhere (Google Business Profile, Yelp, Apple Maps, Bing). David will work through these throughout the week.
13. **Apple Maps (Apple Business Connect) and Bing Places** — likely still old brand.
14. **Old iMatrix site rebrand** — David is updating the old site's title/header to "Bennett Veterinary Service / Compassionate Mobile Veterinary Service / Formerly Dr. Bennett's Veterinary House Calls" before DNS cutover.
15. **Banner image (Banner-Bennettvet.com.jpg)** — designer-made banner is on hold. Issues: "Contra Costa County only" excludes 3 Alameda County cities served; baked-in text is unreadable to Google; banner's logo differs from site logo. Currently NOT placed.

## Recommended next-session order

1. Resume Google Workspace email setup (Cloudflare creds in hand Monday)
2. Verify GBP name change result; sweep description + post if approved
3. Facebook rename + phone fix (David's manual work, instruct as needed)
4. Continue photo additions as David delivers (Alamo, Oakland Hills, home, services)
5. iMatrix old-site rebrand check-in
6. DNS cutover at Cloudflare when David greenlights
7. **After cutover:** Yelp rename (Yelp requires the live `bennettvet.com` to show the new brand before they will rename — confirmed by Yelp Support 2026-05-20)
8. Google Search Console setup once David has studied it — verify ownership via Cloudflare DNS TXT, submit sitemap.xml, monitor crawl coverage
9. Sweep placeholders ([email TBD], [TO BE ADDED] for permit, [TO BE SET ON LAUNCH] for effective dates) once info is in hand

## Email cutover — Google Workspace MX records (use on cutover day)

Workspace account created 2026-05-18. Using Google's current simplified MX setup:

```
Type:     MX
Name:     @
Priority: 1
Value:    smtp.google.com
TTL:      3600 (or Auto)
```

ONE record only. (Legacy Workspace accounts used 5 records — `aspmx.l.google.com` + 4 alternates — but those are deprecated.)

On cutover day, at Cloudflare DNS:
1. REMOVE the current iMatrix MX record (`mx.imatrixbase.com`)
2. ADD the Google MX record above
3. Wait ~5-30 min for propagation
4. Test: send an email to `davidbennett@bennettvet.com` from an external account; should arrive in Workspace Gmail

The TXT verification record (`google-site-verification=LS3StdqdvdIrFi_VcQQZkxdTQ2Y822DHhpXZBbtFTB0`) is already in place at Cloudflare — added by iMatrix on 2026-05-18.

Worth setting up at iMatrix BEFORE the MX cutover: forward `davidbennett@bennettvet.com` → `bennettvet@gmail.com` so any emails arriving at iMatrix during the brief cutover window get auto-forwarded as a safety net.

## Important constraints (do not change)

- Live `bennettvet.com` (iMatrix) must remain undisturbed until launch.
- Domain registrar: **register.com** (just registration; renewal happens there).
- DNS host: **Cloudflare** (NS: doug.ns.cloudflare.com, chan.ns.cloudflare.com).
  All MX/A/CNAME/TXT record changes happen at cloudflare.com, NOT register.com.
- Keep `bennettvet.com` as primary domain (16 years of SEO equity).
- No git pushes to remote until explicitly authorized.

## Photo source paths (for next-session reference)

Most photos: `C:\Users\Vetpe\OneDrive\Docusign documents\Desktop\`
- `web-16x9\` — landscape JPG/PNG
- `web-1;1\` — square JPG/PNG
- `bennettvet-pictures\` — mostly HEIC (need conversion)
- Dr. Bennett portraits at parent Desktop level

Earlier abandoned attempt at `C:\Users\Vetpe\dev\Bennettvet\` — useful regulatory text already mined into footers.
