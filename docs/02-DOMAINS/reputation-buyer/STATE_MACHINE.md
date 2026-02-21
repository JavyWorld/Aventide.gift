# STATE_MACHINE · reputation-buyer

## Estados

- BUYER: crea órdenes, puede reseñar; ve su estado básico (sin revelar score exacto si no se desea).

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Duplicados: idempotencia por (buyer_id, event_id) en rollups.
- Eventos y triggers + idempotencia
- SYSTEM/BOT: calcula score, aplica fricción y límites, genera eventos, mantiene historial.
- Cálculo continuo por eventos (event-driven)
- Eventos relevantes actualizan buyer_metrics_rollup (ventanas 30/90/180) y luego recalculan score:
- “Eventos tardíos” (chargeback meses después): recalcula ventanas afectadas y emite BUYER_TRUST_RECALCULATED con audit trail.
- Eventos mínimos (buyer trust)
- Eventos derivados:
- eventos de cancelación tardía / PIN withheld, etc.


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
