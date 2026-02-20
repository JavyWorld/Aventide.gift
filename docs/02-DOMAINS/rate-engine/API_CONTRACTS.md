# API_CONTRACTS · rate-engine

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- rates.capfloor.change.request.create (ops lead/admin)
- rates.capfloor.change.request.approve (super_admin)
- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Se crea CapFloorChangeRequest con evidencia + rango propuesto + vigencia temporal + plan canary.
- 6.5 cap_floor_change_requests
- request_id
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- status (OPEN|APPROVED|REJECTED|EXECUTED)
- CAP_FLOOR_CHANGE_REQUEST_CREATED/APPROVED/REJECTED/EXECUTED
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Fallbacks
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
