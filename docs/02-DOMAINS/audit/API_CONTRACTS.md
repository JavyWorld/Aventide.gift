# API_CONTRACTS · audit

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- admin.four_eyes.request/create/approve (ops/admin; auditado)
- AuthGuard
- metadata (ip, ua, geo, request_id),
- RBAC_AUDIT: cambios de permisos/roles con IP, contexto, scope.
- request_id, requester, approver, action, timestamps.
- Requester + Approver con request_id en auditoría.
- metadata (JSONB: ip, user-agent, geo, request context)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Auditoría v2.0 (Aventide Black Box) — corregido y unificado
- Fuente de verdad: “Sistema de Auditoría Unificada (“Aventide Black Box”)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Auditoría es un sistema WORM (Write-Once, Read-Many) y append-only que registra, de forma consultable y verificable, quién hizo qué, cuándo, dónde, sobre qué recurso y con qué evidencia, incluyendo snapshotting (“máquina del tiempo”) para que el pasado de una orden no pueda reescribirse.

## Trazabilidad
- Documento origen: `sistema-de-auditoria-260207_0947.docx`
