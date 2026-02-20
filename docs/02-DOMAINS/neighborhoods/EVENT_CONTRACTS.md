# EVENT_CONTRACTS · neighborhoods

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Miembros del círculo (usuarios Aventide) + invitación/aceptación (evento explícito).
- SYSTEM: dispara recordatorios/notificaciones a partir de eventos del círculo, y emite auditoría.
- Sistema emite evento circle_invite_sent.
- Si notificar: se emite evento a Notificaciones: “incoming gift” sin detalles del producto.
- Eventos: circle_invite_sent/accepted (mencionado explícitamente).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos de dominio (mínimos)
- Invitaciones sin ciclo de vida → corregido: SENT/ACCEPTED/REJECTED/EXPIRED/REVOKED + eventos circle_invite_sent/accepted explícitos.
- Inferencia (marcada): la documentación define el concepto y componentes, pero no especifica esquema de tablas, TTLs de invitación, ni campos exactos; se propuso un modelo mínimo compatible con el estilo del proyecto (eventos, privacidad, dependencias, idempotencia) sin inventar funcionalidades públicas no descritas.
- Sistema Barrio v2.0 (Círculos privados) — corregido y unificado

## Trazabilidad
- Documento origen: `sistema-de-barrio-260207_1012.docx`
