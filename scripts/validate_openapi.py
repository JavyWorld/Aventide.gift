#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml
from openapi_spec_validator import validate_spec

ROOT = Path(__file__).resolve().parents[1]
API_DIR = ROOT / "contracts" / "api"


def main() -> int:
    errors = []
    for spec_path in sorted(API_DIR.glob("*.yaml")):
        try:
            with spec_path.open("r", encoding="utf-8") as fh:
                spec = yaml.safe_load(fh)
            validate_spec(spec)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{spec_path.relative_to(ROOT)}: {exc}")

    if errors:
        print("❌ Validación OpenAPI fallida:")
        for err in errors:
            print(f" - {err}")
        return 1

    print(f"✅ OpenAPI válido en {len(list(API_DIR.glob('*.yaml')))} archivo(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
