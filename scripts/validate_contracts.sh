#!/usr/bin/env bash
set -euo pipefail

python3 scripts/validate_openapi.py
python3 scripts/validate_json_schemas.py
