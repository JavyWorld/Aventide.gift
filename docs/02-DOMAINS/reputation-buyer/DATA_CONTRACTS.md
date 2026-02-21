# DATA_CONTRACTS · reputation-buyer

## Entidades y campos
- Se guarda snapshot diario buyer_score_history con subscores, score final, delta y drivers.
- no se revela identidad, pero el seller sigue viendo el Trust Badge/Level para tomar decisiones seguras.
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Snapshot diario: (buyer_id, date)
- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que calcula un Buyer Trust Score (0–100) y lo expone al seller como Trust Level + Trust Badge (semi-visible) para equilibrar privacidad (incl. “Admirador Secreto”) con seguridad operacional. No es público ni “humilla” al buyer; es un control de riesgo para sellers y plataforma.

## Constraints y claves de negocio
- Duplicados: idempotencia por (buyer_id, event_id) en rollups.
- confirmaciones extra en fechas pico (high-demand).
- Cancelaciones tardías repetidas ⇒ límites + confirmaciones extra.
- 7) Eventos y triggers + idempotencia
- Idempotencia
- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora


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
