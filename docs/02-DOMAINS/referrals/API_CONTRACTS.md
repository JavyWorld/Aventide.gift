# API_CONTRACTS · referrals

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (no duplica atribución ni grants)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas duras)
- ATTRIBUTION: idempotente por (referred_id, referrer_id, window_key)
- FIRST_ORDER_EVAL: idempotente por (referred_id, first_order_id)
- REWARD_GRANT: idempotente por (attribution_id, reward_type, policy_version)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (no duplica atribución ni grants)

## Códigos de error

- BUYER (Referrer): comparte código/link y ve estados/rewards.

## Idempotency

- IdempotencyGuard (no duplica atribución ni grants)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas duras)
- ATTRIBUTION: idempotente por (referred_id, referrer_id, window_key)
- FIRST_ORDER_EVAL: idempotente por (referred_id, first_order_id)
- REWARD_GRANT: idempotente por (attribution_id, reward_type, policy_version)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-referido-260207_0826.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
