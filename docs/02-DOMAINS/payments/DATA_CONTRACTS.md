# DATA_CONTRACTS · payments

## Entidades y campos
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Registrar todo en un ledger interno inmutable,
- “Snapshot manda”: fees/taxes/processing se snapshottean en la orden para no cambiar retrospectivamente.
- Split de fondos por orden y ledger inmutable como fuente contable.
- SYSTEM/BOT: webhooks, workers (escrow release, split, ledger, payout, billing, reconciliation).
- ledger.read (finance/audit)
- 4.1 Checkout → Cobro buyer (Rapyd Collect) + snapshot
- Se crea orden con locked_fee_structure, locked_tax_config, locked_processing_fee (snapshot).

## Constraints y claves de negocio
- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- “Dinero retenido”: no sale de escrow sin entrega confirmada o decisión de disputa.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- valida hash del PIN (nunca PIN plano),
- valida estado e idempotencia.
- Regla dura: Soporte elige outcome template + banda/items; el sistema calcula buckets desde snapshot + policy; ejecuta Saga idempotente.
- EXECUTE_REFUND (si aplica; idempotency key refund:{order}:{dispute}:{attempt})

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
