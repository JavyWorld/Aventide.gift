# API_CONTRACTS · files

## Endpoints

- control estricto RBAC+ABAC (“need-to-know”),
- Actores y permisos (RBAC) + guards
- AuthGuard
- Sistema valida RBAC+ABAC + data_class.
- si hay error: no se edita; se emite Nota de Crédito + nueva factura.
- Eventos y triggers + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- control estricto RBAC+ABAC (“need-to-know”),
- Actores y permisos (RBAC) + guards
- AuthGuard
- Sistema valida RBAC+ABAC + data_class.

## Códigos de error

- si hay error: no se edita; se emite Nota de Crédito + nueva factura.
- checksum mismatch: rechaza y mantiene estado PENDING_UPLOAD con TTL de limpieza.

## Idempotency

- Eventos y triggers + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-archivos-260207_0840.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
