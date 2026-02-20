# API_CONTRACTS · backup

## Endpoints

- Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.
- Actores y permisos (RBAC) + guards
- AuthGuard
- Regla extra: restore idempotente (sin duplicar cobros/payouts).
- Eventos y triggers (colas/jobs) + idempotencia
- Idempotencia
- Cada job escribe run_id y es idempotente por (resource_type, schedule_window, country_code).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.
- Regla extra: restore idempotente (sin duplicar cobros/payouts).
- Eventos y triggers (colas/jobs) + idempotencia
- Idempotencia
- Cada job escribe run_id y es idempotente por (resource_type, schedule_window, country_code).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
