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
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: La Reserva Nacional (por país) es una cuenta de ledger (COUNTRY_RESERVE_{country}) de custodia corporativa que:


## Control operativo verificable

- Owner: `Equipo reservas-country`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RESERVASCOUN-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reservas-country/dominio-reservas-country-operacion`
  - `https://jira.aventide.gift/browse/OPS-RESERVASCOUN-241`

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo reservas-country`
- **Owner negocio/regulatorio:** `Product + Compliance (reservas-country)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

