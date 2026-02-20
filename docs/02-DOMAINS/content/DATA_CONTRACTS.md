# DATA_CONTRACTS · content

## Entidades y campos
- SYSTEM/BOT: pipelines de pre-moderación IA, indexación, invalidación de cachés, sincronización de visibilidad.
- content.attributes_schema.manage (super_admin)
- Falta alérgenos (categoría comida): el producto no sale de DRAFT (campo crítico).
- 4.3 Publicación (ACTIVE) e indexación
- Se indexa en búsqueda y feed.
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Entidad: products
- Entidad: product_localizations

## Constraints y claves de negocio
- category_id, country_code?, required_keys[], constraints_json (enum/range/regex)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- event_id único por transición.
- Mutaciones con idempotency_key (submit, approve, pause, upload asset).
- Sistema de Contenido v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-de-contenido-260206_2344.docx`
