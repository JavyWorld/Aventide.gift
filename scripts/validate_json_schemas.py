#!/usr/bin/env python3
from pathlib import Path
import json
import sys
from jsonschema import validators

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIRS = [ROOT / "contracts" / "data", ROOT / "contracts" / "events"]


def validate_schema(path: Path) -> str | None:
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
        validator_cls = validators.validator_for(schema)
        validator_cls.check_schema(schema)
        return None
    except Exception as exc:  # noqa: BLE001
        return f"{path.relative_to(ROOT)}: {exc}"


def main() -> int:
    errors = []
    count = 0
    for directory in SCHEMA_DIRS:
        for schema_path in sorted(directory.glob("*.json")):
            count += 1
            err = validate_schema(schema_path)
            if err:
                errors.append(err)

    if errors:
        print("❌ Validación JSON Schema fallida:")
        for err in errors:
            print(f" - {err}")
        return 1

    print(f"✅ JSON Schema válido en {count} archivo(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
