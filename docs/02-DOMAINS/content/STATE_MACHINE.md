# STATE_MACHINE · content

## Estados detectados/derivados
- Moderation State (gate de calidad).
- Workflow de publicación y estados (DRAFT→PENDING→ACTIVE, etc.) con gates por capacidad/logística/moderación.
- Moderación/Trust & Safety completa (Contenido integra gates/estados y dispara/recibe decisiones).
- QualityGateGuard (capacidad + logística + assets + atributos requeridos + estado de seller)
- 4) Flujos end-to-end (happy path + edge cases)
- Rechazo: estado REJECTED con razón específica (“foto borrosa”, “descripción engañosa”).

## Transiciones y eventos de entrada/salida
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Contenido
- event_id único por transición.
- Suspensión seller lenta → corregido: regla de desindex < 1 minuto con evento y métricas.
- Sistema de Contenido v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- 1) Definición y objetivos del sistema/módulo
- Definición: Motor que gestiona la “Verdad Visible” del marketplace: todo lo que se muestra en feed/búsqueda/ficha y todo lo que se puede comprar con confianza. Un producto no es un registro plano: es un objeto inteligente con:

## Trazabilidad
- Documento origen: `sistema-de-contenido-260206_2344.docx`
