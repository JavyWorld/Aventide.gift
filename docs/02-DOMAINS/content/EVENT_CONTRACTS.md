# EVENT_CONTRACTS · content

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Contenido
- event_id único por transición.
- Suspensión seller lenta → corregido: regla de desindex < 1 minuto con evento y métricas.
- Sistema de Contenido v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Motor que gestiona la “Verdad Visible” del marketplace: Operación definida y validada lo que se muestra en feed/búsqueda/ficha y Operación definida y validada lo que se puede comprar con confianza. Un producto no es un registro plano: es un objeto inteligente con:
- Core_Data (global),
- Localized_Data (por país/idioma/temporada),


## Control operativo verificable

- Owner: `Equipo content`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-CONTENT-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/content/dominio-content-operacion`
  - `https://jira.aventide.gift/browse/OPS-CONTENT-241`

## Trazabilidad
- Documento origen: `sistema-de-contenido-260206_2344.docx`
