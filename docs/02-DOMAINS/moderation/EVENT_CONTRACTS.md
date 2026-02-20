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

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
