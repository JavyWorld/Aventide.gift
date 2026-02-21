.PHONY: validate-docs validate-openapi validate-jsonschema validate-contracts validate-cross-domain validate-release-gates

validate-docs:
	./scripts/validate_docs.sh

validate-openapi:
	python3 scripts/validate_openapi.py

validate-jsonschema:
	python3 scripts/validate_json_schemas.py

validate-contracts: validate-openapi validate-jsonschema

validate-cross-domain:
	./scripts/validate_cross_domain.sh


validate-release-gates:
	python3 scripts/validate_release_gates.py
