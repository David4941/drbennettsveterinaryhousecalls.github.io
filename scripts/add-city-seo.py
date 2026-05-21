"""
Add BreadcrumbList schema + 'Nearby East Bay communities' cross-links to
every city page. Idempotent — re-running won't double-insert.

Why:
- BreadcrumbList helps Google render breadcrumbs in search results, boosts
  the click-through rate, and clarifies site hierarchy.
- Cross-linking city pages to nearby ones builds a denser internal link
  graph, which helps Google understand the service-area cluster and
  distributes PageRank to less-popular city pages.
"""

from pathlib import Path
import re
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# city slug -> display name + adjacent cities (slug + display)
CITIES = {
    "walnut-creek":  ("Walnut Creek",  ["pleasant-hill", "lafayette", "concord", "alamo"]),
    "lafayette":     ("Lafayette",     ["walnut-creek", "orinda", "moraga", "pleasant-hill"]),
    "orinda":        ("Orinda",        ["lafayette", "moraga", "berkeley-hills", "piedmont"]),
    "alamo":         ("Alamo",         ["walnut-creek", "lafayette", "moraga"]),
    "martinez":      ("Martinez",      ["pleasant-hill", "concord", "walnut-creek", "hercules"]),
    "pleasant-hill": ("Pleasant Hill", ["walnut-creek", "concord", "martinez", "lafayette"]),
    "concord":       ("Concord",       ["pleasant-hill", "walnut-creek", "clayton", "martinez"]),
    "clayton":       ("Clayton",       ["concord", "walnut-creek", "pleasant-hill"]),
    "moraga":        ("Moraga",        ["lafayette", "orinda", "alamo", "walnut-creek"]),
    "el-sobrante":   ("El Sobrante",   ["pinole", "hercules", "berkeley-hills"]),
    "pinole":        ("Pinole",        ["hercules", "el-sobrante"]),
    "hercules":      ("Hercules",      ["pinole", "el-sobrante", "martinez"]),
    "piedmont":      ("Piedmont",      ["oakland-hills", "berkeley-hills", "orinda"]),
    "oakland-hills": ("Oakland Hills", ["piedmont", "berkeley-hills", "orinda"]),
    "berkeley-hills":("Berkeley Hills",["oakland-hills", "piedmont", "orinda", "el-sobrante"]),
}

# Markers we look for to find injection points and detect prior runs
BREADCRUMB_MARK = "BreadcrumbList"
NEARBY_MARK = "Nearby East Bay communities"


def breadcrumb_schema(slug: str, display: str) -> str:
    return f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://bennettvet.com/"}},
      {{"@type": "ListItem", "position": 2, "name": "In-Home Pet Euthanasia", "item": "https://bennettvet.com/in-home-pet-euthanasia/"}},
      {{"@type": "ListItem", "position": 3, "name": "{display}", "item": "https://bennettvet.com/{slug}/"}}
    ]
  }}
  </script>
"""


def nearby_section(neighbors: list[str]) -> str:
    items = "\n".join(
        f'          <li><a href="/{slug}/">{CITIES[slug][0]}</a></li>'
        for slug in neighbors
    )
    return f"""      <h2>Nearby East Bay Communities We Serve</h2>
      <p>Dr. Bennett also provides house-call veterinary care in nearby communities. If you have friends or neighbors in any of these cities who might benefit, please share:</p>
      <ul>
{items}
      </ul>

"""


def process_city(slug: str, display: str, neighbors: list[str]) -> str:
    path = PROJECT_ROOT / slug / "index.html"
    if not path.exists():
        return f"  SKIP (file not found): {slug}"

    html = path.read_text(encoding="utf-8")
    changed = False
    notes = []

    # 1. Inject BreadcrumbList schema before </head>, if not already present
    if BREADCRUMB_MARK not in html:
        inject = breadcrumb_schema(slug, display)
        html = html.replace("</head>", inject + "</head>", 1)
        changed = True
        notes.append("+breadcrumb")
    else:
        notes.append("breadcrumb-exists")

    # 2. Inject 'Nearby East Bay Communities' section before the closing
    #    cta-block, if not already present
    if NEARBY_MARK not in html:
        section = nearby_section(neighbors)
        # Find the CTA block that comes just before </main>; insert before it.
        # The pattern looks for the FIRST cta-block in the .container.content area.
        cta_pattern = r'(\s*)(<div class="cta-block">)'
        match = re.search(cta_pattern, html)
        if match:
            indent = match.group(1).rstrip("\n").rstrip()
            html = html.replace(match.group(0), f"\n      {section}{match.group(1)}{match.group(2)}", 1)
            changed = True
            notes.append("+nearby")
        else:
            notes.append("no-cta-anchor")
    else:
        notes.append("nearby-exists")

    if changed:
        path.write_text(html, encoding="utf-8", newline="\n")

    return f"  {slug:<16} -> {', '.join(notes)}"


def main() -> int:
    print(f"Processing {len(CITIES)} city pages...")
    for slug, (display, neighbors) in CITIES.items():
        print(process_city(slug, display, neighbors))
    print("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
