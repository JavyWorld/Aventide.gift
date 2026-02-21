# RUNBOOKS · geo-intelligence-map

## Operación
- Ops Lead ve el mapa solo dentro de su operación (país completo, zonas activas e inactivas visibles) y opera cambios permitidos (ej. estado de zona).
- SuperAdmin/Global Management ve el mundo completo y puede “drill down” Mundo→País→Hub→Zona→Seller.
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.
- Operación de zona: cambiar estado de zona (kill switch / paused / saturated) desde el mapa, con motivo y auditoría.
- Regla “solo ve su operación”
- 5.4 Versionado/rollback de capas

## Incidentes, rollback y backfill
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.
- 5.4 Versionado/rollback de capas
- Capas del mapa son datasets versionados; población debe tener census_dataset_version; el mapa sirve “current” por país con rollback si falla ingesta (patrón resiliencia).
- Fallback/rollback: si falla ingesta, mantener dataset_version_current y alertar; permitir rollback explícito auditado.
- Si quieres que quede 100% cerrado “por país” (CO/USA/RD), hace falta que indiques qué fuente oficial usar en cada uno; el sistema ya queda definido para soportarlo vía Integration Registry + adapters + versionado/rollback.
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora


## Control operativo verificable

- Owner: `Equipo geo-intelligence-map`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GEOINTELLIGE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/geo-intelligence-map/dominio-geo-intelligence-map-operacion`
  - `https://jira.aventide.gift/browse/OPS-GEOINTELLIGE-241`

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo geo-intelligence-map`
- **Owner negocio/regulatorio:** `Product + Compliance (geo-intelligence-map)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

