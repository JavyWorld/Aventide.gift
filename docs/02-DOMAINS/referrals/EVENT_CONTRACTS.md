# EVENT_CONTRACTS · referrals

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Ser reversible: toda recompensa registrada en ledger y reversible por eventos negativos.
- Si falla gating fuerte → FRAUD_BLOCKED (si evidencia fuerte) o REVOKED (si evento negativo).
- Cualquier evento negativo durante hold o post-grant:
- 6.4 referral_events (append-only)
- referral_events(attribution_id, type, payload_json, created_at)Tipos esperados (mínimo coherente con estados):
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos analíticos (existentes en docs)
- Consumir eventos de REFUND_EXECUTED, CHARGEBACK_RECEIVED, DISPUTE_RESOLVED para reversión.
- Sistema de Referidos v2.0 (Referral Program) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X E).


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
