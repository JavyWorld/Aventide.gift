# INVARIANTS · content

Reglas no negociables del dominio:
- Fuente de verdad: “Sistema de Contenidos — Motor de Contenido y Catálogo (Content & Experience Engine)”.Objetivo del rewrite: eliminar incoherencias típicas de catálogo (publicación sin capacidad/logística, variaciones locales caóticas, UGC sin control, stock mostrando cosas incomprables, fuga de plataforma, moderación inconsistente) y dejarlo robusto, multi-país, policy-driven, auditable, y 100% integrado con Capacidad, Logística y Reputación/Moderación.
- Si seller trusted (reputación > 90): Fast Track (publicación automática) con auditoría posterior aleatoria.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- Mutaciones con idempotency_key (submit, approve, pause, upload asset).
- Input: score seller; si >90 habilita fast-track con auditoría posterior.
- 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)
- Auditoría obligatoria
- Sistema de Contenido v2.0 (corregido y unificado)
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora


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
