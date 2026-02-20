# STATE_MACHINE · neighborhoods

## Estados detectados/derivados
- Miembros del círculo (usuarios Aventide) + invitación/aceptación (evento explícito).
- SYSTEM: dispara recordatorios/notificaciones a partir de eventos del círculo, y emite auditoría.
- 4) Flujos end-to-end (happy path + edge cases)
- Sistema emite evento circle_invite_sent.
- Si notificar: se emite evento a Notificaciones: “incoming gift” sin detalles del producto.
- Eventos: circle_invite_sent/accepted (mencionado explícitamente).

## Transiciones y eventos de entrada/salida
- Miembros del círculo (usuarios Aventide) + invitación/aceptación (evento explícito).
- SYSTEM: dispara recordatorios/notificaciones a partir de eventos del círculo, y emite auditoría.
- Sistema emite evento circle_invite_sent.
- Si notificar: se emite evento a Notificaciones: “incoming gift” sin detalles del producto.
- Eventos: circle_invite_sent/accepted (mencionado explícitamente).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos de dominio (mínimos)
- Invitaciones sin ciclo de vida → corregido: SENT/ACCEPTED/REJECTED/EXPIRED/REVOKED + eventos circle_invite_sent/accepted explícitos.

## Trazabilidad
- Documento origen: `sistema-de-barrio-260207_1012.docx`
