# API_CONTRACTS · support

## Endpoints y auth
- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- 3) Actores y permisos (RBAC) + guards
- support.dispute.execute_saga (system; L2 dispara “request execution”)
- Auth
- requester_type (BUYER/SELLER/INTERNAL), requester_id
- sla_first_response_at, sla_resolution_at
- saga_state, idempotency_keys[]
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Soporte v2.0 (Support OS + Disputas) — corregido y unificado
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- 1) Definición y objetivos del sistema/módulo
- Definición: Support OS es el sistema interno para resolver incidentes y disputas con evidencia y reglas. Opera como orquestador de:

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
