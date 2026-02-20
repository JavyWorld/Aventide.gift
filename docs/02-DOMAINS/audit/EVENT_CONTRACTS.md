# EVENT_CONTRACTS · audit

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- SYSTEM/WORKER (Service_ID): produce eventos obligatorios por write-path.
- SensitiveReadGuard (VIEW_SENSITIVE siempre genera evento)
- En la misma transacción (o mediante outbox) produce audit_log con:
- Fallo en escritura de auditoría: la acción crítica debe fallar (enforcement) o entrar en modo safe (bloqueo) según severidad. (Inferencia: consistente con “toda acción crítica write debe producir evento”.)
- Todo evento debe tener actor_id y actor_type (USER|SERVICE).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (audit-aware)
- audit insert: idempotente por event_id (si se usa outbox) o por (request_id, action_type, resource_id, created_at_bucket) según fuente.
- audit_events_ingested_total{resource_type,action_type,country}
- flag_red_events_total{type,country}

## Trazabilidad
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
