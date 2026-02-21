# RUNBOOKS · reputation-buyer

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Spike de cancelaciones tardías (operación/logística rota)
- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora

## Incidentes, rollback y backfill
- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que calcula un Buyer Trust Score (0–100) y lo expone al seller como Trust Level + Trust Badge (semi-visible) para equilibrar privacidad (incl. “Admirador Secreto”) con seguridad operacional. No es público ni “humilla” al buyer; es un control de riesgo para sellers y plataforma.
- Objetivos:
- Reducir fraude/chargebacks, abuso de cancelaciones y disputas maliciosas sin matar conversión.
- Ser resistente a abuso: anti-review bombing, anti-multicuentas y anti-extorsión en chat.
- Ser explicable y auditable: score con subscores, historial diario y reason codes.


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
