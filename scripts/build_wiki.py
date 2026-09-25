#!/usr/bin/env python3
"""Copy wiki/*.md into a GitHub Wiki checkout and rewrite links.

GitHub Wiki pages are addressed without ".md", and files outside wiki/
(rules, templates, ...) do not exist in the Wiki repository. So:
  - links to other wiki pages:  "Page.md#anchor" -> "Page#anchor"
  - links to repo files:        "../rules/x.md"  -> full GitHub URL

Usage: python3 scripts/build_wiki.py <wiki-checkout-dir>
"""
import os
import re
import sys
from pathlib import Path

REPO_URL = os.environ.get(
    "REPO_URL", "https://github.com/Pixeldieb/Rabenregatta"
).rstrip("/")
BRANCH = os.environ.get("BRANCH", "main")

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "wiki"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
SRC_ATTR = re.compile(r'(src=")([^"]+)(")')
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def rewrite(link: str) -> str:
    if re.match(r"^[a-z]+:", link) or link.startswith("#"):
        return link
    path, _, anchor = link.partition("#")
    anchor = f"#{anchor}" if anchor else ""
    target = (SRC / path).resolve()

    # Page inside the wiki folder (top level only)
    if target.parent == SRC and target.suffix == ".md":
        return target.stem + anchor

    # Anything else: link to the file or folder in the main repository.
    # Images need the raw file, otherwise the Wiki shows a broken image.
    rel = target.relative_to(ROOT).as_posix()
    if target.is_dir():
        kind = "tree"
    elif target.suffix.lower() in IMAGE_SUFFIXES:
        kind = "raw"
    else:
        kind = "blob"
    return f"{REPO_URL}/{kind}/{BRANCH}/{rel}{anchor}"


def main() -> None:
    out = Path(sys.argv[1])
    for page in sorted(SRC.glob("*.md")):
        text = page.read_text(encoding="utf-8")
        for pattern in (LINK, SRC_ATTR):
            text = pattern.sub(lambda m: m.group(1) + rewrite(m.group(2)) + m.group(3), text)
        (out / page.name).write_text(text, encoding="utf-8")
        print(f"built {page.name}")


if __name__ == "__main__":
    main()
