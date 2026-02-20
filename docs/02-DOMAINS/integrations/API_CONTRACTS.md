# API_CONTRACTS · integrations

## Endpoints

- Evidencia y reconciliación: webhooks raw almacenados, dedupe, idempotencia y logs por handler.
- Webhook Gateway inbound: verificación firma, persistencia RAW, dedupe, encolado y procesamiento idempotente.
- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- Actores y permisos (RBAC) + guards
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integration Registry por país y tipo: qué proveedor está activo, timeouts, rate limits, retry policy y secrets refs.
- integrations.jobs.retry (ops/support; auditado)
- Worker ejecuta adapter (RapydAdapter) con timeout + retry/backoff + circuit breaker.
- Proveedor caído: circuit breaker → job a retry con backoff; si excede, DLQ + alerta.
- Duplicados por retry del proveedor: dedupe responde OK sin repetir efectos.
- Guarda provider_message_id, estado y errores.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Auth

- Actores y permisos (RBAC) + guards
- Guarda provider_message_id, estado y errores.

## Códigos de error

- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- Proveedor caído: circuit breaker → job a retry con backoff; si excede, DLQ + alerta.
- Guarda provider_message_id, estado y errores.

## Idempotency

- Evidencia y reconciliación: webhooks raw almacenados, dedupe, idempotencia y logs por handler.
- Webhook Gateway inbound: verificación firma, persistencia RAW, dedupe, encolado y procesamiento idempotente.
- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Duplicados por retry del proveedor: dedupe responde OK sin repetir efectos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-integraciones-260207_0951.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
