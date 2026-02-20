# RUNBOOKS · moderation

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Observabilidad: métricas por signals/colas y alertas por waves.
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo

## Incidentes, rollback y backfill
- Por contenido: event_key = (content_type, content_id, change_version) evita doble moderación por reintentos.
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Moderación es un sistema transversal que gobierna qué contenido UGC puede existir, cuándo se vuelve visible/“válido” y qué consecuencias operativas se aplican al usuario (restricciones, shadowban, ban, reserva de fondos, freeze), manteniendo el marketplace legal, seguro y difícil de abusar. Todo UGC (producto, review, chat, fotos, PoD) pasa por un embudo oficial de 4 capas antes de ser visible o aceptado como evidencia operativa.
- Objetivos:
- Evitar contenido ilegal, fraude, spam y “platform leakage” (evasión por contacto/pago directo).
- Minimizar falsos positivos con risk scoring + revisión humana.

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
