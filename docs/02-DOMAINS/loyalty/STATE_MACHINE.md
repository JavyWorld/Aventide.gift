# STATE_MACHINE · loyalty

## Estados detectados/derivados
- “Fases de Desarrollo v1.1 — Loyalty (ledger-first) + eventos + modelo de datos”
- 4) Flujos end-to-end (happy path + edge cases)
- Backend aplica FS con clamp duro:fs_applied = min(fs_balance_available, platform_fee_amount)y genera evento FEE_CREDIT_APPLIED (max_applied = platform_fee_amount).
- 6.1 loyalty_accounts (estado materializado)
- caps_state_monthly (JSON: used_fs_this_month, month_key, etc.)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Transiciones y eventos de entrada/salida
- “Fases de Desarrollo v1.1 — Loyalty (ledger-first) + eventos + modelo de datos”
- Backend aplica FS con clamp duro:fs_applied = min(fs_balance_available, platform_fee_amount)y genera evento FEE_CREDIT_APPLIED (max_applied = platform_fee_amount).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- No reversión ante refund/chargeback → corregido: eventos REVOKED/ajuste negativo y bloqueo según policy país.
- Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos”
- Integración obligatoria con Disputas/Refunds (reversión)

## Trazabilidad
- Documento origen: `sistema-de-lealtad-260207_0817.docx`
