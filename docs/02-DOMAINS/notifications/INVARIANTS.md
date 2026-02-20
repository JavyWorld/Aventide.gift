# INVARIANTS · notifications

Reglas no negociables del dominio:
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.
- Auditoría: trazabilidad WORM/ledger-style por evento/canal/plantilla/recipient.
- Notification Orchestrator (rules engine + renderer + dispatcher + inbox writer + audit log).
- FINANCE/AUDIT: lectura compliance (si habilitado).
- SYSTEM/BOT: orquestación, envío, reintentos, escritura Inbox, auditoría.
- notifications.audit.read (audit/finance/admin)
- AuditGuard (log obligatorio)
- Inbox Writer (siempre)
- Audit Log (WORM-style)
- P0 nunca se agrupa con otros eventos (mantener urgencia y claridad).

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
