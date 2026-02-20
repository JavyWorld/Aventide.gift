# API_CONTRACTS · continuity

## Endpoints y auth
- Workflow de desembolso desde COUNTRY_RESERVE con four-eyes + ejecución idempotente por worker + auditoría WORM.
- 3) Actores y permisos (RBAC) + guards
- SYSTEM/WORKERS: ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).
- money.reserve.disbursement.request/create (finance_admin)
- Cadena base: AuthGuard → RoleGuard → ScopeGuard → PermissionGuard → PolicyGuard.
- RBAC_ROLE_REVOKED + RBAC_SCOPE_REVOKED al COL saliente + invalidación de sesiones/claims.
- (Recomendación operativa del sistema) four-eyes: requester ≠ approver para asignación de COL.
- 6.5 reserve_disbursement_request

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- status: REQUESTED | APPROVED | EXECUTED | REJECTED
- RESERVE_DISBURSEMENT_REQUESTED/APPROVED/EXECUTED/REJECTED
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”
- Fuente de verdad: Documento “resumen-260207_1014”.

## Trazabilidad
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
