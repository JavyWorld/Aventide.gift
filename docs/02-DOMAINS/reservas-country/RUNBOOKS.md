# RUNBOOKS · reservas-country

## Operación
- “resumen-260207_1014” (Continuidad, vacancia, routing a reserva, break-glass, four-eyes, monitoreo).
- Recibe automáticamente el diferencial / bucket destinado a operación país cuando aplica (p.ej., vacancia de COL o decisiones de riesgo/policy).
- Riesgo: absorber pérdidas locales (chargebacks, fraude, refunds irreversibles, penalidades atribuibles a operación país si policy lo admite) con orden fijo y trazabilidad.
- Observabilidad + alertas por salud de reserva y anomalías de uso (abuso interno, disbursements atípicos).
- 4.2 Disbursement desde Reserva Nacional (operación legítima)
- Gastos operativos del país (tooling, soporte, operación).

## Incidentes, rollback y backfill
- Reintentos del worker: idempotencia por idempotency_key.
- Disbursements que impliquen payout pasan por workers y proveedores; auditoría y reintentos estándar (DLQ, circuit breaker), sin duplicar efectos (idempotencia). (Coherente con el enfoque de workers y auditoría del proyecto; los detalles operativos viven en Integraciones, aquí solo se exige el contrato de idempotencia + evidencia.)
- Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)
- Fuentes de verdad:
- “resumen-260207_1014” (Continuidad, vacancia, routing a reserva, break-glass, four-eyes, monitoreo).
- “waterfall-engine-v10-260207_0941” (Waterfall de pérdidas, layers, loss_case, recovery al COL, guardrails, ledger doble-entry).
- 1) Definición y objetivos del sistema/módulo
- Definición: La Reserva Nacional (por país) es una cuenta de ledger (COUNTRY_RESERVE_{country}) de custodia corporativa que:

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
