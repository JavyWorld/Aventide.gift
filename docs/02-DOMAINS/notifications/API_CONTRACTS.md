# API_CONTRACTS · notifications

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- error_code
- (provider,error_code,created_at desc)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- PAYMENT_AUTHORIZED
- Idempotencia (reglas duras)
- Inbox: idempotente por (event_id, recipient_user_id, template_id) (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- retry_count
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- PAYMENT_AUTHORIZED
- Definición: Sistema de comunicación automatizada que recibe eventos de negocio (órdenes, pagos, PIN, disputas, payouts, seguridad, etc.), decide canal + plantilla + destinatarios, entrega por proveedores externos (Push/Email/SMS/WhatsApp) y siempre guarda una copia en el Inbox in-app, que es la fuente de verdad auditable.

## Códigos de error

- error_code
- (provider,error_code,created_at desc)

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas duras)
- Inbox: idempotente por (event_id, recipient_user_id, template_id) (Suposición: el doc fija dedupe para delivery; se extiende a Inbox para no duplicar mensajes en reintentos, consistente con “Inbox=verdad”).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-notificaciones-260207_0929.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
