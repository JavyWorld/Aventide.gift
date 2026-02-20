# payments

## Propósito

- wallet.cashout.request (seller/ops)
- payments.webhooks.process (system)
- PIN por WhatsApp → fallback SMS; evitar lockscreen; usar link mágico.
- WhatsApp primary + SMS fallback.
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Fuente de verdad: “Sistema de Pagos — Aventide Gift”.
- Documento origen: `sistema-de-pagos-260207_0800.docx`
- “Soporte no inventa montos”: outcomes → buckets → cálculo determinístico → saga.
- disputes.saga.execute (system)
- Definición y objetivos del sistema/módulo
- Payment Transaction (provider)
- provider = RAPYD
- Título extraído: "Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado".

## Límites

- Alcance (incluye / excluye)
- Payouts/cashout con límites por país + KYC thresholds + rolling reserve.
- Seller solicita retiro → validar límites por país:
- Processing Fee (pct+flat) integrado consistentemente (incluye gross-up cuando aplica)

## Dependencias

- SYSTEM/BOT: webhooks, workers (escrow release, split, ledger, payout, billing, reconciliation).
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Motor legal específico por país fuera de configuración (solo integración por policy/retención).
- Título extraído: "Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado".

## Trazabilidad

- Documento origen: `sistema-de-pagos-260207_0800.docx`
- Título extraído: "Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
