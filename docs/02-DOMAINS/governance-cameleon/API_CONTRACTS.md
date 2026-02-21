# API_CONTRACTS · governance-cameleon

## Endpoints

- APIs mínimas: resolve context, fetch config UI, evaluate policies, simulate checkout.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Publish ruleset: idempotente por (ruleset_id, version)
- Publish ui_profile: idempotente por (profile_id, config_version)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- GeoIntegrityGuard (address con lat/lng obligatorio)

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
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


## Control operativo verificable

- Owner: `Equipo governance-cameleon`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GOVERNANCECA-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/governance-cameleon/dominio-governance-cameleon-operacion`
  - `https://jira.aventide.gift/browse/OPS-GOVERNANCECA-241`

## Trazabilidad

- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
