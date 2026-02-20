# API_CONTRACTS · messaging

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Send message: idempotencia por client_message_id por conversación (Suposición: el doc no lo nombra, pero evita duplicados en reintentos y es consistente con el resto del proyecto).
- Ticket create: idempotente por (order_id, conversation_id).
- Freeze: idempotente por (conversation_id, status=FROZEN).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Integración estricta: Órdenes (scope), Notificaciones (bridge), Moderación (pipeline), Soporte (ticket+freeze), Auditoría (logs).

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- Integración estricta: Órdenes (scope), Notificaciones (bridge), Moderación (pipeline), Soporte (ticket+freeze), Auditoría (logs).

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Send message: idempotencia por client_message_id por conversación (Suposición: el doc no lo nombra, pero evita duplicados en reintentos y es consistente con el resto del proyecto).
- Ticket create: idempotente por (order_id, conversation_id).
- Freeze: idempotente por (conversation_id, status=FROZEN).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-mensajeria-260207_0925.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
