# EVENT_CONTRACTS · platform-structure

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Tabla idempotency_keys para endpoints críticos; dedupe de webhooks por provider_event_id + firma + ventana.
- webhook_events_raw(provider, provider_event_id, signature_valid, payload_json, received_at, dedupe_key, processed_at, processing_status)
- 8) Eventos y triggers (estructura de integración)
- Emisión confiable de eventos por transiciones (Outbox Pattern) para notificaciones/analítica/workers y trazabilidad del “money journey”.
- Document pipeline: emitir por eventos PAID_IN_ESCROW, COMPLETED, REFUND, con idempotencia document_key=(order_id, doc_type, issuer_entity, version).
- Logs JSON obligatorios con campos estándar (trace_id, request_id, job_id, country/hub/zone, ids dominio, provider_event_id, idempotency_key, status/error/retry/latency).
- Definición: Estructura de deployment es el conjunto de entornos, pipelines, artefactos, estrategias de release y rollback que permiten desplegar el monolito modular (API), los workers (BullMQ), y las superficies (web/mobile/paneles), garantizando:
- “Release complete” + audit event.
- Estructura v2.0 (Estructura del Proyecto / Plataforma Aventide Gift)
- Fuente de verdad: “estructura-260207_1042.docx”.

## Trazabilidad
- Documento origen: `estructura-v2-260207_1049.docx`
