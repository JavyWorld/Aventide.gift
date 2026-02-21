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

## Ownership & Escalation

- **Owner técnico:** `Equipo disputes`
- **Owner negocio/regulatorio:** `Product + Compliance (disputes)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

