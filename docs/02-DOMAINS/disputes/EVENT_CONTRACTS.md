# EVENT_CONTRACTS · disputes

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Reglas fiscales específicas de cada país (se delegan a Facturación & Documentos, invocadas por evento).
- Se crea dispute_case y dispute_events (append-only).
- 6.3 dispute_events (append-only)
- event_id
- event_type (OPENED|EVIDENCE_REQUESTED|EVIDENCE_RECEIVED|OUTCOME_SELECTED|OUTCOME_COMPUTED|SAGA_STEP_*|RESOLVED)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Disputas
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- Fuente de verdad: “Disputas y Resolución (Saga) — ESPECIFICACIÓN FINAL”.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
