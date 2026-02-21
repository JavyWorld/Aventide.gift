# EVENT_CONTRACTS · search

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Pipeline de eventos: search_impression/click/add_to_cart/purchase/zero_results → ranking + trending.
- TrendingScore con decay por eventos ponderados (search/click/add_to_cart/purchase).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos analíticos (señales de ranking + trending)
- Ingest de eventos: event_id único (dedupe).
- Analítica: eventos search_impression/click/atc/purchase/zero_results alimentan trending y ranking.
- Sistema de Búsqueda v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Búsqueda es el sistema que devuelve resultados (productos/sellers/categorías/colecciones) en función de un SearchContext obligatorio, aplicando:


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
