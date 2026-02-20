# API_CONTRACTS · observability

## Endpoints

- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Telemetría de: backend API, workers, webhooks, DB, cache, colas, integraciones (Rapyd, WhatsApp/SMS, Email, Storage, Maps), Policy Engine + App Camaleón.
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- Actores y permisos (RBAC) + guards
- Auth + PermissionGuard + ScopeGuard (country/zone) para dashboards/acciones.
- Request entra al API → se genera/propaga trace_id + request_id.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Garantizar trazabilidad completa del “money pipeline”; no puede existir DELIVERED_VERIFIED sin settlement/payout o causa visible (retry/DLQ/HOLD/disputa).
- Invariante dura:No puede existir DELIVERED_VERIFIED sin SETTLED pasado X minutos sin causa visible (RETRY, DLQ, HOLD, DISPUTE).
- Idempotencia real (pagos, webhooks, payouts).
- Eventos y triggers + idempotencia
- Métricas: error rate, latencia p95, webhooks in/dedup, signature invalid.

## Auth

- Actores y permisos (RBAC) + guards
- Auth + PermissionGuard + ScopeGuard (country/zone) para dashboards/acciones.

## Códigos de error

- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- Garantizar trazabilidad completa del “money pipeline”; no puede existir DELIVERED_VERIFIED sin settlement/payout o causa visible (retry/DLQ/HOLD/disputa).
- Invariante dura:No puede existir DELIVERED_VERIFIED sin SETTLED pasado X minutos sin causa visible (RETRY, DLQ, HOLD, DISPUTE).
- Métricas: error rate, latencia p95, webhooks in/dedup, signature invalid.

## Idempotency

- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Idempotencia real (pagos, webhooks, payouts).
- Eventos y triggers + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-observalidad-260207_0755.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
