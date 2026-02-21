# RUNBOOKS · search

## Operación
- Publicación por versión (rollback rápido).
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Búsqueda v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora

## Incidentes, rollback y backfill
- Publicación por versión (rollback rápido).
- Sistema de Búsqueda v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Búsqueda es el sistema que devuelve resultados (productos/sellers/categorías/colecciones) en función de un SearchContext obligatorio, aplicando:
- Query understanding (normalización, sinónimos, typos).
- Filtros visibles (facets) + filtros invisibles (guardrails).
- Ranking por etapas (retrieval + scoring).


## Control operativo verificable

- Owner: `Equipo search`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-SEARCH-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/search/dominio-search-operacion`
  - `https://jira.aventide.gift/browse/OPS-SEARCH-241`

## Trazabilidad
- Documento origen: `sistema-de-busqueda-260207_0312.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo search`
- **Owner negocio/regulatorio:** `Product + Compliance (search)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

