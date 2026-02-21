# RUNBOOKS · disputes

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs) — aplicado a Disputas
- Alertas mínimas
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- Fuente de verdad: “Disputas y Resolución (Saga) — ESPECIFICACIÓN FINAL”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que resuelve disputas sin improvisación usando:

## Incidentes, rollback y backfill
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- Fuente de verdad: “Disputas y Resolución (Saga) — ESPECIFICACIÓN FINAL”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que resuelve disputas sin improvisación usando:
- Outcomes predefinidos (plantillas) para que soporte no invente montos,
- Resolución por buckets (líneas contables) como única forma de mover dinero,
- Platform Fee protegido por earned schedule (devengado por hitos) + override por culpa (fault),
- ExternalCosts (processing/chargeback/dispute fee) como bucket formal (nunca ignorado),


## Control operativo verificable

- Owner: `Equipo disputes`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-DISPUTES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/disputes/dominio-disputes-operacion`
  - `https://jira.aventide.gift/browse/OPS-DISPUTES-241`

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
