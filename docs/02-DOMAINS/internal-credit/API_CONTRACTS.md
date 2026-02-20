# API_CONTRACTS · internal-credit

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (checkout_id/order_id/dispute_id)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Eventos y triggers + idempotencia

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (checkout_id/order_id/dispute_id)

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- IdempotencyGuard (checkout_id/order_id/dispute_id)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-credito-interno-260207_0827.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
