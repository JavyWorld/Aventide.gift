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
- 1) Definición y objetivos del sistema/módulo
- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Objetivos:

## Trazabilidad
- Documento origen: `sistema-de-observalidad-260207_0755.docx`
