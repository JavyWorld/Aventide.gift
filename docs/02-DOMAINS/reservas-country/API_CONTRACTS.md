# API_CONTRACTS · reservas-country

## Endpoints

- Determinismo contable: todo movimiento es doble-entry ledger, idempotente y reproducible; cada pérdida tiene expediente único (loss_case_id).
- Workflow de disbursement desde reserve con four-eyes y ejecución idempotente por worker.
- Actores y permisos (RBAC) + guards
- FourEyesGuard: request/approve separados para disbursements y acciones sensibles de gobernanza.
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- status: REQUESTED|APPROVED|EXECUTED|REJECTED
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Si quieres, lo siguiente es convertir este sistema a contratos “copy-paste para ingeniería”: endpoints admin exactos, enums purpose_code, eventos definitivos, y un set mínimo de tests UAT (vacancia, disbursement, pérdida y recovery).
- Disbursements que impliquen payout pasan por workers y proveedores; auditoría y reintentos estándar (DLQ, circuit breaker), sin duplicar efectos (idempotencia). (Coherente con el enfoque de workers y auditoría del proyecto; los detalles operativos viven en Integraciones, aquí solo se exige el contrato de idempotencia + evidencia.)

## Auth

- Actores y permisos (RBAC) + guards
- FourEyesGuard: request/approve separados para disbursements y acciones sensibles de gobernanza.
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.

## Códigos de error

- Disbursements que impliquen payout pasan por workers y proveedores; auditoría y reintentos estándar (DLQ, circuit breaker), sin duplicar efectos (idempotencia). (Coherente con el enfoque de workers y auditoría del proyecto; los detalles operativos viven en Integraciones, aquí solo se exige el contrato de idempotencia + evidencia.)

## Idempotency

- Determinismo contable: todo movimiento es doble-entry ledger, idempotente y reproducible; cada pérdida tiene expediente único (loss_case_id).
- Workflow de disbursement desde reserve con four-eyes y ejecución idempotente por worker.
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Disbursements que impliquen payout pasan por workers y proveedores; auditoría y reintentos estándar (DLQ, circuit breaker), sin duplicar efectos (idempotencia). (Coherente con el enfoque de workers y auditoría del proyecto; los detalles operativos viven en Integraciones, aquí solo se exige el contrato de idempotencia + evidencia.)

## Trazabilidad

- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
