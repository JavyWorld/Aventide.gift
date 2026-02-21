# ADR-STR-002: Versionado semántico para contratos cross-domain

## Estado
Pendiente

## Contexto
Los contratos entre dominios críticos (`payments`, `rate-engine`, `waterfall`, `billing-docs`) requieren una convención homogénea para cambios incompatibles, minimizando regresiones y ambigüedad en releases.

## Decisión
Adoptar versionado semántico (MAJOR.MINOR.PATCH) para contratos API/EVENT/DATA cross-domain con reglas:

1. `MAJOR` para breaking changes.
2. `MINOR` para cambios backward-compatible.
3. `PATCH` para correcciones editoriales o aclaraciones sin impacto de integración.
4. Changelog obligatorio por contrato y mapeo de consumidores afectados.

## Dominios afectados
- [Facturación](../02-DOMAINS/FACTURACION.md)
- [Payouts](../02-DOMAINS/PAYOUTS.md)
