# EVENT_CONTRACTS · moderation

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- moderation.event.read
- A) ModerationEvent (auto o manual)
- linked_events[]
- Corrección de incoherencia: StrikeLedger es proyección; los cambios reales ocurren vía eventos STRIKE_APPLIED + policy engine que setea flags en user_status y seller_operational_flags.
- 7) Eventos y triggers + idempotencia
- Eventos mínimos
- Por contenido: event_key = (content_type, content_id, change_version) evita doble moderación por reintentos.
- moderation_events_total{content_type,recommended_action}
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.


## Control operativo verificable

- Owner: `Equipo moderation`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MODERATION-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/moderation/dominio-moderation-operacion`
  - `https://jira.aventide.gift/browse/OPS-MODERATION-241`

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
