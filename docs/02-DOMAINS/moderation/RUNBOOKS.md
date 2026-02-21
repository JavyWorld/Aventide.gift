# RUNBOOKS · moderation

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Observabilidad: métricas por signals/colas y alertas por waves.
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora

## Incidentes, rollback y backfill
- Por contenido: event_key = (content_type, content_id, change_version) evita doble moderación por reintentos.
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Moderación es un sistema transversal que gobierna qué contenido UGC puede existir, cuándo se vuelve visible/“válido” y qué consecuencias operativas se aplican al usuario (restricciones, shadowban, ban, reserva de fondos, freeze), manteniendo el marketplace legal, seguro y difícil de abusar. Operación definida y validada UGC (producto, review, chat, fotos, PoD) pasa por un embudo oficial de 4 capas antes de ser visible o aceptado como evidencia operativa.
- Objetivos:
- Evitar contenido ilegal, fraude, spam y “platform leakage” (evasión por contacto/pago directo).
- Minimizar falsos positivos con risk scoring + revisión humana.


## Control operativo verificable

- Owner: `Equipo moderation`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MODERATION-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/moderation/dominio-moderation-operacion`
  - `https://jira.aventide.gift/browse/OPS-MODERATION-241`

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
