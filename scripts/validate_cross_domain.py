#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DOMAINS_README = ROOT / "docs" / "02-DOMAINS" / "README.md"
DOMAINS_DIR = ROOT / "docs" / "02-DOMAINS"
CONTRACT_DIRS = {
    "api": ROOT / "contracts" / "api",
    "data": ROOT / "contracts" / "data",
    "events": ROOT / "contracts" / "events",
}


def normalize_slug(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def parse_domains_readme() -> tuple[set[str], dict[str, str], dict[str, str]]:
    content = DOMAINS_README.read_text(encoding="utf-8")

    canonical_match = re.search(
        r"## Dominios canónicos \(38\)\n\n(?P<list>.*?)\n\n## Mapeo",
        content,
        re.DOTALL,
    )
    if not canonical_match:
        raise RuntimeError("No se pudo leer la sección de dominios canónicos en docs/02-DOMAINS/README.md")

    canonical = set(re.findall(r"`([^`]+)`", canonical_match.group("list")))

    alias_section = re.search(r"## Alias legacy → Dominio canónico\n\n(?P<section>.*)$", content, re.DOTALL)
    alias_rows = re.findall(r"\| `([^`]+)` \| `([^`]+)` \|", alias_section.group("section") if alias_section else "")
    alias_map = {alias: target for alias, target in alias_rows}

    normalized_to_canonical = {normalize_slug(name): name for name in canonical}
    extra_aliases = {
        "estructura-v2": "platform-structure",
        "sistema-gobernanza-multi-pais-app-camaleon": "governance-cameleon",
    }

    for alias, target in {**alias_map, **extra_aliases}.items():
        normalized_to_canonical[normalize_slug(alias)] = target

    return canonical, alias_map, normalized_to_canonical


def contract_stems(contract_type: str) -> set[str]:
    ext = "yaml" if contract_type == "api" else "json"
    return {p.stem for p in CONTRACT_DIRS[contract_type].glob(f"*.{ext}")}


def main() -> int:
    errors: list[str] = []
    canonical, alias_map, normalized_to_canonical = parse_domains_readme()

    docs_domains = {p.name for p in DOMAINS_DIR.iterdir() if p.is_dir() and p.name != "_shared"}
    missing_docs = sorted(canonical - docs_domains)
    if missing_docs:
        errors.append(f"Faltan carpetas de docs para dominios canónicos: {', '.join(missing_docs)}")

    unknown_docs = sorted(docs_domains - canonical - set(alias_map.keys()))
    if unknown_docs:
        errors.append(f"Existen carpetas docs sin mapping canónico/alias: {', '.join(unknown_docs)}")

    contract_sets = {k: contract_stems(k) for k in CONTRACT_DIRS}
    if not (contract_sets["api"] == contract_sets["data"] == contract_sets["events"]):
        errors.append("Los slugs de contratos no coinciden entre api/data/events.")

    represented_domains: set[str] = set()
    for ctype, stems in contract_sets.items():
        unknown: list[str] = []
        for stem in sorted(stems):
            mapped = normalized_to_canonical.get(normalize_slug(stem))
            if not mapped:
                unknown.append(stem)
            else:
                represented_domains.add(mapped)
        if unknown:
            errors.append(f"{ctype}: slugs de contrato desconocidos: {', '.join(unknown)}")

    for domain in sorted(canonical):
        if domain not in represented_domains:
            errors.append(f"{domain}: no tiene contrato representativo en contracts/*")

    if errors:
        print("❌ Validación de consistencia cruzada fallida:")
        for error in errors:
            print(f" - {error}")
        return 1

    print("✅ Consistencia cruzada aprobada entre dominios canónicos, contratos y docs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
