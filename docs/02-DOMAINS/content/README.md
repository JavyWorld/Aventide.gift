# content

## Propósito

- Sistema de Contenido v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- content.product.reject (moderator/ops)
- content.product_approved/rejected
- ugc.review_submitted/approved/rejected/blocked
- Documento origen: `sistema-de-contenido-260206_2344.docx`
- Moderation State (gate de calidad).
- Definición y objetivos del sistema/módulo
- Definición: Motor que gestiona la “Verdad Visible” del marketplace: todo lo que se muestra en feed/búsqueda/ficha y todo lo que se puede comprar con confianza. Un producto no es un registro plano: es un objeto inteligente con:
- Integridad
- Título extraído: "Sistema de Contenido v2.0 (corregido y unificado)".

## Límites

- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- Suspensión seller lenta → corregido: regla de desindex < 1 minuto con evento y métricas.
- Alcance (incluye / excluye)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Jerarquía/RBAC: Ops Lead scoped por país para revisión; seller solo lo suyo.
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Integración con IA (ej. Rekognition/Vision) para nudity/text/contact info/duplication signals.

## Trazabilidad

- Documento origen: `sistema-de-contenido-260206_2344.docx`
- Título extraído: "Sistema de Contenido v2.0 (corregido y unificado)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
