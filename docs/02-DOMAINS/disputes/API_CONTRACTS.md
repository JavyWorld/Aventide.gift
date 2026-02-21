# API_CONTRACTS · disputes

## Endpoints

- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Genera un settlement_plan idempotente (hash del input).
- Ejecución Saga (steps idempotentes)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.

## Códigos de error

- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.

## Idempotency

- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- Genera un settlement_plan idempotente (hash del input).
- Ejecución Saga (steps idempotentes)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.


## Control operativo verificable

- Owner: `Equipo disputes`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-DISPUTES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/disputes/dominio-disputes-operacion`
  - `https://jira.aventide.gift/browse/OPS-DISPUTES-241`

## Trazabilidad

- Documento origen: `disputas-260207_0809.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
