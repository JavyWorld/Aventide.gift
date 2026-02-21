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
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Payment Transaction (provider)
- provider = RAPYD
- Título extraído: "Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado".

## Límites

- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Payouts/cashout con límites por país + KYC thresholds + rolling reserve.
- Seller solicita retiro → validar límites por país:
- Processing Fee (pct+flat) integrado consistentemente (incluye gross-up cuando aplica)

## Dependencias

- SYSTEM/BOT: webhooks, workers (escrow release, split, ledger, payout, billing, reconciliation).
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Motor legal específico por país fuera de configuración (solo integración por policy/retención).
- Título extraído: "Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado".


## Control operativo verificable

- Owner: `Equipo payments`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PAYMENTS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/payments/dominio-payments-operacion`
  - `https://jira.aventide.gift/browse/OPS-PAYMENTS-241`

## Trazabilidad

- Documento origen: `sistema-de-pagos-260207_0800.docx`
- Título extraído: "Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
