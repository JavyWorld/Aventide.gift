# API_CONTRACTS · reservas-country

## Endpoints y auth
- Se gobierna con workflow formal (request/approve/execute), auditoría WORM y controles break-glass para cualquier movimiento sensible.
- Determinismo contable: todo movimiento es doble-entry ledger, idempotente y reproducible; cada pérdida tiene expediente único (loss_case_id).
- Workflow de disbursement desde reserve con four-eyes y ejecución idempotente por worker.
- 3) Actores y permisos (RBAC) + guards
- reserve.disbursement.request.create{country} (finance_admin)
- reserve.disbursement.request.approve{country} (finance_admin distinto; four-eyes)
- FourEyesGuard: request/approve separados para disbursements y acciones sensibles de gobernanza.
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- status: REQUESTED|APPROVED|EXECUTED|REJECTED
- RESERVE_DISBURSEMENT_REQUESTED/APPROVED/EXECUTED/REJECTED
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Reserva Nacional v2.0 (COUNTRY_RESERVE + GOVERNANCE + WATERFALL)
- Fuentes de verdad:

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
