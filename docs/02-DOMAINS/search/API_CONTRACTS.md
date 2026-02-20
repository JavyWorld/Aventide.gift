# API_CONTRACTS · search

## Endpoints y auth
- Search API: /search, /suggest, /trending.
- 3) Actores y permisos (RBAC) + guards
- Auth (si hay personalización; si anónimo, se autentica como “public session”)
- RBAC (solo para endpoints admin/ops de merchandising, con auditoría).
- Search API aplica:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- requiere RBAC Ops/Admin,

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- zone.status != ACTIVE (kill switch): devuelve resultados vacíos + mensaje/razón contextual (sin exponer internals) y no hace “fallback” a otra zona automáticamente (evita engaños).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Búsqueda v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-de-busqueda-260207_0312.docx`
