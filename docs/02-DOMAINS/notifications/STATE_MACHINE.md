# STATE_MACHINE · notifications

## Estados

- Definir estados explícitos del ciclo de vida para entidades principales del dominio.

## Transiciones

- Inbox: idempotente por (event_id, recipient_user_id, template_id) (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Inbox: idempotente por (event_id, recipient_user_id, template_id) (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).
- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.
- Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.
- Catálogo de eventos notificados (Órdenes, Pagos, Disputas, Payouts, Seguridad/Identidad).
- “Smart notifications” desde Chat (evento NEW_CHAT_MESSAGE con reglas online/offline).
- Chat como feature (es Mensajería; aquí solo consume eventos).
- Emisión desde un evento de dominio (Outbox → Orchestrator)


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
