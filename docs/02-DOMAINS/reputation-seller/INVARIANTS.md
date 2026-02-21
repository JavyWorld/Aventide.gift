# INVARIANTS · reputation-seller

Reglas no negociables del dominio:
- Definición: Sistema que calcula y expone la Reputación del Seller (pública) y el Seller Score operativo (interno) usando únicamente “verdad verificada” (órdenes COMPLETED con PIN, outcomes de disputas, cancelaciones con culpa atribuida y señales auditables).
- Integrarse sin romper invariantes: Órdenes (solo COMPLETED), Disputas (outcomes), Moderación (review/media), Búsqueda/Ranking (performance multipliers) y Pagos (rolling reserve/freeze por policy, no por acción manual).
- reputation.penalties.enforce (system/admin; auditado)
- reputation.badges.manage (system/admin; auditado)
- reputation.audit.read (audit/finance/admin)
- AuditGuard (cambios de score/badge/penalty y review status quedan trazables)
- Regla dura: UI muestra Rating_bayes + #reviews (nunca R sin bayesiano).
- Regla dura: badges se revocan si cae el desempeño (no “para siempre”).
- penalty_events(entity_type=Seller, entity_id, penalty_code, severity, reason_codes[], starts_at, ends_at, created_by(AUTO|ADMIN), audit_ref)Índices:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia


## Control operativo verificable

- Owner: `Equipo reputation-seller`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-REPUTATIONSE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reputation-seller/dominio-reputation-seller-operacion`
  - `https://jira.aventide.gift/browse/OPS-REPUTATIONSE-241`

## Trazabilidad
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
