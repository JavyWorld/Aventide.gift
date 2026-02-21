# EVENT_CONTRACTS · payments

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Webhook duplicado: dedupe por provider_event_id / rapyd_transaction_id.
- emite evento a cola,
- event_type (PAYMENT_RECEIVED_ESCROW, FUNDS_RELEASED_TO_WALLETS, REFUND_ISSUED, CHARGEBACK_RECEIVED, …)
- (event_type, ts_utc)
- dispute_cases, dispute_outcomes_catalog, dispute_events (append-only) — referencian snapshot y ledger.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos mínimos
- webhook:{provider_event_id} unique
- Webhooks: fuente de eventos + reconciliación.
- Analítica: eventos server-side (PAYMENT_ESCROWED, ESCROW_RELEASED, REFUND_ISSUED…) alimentan facts/rollups.


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
