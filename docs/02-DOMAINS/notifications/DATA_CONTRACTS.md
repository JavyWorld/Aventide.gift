# DATA_CONTRACTS · notifications

## Entidades y campos
- Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.
- Catálogo de eventos notificados (Órdenes, Pagos, Disputas, Payouts, Seguridad/Identidad).
- Campos:
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Campos mínimos:
- Campos definidos:
- Seguridad/Identidad
- Sistema de Notificaciones v2.0 (Notification Center + Inbox) — corregido y unificado

## Constraints y claves de negocio
- P1 Importante: pago confirmado, orden aceptada/rechazada, en camino.
- Corrección de incoherencia: los límites se aplican en el Orchestrator (no en cada servicio de dominio) para que el enforcement sea único.
- rendered_hash
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia (reglas duras)
- Inbox: idempotente por (event_id, recipient_user_id, template_id) (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).
- Outbox publish: idempotente por event_id.
- PAID_IN_ESCROW → Email puede incluir PDF (recibo/factura) generado por motor fiscal, referenciado como attachment (links firmados).


## Control operativo verificable

- Owner: `Equipo notifications`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-NOTIFICATION-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/notifications/dominio-notifications-operacion`
  - `https://jira.aventide.gift/browse/OPS-NOTIFICATION-241`

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
