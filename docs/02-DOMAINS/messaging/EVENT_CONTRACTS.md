# EVENT_CONTRACTS · messaging

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Bridge a Notification Center: evento canónico NEW_CHAT_MESSAGE.
- SYSTEM: mensajes de sistema, auto-replies, eventos; emite notificaciones.
- StatusGuard: si Conversation.status=FROZEN ⇒ solo lectura; solo SYSTEM/SUPPORT pueden emitir SYSTEM_EVENT.
- BLOCK → no persistir o persistir como “blocked event” (ver 7) según auditoría.
- Solo SYSTEM/SUPPORT agrega SYSTEM_EVENT en frozen (p.ej. “Ticket creado”).
- type ENUM: TEXT | TEMPLATE | ATTACHMENT | SYSTEM_EVENT
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos auditables mínimos (obligatorios)
- 7.2 Evento canónico de notificaciones
- Auditoría: eventos mínimos auditables.


## Control operativo verificable

- Owner: `Equipo messaging`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MESSAGING-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/messaging/dominio-messaging-operacion`
  - `https://jira.aventide.gift/browse/OPS-MESSAGING-241`

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
