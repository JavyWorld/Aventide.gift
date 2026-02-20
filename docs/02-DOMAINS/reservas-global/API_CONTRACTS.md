# API_CONTRACTS · reservas-global

## Endpoints y auth
- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- 3) Actores y permisos (RBAC) + guards
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- global_reserve.emergency.freeze.request/approve (super_admin/finance_admin)
- global_reserve.disbursement.request/create (finance_admin) (solo si existe uso fuera del waterfall; ver 8.2)
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.
- plan de recapitalización/priorización.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Reserva Global v2.0 (GLOBAL_RESERVE + GLOBAL_RECOVERY + CRISIS)
- Fuentes de verdad:
- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Continuidad / Country Governance (VACANT/LOCKDOWN, break-glass, four-eyes, WORM).

## Trazabilidad
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
