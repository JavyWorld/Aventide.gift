# API_CONTRACTS · files

## Endpoints y auth
- control estricto RBAC+ABAC (“need-to-know”),
- 3) Actores y permisos (RBAC) + guards
- privacy.delete_request.submit
- AuthGuard
- Sistema valida RBAC+ABAC + data_class.
- si hay error: no se edita; se emite Nota de Crédito + nueva factura.
- action (VIEW/DOWNLOAD/ISSUE_SIGNED_URL/UPLOAD/DELETE_REQUEST/LEGAL_HOLD)
- 7) Eventos y triggers + idempotencia

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- si hay error: no se edita; se emite Nota de Crédito + nueva factura.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Archivos v2.0 (Storage & Attachments) — corregido y unificado
- Fuente de verdad: “Sistema de Archivos (Storage & Attachments)”.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-de-archivos-260207_0840.docx`
