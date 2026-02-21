# INVARIANTS · analytics

Reglas no negociables del dominio:
- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- Eventos críticos server-side (inmutables, append-only).
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- Dashboards por rol: Admin Global, Country Ops Lead, Seller, Soporte/Moderación/Auditoría.
- Auditoría legal WORM como repositorio de evidencia: analítica referencia case_id/audit_ref, pero no sustituye evidencia.
- SUPPORT / MODERATION / AUDIT: timelines, evidencia referenciada, calidad, fraude.
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
