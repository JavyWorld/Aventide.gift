# INVARIANTS · messaging

Reglas no negociables del dominio:
- Ser evidencia operativa/legal: inmutable, auditable y exportable para Soporte/Disputas.
- Integración estricta: Órdenes (scope), Notificaciones (bridge), Moderación (pipeline), Soporte (ticket+freeze), Auditoría (logs).
- Chat buyer ↔ seller por order_id (trazable y auditable).
- Intercambio directo de email/teléfono (siempre enmascarado; nunca PII).
- SUPPORT: convierte a ticket, lee evidencia, congela/gestiona; acceso auditado.
- ADMIN/OPS LEAD: auditoría/operación (scoped por país).
- chat.audit.read (audit/admin)
- AuditGuard (acciones y accesos).
- Órdenes canceladas: conversación puede archivarse temprano o bloquear envío (policy), pero nunca debe permitir chat “sin orden”.
- BLOCK → no persistir o persistir como “blocked event” (ver 7) según auditoría.

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
