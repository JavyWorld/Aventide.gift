# API_CONTRACTS · content

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- Auth
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- Mutaciones con idempotency_key (submit, approve, pause, upload asset).
- Jerarquía/RBAC: Ops Lead scoped por país para revisión; seller solo lo suyo.
- Sistema de Contenido v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- content.product.reject (moderator/ops)
- Rechazo: estado REJECTED con razón específica (“foto borrosa”, “descripción engañosa”).
- content.product_approved/rejected
- ugc.review_submitted/approved/rejected/blocked
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Trazabilidad
- Documento origen: `sistema-de-contenido-260206_2344.docx`
