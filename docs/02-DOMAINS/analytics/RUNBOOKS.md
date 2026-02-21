# RUNBOOKS · analytics

## Operación
- Definición: Sistema de Analítica es el “HUB central” que captura, consolida y expone métricas de negocio y operación del marketplace, derivadas de:
- Modelos analíticos (facts/dims) y rollups para BI y operación near-real-time.
- Real-time operativo / eventual para BI profundo: operación “hoy/última hora” near-real-time; cohortes/finanzas pesadas con jobs.
- COUNTRY_OPS_LEAD (Regional OS): operación + crecimiento de su país/hub/zone.
- 4.3 Rollups para operación y BI
- 9) Observabilidad (logs, métricas, alertas, SLOs) — aplicado a Analítica

## Incidentes, rollback y backfill
- Reintento de evento: dedupe por event_id (idempotencia).
- Sistema de Analítica v2.0 (corregido y unificado)
- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema de Analítica es el “HUB central” que captura, consolida y expone métricas de negocio y operación del marketplace, derivadas de:
- Eventos críticos server-side (inmutables, append-only).
- Estados finales de órdenes y snapshots financieros (para evitar descuadres ante cambios futuros de fees/reglas).
- Modelos analíticos (facts/dims) y rollups para BI y operación near-real-time.


## Control operativo verificable

- Owner: `Equipo analytics`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ANALYTICS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/analytics/dominio-analytics-operacion`
  - `https://jira.aventide.gift/browse/OPS-ANALYTICS-241`

## Trazabilidad
- Documento origen: `sistema-de-analitica-260206_2336.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo analytics`
- **Owner negocio/regulatorio:** `Product + Compliance (analytics)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

