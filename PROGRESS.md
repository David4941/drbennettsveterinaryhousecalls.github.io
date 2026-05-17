# Bennett Vet new-site — progress notes

Updated: 2026-05-17. Resume in next session by reading this file first.

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
8. **DNS cutover at Cloudflare** (not register.com) at launch — change A/CNAME records when David is ready. Planned: early week of 2026-05-19.
9. **Email migration (Google Workspace)** — paused 2026-05-16 pending Cloudflare credentials. Resumes Monday 2026-05-18. Will create info@bennettvet.com (or davidbennett@bennettvet.com matching iMatrix). Need to: reclaim abandoned Workspace setup, verify domain via Cloudflare DNS, migrate email from iMatrix.
10. **Google Business Profile rename** in progress — David requested change from "Dr. Bennett's Veterinary House Calls" to "Bennett Veterinary Service" on 2026-05-17. Google's review pending over the weekend. ⚠️ He initially put descriptors in the name field (keyword stuffing); needs to edit to just `Bennett Veterinary Service` (singular, no extra text). Descriptors go in Description field, not name.
11. **Yelp rename + add "formerly" note** — old Yelp listing has 89 reviews and 16 photos under "Dr. Bennett's Veterinary House Calls." Needs rename via biz.yelp.com.
12. **Facebook rename + phone fix** — old FB page has wrong phone (510-758-7921). Should be (925) 519-2316. Old brand name still there.
13. **Apple Maps (Apple Business Connect) and Bing Places** — likely still old brand.
14. **Old iMatrix site rebrand** — David is updating the old site's title/header to "Bennett Veterinary Service / Compassionate Mobile Veterinary Service / Formerly Dr. Bennett's Veterinary House Calls" before DNS cutover.
15. **Banner image (Banner-Bennettvet.com.jpg)** — designer-made banner is on hold. Issues: "Contra Costa County only" excludes 3 Alameda County cities served; baked-in text is unreadable to Google; banner's logo differs from site logo. Currently NOT placed.

## Recommended next-session order

1. Resume Google Workspace email setup (Cloudflare creds in hand Monday)
2. Verify GBP name change result; sweep description + post if approved
3. Yelp + Facebook renames (David's manual work, instruct as needed)
4. Continue photo additions as David delivers (Alamo, Oakland Hills, home, services)
5. iMatrix old-site rebrand check-in
6. DNS cutover at Cloudflare when David greenlights
7. Sweep placeholders ([email TBD], [TO BE ADDED] for permit, [TO BE SET ON LAUNCH] for effective dates) once info is in hand

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
