# RUNBOOKS · governance-cameleon

## Operación
- Cero hardcode por país: UI y reglas cambian desde consola ops con auditoría + rollback.
- Consola “Regional OS”: edición visual de UI + rulesets + simulador + auditoría + rollback.
- COUNTRY_OPS_LEAD: administra hubs/zones y rulesets; edita ui_profile; programa cambios; rollback.
- rollback.execute (ops lead/admin; scoped)
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- rollback_total{entity_type,country}

## Incidentes, rollback y backfill
- Cero hardcode por país: UI y reglas cambian desde consola ops con auditoría + rollback.
- Consola “Regional OS”: edición visual de UI + rulesets + simulador + auditoría + rollback.
- COUNTRY_OPS_LEAD: administra hubs/zones y rulesets; edita ui_profile; programa cambios; rollback.
- rollback.execute (ops lead/admin; scoped)
- rollback_total{entity_type,country}
- rollbacks frecuentes (governance inestable)
- Rollback rápido: siempre disponible con historial.
- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado


## Control operativo verificable

- Owner: `Equipo governance-cameleon`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GOVERNANCECA-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/governance-cameleon/dominio-governance-cameleon-operacion`
  - `https://jira.aventide.gift/browse/OPS-GOVERNANCECA-241`

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
