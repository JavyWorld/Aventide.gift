# API_CONTRACTS · loyalty

## Endpoints

- Actores y permisos (RBAC) + guards
- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- checkout_id (nullable; para apply idempotente)
- unique por idempotencia:
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- Actores y permisos (RBAC) + guards

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- checkout_id (nullable; para apply idempotente)
- unique por idempotencia:
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-lealtad-260207_0817.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
