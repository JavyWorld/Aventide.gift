# STATE_MACHINE · messaging

## Estados

- Ser eficiente: plantillas rápidas por estado y auto-replies por horario.
- Plantillas rápidas por estado + auto-replies + “horario de silencio” (derivado de schedule).
- Plantillas dependen del estado de orden (IN_TRANSIT, DELIVERED, etc.).

## Transiciones

- Send message: idempotencia por client_message_id por conversación (Suposición: el doc no lo nombra, pero evita duplicados en reintentos y es consistente con el resto del proyecto).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Definición: Mensajería es un chat in-app, contextual a una orden, diseñado para que el flujo ideal sea cero conversación (“silencio por defecto”) y el chat se active solo por excepción, funcionando como puente hacia notificaciones externas (push/email) para que ninguna parte quede “a ciegas”. No es chat social.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Bridge a Notification Center: evento canónico NEW_CHAT_MESSAGE.
- SYSTEM: mensajes de sistema, auto-replies, eventos; emite notificaciones.
- Eventos auditables mínimos (obligatorios)
- Evento canónico de notificaciones
- Auditoría: eventos mínimos auditables.

## Trazabilidad

- Documento origen: `sistema-de-mensajeria-260207_0925.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
