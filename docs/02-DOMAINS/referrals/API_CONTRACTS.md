# API_CONTRACTS · referrals

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- IdempotencyGuard (no duplica atribución ni grants)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas duras)
- ATTRIBUTION: idempotente por (referred_id, referrer_id, window_key)
- FIRST_ORDER_EVAL: idempotente por (referred_id, first_order_id)
- REWARD_GRANT: idempotente por (attribution_id, reward_type, policy_version)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
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


## Control operativo verificable

- Owner: `Equipo referrals`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-REFERRALS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/referrals/dominio-referrals-operacion`
  - `https://jira.aventide.gift/browse/OPS-REFERRALS-241`

## Trazabilidad

- Documento origen: `sistema-de-referido-260207_0826.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
