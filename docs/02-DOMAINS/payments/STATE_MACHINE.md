# STATE_MACHINE · payments

## Estados

- Estados financieros acoplados a la máquina de órdenes (alto nivel).
- StateGuard (compatibilidad con estados de orden: CREATED/PAID_IN_ESCROW/…)

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Triggers

- Webhook duplicado: dedupe por provider_event_id / rapyd_transaction_id.

## Trazabilidad

- Documento origen: `sistema-de-pagos-260207_0800.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
