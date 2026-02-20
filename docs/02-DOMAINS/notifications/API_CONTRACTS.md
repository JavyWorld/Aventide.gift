# API_CONTRACTS · notifications

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- error_code
- (provider,error_code,created_at desc)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- PAYMENT_AUTHORIZED
- 7.2 Idempotencia (reglas duras)
- Inbox: idempotente por (event_id, recipient_user_id, template_id) (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- WhatsApp (si opt-in) o SMS fallback
- error_code
- retry_count
- (provider,error_code,created_at desc)
- ORDER_ACCEPTED / ORDER_REJECTED

## Trazabilidad
- Documento origen: `sistema-de-notificaciones-260207_0929.docx`
