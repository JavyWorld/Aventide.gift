# EVENT_CONTRACTS · observability

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Garantizar trazabilidad completa del “money pipeline”; no puede existir DELIVERED_VERIFIED sin settlement/payout o causa visible (retry/DLQ/HOLD/disputa).
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- provider, provider_request_id, provider_event_id
- 7) Eventos y triggers + idempotencia
- Eventos (mínimos)
- Sistema de Observabilidad v2.0 (SRE / “Sistema Nervioso Central”) — corregido y unificado
- Fuentes de verdad:
- “Observabilidad (SRE) — Especificación Técnica”
- “Sistema— Observabilidad + Resiliencia (SRE / ‘Sistema Nervioso Central’)”

## Trazabilidad
- Documento origen: `sistema-de-observalidad-260207_0755.docx`
