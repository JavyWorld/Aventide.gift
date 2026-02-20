# STATE_MACHINE · observability

## Estados detectados/derivados
- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- 4) Flujos end-to-end (happy path + edge cases)
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- 4.2 Flujo “Money Pipeline” (monitor de invariantes)
- Órdenes activas continúan; no se rompe el flujo existente.
- No “estado final sin rastro”: todo irreversible deja telemetría + auditoría.

## Transiciones y eventos de entrada/salida
- Telemetría de: backend API, workers, webhooks, DB, cache, colas, integraciones (Rapyd, WhatsApp/SMS, Email, Storage, Maps), Policy Engine + App Camaleón.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- Idempotencia real (pagos, webhooks, payouts).
- 7) Eventos y triggers + idempotencia
- Eventos (mínimos)
- Métricas: error rate, latencia p95, webhooks in/dedup, signature invalid.
- webhook_invalid_signature_rate > 0 (ataque/misconfig)

## Trazabilidad
- Documento origen: `sistema-de-observalidad-260207_0755.docx`
