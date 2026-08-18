#!/usr/bin/env python3

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from urllib.parse import quote

BASE_URL = "https://aiphad0c.github.io/AIphaD0ctrine"
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "sitemap.xml"

# Tiedostot ja hakemistot, joita ei julkaista hakukoneiden sitemapissa.
EXCLUDED_NAMES = {
    "README.md",
    "LICENSE.md",
    "CONTRIBUTING.md",
}

EXCLUDED_DIRECTORIES = {
    ".git",
    ".github",
    "_layouts",
    "_includes",
    "_sass",
    "assets",
    "scripts",
    "vendor",
    "node_modules",
}


def read_front_matter(path: Path) -> dict[str, str]:
    """Read simple key: value pairs from Jekyll YAML front matter."""
    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        return {}

    match = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        return {}

    metadata: dict[str, str] = {}

    for line in match.group(1).splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("'\"")

    return metadata


def is_publishable(path: Path) -> bool:
    """Include Markdown pages that have Jekyll front matter."""
    relative = path.relative_to(ROOT)

    if path.name in EXCLUDED_NAMES:
        return False

    if any(part in EXCLUDED_DIRECTORIES for part in relative.parts):
    return False

    # VIAL pages are intentionally published without front matter.
    if re.fullmatch(r"vial\d+\.md", path.name, re.IGNORECASE):
        return True

metadata = read_front_matter(path)

    # Jekyll pages in this repository use front matter.
    if not metadata:
        return False

    # Allow an explicit sitemap exclusion when needed.
    if metadata.get("sitemap", "").lower() in {"false", "no", "0"}:
        return False

    return True


def page_url(path: Path, metadata: dict[str, str]) -> str:
    """Convert a source Markdown file to its public GitHub Pages URL."""
    permalink = metadata.get("permalink")

    if permalink:
        if not permalink.startswith("/"):
            permalink = "/" + permalink

        if permalink == "/":
            return BASE_URL + "/"

        return BASE_URL + permalink

    relative = path.relative_to(ROOT)

    if relative.name == "index.md":
        parent = relative.parent.as_posix()

        if parent == ".":
            return BASE_URL + "/"

        return f"{BASE_URL}/{quote(parent)}/"

    html_path = relative.with_suffix(".html").as_posix()
    return f"{BASE_URL}/{quote(html_path, safe='/')}"


def last_modified(path: Path) -> str:
    """Return the latest Git commit date for the source file."""
    relative = path.relative_to(ROOT).as_posix()

    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", relative],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    date = result.stdout.strip()

    if not date:
        raise RuntimeError(f"No Git history found for {relative}")

    return date


def xml_escape(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def main() -> None:
    pages: list[tuple[str, str]] = []

    for path in sorted(ROOT.rglob("*.md")):
        if not is_publishable(path):
            continue

        metadata = read_front_matter(path)
        url = page_url(path, metadata)
        modified = last_modified(path)
        pages.append((url, modified))

    # Remove duplicate public URLs while keeping the newest source date.
    unique_pages: dict[str, str] = {}

    for url, modified in pages:
        previous = unique_pages.get(url)

        if previous is None or modified > previous:
            unique_pages[url] = modified

    ordered_pages = sorted(
        unique_pages.items(),
        key=lambda item: (item[0] != BASE_URL + "/", item[0]),
    )

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">',
        "",
    ]

    for url, modified in ordered_pages:
        lines.extend(
            [
                "  <url>",
                f"    <loc>{xml_escape(url)}</loc>",
                f"    <lastmod>{modified}</lastmod>",
                "  </url>",
                "",
            ]
        )

    lines.append("</urlset>")
    lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Generated {OUTPUT.relative_to(ROOT)} with {len(ordered_pages)} URLs.")

    for url, modified in ordered_pages:
        print(f"{modified}  {url}")


if __name__ == "__main__":
    main()
