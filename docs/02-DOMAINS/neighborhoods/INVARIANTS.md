# INVARIANTS · neighborhoods

Reglas no negociables del dominio:
- SYSTEM: dispara recordatorios/notificaciones a partir de eventos del círculo, y emite auditoría.
- Círculos siempre privados: no indexables, no descubribles.
- anonimato se respeta siempre.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (Suposición necesaria)
- Invite: idempotente por (circle_id, invitee_user_id/contact_hash, active_window)
- Accept: idempotente por (invite_id)
- Link recipient: idempotente por unique key en circle_recipients.
- 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)
- Auditoría append-only de:

## Trazabilidad
- Documento origen: `sistema-de-barrio-260207_1012.docx`
