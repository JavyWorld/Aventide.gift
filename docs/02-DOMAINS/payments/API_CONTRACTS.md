# API_CONTRACTS · payments

## Endpoints y auth
- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- 3) Actores y permisos (RBAC) + guards
- SYSTEM/BOT: webhooks, workers (escrow release, split, ledger, payout, billing, reconciliation).
- wallet.cashout.request (seller/ops)
- payments.webhooks.process (system)
- Auth

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- PIN por WhatsApp → fallback SMS; evitar lockscreen; usar link mágico.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- WhatsApp primary + SMS fallback.
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Fuente de verdad: “Sistema de Pagos — Aventide Gift”.

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
