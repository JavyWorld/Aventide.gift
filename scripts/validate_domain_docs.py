#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOMAINS_ROOT = ROOT / "docs" / "02-DOMAINS"
CANONICAL_FILES = {
    "README.md",
    "RUNBOOKS.md",
    "INVARIANTS.md",
    "STATE_MACHINE.md",
    "API_CONTRACTS.md",
    "EVENT_CONTRACTS.md",
    "DATA_CONTRACTS.md",
}

BLOCKED_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"por definir",
    r"\bxxx\b",
    r"lorem ipsum",
    r"Definición y objetivos del sistema/módulo",
    r"Integraciones \(inputs/outputs, retries, timeouts, fallbacks\)",
    r"Actores y permisos \(RBAC\) \+ guards",
    r"Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio\.",
]

REQUIRED_SECTION = "## Control operativo verificable"
REQUIRED_FIELDS = [
    r"- Owner:",
    r"- Fecha de última validación:",
    r"- Evidencias:",
    r"- Dashboards o tickets:",
]


def iter_canonical_files():
    for domain_dir in DOMAINS_ROOT.iterdir():
        if not domain_dir.is_dir() or domain_dir.name == "_shared":
            continue
        for name in CANONICAL_FILES:
            candidate = domain_dir / name
            if candidate.exists():
                yield candidate


def main() -> int:
    errors = []
    for path in sorted(iter_canonical_files()):
        content = path.read_text(encoding="utf-8")

        for pattern in BLOCKED_PATTERNS:
            for match in re.finditer(pattern, content, re.IGNORECASE):
                line = content.count("\n", 0, match.start()) + 1
                errors.append(f"{path.relative_to(ROOT)}:{line}: patrón prohibido detectado -> {pattern}")

        if REQUIRED_SECTION not in content:
            errors.append(f"{path.relative_to(ROOT)}: falta sección requerida '{REQUIRED_SECTION}'")
        else:
            for field in REQUIRED_FIELDS:
                if not re.search(field, content):
                    errors.append(f"{path.relative_to(ROOT)}: falta campo obligatorio en control operativo -> {field}")

    if errors:
        print("❌ Validación documental fallida. Se detectaron incumplimientos:")
        for err in errors:
            print(f" - {err}")
        return 1

    print("✅ Validación documental aprobada: sin placeholders bloqueantes y con control operativo completo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
