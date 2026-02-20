# API_CONTRACTS · integrations

## Endpoints y auth
- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).
- Un pool de Workers asíncronos ejecuta llamadas externas y procesa confirmaciones vía Webhooks.
- No bloquear UX: llamadas externas críticas nunca se ejecutan en request síncrono (salvo validate liviano).
- Evidencia y reconciliación: webhooks raw almacenados, dedupe, idempotencia y logs por handler.
- Adapters por proveedor: PaymentsProvider, MessagingProvider, MapsProvider, StorageProvider + WebhookVerifier.
- Webhook Gateway inbound: verificación firma, persistencia RAW, dedupe, encolado y procesamiento idempotente.
- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- 3) Actores y permisos (RBAC) + guards

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Integration Registry por país y tipo: qué proveedor está activo, timeouts, rate limits, retry policy y secrets refs.
- integrations.jobs.retry (ops/support; auditado)
- Worker ejecuta adapter (RapydAdapter) con timeout + retry/backoff + circuit breaker.
- Proveedor caído: circuit breaker → job a retry con backoff; si excede, DLQ + alerta.
- Duplicados por retry del proveedor: dedupe responde OK sin repetir efectos.

## Trazabilidad
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
