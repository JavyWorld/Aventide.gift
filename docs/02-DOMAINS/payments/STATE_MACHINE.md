# STATE_MACHINE · payments

## Estados detectados/derivados
- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “Soporte no inventa montos”: outcomes → buckets → cálculo determinístico → saga.
- Estados financieros acoplados a la máquina de órdenes (alto nivel).
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- disputes.saga.execute (system)
- StateGuard (compatibilidad con estados de orden: CREATED/PAID_IN_ESCROW/…)

## Transiciones y eventos de entrada/salida
- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- “Soporte no inventa montos”: outcomes → buckets → cálculo determinístico → saga.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- SYSTEM/BOT: webhooks, workers (escrow release, split, ledger, payout, billing, reconciliation).
- payments.webhooks.process (system)
- disputes.saga.execute (system)
- Webhook duplicado: dedupe por provider_event_id / rapyd_transaction_id.

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
