# EVENT_CONTRACTS · reputation-buyer

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- SYSTEM/BOT: calcula score, aplica fricción y límites, genera eventos, mantiene historial.
- 4.1 Cálculo continuo por eventos (event-driven)
- Eventos relevantes actualizan buyer_metrics_rollup (ventanas 30/90/180) y luego recalculan score:
- Duplicados: idempotencia por (buyer_id, event_id) en rollups.
- “Eventos tardíos” (chargeback meses después): recalcula ventanas afectadas y emite BUYER_TRUST_RECALCULATED con audit trail.
- pin_withheld_events (retención/negativa del PIN sin causa)
- 6.5 penalty_events (Buyer)
- penalty_events(entity_type=Buyer, entity_id, penalty_code, severity, reason_codes[], starts_at, ends_at, created_by(AUTO|ADMIN), audit_ref)
- 7) Eventos y triggers + idempotencia
- Eventos mínimos (buyer trust)


## Control operativo verificable

- Owner: `Equipo reputation-buyer`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-REPUTATIONBU-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reputation-buyer/dominio-reputation-buyer-operacion`
  - `https://jira.aventide.gift/browse/OPS-REPUTATIONBU-241`

## Trazabilidad
- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
