# EVENT_CONTRACTS · notifications

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Fuente de verdad: “Sistema de Notificaciones”.Dependencia directa: “Sistema de Mensajería” (evento NEW_CHAT_MESSAGE).
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.
- Garantizar consistencia: Inbox = verdad, canales externos = delivery (no garantizado).
- Confiabilidad: Outbox pattern para no perder notificaciones bajo fallos/reintentos.
- Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.
- Outbox Pattern acoplado a transacciones de dominio (orden/pago/disputa).
- Catálogo de eventos notificados (Órdenes, Pagos, Disputas, Payouts, Seguridad/Identidad).
- “Smart notifications” desde Chat (evento NEW_CHAT_MESSAGE con reglas online/offline).
- Chat como feature (es Mensajería; aquí solo consume eventos).
- 4.1 Emisión desde un evento de dominio (Outbox → Orchestrator)

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
