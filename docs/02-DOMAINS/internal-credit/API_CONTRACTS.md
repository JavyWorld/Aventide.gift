# API_CONTRACTS · internal-credit

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- IdempotencyGuard (checkout_id/order_id/dispute_id)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Eventos y triggers + idempotencia

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- IdempotencyGuard (checkout_id/order_id/dispute_id)

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- IdempotencyGuard (checkout_id/order_id/dispute_id)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers + idempotencia


## Control operativo verificable

- Owner: `Equipo internal-credit`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-INTERNALCRED-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/internal-credit/dominio-internal-credit-operacion`
  - `https://jira.aventide.gift/browse/OPS-INTERNALCRED-241`

## Trazabilidad

- Documento origen: `sistema-de-credito-interno-260207_0827.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
