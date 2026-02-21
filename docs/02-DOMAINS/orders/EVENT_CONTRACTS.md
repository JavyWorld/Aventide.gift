# EVENT_CONTRACTS · orders

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Motor de logística/driver como sistema completo (Órdenes emite/consume eventos).
- evento “no atendida”,
- Si vence accept_by: evento + notificación + escalamiento a ops/soporte.Suposición: la decisión final de auto-cancel vs reasignación se define por Policy Engine por país/zona, consistente con multi-país. (No está cerrado en el doc; se implementa policy-driven.)
- order_events
- event_id (UUID unique)
- event_name
- from_status, to_status (nullable para eventos no estado)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos mínimos del dominio Órdenes
- Al pasar READY_FOR_PICKUP → emitir evento consumible por Logística: ORDER_READY_FOR_PICKUP


## Control operativo verificable

- Owner: `Equipo orders`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ORDERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/orders/dominio-orders-operacion`
  - `https://jira.aventide.gift/browse/OPS-ORDERS-241`

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
