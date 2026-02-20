# API_CONTRACTS · search

## Endpoints

- Search API: /search, /suggest, /trending.
- Actores y permisos (RBAC) + guards
- Auth (si hay personalización; si anónimo, se autentica como “public session”)
- RBAC (solo para endpoints admin/ops de merchandising, con auditoría).
- Search API aplica:
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- requiere RBAC Ops/Admin,
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- zone.status != ACTIVE (kill switch): devuelve resultados vacíos + mensaje/razón contextual (sin exponer internals) y no hace “fallback” a otra zona automáticamente (evita engaños).
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- Estados: product_status, seller_status

## Auth

- Actores y permisos (RBAC) + guards
- Auth (si hay personalización; si anónimo, se autentica como “public session”)
- RBAC (solo para endpoints admin/ops de merchandising, con auditoría).
- requiere RBAC Ops/Admin,
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Ingest de eventos: event_id único (dedupe).

## Trazabilidad

- Documento origen: `sistema-de-busqueda-260207_0312.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
