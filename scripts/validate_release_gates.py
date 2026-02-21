#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import os
import re
import subprocess
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
RELEASES_DIR = ROOT / "docs" / "releases"
CHANGELOG = ROOT / "docs" / "04-CHANGELOG.md"
DOMAINS_README = ROOT / "docs" / "02-DOMAINS" / "README.md"

RELEASE_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}-[a-z0-9-]+)\.md$")
APPROVAL_STATUS_RE = re.compile(r"\*\*Estado de aprobación:\*\*\s*(aprobado|pendiente|rechazado)\s*$", re.MULTILINE)
LINK_FIELDS = [
    "Dashboard",
    "Incident Drill",
    "Pruebas E2E",
    "Aprobación legal/regulatoria",
]

CRITICAL_DOMAINS = {
    "orders",
    "payments",
    "billing-docs",
    "security",
    "audit",
    "continuity",
    "internal-credit",
    "reservas-global",
    "reservas-country",
    "rate-engine",
}


def normalize_slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def parse_aliases() -> dict[str, str]:
    content = DOMAINS_README.read_text(encoding="utf-8")
    alias_section = re.search(r"## Alias legacy → Dominio canónico\n\n(?P<section>.*)$", content, re.DOTALL)
    alias_rows = re.findall(r"\| `([^`]+)` \| `([^`]+)` \|", alias_section.group("section") if alias_section else "")
    mapping = {normalize_slug(alias): target for alias, target in alias_rows}
    mapping["estructura-v2"] = "platform-structure"
    mapping["sistema-gobernanza-multi-pais-app-camaleon"] = "governance-cameleon"
    return mapping


def get_changed_files() -> list[str]:
    event_name = os.getenv("GITHUB_EVENT_NAME", "")
    base_ref = os.getenv("GITHUB_BASE_REF", "")

    if event_name == "pull_request" and base_ref:
        subprocess.run(["git", "fetch", "origin", base_ref, "--depth=1"], cwd=ROOT, check=True, capture_output=True)
        cmd = ["git", "diff", "--name-only", f"origin/{base_ref}...HEAD"]
    else:
        cmd = ["git", "diff", "--name-only", "HEAD~1..HEAD"]

    result = subprocess.run(cmd, cwd=ROOT, check=True, capture_output=True, text=True)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def touched_critical_domain(changed_files: list[str], aliases: dict[str, str]) -> bool:
    for path in changed_files:
        if path.startswith("docs/02-DOMAINS/"):
            parts = Path(path).parts
            if len(parts) >= 3 and parts[2] in CRITICAL_DOMAINS:
                return True

        if path.startswith("contracts/"):
            stem = Path(path).stem
            mapped = aliases.get(normalize_slug(stem), normalize_slug(stem))
            if mapped in CRITICAL_DOMAINS:
                return True

    return False


def validate_release_files() -> list[str]:
    errors: list[str] = []
    if not RELEASES_DIR.exists():
        return ["No existe el directorio docs/releases/."]

    release_ids: set[str] = set()
    release_files = sorted(RELEASES_DIR.glob("*.md"))
    for file in release_files:
        if file.name in {"README.md", "YYYY-MM-DD-release-id.md"}:
            continue

        match = RELEASE_FILE_RE.match(file.name)
        if not match:
            errors.append(f"{file.as_posix()}: nombre inválido. Debe ser YYYY-MM-DD-release-id.md")
            continue

        release_id = match.group(1)
        if release_id in release_ids:
            errors.append(f"Release ID duplicado: {release_id}")
        release_ids.add(release_id)

        content = file.read_text(encoding="utf-8")
        if not re.search(rf"^#{{2,6}}\s+Release:\s+{re.escape(release_id)}\s*$", content, re.MULTILINE):
            errors.append(f"{file.as_posix()}: debe incluir un encabezado 'Release: {release_id}'.")

        for field in LINK_FIELDS:
            if not re.search(rf"\*\*{re.escape(field)}:\*\*\s*\[[^\]]+\]\((https?://[^)]+)\)", content):
                errors.append(f"{file.as_posix()}: falta enlace concreto para '{field}'.")

        if not APPROVAL_STATUS_RE.search(content):
            errors.append(f"{file.as_posix()}: falta '**Estado de aprobación:** aprobado|pendiente|rechazado'.")

    changelog = CHANGELOG.read_text(encoding="utf-8") if CHANGELOG.exists() else ""
    for release_id in release_ids:
        if f"**Release ID:** {release_id}" not in changelog:
            errors.append(f"docs/04-CHANGELOG.md: falta referencia a Release ID {release_id}.")

    return errors


def main() -> int:
    errors = validate_release_files()

    aliases = parse_aliases()
    changed_files = get_changed_files()
    if touched_critical_domain(changed_files, aliases):
        has_release_in_pr = any(
            path.startswith("docs/releases/") and RELEASE_FILE_RE.match(Path(path).name)
            for path in changed_files
        )
        has_changelog_update = "docs/04-CHANGELOG.md" in changed_files

        if not has_release_in_pr:
            errors.append(
                "El PR toca dominios críticos, pero no agrega/actualiza un release gate en docs/releases/YYYY-MM-DD-release-id.md."
            )
        if not has_changelog_update:
            errors.append("El PR toca dominios críticos, pero no actualiza docs/04-CHANGELOG.md.")

    if errors:
        print("❌ Validación de release gates fallida:")
        for err in errors:
            print(f" - {err}")
        return 1

    print("✅ Validación de release gates aprobada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
