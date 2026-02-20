# API_CONTRACTS · orders

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- orders.cancel.request_post_accept (buyer → crea caso, no cancela directo)
- Auth
- OwnershipGuard (buyer_id/seller_id según endpoint)
- Reintentos: idempotencia por payment_attempt_id.
- Regla dura: estado de orden ≠ estado de refund.Refund flow (ejemplo): REQUESTED → UNDER_REVIEW → APPROVED/REJECTED → PARTIAL_REFUNDLa orden puede estar DELIVERED_PENDING_RELEASE o COMPLETED mientras corre el refund.
- cancel_meta JSON {requested_by, reason_code, requested_at, outcome_case_id}
- trace_id, request_id

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Regla dura: estado de orden ≠ estado de refund.Refund flow (ejemplo): REQUESTED → UNDER_REVIEW → APPROVED/REJECTED → PARTIAL_REFUNDLa orden puede estar DELIVERED_PENDING_RELEASE o COMPLETED mientras corre el refund.
- state (REQUESTED/UNDER_REVIEW/APPROVED/REJECTED/PARTIAL_REFUND)
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Órdenes v2.0 (corregido y unificado)
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
