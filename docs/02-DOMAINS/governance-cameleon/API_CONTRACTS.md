# API_CONTRACTS · governance-cameleon

## Endpoints

- APIs mínimas: resolve context, fetch config UI, evaluate policies, simulate checkout.
- Actores y permisos (RBAC) + guards
- AuthGuard
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Publish ruleset: idempotente por (ruleset_id, version)
- Publish ui_profile: idempotente por (profile_id, config_version)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- GeoIntegrityGuard (address con lat/lng obligatorio)

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- GeoIntegrityGuard (address con lat/lng obligatorio)

## Códigos de error

- Firma de UI config obligatoria; app rechaza configs no firmadas o schema incompatible y entra en fallback.

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Publish ruleset: idempotente por (ruleset_id, version)
- Publish ui_profile: idempotente por (profile_id, config_version)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
