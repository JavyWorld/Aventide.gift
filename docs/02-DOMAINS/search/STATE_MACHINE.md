# STATE_MACHINE · search

## Estados

- Motor de Contenido/Catálogo (solo consume su estado “ACTIVE”, stock, tags, etc.).
- Corrección clave: “% resultados no comprables” debe tender a 0 porque se filtra por zona/estado.
- Estados: product_status, seller_status

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Pipeline de eventos: search_impression/click/add_to_cart/purchase/zero_results → ranking + trending.
- TrendingScore con decay por eventos ponderados (search/click/add_to_cart/purchase).
- Eventos analíticos (señales de ranking + trending)
- Ingest de eventos: event_id único (dedupe).
- Analítica: eventos search_impression/click/atc/purchase/zero_results alimentan trending y ranking.


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
