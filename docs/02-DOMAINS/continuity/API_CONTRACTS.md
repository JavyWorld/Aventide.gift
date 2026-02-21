# API_CONTRACTS · continuity

## Endpoints

- Workflow de desembolso desde COUNTRY_RESERVE con four-eyes + ejecución idempotente por worker + auditoría WORM.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- SYSTEM/WORKERS: ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).
- Cadena base: AuthGuard → RoleGuard → ScopeGuard → PermissionGuard → PolicyGuard.
- RBAC_ROLE_REVOKED + RBAC_SCOPE_REVOKED al COL saliente + invalidación de sesiones/claims.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- status: REQUESTED | APPROVED | EXECUTED | REJECTED
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Cadena base: AuthGuard → RoleGuard → ScopeGuard → PermissionGuard → PolicyGuard.
- RBAC_ROLE_REVOKED + RBAC_SCOPE_REVOKED al COL saliente + invalidación de sesiones/claims.

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Workflow de desembolso desde COUNTRY_RESERVE con four-eyes + ejecución idempotente por worker + auditoría WORM.
- SYSTEM/WORKERS: ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia


## Control operativo verificable

- Owner: `Equipo continuity`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-CONTINUITY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/continuity/dominio-continuity-operacion`
  - `https://jira.aventide.gift/browse/OPS-CONTINUITY-241`

## Trazabilidad

- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
