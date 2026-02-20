# API_CONTRACTS · loyalty

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- Auth
- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- checkout_id (nullable; para apply idempotente)
- unique por idempotencia:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos”
- “Fases de Desarrollo v1.1 — Loyalty (ledger-first) + eventos + modelo de datos”

## Trazabilidad
- Documento origen: `sistema-de-lealtad-260207_0817.docx`
