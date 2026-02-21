#!/usr/bin/env bash
set -euo pipefail

npx --yes markdownlint-cli2 "**/*.md" "#node_modules"
python3 scripts/validate_markdown_links.py
python3 scripts/validate_domain_docs.py
