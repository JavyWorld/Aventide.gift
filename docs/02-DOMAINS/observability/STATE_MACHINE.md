# STATE_MACHINE · observability

## Estados

- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- No “estado final sin rastro”: todo irreversible deja telemetría + auditoría.

## Transiciones

- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)
- Flujo “Money Pipeline” (monitor de invariantes)
- Órdenes activas continúan; no se rompe el flujo existente.

## Triggers

- Request entra al API → se genera/propaga trace_id + request_id.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- Eventos y triggers + idempotencia
- Eventos (mínimos)

## Trazabilidad

- Documento origen: `sistema-de-observalidad-260207_0755.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
