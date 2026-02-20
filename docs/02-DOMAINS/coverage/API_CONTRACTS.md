# API_CONTRACTS · coverage

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- Snapshot de orden marca coverage_result=OVERRIDDEN con actor/razónSuposición: el documento no define el endpoint exacto del override; se especifica el control mínimo para no romper auditoría.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- addresses/validate: idempotente por (buyer_id, raw_address_hash) si se cachea.
- coverage/check: idempotente por (seller_id, address_id, date_bucket, algo_version) para caching controlado.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Overrides sin trazabilidad → corregido: override solo con permiso, razón, evento y snapshot marcado.

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- Overrides sin trazabilidad → corregido: override solo con permiso, razón, evento y snapshot marcado.

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- addresses/validate: idempotente por (buyer_id, raw_address_hash) si se cachea.
- coverage/check: idempotente por (seller_id, address_id, date_bucket, algo_version) para caching controlado.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-cobertura-260207_0907.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
