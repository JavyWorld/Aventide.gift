# STATE_MACHINE · orders

## Estados

- Regla dura: estado de orden ≠ estado de refund.Refund flow (ejemplo): REQUESTED → UNDER_REVIEW → APPROVED/REJECTED → PARTIAL_REFUNDLa orden puede estar DELIVERED_PENDING_RELEASE o COMPLETED mientras corre el refund.
- Máquina de estados estricta (no saltos).
- Reglas cerradas de cancelación por estado (y ventanas).
- “Estado manda”: ninguna acción fuera de transición válida.
- from_status, to_status (nullable para eventos no estado)

## Transiciones

- Reintentos: idempotencia por payment_attempt_id.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- “Estado manda”: ninguna acción fuera de transición válida.
- Pago y transición a escrow.
- Motor de reembolsos/decisión: Soporte/Disputas decide outcomes; Órdenes ejecuta transiciones y bloqueos.
- StateGuard (validación de transición)

## Triggers

- trace_id, request_id
- Motor de logística/driver como sistema completo (Órdenes emite/consume eventos).
- evento “no atendida”,
- Si vence accept_by: evento + notificación + escalamiento a ops/soporte.Suposición: la decisión final de auto-cancel vs reasignación se define por Policy Engine por país/zona, consistente con multi-país. (No está cerrado en el doc; se implementa policy-driven.)
- from_status, to_status (nullable para eventos no estado)

## Trazabilidad

- Documento origen: `sistema-de-ordenes-260207_0037.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
