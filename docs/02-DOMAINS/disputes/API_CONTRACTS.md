# API_CONTRACTS · disputes

## Endpoints y auth
- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- 3) Actores y permisos (RBAC) + guards
- disputes.evidence.request/read/write
- disputes.finance.approval.request / disputes.finance.approval.grant
- Auth
- Genera un settlement_plan idempotente (hash del input).
- 4.5 Ejecución Saga (steps idempotentes)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- Fuente de verdad: “Disputas y Resolución (Saga) — ESPECIFICACIÓN FINAL”.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
