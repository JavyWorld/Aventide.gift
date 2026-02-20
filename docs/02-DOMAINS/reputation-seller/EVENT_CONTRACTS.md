# EVENT_CONTRACTS · reputation-seller

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Event-driven:
- Corrección clave: reputación no ejecuta pagos; solo emite penalty_event que Policy Engine/Pagos traduce a flags (reserve/hold).
- 6.5 penalty_events
- penalty_events(entity_type=Seller, entity_id, penalty_code, severity, reason_codes[], starts_at, ends_at, created_by(AUTO|ADMIN), audit_ref)Índices:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (seller reputation)
- Rollup update idempotente por (seller_id, window, event_id)
- Penalty event idempotente por (seller_id, penalty_code, window_key)
- Solo “verdad verificada” cuenta: review y métricas derivan de eventos auditables (COMPLETED, outcomes, cancel_reason).
- Reputación moviendo dinero → corregido: solo emite penalty_events; pagos/policy aplican holds/reserve/freeze.

## Trazabilidad
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
