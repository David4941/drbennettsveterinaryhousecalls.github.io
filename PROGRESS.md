# Bennett Vet new-site — progress notes

Updated: 2026-05-10. Resume in next session by reading this file first.

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

**All 14 city pages BUILT** (with consistent template, intro copy, SEO schema):
- Walnut Creek, Lafayette, Orinda, Alamo, Martinez, Pleasant Hill, Concord, Clayton, Moraga, El Sobrante, Pinole, Hercules, Oakland Hills, Berkeley Hills.

Photos in place on: Walnut Creek (bridges), Orinda (theater), Pleasant Hill (War Memorial — floated portrait inset), Concord (Mt. Diablo), Clayton (downtown park / dancing children sculpture, 16:9 hero).

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

## Open items / decisions David still needs to provide

1. **Public contact email** — placeholder `[email TBD]` on privacy page.
2. **Hospital permit #** — placeholder `[TO BE ADDED]` in every footer.
3. **Privacy policy effective date** — currently `[TO BE SET ON LAUNCH]`.
4. **Formspree form ID** — `/contact/index.html` has placeholder `YOUR_FORM_ID_HERE`. David needs to:
    - Sign in at formspree.io, create a new form
    - Copy the form endpoint URL
    - Replace the placeholder
    - In Formspree dashboard, configure the autoresponder with "do not reply" wording (instructions are in HTML comments above the form)
5. **City photos still to swap in** — Lafayette, Alamo, Martinez, Moraga, El Sobrante, Pinole, Hercules, Oakland Hills, Berkeley Hills currently text-only.
6. **HEIC photo conversions** — bennettvet-pictures folder has HEIC files (Pleasant Hill, more Orinda, more Walnut Creek) that need David to "Save as JPEG" in Windows Photos before re-running the optimizer.
7. **CA VMB regulatory disclosure verification** — email vmb@dca.ca.gov to confirm exact wording required.
8. **Final review + register.com DNS cutover at launch** — change A/CNAME records at register.com when David is ready.

## Recommended next-session order

1. Review the live preview at https://bennettvet-preview.netlify.app on desktop and phone.
2. Sort out Formspree form ID + autoresponder (so the contact form actually works).
3. As David provides email, permit #, and effective date — sweep the placeholders.
4. Convert and swap in remaining city photos.
5. Confirm CA VMB regulatory wording.
6. DNS cutover at register.com when David gives the green light.

## Important constraints (do not change)

- Live `bennettvet.com` (iMatrix) must remain undisturbed until launch.
- Domain registrar: **register.com** (DNS will be changed there at launch).
- Keep `bennettvet.com` as primary domain (16 years of SEO equity).
- No git pushes to remote until explicitly authorized.

## Photo source paths (for next-session reference)

Most photos: `C:\Users\Vetpe\OneDrive\Docusign documents\Desktop\`
- `web-16x9\` — landscape JPG/PNG
- `web-1;1\` — square JPG/PNG
- `bennettvet-pictures\` — mostly HEIC (need conversion)
- Dr. Bennett portraits at parent Desktop level

Earlier abandoned attempt at `C:\Users\Vetpe\dev\Bennettvet\` — useful regulatory text already mined into footers.
