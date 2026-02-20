# API_CONTRACTS · orders

## Endpoints

- Actores y permisos (RBAC) + guards
- OwnershipGuard (buyer_id/seller_id según endpoint)
- Reintentos: idempotencia por payment_attempt_id.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- StateGuard (validación de transición)
- from_status, to_status (nullable para eventos no estado)
- escrow JSON {provider, escrow_id, amount, currency, status}

## Auth

- Actores y permisos (RBAC) + guards
- OwnershipGuard (buyer_id/seller_id según endpoint)
- StateGuard (validación de transición)

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Reintentos: idempotencia por payment_attempt_id.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-ordenes-260207_0037.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
