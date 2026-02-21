# DATA_CONTRACTS · neighborhoods

## Entidades y campos
- Control total de consentimientos (opt-in por campo/fecha, y por notificación de regalo entrante).
- Anonimato guard: si el buyer está en modo anónimo, se respeta (no revelar identidad).
- Si buyer está en modo anónimo, se respeta (no se revela identidad).
- Círculos siempre privados: no indexables, no descubribles.
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- identidad y membresía son por user_id.
- Usuarios: identidad, control de acceso, invitaciones.
- “Barrio” confundido con “Zone/Barrio geográfico” → corregido: Barrio aquí es capa social (Círculos); lo geográfico es Zone en Cobertura/Gobernanza (otra entidad).

## Constraints y claves de negocio
- Esos temas alimentan recipient_fit para recomendaciones (Genie/Search), sin convertirse en catálogo fijo. (Inferencia: el doc lo afirma conceptualmente).
- invitee_contact (hash/normalizado si es por teléfono/email; si aplica)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (Suposición necesaria)
- Invite: idempotente por (circle_id, invitee_user_id/contact_hash, active_window)
- Accept: idempotente por (invite_id)
- Link recipient: idempotente por unique key en circle_recipients.
- Auditoría append-only de:


## Control operativo verificable

- Owner: `Equipo neighborhoods`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-NEIGHBORHOOD-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/neighborhoods/dominio-neighborhoods-operacion`
  - `https://jira.aventide.gift/browse/OPS-NEIGHBORHOOD-241`

## Trazabilidad
- Documento origen: `sistema-de-barrio-260207_1012.docx`
