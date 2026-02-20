# API_CONTRACTS · neighborhoods

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- Permisos mínimos (RBAC/ABAC)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- GIFT_INCOMING_NOTIFICATION_REQUESTED (checkout)
- Idempotencia (Suposición necesaria)
- Invite: idempotente por (circle_id, invitee_user_id/contact_hash, active_window)
- Accept: idempotente por (invite_id)
- Link recipient: idempotente por unique key en circle_recipients.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- circle.invite.accept / circle.invite.reject
- status (SENT|ACCEPTED|REJECTED|EXPIRED|REVOKED)
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Errores de notificación “gift incoming” (dependencia Notificaciones)
- Invitaciones sin ciclo de vida → corregido: SENT/ACCEPTED/REJECTED/EXPIRED/REVOKED + eventos circle_invite_sent/accepted explícitos.

## Trazabilidad
- Documento origen: `sistema-de-barrio-260207_1012.docx`
