# RUNBOOKS · observability

## Operación
- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- 5 pilares: Logs, Métricas, Trazas, Health Checks, Alertas (con severidad y ruteo).
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- Backups/DR + restore drills.
- obs.alerts.manage (SRE)
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.

## Incidentes, rollback y backfill
- DLQ: reintento manual (SRE) con auditoría.
- Sistema de Observabilidad v2.0 (SRE / “Sistema Nervioso Central”) — corregido y unificado
- Fuentes de verdad:
- “Observabilidad (SRE) — Especificación Técnica”
- “Sistema— Observabilidad + Resiliencia (SRE / ‘Sistema Nervioso Central’)”
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Objetivos:


## Control operativo verificable

- Owner: `Equipo observability`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-OBSERVABILIT-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/observability/dominio-observability-operacion`
  - `https://jira.aventide.gift/browse/OPS-OBSERVABILIT-241`

## Trazabilidad
- Documento origen: `sistema-de-observalidad-260207_0755.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo observability`
- **Owner negocio/regulatorio:** `Product + Compliance (observability)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

