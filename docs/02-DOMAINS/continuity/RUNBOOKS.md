# RUNBOOKS · continuity

## Operación
- Observabilidad y respuesta automática: monitoreo de anomalías por país/rol y disparo de medidas (hold, bloqueo, reroute).
- Re-enrutamiento de colas operativas cuando falta COL (incidentes, aprobaciones, tickets/disputas).
- Detección/alerta de abuso de rol (break-glass bursts, exportaciones, cambios de zona, spikes de aprobaciones).
- COUNTRY_OPS_LEAD (COL): operación local (control plane).
- Reroute colas: items que antes iban al COL (incidentes L3, aprobaciones, etc.) pasan a GLOBAL_ONCALL_QUEUE/SUPER_ADMIN_QUEUE.
- Trigger: anomalías por seguridad/abuso (ver 9) o incidentes de integridad.

## Incidentes, rollback y backfill
- Re-enrutamiento de colas operativas cuando falta COL (incidentes, aprobaciones, tickets/disputas).
- Reroute colas: items que antes iban al COL (incidentes L3, aprobaciones, etc.) pasan a GLOBAL_ONCALL_QUEUE/SUPER_ADMIN_QUEUE.
- Trigger: anomalías por seguridad/abuso (ver 9) o incidentes de integridad.
- ACTIVE (reinstatement): retorno pleno con monitoreo reforzado post-incidente.
- A2. Reroute operativo (0–60 min)4) Reroute de colas: approvals, incidentes, tickets/disputas a GLOBAL_ONCALL_QUEUE/SUPER_ADMIN_QUEUE.
- 7) “Done criteria” por fase (para cerrar incidentes)
- Sistema de Continuidad v2.0 (Solo Continuidad) — “Role Continuity & Country Governance”
- Fuente de verdad: Documento “resumen-260207_1014”.


## Control operativo verificable

- Owner: `Equipo continuity`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-CONTINUITY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/continuity/dominio-continuity-operacion`
  - `https://jira.aventide.gift/browse/OPS-CONTINUITY-241`

## Trazabilidad
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo continuity`
- **Owner negocio/regulatorio:** `Product + Compliance (continuity)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

