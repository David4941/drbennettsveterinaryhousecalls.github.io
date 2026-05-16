#!/usr/bin/env python3
"""
Generate sitemap.xml for bennettvet.com from the current site state.

Runs automatically on every Netlify deploy via netlify.toml [build].command.
Also invoked by the local deploy.ps1 wrapper.

Behavior:
- Walks all *.html under the project root
- Skips dev-helper files (deploy-netlify-steps, setup-github-steps),
  404.html, and the thank-you/ form-confirmation page
- Skips any page with <meta name='robots' content='noindex'>
  (privacy/, accessibility/) so we never give Google conflicting signals
- Derives canonical URL from the file path
- <lastmod> comes from the file's last git-commit date (falls back to
  mtime if untracked or git isn't available). lastmod is the most
  important SEO field for crawl scheduling.
- Auto-detects the page's primary image from <meta property='og:image'>
  and emits an <image:image> entry with caption (og:image:alt) and
  title (page <title>). This means new image meta added to any page is
  automatically reflected in the sitemap without manual edits.
- Sorts: home first, then by priority desc, then alphabetically by URL
"""

from __future__ import annotations
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

BASE_URL = "https://bennettvet.com"
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Files to skip entirely (never in sitemap)
SKIP_FILES = {
    "404.html",                      # error page
    "deploy-netlify-steps.html",     # local dev helper (gitignored)
    "setup-github-steps.html",       # local dev helper (gitignored)
}
# Directories to skip during walk
SKIP_DIRS = {".git", ".netlify", ".claude", "node_modules", "images", "css", "scripts"}

# Priority by URL path (modern Google mostly ignores priority, but it's
# still meaningful for some search engines and harmless).
PRIORITY_BY_PATH = {
    "/": 1.0,
    "/in-home-pet-euthanasia/": 0.9,
    "/services/": 0.7,
    "/contact/": 0.6,
    "/about/": 0.5,
}
DEFAULT_PRIORITY = 0.7   # city pages, etc.

NOINDEX_RE = re.compile(
    r'<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*noindex',
    re.IGNORECASE,
)
OG_IMAGE_RE = re.compile(
    r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']+)["\']',
    re.IGNORECASE,
)
OG_IMAGE_ALT_RE = re.compile(
    r'<meta\s+property=["\']og:image:alt["\']\s+content=["\']([^"\']+)["\']',
    re.IGNORECASE,
)
TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.IGNORECASE)


def file_to_url(path: Path) -> str | None:
    """Convert a project file path to its canonical site URL, or None to skip."""
    rel = path.relative_to(PROJECT_ROOT).as_posix()
    # form-confirmation page intentionally excluded
    if rel == "thank-you/index.html":
        return None
    if rel == "index.html":
        return f"{BASE_URL}/"
    if rel.endswith("/index.html"):
        return f"{BASE_URL}/{rel[:-len('index.html')]}"
    if rel.endswith(".html"):
        return f"{BASE_URL}/{rel}"
    return None


def get_lastmod(path: Path) -> str:
    """Return ISO-8601 last-modified: git commit time if available, else mtime."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(path)],
            capture_output=True, text=True, cwd=PROJECT_ROOT, check=False,
            timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return mtime.isoformat()


def is_indexable(html: str) -> bool:
    return NOINDEX_RE.search(html) is None


def extract_image(html: str) -> dict | None:
    """Return {url, caption, title} for the page's og:image, or None."""
    m = OG_IMAGE_RE.search(html)
    if not m:
        return None
    url = unescape(m.group(1))
    alt_m = OG_IMAGE_ALT_RE.search(html)
    caption = unescape(alt_m.group(1)) if alt_m else ""
    title_m = TITLE_RE.search(html)
    title = unescape(title_m.group(1).strip()) if title_m else ""
    return {"url": url, "caption": caption, "title": title}


def walk_html_files() -> list[Path]:
    out: list[Path] = []
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Prune skip-dirs in-place (also skip hidden dirs)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for name in files:
            if name.endswith(".html") and name not in SKIP_FILES:
                out.append(Path(root) / name)
    out.sort()
    return out


def build_sitemap() -> tuple[str, int, int]:
    """Return (xml string, page count, image count)."""
    entries = []
    for html_file in walk_html_files():
        html = html_file.read_text(encoding="utf-8")
        if not is_indexable(html):
            continue
        url = file_to_url(html_file)
        if not url:
            continue
        rel_path = url[len(BASE_URL):]
        priority = PRIORITY_BY_PATH.get(rel_path, DEFAULT_PRIORITY)
        entries.append({
            "url": url,
            "lastmod": get_lastmod(html_file),
            "priority": priority,
            "image": extract_image(html),
        })

    # Sort: home first, then by priority desc, then by URL
    entries.sort(key=lambda e: (e["url"] != f"{BASE_URL}/", -e["priority"], e["url"]))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
        '',
        '  <!-- Auto-generated by scripts/build-sitemap.py. Do not edit by hand. -->',
        '',
    ]
    image_count = 0
    for e in entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{xml_escape(e['url'])}</loc>")
        lines.append(f"    <lastmod>{e['lastmod']}</lastmod>")
        lines.append(f"    <priority>{e['priority']:.1f}</priority>")
        if e["image"]:
            img = e["image"]
            lines.append("    <image:image>")
            lines.append(f"      <image:loc>{xml_escape(img['url'])}</image:loc>")
            if img["caption"]:
                lines.append(f"      <image:caption>{xml_escape(img['caption'])}</image:caption>")
            if img["title"]:
                lines.append(f"      <image:title>{xml_escape(img['title'])}</image:title>")
            lines.append("    </image:image>")
            image_count += 1
        lines.append("  </url>")
    lines.append("")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n", len(entries), image_count


def main() -> int:
    xml, pages, images = build_sitemap()
    out_path = PROJECT_ROOT / "sitemap.xml"
    out_path.write_text(xml, encoding="utf-8", newline="\n")
    print(f"sitemap.xml generated: {pages} URLs, {images} with image entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
