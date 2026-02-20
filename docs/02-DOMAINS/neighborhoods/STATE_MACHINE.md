# STATE_MACHINE · neighborhoods

## Estados

- Definir estados explícitos del ciclo de vida para entidades principales del dominio.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Invitaciones sin ciclo de vida → corregido: SENT/ACCEPTED/REJECTED/EXPIRED/REVOKED + eventos circle_invite_sent/accepted explícitos.
- Miembros del círculo (usuarios Aventide) + invitación/aceptación (evento explícito).
- SYSTEM: dispara recordatorios/notificaciones a partir de eventos del círculo, y emite auditoría.
- Sistema emite evento circle_invite_sent.
- Si notificar: se emite evento a Notificaciones: “incoming gift” sin detalles del producto.
- Eventos: circle_invite_sent/accepted (mencionado explícitamente).
- Eventos de dominio (mínimos)

## Trazabilidad

- Documento origen: `sistema-de-barrio-260207_1012.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
