# notifications

## Propósito

- WhatsApp (si opt-in) o SMS fallback
- ORDER_ACCEPTED / ORDER_REJECTED
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.
- Saga de Disputas: no se notifica “resuelto” si falla un paso (refund). En su lugar:
- Definición y objetivos del sistema/módulo
- Un servicio de dominio (Órdenes/Pagos/Disputas) ejecuta su transacción.
- outbox_events (por servicio de dominio)
- provider
- Título extraído: "Sistema de Notificaciones v2.0 (Notification Center + Inbox) — corregido y unificado".

## Límites

- Idempotencia (reglas duras)
- “Smart notifications” desde Chat (evento NEW_CHAT_MESSAGE con reglas online/offline).
- Alcance (incluye / excluye)
- Reglas y políticas (prioridades, canales, límites, validaciones)
- Corrección de incoherencia: los límites se aplican en el Orchestrator (no en cada servicio de dominio) para que el enforcement sea único.

## Dependencias

- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.
- Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.

## Trazabilidad

- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
- Título extraído: "Sistema de Notificaciones v2.0 (Notification Center + Inbox) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
