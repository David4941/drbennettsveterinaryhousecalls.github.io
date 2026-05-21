# Bennett Veterinary Service — Rebrand & Launch Checklist

Updated: 2026-05-20.
Print from VS Code: open this file → File → Print (or Ctrl+P).

This is the complete list of remaining work to fully transition from
"Dr. Bennett's Veterinary House Calls" / iMatrix-hosted site to
"Bennett Veterinary Service" on the new Netlify-hosted site, with
Google Workspace email and the domain at GoDaddy.

═══════════════════════════════════════════════════════════════════════
ACTIVE — STILL TO DO
═══════════════════════════════════════════════════════════════════════

──── EMAIL & GOOGLE WORKSPACE ────────────────────────────────────────

[ ] Set up iMatrix → bennettvet@gmail.com email forwarding (safety net)
    Where: iMatrix email control panel (the one used to add the TXT
    record). Set davidbennett@bennettvet.com and info@bennettvet.com to
    forward to bennettvet@gmail.com.
    Why: catches in-flight emails during the MX cutover window so
    nothing gets lost.
    When: a day or two BEFORE cutover.

[ ] Configure Workspace Gmail signature
    Where: mail.google.com (signed in as davidbennett@bennettvet.com)
    → Settings (gear icon) → See all settings → Signature
    Suggested:
    --
    David Bennett, DVM
    Bennett Veterinary Service
    (formerly Dr. Bennett's Veterinary House Calls)
    (925) 519-2316  ·  bennettvet.com

[ ] Configure Workspace Gmail forwarding rule (optional)
    Where: mail.google.com → Settings → Forwarding and POP/IMAP
    If you want a copy of all Workspace email to also go to
    bennettvet@gmail.com or davidbvet@icloud.com as backup, set it up
    here.

[ ] Enable 2-Step Verification on davidbennett@bennettvet.com
    Where: https://myaccount.google.com/security
    Strongly recommended for the business admin account. Use your
    phone for the 2FA codes. Save backup codes somewhere safe.


──── DOMAIN TRANSFER (waiting on iMatrix auth code) ──────────────────

[ ] Create GoDaddy account if not already done
    Where: https://www.godaddy.com → Sign In → Create Account
    Use davidbvet@icloud.com or bennettvet@gmail.com as the account
    email. Pick a strong password. Save it.

[ ] Receive auth/EPP code from iMatrix
    Status: requested 2026-05-18. iMatrix said 3-7 days. Window: by
    ~2026-05-25. Follow up if not received by then.

[ ] Transfer domain to GoDaddy
    Where: GoDaddy → Domains → Transfer Domain → enter bennettvet.com
    Paste the auth/EPP code, pay ~$10 transfer fee (includes renewal).
    ICANN-mandated 5-7 day waiting period after.

[ ] Confirm domain transfer in both old and new registrar emails
    You'll get confirmation emails from both — click "Approve" /
    "Confirm" in each.


──── WEBSITE CUTOVER DAY (one big coordinated step) ──────────────────

Pick a quiet day (early morning or late evening; mid-week is best,
not Friday). Plan ~30 min of focused work plus monitoring for 24 hrs.

[ ] Day-of pre-flight
    [ ] Double-check Workspace inbox is signed in and working
    [ ] Confirm iMatrix forwarding rule is active (from above)
    [ ] Have Cloudflare login open
    [ ] Have Netlify dashboard open

[ ] Change A and CNAME records at Cloudflare (website cutover)
    Where: dash.cloudflare.com → bennettvet.com → DNS
    Remove existing A record pointing to iMatrix's IP.
    Add A record pointing to Netlify's apex IP (Netlify provides this).
    CNAME for www → apex-loadbalancer.netlify.com.

[ ] Change MX records at Cloudflare (email cutover)
    Remove iMatrix MX record (mx.imatrixbase.com).
    Add Google's MX record:
        Type: MX
        Name: @
        Priority: 1
        Value: smtp.google.com
        TTL: 3600 (or Auto)

[ ] Update SPF record at Cloudflare
    Change existing TXT from:
        v=spf1 include:_spf.hostedemail.com ~all
    To:
        v=spf1 include:_spf.google.com ~all

[ ] Wait 10-30 minutes for DNS propagation

[ ] Verify website
    Visit https://bennettvet.com — should load new site (not old)
    Try a few old URLs: /about-us.html should redirect to /about/
    Try a city page: /walnut-creek/ should load

[ ] Verify email
    Send a test from davidbvet@icloud.com → davidbennett@bennettvet.com
    Should arrive in Workspace Gmail within 1-2 minutes
    Send a test FROM davidbennett@bennettvet.com → personal Gmail
    Should arrive normally

[ ] Monitor for 24 hours
    Watch bennettvet@gmail.com for any forwarded emails from iMatrix
    (indicates email still routing to iMatrix briefly during the
    propagation window). Should taper off quickly.


──── GOOGLE BUSINESS PROFILE (in progress) ──────────────────────────

[ ] Confirm name change to "Bennett Veterinary Service" went through
    Google your business — does the panel on right show new name?

[ ] Edit business description in GBP
    Where: https://business.google.com → your business → Edit profile
    → About → Description
    Add line: "Bennett Veterinary Service was formerly known as
    Dr. Bennett's Veterinary House Calls."

[ ] Update GBP website URL to https://bennettvet.com (after cutover)
    Should already be correct, but verify.

[ ] Optional: publish a "We've rebranded" Post in GBP
    Edit profile → Posts → Add update
    "Dr. Bennett's Veterinary House Calls is now Bennett Veterinary
    Service. Same Dr. Bennett, same compassionate in-home care for
    East Bay pets and families. Call (925) 519-2316."


──── YELP ────────────────────────────────────────────────────────────

⚠ Yelp Support confirmed (2026-05-20) they will not change the business
  name until bennettvet.com displays the new name. So the rename has
  to wait for DNS cutover. The 89 reviews stay attached either way.

[ ] AFTER DNS CUTOVER: request name change on biz.yelp.com
    Where: biz.yelp.com → Business Information → Name
    New name: Bennett Veterinary Service (singular, no extra text)
    Yelp will re-crawl bennettvet.com to verify the new name is
    displayed prominently in the header/title.

[ ] Update Yelp business description (do this any time)
    Where: biz.yelp.com → Business Information → Description
    Add: "Bennett Veterinary Service (formerly Dr. Bennett's
    Veterinary House Calls) — same Dr. Bennett, same in-home care."

[ ] If Yelp still refuses after cutover, supply documentation:
    CA Vet License #12991 + DBA filing for Bennett Veterinary Service.


──── FACEBOOK ────────────────────────────────────────────────────────

[ ] Sign in to Facebook with the account that admins the page

[ ] Update page name to "Bennett Veterinary Service"
    Settings → Page info → Name
    (Facebook reviews name changes for 1-7 days)

[ ] Fix phone number — change from 510-758-7921 to (925) 519-2316

[ ] Update About / Description with rebrand notice
    "Bennett Veterinary Service (formerly Dr. Bennett's Veterinary
    House Calls). Compassionate mobile veterinary care throughout
    the East Bay."

[ ] Update website URL to https://bennettvet.com

[ ] Publish "We've rebranded" Facebook post (optional, one-time)


──── APPLE MAPS (Apple Business Connect) ────────────────────────────

[ ] Resume the Apple Business Connect setup
    Where: https://businessconnect.apple.com
    Sign in with your Apple ID (davidbvet@icloud.com)
    Last attempt hit a snag — try again, claim/edit your listing
    Update name to "Bennett Veterinary Service" (singular)
    Update phone, website, description
    Verify ownership via phone call


──── BING PLACES ─────────────────────────────────────────────────────

[ ] Wait until GBP name change is approved by Google

[ ] Then go to https://www.bingplaces.com → sync from GBP
    Once GBP is correct, the sync pulls correct info into Bing.


──── GOOGLE SEARCH CONSOLE (after cutover) ───────────────────────────

What it is: free Google tool that shows how Google sees your site —
which queries bring visitors, which pages are indexed, any crawl
errors, mobile-usability issues, and Core Web Vitals scores. Set up
once and check it monthly.

[ ] Go to https://search.google.com/search-console
    Sign in with the Google account you use for GBP / Workspace.

[ ] Add property → "Domain" (not "URL prefix")
    Enter: bennettvet.com
    Domain property covers https/http/www/non-www in one shot.

[ ] Verify ownership via DNS TXT record at Cloudflare
    GSC will give you a string like google-site-verification=XXXX
    Add it as a TXT record at Cloudflare (Name: @, Value: that string)
    Click Verify in GSC. Takes a few minutes.

[ ] Submit sitemap
    Sitemaps → Add a new sitemap → enter "sitemap.xml" → Submit
    Status should be "Success" within a day.

[ ] Monthly check-in: look at Performance, Coverage, Core Web Vitals
    First useful data takes ~7 days to populate. Don't worry about
    rankings the first month; just confirm pages are being indexed.


──── iMATRIX OLD SITE ────────────────────────────────────────────────

[ ] Update old iMatrix site title/header to new brand
    "Bennett Veterinary Service" / "Compassionate Mobile Veterinary
    Service" / "Formerly Dr. Bennett's Veterinary House Calls"
    Only do this if iMatrix's editor is quick. Otherwise skip — the
    DNS cutover replaces the whole site anyway.

[ ] AFTER cutover is verified (~48 hours stable): call iMatrix to
    cancel the subscription. Get cancellation confirmation in writing
    (email). Don't tell them you're leaving until you're DONE leaving.


──── PHOTOS STILL NEEDED ─────────────────────────────────────────────

[ ] Alamo city page hero photo
    Suggestion: Round Hill area, San Ramon Valley, or oak-shaded
    streets. 16:9 landscape, ~1600x900 ideal.

[ ] Oakland Hills city page hero photo
    Suggestion: Montclair village, view from Skyline Blvd, or
    eucalyptus/redwood scenery. 16:9 landscape.

[ ] Home page hero photo
    Best fit: a service-in-action shot like the new Services page
    photo, but landscape (16:9). Could be Dr. Bennett with a dog or
    cat in a home setting.

[ ] More wellness/service photos for future reviews page or
    additional pages (optional)


──── REVIEWS PAGE (planned, you'll provide content) ──────────────────

[ ] Browse Yelp + Google reviews; pick 8-12 favorites

[ ] Send me each as:
        "Quote text..."
        — Sarah B., April 2026 (Yelp, 5★)

[ ] Send me the Google Business Profile URL once GBP rename is
    approved (so we can link to "see all reviews on Google")

[ ] I'll build:
    - /reviews/ page with all featured reviews + AggregateRating
      schema
    - Home page section with 3-card preview
    - Two prominent buttons: "See us on Yelp" / "Find us on Google"
    - Update old iMatrix /veterinarian-reviews.html redirect to point
      to /reviews/


──── FOOTER PLACEHOLDERS (one-pass sweep when info is ready) ────────

[ ] Hospital Permit # — currently "[TO BE ADDED]" in every footer
    When you have the number, paste it here and I'll sweep all 24
    pages in one pass.

[ ] Privacy policy "Effective Date" — currently
    "[TO BE SET ON LAUNCH]" — set to the actual cutover date on
    launch day.

[ ] Accessibility statement "Effective Date" — same as above.

[ ] Public contact email on privacy page — currently "[email TBD]"
    After Workspace cutover, change to info@bennettvet.com.


──── REGULATORY ──────────────────────────────────────────────────────

[ ] Confirm CA VMB (Veterinary Medical Board) regulatory disclosure
    wording is exactly what's required
    Send a brief email to vmb@dca.ca.gov asking them to confirm the
    exact wording for the records-access disclosure currently in the
    footer.


══════════════════════════════════════════════════════════════════════
ALREADY DONE (for reference)
══════════════════════════════════════════════════════════════════════

[X] Built complete new website on Netlify (24 pages: home, services,
    about, contact, privacy, accessibility, 15 city pages, etc.)
[X] Logo placed in every page header
[X] Favicon + apple-touch-icon set up
[X] Rebrand notice "Formerly Dr. Bennett's Veterinary House Calls"
    added to homepage, About, and every footer
[X] schema.org alternateName added across all 17 schema-bearing pages
[X] 17 of 20 pages have images:
    Home (no hero yet), About (Dr. Bennett portrait), Services (NEW —
    wellness exam), Contact (Dr. Bennett with two dogs), Walnut Creek,
    Orinda, Pleasant Hill, Concord, Clayton, Piedmont, Hercules,
    Lafayette, Martinez, Pinole, El Sobrante, Moraga, Berkeley Hills.
[X] FAQ section + FAQPage schema on /in-home-pet-euthanasia/
[X] "How to Prepare" section, Trust Signals, HHHHHMM Quality-of-Life
    Framework on /in-home-pet-euthanasia/
[X] Formspree contact form wired (xlgajjyz)
[X] 301 redirects from old iMatrix URLs (e.g., /about-us.html →
    /about/) — preserves 16 years of SEO at cutover
[X] Security headers: HSTS, CSP, X-Frame-Options, Content-Type-Options,
    Referrer-Policy, Permissions-Policy, COOP, CORP
[X] Auto-generating sitemap.xml on every deploy (build-sitemap.py)
[X] CCPA/CPRA section in privacy policy
[X] Prescription disclaimer in every footer (CA Bus. & Prof. Code §4170)
[X] Accessibility statement (/accessibility/, WCAG 2.1 AA)
[X] Google Workspace set up at bennettvet.com
[X] davidbennett@bennettvet.com primary user created
[X] info@bennettvet.com alias active (plus bennett@ also)
[X] Workspace password set, tested working
[X] Google domain verification TXT record live at Cloudflare
[X] MX records for cutover day documented (smtp.google.com priority 1)

══════════════════════════════════════════════════════════════════════
TIMELINE SUMMARY
══════════════════════════════════════════════════════════════════════

Today (2026-05-20):
  - Continue collecting photos
  - Set up iMatrix forwarding to bennettvet@gmail.com
  - Configure Gmail signature + 2-Step Verification
  - Create GoDaddy account

By Wednesday 2026-05-25:
  - Auth code from iMatrix should arrive
  - Initiate transfer at GoDaddy

By Friday 2026-05-23 (or whenever ready):
  - Pick cutover day (recommend mid-week early morning)
  - Coordinate DNS changes at Cloudflare

Cutover day:
  - Change A/CNAME (web) + MX (email) + SPF at Cloudflare
  - Verify site and email
  - Begin 24-hr monitoring

48 hours after verified working:
  - Cancel iMatrix subscription
  - Update old site references in any places not yet handled
  - Continue Apple Maps + Bing Places rebrand follow-ups

══════════════════════════════════════════════════════════════════════
KEY DETAILS — KEEP HANDY
══════════════════════════════════════════════════════════════════════

Domain:               bennettvet.com
DBA:                  Bennett Veterinary Service
California Vet License: #12991
Phone:                (925) 519-2316
Business address:     Walnut Creek, CA 94598

Workspace login:      davidbennett@bennettvet.com
Recovery email:       davidbvet@icloud.com
Personal Gmail:       bennettvet@gmail.com

New website host:     Netlify (preview: bennettvet-preview.netlify.app)
DNS host:             Cloudflare
Domain registrar:     register.com (will transfer to GoDaddy)
Email host (current): iMatrix → moving to Google Workspace
Email host (target):  Google Workspace (smtp.google.com)

GitHub repo:          github.com/David4941/drbennettsveterinaryhousecalls.github.io

Google verification TXT (already live in DNS):
  google-site-verification=LS3StdqdvdIrFi_VcQQZkxdTQ2Y822DHhpXZBbtFTB0

═══════════════════════════════════════════════════════════════════════
END OF CHECKLIST
═══════════════════════════════════════════════════════════════════════
