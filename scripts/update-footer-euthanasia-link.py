"""
Update the footer Quick Links across every HTML page on the site.

Before:  <li><a href="/in-home-pet-euthanasia/">In-Home Pet Euthanasia</a></li>
After:   <li><a href="https://petsforangels.com" target="_blank" rel="noopener">Pet Euthanasia Services</a></li>

Idempotent — pages already updated are skipped.
"""
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".netlify", ".claude", "node_modules", "images", "css", "scripts"}

OLD_LINK = '<li><a href="/in-home-pet-euthanasia/">In-Home Pet Euthanasia</a></li>'
NEW_LINK = '<li><a href="https://petsforangels.com" target="_blank" rel="noopener">Pet Euthanasia Services</a></li>'


def walk_html_files():
    out = []
    for root, dirs, files in __import__("os").walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for name in files:
            if name.endswith(".html"):
                out.append(Path(root) / name)
    return sorted(out)


def main() -> int:
    updated = 0
    skipped = 0
    for path in walk_html_files():
        html = path.read_text(encoding="utf-8")
        if OLD_LINK not in html:
            skipped += 1
            continue
        html = html.replace(OLD_LINK, NEW_LINK)
        path.write_text(html, encoding="utf-8", newline="\n")
        rel = path.relative_to(PROJECT_ROOT)
        print(f"  {rel} -> updated")
        updated += 1
    print(f"\n{updated} files updated, {skipped} already current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
