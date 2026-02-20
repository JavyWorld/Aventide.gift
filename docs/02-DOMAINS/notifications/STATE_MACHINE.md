# STATE_MACHINE · notifications

## Estados detectados/derivados
- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.
- Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.
- Catálogo de eventos notificados (Órdenes, Pagos, Disputas, Payouts, Seguridad/Identidad).
- “Smart notifications” desde Chat (evento NEW_CHAT_MESSAGE con reglas online/offline).
- Chat como feature (es Mensajería; aquí solo consume eventos).

## Transiciones y eventos de entrada/salida
- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.
- Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.
- Catálogo de eventos notificados (Órdenes, Pagos, Disputas, Payouts, Seguridad/Identidad).
- “Smart notifications” desde Chat (evento NEW_CHAT_MESSAGE con reglas online/offline).
- Chat como feature (es Mensajería; aquí solo consume eventos).
- 4.1 Emisión desde un evento de dominio (Outbox → Orchestrator)
- Saga de Disputas: no se notifica “resuelto” si falla un paso (refund). En su lugar:

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
