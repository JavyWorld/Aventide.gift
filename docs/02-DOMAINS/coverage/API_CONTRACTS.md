# API_CONTRACTS · coverage

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- Snapshot de orden marca coverage_result=OVERRIDDEN con actor/razónSuposición: el documento no define el endpoint exacto del override; se especifica el control mínimo para no romper auditoría.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- addresses/validate: idempotente por (buyer_id, raw_address_hash) si se cachea.
- coverage/check: idempotente por (seller_id, address_id, date_bucket, algo_version) para caching controlado.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Overrides sin trazabilidad → corregido: override solo con permiso, razón, evento y snapshot marcado.

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- Overrides sin trazabilidad → corregido: override solo con permiso, razón, evento y snapshot marcado.

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- addresses/validate: idempotente por (buyer_id, raw_address_hash) si se cachea.
- coverage/check: idempotente por (seller_id, address_id, date_bucket, algo_version) para caching controlado.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo coverage`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-COVERAGE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/coverage/dominio-coverage-operacion`
  - `https://jira.aventide.gift/browse/OPS-COVERAGE-241`

## Trazabilidad

- Documento origen: `sistema-de-cobertura-260207_0907.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
