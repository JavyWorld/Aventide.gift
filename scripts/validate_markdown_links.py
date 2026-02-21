#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")


def github_anchor(text: str) -> str:
    clean = text.strip().lower()
    clean = re.sub(r"[`*_~]", "", clean)
    clean = re.sub(r"[^\w\-\s]", "", clean)
    clean = re.sub(r"\s+", "-", clean)
    clean = re.sub(r"-+", "-", clean)
    return clean.strip("-")


def extract_anchors(md_path: Path) -> set[str]:
    anchors: set[str] = set()
    content = md_path.read_text(encoding="utf-8")
    for line in content.splitlines():
        m = HEADING_RE.match(line)
        if m:
            anchors.add(github_anchor(m.group(2)))
    return anchors


def check_links(md_path: Path) -> list[str]:
    errors: list[str] = []
    content = md_path.read_text(encoding="utf-8")
    for i, line in enumerate(content.splitlines(), start=1):
        for match in LINK_RE.finditer(line):
            target = match.group(1)
            if target.startswith(SKIP_PREFIXES):
                if target.startswith("#"):
                    anchor = target[1:]
                    if anchor and anchor not in extract_anchors(md_path):
                        errors.append(f"{md_path.relative_to(ROOT)}:{i}: anchor interno inexistente '{target}'")
                continue

            file_part, _, anchor = target.partition("#")
            normalized = file_part.split("?")[0]
            target_path = (md_path.parent / normalized).resolve()
            if not target_path.exists():
                errors.append(f"{md_path.relative_to(ROOT)}:{i}: enlace roto '{target}'")
                continue
            if anchor and target_path.suffix.lower() == ".md":
                if anchor not in extract_anchors(target_path):
                    errors.append(
                        f"{md_path.relative_to(ROOT)}:{i}: anchor inexistente '{anchor}' en '{target_path.relative_to(ROOT)}'"
                    )
    return errors


def main() -> int:
    errors: list[str] = []
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        errors.extend(check_links(md))

    if errors:
        print("❌ Validación de enlaces markdown fallida:")
        for err in errors:
            print(f" - {err}")
        return 1

    print("✅ Validación de enlaces markdown internos aprobada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
