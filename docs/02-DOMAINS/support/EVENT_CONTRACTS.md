# EVENT_CONTRACTS · support

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos principales
- order_events/timeline (“Audit Timeline”)
- eventos pin_attempt_failed, geo_mismatch, photo_uploaded
- timeline de eventos,
- Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:
- Tickets (gestión operativa y comunicación),


## Control operativo verificable

- Owner: `Equipo support`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-SUPPORT-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/support/dominio-support-operacion`
  - `https://jira.aventide.gift/browse/OPS-SUPPORT-241`

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
