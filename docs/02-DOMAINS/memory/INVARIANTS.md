# INVARIANTS · memory

Reglas no negociables del dominio:
- Seguridad/compliance: PII y datos sensibles con clases de datos y retención; acceso mínimo y auditado.
- memory.audit.read (audit/admin)
- AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).
- Duplicados: si el buyer crea dos recipients con nombres parecidos, se permite, pero se sugiere merge (merge requiere acción explícita y queda auditado). (Suposición: el doc no detalla merge; se define el control mínimo consistente con evitar pérdida de historial).
- Si el buyer marca un campo como “shareable”, solo se comparte en contextos definidos (p. ej. “mensaje en tarjeta”); nunca alergias o notas privadas.
- Acceso staff requiere reason + VIEW_SENSITIVE auditado.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- GIFT_HISTORY_ADDED idempotente por (buyer_id, order_id) (si 1 recipient por orden).
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).

## Trazabilidad
- Documento origen: `sistema-de-memory-260207_1012.docx`
