# STATE_MACHINE · search

## Estados detectados/derivados
- Pipeline de eventos: search_impression/click/add_to_cart/purchase/zero_results → ranking + trending.
- Motor de Contenido/Catálogo (solo consume su estado “ACTIVE”, stock, tags, etc.).
- 4) Flujos end-to-end (happy path + edge cases)
- TrendingScore con decay por eventos ponderados (search/click/add_to_cart/purchase).
- Corrección clave: “% resultados no comprables” debe tender a 0 porque se filtra por zona/estado.
- Estados: product_status, seller_status

## Transiciones y eventos de entrada/salida
- Pipeline de eventos: search_impression/click/add_to_cart/purchase/zero_results → ranking + trending.
- TrendingScore con decay por eventos ponderados (search/click/add_to_cart/purchase).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos analíticos (señales de ranking + trending)
- Ingest de eventos: event_id único (dedupe).
- Analítica: eventos search_impression/click/atc/purchase/zero_results alimentan trending y ranking.
- Sistema de Búsqueda v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.

## Trazabilidad
- Documento origen: `sistema-de-busqueda-260207_0312.docx`
