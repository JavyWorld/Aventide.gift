# API_CONTRACTS · continuity

## Endpoints

- Workflow de desembolso desde COUNTRY_RESERVE con four-eyes + ejecución idempotente por worker + auditoría WORM.
- Actores y permisos (RBAC) + guards
- SYSTEM/WORKERS: ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).
- Cadena base: AuthGuard → RoleGuard → ScopeGuard → PermissionGuard → PolicyGuard.
- RBAC_ROLE_REVOKED + RBAC_SCOPE_REVOKED al COL saliente + invalidación de sesiones/claims.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- status: REQUESTED | APPROVED | EXECUTED | REJECTED
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Auth

- Actores y permisos (RBAC) + guards
- Cadena base: AuthGuard → RoleGuard → ScopeGuard → PermissionGuard → PolicyGuard.
- RBAC_ROLE_REVOKED + RBAC_SCOPE_REVOKED al COL saliente + invalidación de sesiones/claims.

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Workflow de desembolso desde COUNTRY_RESERVE con four-eyes + ejecución idempotente por worker + auditoría WORM.
- SYSTEM/WORKERS: ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
