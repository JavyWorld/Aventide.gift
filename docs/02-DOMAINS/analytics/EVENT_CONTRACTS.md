# EVENT_CONTRACTS · analytics

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Eventos críticos server-side (inmutables, append-only).
- Real-time operativo / eventual para BI profundo: operación “hoy/última hora” near-real-time; cohortes/finanzas pesadas con jobs.
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- SYSTEM/BOT: inserción de eventos y jobs.
- analytics.events.ingest (System)
- 4.1 Ingesta de eventos (server-side primero)
- Backend emite evento analítico inmutable con event_id y trace_id/request_id.
- Se guarda en analytics_events_raw (append-only).
- Reintento de evento: dedupe por event_id (idempotencia).
- Evento llega sin country/hub/zone: rechazado o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).


## Control operativo verificable

- Owner: `Equipo analytics`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ANALYTICS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/analytics/dominio-analytics-operacion`
  - `https://jira.aventide.gift/browse/OPS-ANALYTICS-241`

## Trazabilidad
- Documento origen: `sistema-de-analitica-260206_2336.docx`
