# API_CONTRACTS · referrals

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (no duplica atribución ni grants)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia (reglas duras)
- ATTRIBUTION: idempotente por (referred_id, referrer_id, window_key)
- FIRST_ORDER_EVAL: idempotente por (referred_id, first_order_id)
- REWARD_GRANT: idempotente por (attribution_id, reward_type, policy_version)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Referidos v2.0 (Referral Program) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X E).
- 1) Definición y objetivos del sistema/módulo
- Definición: Programa de adquisición y activación que atribuye un referrer (buyer existente) a un referred (buyer nuevo) y paga recompensas solo después de una “primera orden válida”, usando AP (Aventide Points) y opcionalmente FS (Fee Shields), con ledger auditable y reversión por fraude/refund/chargeback/disputa.

## Trazabilidad
- Documento origen: `sistema-de-referido-260207_0826.docx`
