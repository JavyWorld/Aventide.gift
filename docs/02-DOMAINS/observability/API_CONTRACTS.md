# API_CONTRACTS · observability

## Endpoints y auth
- Definición: Observabilidad es el sistema que hace la plataforma medible, auto-diagnosticable, auditada y recuperable, con telemetría completa (logs, métricas, trazas, health checks y alertas) y resiliencia (retries, idempotencia, colas/DLQ, circuit breakers, degradación) enfocada en el flujo crítico:Order → Payment → Delivery → PIN → Settlement → Payout, sin estados “mágicos” sin explicación.
- Telemetría de: backend API, workers, webhooks, DB, cache, colas, integraciones (Rapyd, WhatsApp/SMS, Email, Storage, Maps), Policy Engine + App Camaleón.
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- 3) Actores y permisos (RBAC) + guards
- Auth + PermissionGuard + ScopeGuard (country/zone) para dashboards/acciones.
- Request entra al API → se genera/propaga trace_id + request_id.
- Webhooks duplicados (Rapyd): dedupe por provider_event_id y idempotencia por idempotency_key; métricas de dedupe suben y disparan alerta.
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Garantizar trazabilidad completa del “money pipeline”; no puede existir DELIVERED_VERIFIED sin settlement/payout o causa visible (retry/DLQ/HOLD/disputa).
- Resiliencia: timeouts/retries, idempotencia, colas+DLQ, monitores de invariantes, circuit breaker y modo degradado.
- Evento crítico sin correlación (sin ids): se registra como error y se envía a DLQ/tabla de errores. (En “money pipeline” se exige causa visible).
- Invariante dura:No puede existir DELIVERED_VERIFIED sin SETTLED pasado X minutos sin causa visible (RETRY, DLQ, HOLD, DISPUTE).
- Si search degradado: fallback a colecciones curadas/home builder server-driven.

## Trazabilidad
- Documento origen: `sistema-de-observalidad-260207_0755.docx`
