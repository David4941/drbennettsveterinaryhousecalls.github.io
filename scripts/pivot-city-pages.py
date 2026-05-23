"""
Rewrite all 15 city pages from euthanasia-leaning to general-practice
positioning. Euthanasia drops to a subtle link to petsforangels.com.

What changes per file:
- <title>, meta description, og:title, og:description, twitter meta
- Service schema: serviceType + name updated
- BreadcrumbList second item updated
- H1 + hero lead
- Body content between first H2 ("Compassionate End-of-Life Care...") and
  the existing 'Nearby East Bay Communities' section is replaced with a
  per-city general-practice template (neighborhood references preserved
  so we don't end up with cookie-cutter duplicate content)

Idempotent — re-running on an already-pivoted page won't damage it.
"""
from pathlib import Path
import re
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Per-city: display name + neighborhood/landmark phrase for the intro paragraph.
# Variation here keeps the rewritten pages from triggering duplicate-content
# heuristics at Google.
CITIES = {
    "walnut-creek":  ("Walnut Creek",  "downtown's Broadway Plaza, the Iron Horse Trail, and the established neighborhoods looking up at Mt. Diablo"),
    "lafayette":     ("Lafayette",     "the Lafayette Reservoir trail, the Lamorinda hills, and the quiet residential streets above Mt. Diablo Boulevard"),
    "orinda":        ("Orinda",        "the Orinda Theater Square, the Lamorinda hills, and the wooded properties off Camino Pablo"),
    "alamo":         ("Alamo",         "Round Hill, the long driveways of the San Ramon Valley, and the oak-shaded estates of the area"),
    "martinez":      ("Martinez",      "the Martinez Marina, the historic downtown, and the hillside neighborhoods overlooking the Carquinez Strait"),
    "pleasant-hill": ("Pleasant Hill", "the Pleasant Hill War Memorial area, Gregory Gardens, and the established neighborhoods near Diablo Valley College"),
    "concord":       ("Concord",       "Todos Santos Plaza, the Crystyl Ranch area, and the neighborhoods at the foot of Mt. Diablo"),
    "clayton":       ("Clayton",       "downtown Clayton's town square, the trails near Mt. Diablo State Park, and the quiet residential streets of the Oakhurst neighborhood"),
    "moraga":        ("Moraga",        "the Rheem Valley, the campus area around Saint Mary's College, and the rolling hills of the Lamorinda foothills"),
    "el-sobrante":   ("El Sobrante",   "the rural lanes off Appian Way, the hillside properties along Valley View Road, and the open ranch land of the El Sobrante valley"),
    "pinole":        ("Pinole",        "the historic downtown along Tennent Avenue, the family neighborhoods up by Pinole Valley High, and the rolling hills toward Refugio Valley"),
    "hercules":      ("Hercules",      "the Refugio Valley Park area, the planned neighborhoods of Victoria by the Bay, and the family streets near Pinole Valley Road"),
    "piedmont":      ("Piedmont",      "the Piedmont Park Exedra, Mountain Avenue, and the tree-lined streets above Lake Merritt"),
    "oakland-hills": ("Oakland Hills", "the Skyline Boulevard ridges, the trails of Redwood Regional Park, and the wooded properties of Montclair and the Oakmore neighborhood"),
    "berkeley-hills":("Berkeley Hills","the panoramic vistas along Grizzly Peak Boulevard, the wooded Tilden Park borders, and the eucalyptus-shaded streets of the upper Berkeley hills"),
}

# Reused content blocks (uniform across cities — only the city name varies)
NEW_DESCRIPTION = "Compassionate house-call veterinary care in {city}, CA. Dr. David Bennett, DVM brings wellness exams, vaccinations, dermatology, illness diagnostics, and chronic disease care to your home. Call (925) 519-2316."
NEW_OG_DESCRIPTION = "Compassionate house-call veterinary care in {city}, California — wellness, illness, dermatology, and chronic care at home."

def head_replacements(html: str, city: str) -> str:
    """Apply all head-section replacements: title, meta, og, twitter, schema."""

    # <title>
    html = re.sub(
        r"<title>In-Home Pet Euthanasia in " + re.escape(city) + r", CA \| Bennett Veterinary Service</title>",
        f"<title>House-Call Veterinarian in {city}, CA | Bennett Veterinary Service</title>",
        html,
    )

    # <meta name="description">
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{NEW_DESCRIPTION.format(city=city)}">',
        html, count=1,
    )

    # og:title
    html = re.sub(
        r'<meta property="og:title" content="In-Home Pet Euthanasia in ' + re.escape(city) + r', CA \| Bennett Veterinary Service">',
        f'<meta property="og:title" content="House-Call Veterinarian in {city}, CA | Bennett Veterinary Service">',
        html,
    )

    # og:description
    html = re.sub(
        r'<meta property="og:description" content="Compassionate, dignified in-home pet euthanasia in ' + re.escape(city) + r', California\.">',
        f'<meta property="og:description" content="{NEW_OG_DESCRIPTION.format(city=city)}">',
        html,
    )

    # twitter:title (where present)
    html = re.sub(
        r'<meta name="twitter:title" content="In-Home Pet Euthanasia in ' + re.escape(city) + r', CA \| Bennett Veterinary Service">',
        f'<meta name="twitter:title" content="House-Call Veterinarian in {city}, CA | Bennett Veterinary Service">',
        html,
    )

    # twitter:description (where present)
    html = re.sub(
        r'<meta name="twitter:description" content="Compassionate, dignified in-home pet euthanasia in ' + re.escape(city) + r', California\.">',
        f'<meta name="twitter:description" content="{NEW_OG_DESCRIPTION.format(city=city)}">',
        html,
    )

    # JSON-LD Service schema — serviceType + name
    html = html.replace(
        '"serviceType": "In-Home Pet Euthanasia",',
        '"serviceType": "House-Call Veterinary Care",',
    )
    html = html.replace(
        f'"name": "In-Home Pet Euthanasia in {city}",',
        f'"name": "House-Call Veterinary Care in {city}",',
    )

    # BreadcrumbList — change the middle item from In-Home Pet Euthanasia → Wellness & Medical Care
    html = html.replace(
        '"@type": "ListItem", "position": 2, "name": "In-Home Pet Euthanasia", "item": "https://bennettvet.com/in-home-pet-euthanasia/"',
        '"@type": "ListItem", "position": 2, "name": "Wellness & Medical Care", "item": "https://bennettvet.com/services/"',
    )

    return html


def new_body_section(city: str, snippet: str) -> str:
    """Build the new general-practice body that replaces the old euthanasia content.

    Spans from the first H2 ("Compassionate End-of-Life Care...") through the
    last paragraph BEFORE the 'Nearby East Bay Communities We Serve' section.
    """
    return f"""      <h2>House-Call Veterinary Care in {city}</h2>
      <p>From {snippet}, Dr. Bennett brings compassionate house-call veterinary care to {city} families and their pets. No carriers, no waiting rooms, no unfamiliar smells &mdash; just calm, unhurried attention for your pet in the place they feel safest.</p>

      <h2>Services for {city} Pets</h2>
      <ul>
        <li>Wellness exams and vaccinations</li>
        <li>Veterinary dermatology and skin care</li>
        <li>Illness diagnostics and treatment</li>
        <li>Chronic disease management &mdash; diabetes, thyroid, kidney</li>
        <li>Hospice and comfort care</li>
        <li>Health certificates</li>
      </ul>
      <p><a href="/services/">See the full list of services &rarr;</a></p>

      <h2>Why a House Call?</h2>
      <p>Many pets find clinic visits stressful &mdash; the car ride, the carrier, the unfamiliar smells, the other animals. For {city} families who would rather their pet stay calm and comfortable, a house call means Dr. Bennett comes to you. There is no waiting room, no rush, and you stay with your pet through the entire visit.</p>

      <h2>End-of-Life Care</h2>
      <p>For families facing the decision of saying goodbye to a beloved pet, Dr. Bennett offers compassionate in-home euthanasia through <a href="https://petsforangels.com" target="_blank" rel="noopener">Pets for Angels</a> &mdash; a separate practice dedicated exclusively to peaceful, dignified end-of-life care at home.</p>

"""


def hero_replacements(html: str, city: str) -> str:
    """Replace H1 + hero lead with general-practice copy."""
    html = re.sub(
        r"<h1>In-Home Pet Euthanasia in " + re.escape(city) + r", CA</h1>",
        f"<h1>House-Call Veterinarian in {city}, CA</h1>",
        html,
    )
    html = re.sub(
        r'<p class="hero__lead">A peaceful goodbye for your pet, in the comfort of your ' + re.escape(city) + r' home\.</p>',
        f'<p class="hero__lead">Compassionate house-call veterinary care for {city} pets and the families who love them.</p>',
        html,
    )
    return html


def replace_body_section(html: str, city: str, snippet: str) -> str:
    """Cut out the old euthanasia-focused body (first H2 through the
    paragraph before 'Nearby East Bay Communities') and replace with the
    new general-practice template.
    """
    # Pattern: start at the first H2 after the figure, end just before
    # the 'Nearby East Bay Communities' H2. The DOTALL flag lets . match
    # newlines so we can span the multi-paragraph section.
    pattern = re.compile(
        r"      <h2>Compassionate End-of-Life Care, at Home in " + re.escape(city) + r"</h2>.*?(?=\s*<h2>Nearby East Bay Communities)",
        re.DOTALL,
    )
    new_body = new_body_section(city, snippet)
    return pattern.sub(new_body, html, count=1)


def process_city(slug: str, city: str, snippet: str) -> str:
    path = PROJECT_ROOT / slug / "index.html"
    if not path.exists():
        return f"  SKIP (not found): {slug}"

    html = path.read_text(encoding="utf-8")
    original = html

    html = head_replacements(html, city)
    html = hero_replacements(html, city)
    html = replace_body_section(html, city, snippet)

    if html == original:
        return f"  {slug:<16} -> no changes (already pivoted?)"

    path.write_text(html, encoding="utf-8", newline="\n")
    return f"  {slug:<16} -> rewritten"


def main() -> int:
    print(f"Pivoting {len(CITIES)} city pages to general-practice positioning...")
    for slug, (city, snippet) in CITIES.items():
        print(process_city(slug, city, snippet))
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
