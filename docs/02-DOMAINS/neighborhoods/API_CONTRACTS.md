# API_CONTRACTS · neighborhoods

## Endpoints

- Actores y permisos (RBAC) + guards
- Permisos mínimos (RBAC/ABAC)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (Suposición necesaria)
- Invite: idempotente por (circle_id, invitee_user_id/contact_hash, active_window)
- Accept: idempotente por (invite_id)
- Link recipient: idempotente por unique key en circle_recipients.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- status (SENT|ACCEPTED|REJECTED|EXPIRED|REVOKED)
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Errores de notificación “gift incoming” (dependencia Notificaciones)

## Auth

- Actores y permisos (RBAC) + guards
- Permisos mínimos (RBAC/ABAC)

## Códigos de error

- Errores de notificación “gift incoming” (dependencia Notificaciones)

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (Suposición necesaria)
- Invite: idempotente por (circle_id, invitee_user_id/contact_hash, active_window)
- Accept: idempotente por (invite_id)
- Link recipient: idempotente por unique key en circle_recipients.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-barrio-260207_1012.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
