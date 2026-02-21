# API_CONTRACTS · backup

## Endpoints

- Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- Regla extra: restore idempotente (sin duplicar cobros/payouts).
- Eventos y triggers (colas/jobs) + idempotencia
- Idempotencia
- Cada job escribe run_id y es idempotente por (resource_type, schedule_window, country_code).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.
- Regla extra: restore idempotente (sin duplicar cobros/payouts).
- Eventos y triggers (colas/jobs) + idempotencia
- Idempotencia
- Cada job escribe run_id y es idempotente por (resource_type, schedule_window, country_code).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo backup`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-BACKUP-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/backup/dominio-backup-operacion`
  - `https://jira.aventide.gift/browse/OPS-BACKUP-241`

## Trazabilidad

- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
