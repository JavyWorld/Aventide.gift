# DATA_CONTRACTS · search

## Entidades y campos
- Indexación: OpenSearch/Elasticsearch como índice principal; Postgres como fuente de verdad.
- SYSTEM/BOT: indexación, scoring jobs, trending jobs.
- search.index.rebuild (system/admin con break-glass si aplica)
- Cambios rápidos (seller suspendido / producto pausado): invalidación de caché y deindexación; objetivo: cero “no comprables”.
- Corrección clave: “% resultados no comprables” debe tender a 0 porque se filtra por zona/estado.
- BM25/lexical con campos ponderados: title^3, category^2, tags^2, seller_name^1.5, description^1
- 6.1 Search Index (OpenSearch/Elastic) — documento “ProductSearchDoc”
- Campos mínimos (recomendados por el diseño):

## Constraints y claves de negocio
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- Corrección clave: “% resultados no comprables” debe tender a 0 porque se filtra por zona/estado.
- Auditoría append-only para cada cambio.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- Ingest de eventos: event_id único (dedupe).
- Caché por key = hash(query + context + filters + sort).
- Logs sin PII; usar IDs internos/hashed si hace falta.


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
