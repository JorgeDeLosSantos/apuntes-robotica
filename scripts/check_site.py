#!/usr/bin/env python3
"""Sanity-check the static Jupyter Book 2 export before GitHub Pages upload."""

from html.parser import HTMLParser
import os
from pathlib import Path
from urllib.parse import urlsplit

SITE = Path("_build/html")
BASE_URL = os.environ.get("BASE_URL", "/apuntes-robotica").rstrip("/")
STATCOUNTER_MARKER = "sc_project=13211697"
STATCOUNTER_SECURITY = 'sc_security="fb36e920"'
PAGES = (
    "index.html",
    "introrob/index.html",
    "htra/index.html",
    "fkin/index.html",
    "ikin/index.html",
    "dkin/index.html",
    "dyna/index.html",
    "gentra/index.html",
    "premat/index.html",
    "numed/index.html",
)


class SiteLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"a", "img", "script", "link", "source"}:
            return
        values = dict(attrs)
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.links.append((tag, attribute, values[attribute]))


def main():
    if not BASE_URL.startswith("/") or BASE_URL == "/":
        raise SystemExit("Set BASE_URL to the repository path (e.g. /apuntes-robotica).")

    problems = []
    checks = 0
    for page in PAGES:
        html_path = SITE / page
        if not html_path.is_file():
            problems.append(f"Missing HTML page: {html_path}")
            continue
        content = html_path.read_text(encoding="utf-8")
        if content.count(STATCOUNTER_MARKER) != 1:
            problems.append(f"{page}: expected exactly one robotics Statcounter tag")
        if STATCOUNTER_SECURITY not in content:
            problems.append(f"{page}: missing robotics Statcounter security code")
        parser = SiteLinks()
        parser.feed(content)
        for tag, attribute, value in parser.links:
            parsed = urlsplit(value)
            if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
                continue  # External links, anchors and relative links.
            checks += 1
            path = parsed.path
            if path != BASE_URL and not path.startswith(BASE_URL + "/"):
                problems.append(f"{page}: {tag}.{attribute} points outside BASE_URL: {value}")
                continue
            relative = path[len(BASE_URL):].lstrip("/")
            destination = SITE / relative
            if relative and not destination.is_file() and not (destination / "index.html").is_file():
                problems.append(f"{page}: target not found: {value}")

    if problems:
        print("\n".join(problems[:40]))
        raise SystemExit(f"Failed: {len(problems)} broken root-relative URLs or files.")
    print(f"Validated {len(PAGES)} pages and {checks} root-relative links with BASE_URL={BASE_URL}.")


if __name__ == "__main__":
    main()
