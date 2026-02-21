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

## Ownership & Escalation

- **Owner técnico:** `Equipo governance-cameleon`
- **Owner negocio/regulatorio:** `Product + Compliance (governance-cameleon)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

