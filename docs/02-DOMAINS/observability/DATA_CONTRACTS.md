# DATA_CONTRACTS · observability

## Entidades y campos
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- Snapshot financiero en checkout (no recalcular después).
- Campos estándar (mínimo):Correlación
- Búsqueda: search_latency_p95, index_freshness_lag, zero-results anormal.
- Sistema de Observabilidad v2.0 (SRE / “Sistema Nervioso Central”) — corregido y unificado
- Fuentes de verdad:
- “Observabilidad (SRE) — Especificación Técnica”
- “Sistema— Observabilidad + Resiliencia (SRE / ‘Sistema Nervioso Central’)”

## Constraints y claves de negocio
- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Idempotencia real (pagos, webhooks, payouts).
- Retries solo cuando es seguro (idempotente).
- actor_role, actor_id, actor_hash
- idempotency_key, dedupe_key
- 7) Eventos y triggers + idempotencia


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
