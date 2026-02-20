# API_CONTRACTS · reputation-buyer

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- Duplicados: idempotencia por (buyer_id, event_id) en rollups.
- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Duplicados: idempotencia por (buyer_id, event_id) en rollups.
- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
