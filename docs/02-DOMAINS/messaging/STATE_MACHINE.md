# STATE_MACHINE · messaging

## Estados detectados/derivados
- Definición: Mensajería es un chat in-app, contextual a una orden, diseñado para que el flujo ideal sea cero conversación (“silencio por defecto”) y el chat se active solo por excepción, funcionando como puente hacia notificaciones externas (push/email) para que ninguna parte quede “a ciegas”. No es chat social.
- Ser eficiente: plantillas rápidas por estado y auto-replies por horario.
- Plantillas rápidas por estado + auto-replies + “horario de silencio” (derivado de schedule).
- Bridge a Notification Center: evento canónico NEW_CHAT_MESSAGE.
- SYSTEM: mensajes de sistema, auto-replies, eventos; emite notificaciones.
- 4) Flujos end-to-end (happy path + edge cases)

## Transiciones y eventos de entrada/salida
- Bridge a Notification Center: evento canónico NEW_CHAT_MESSAGE.
- SYSTEM: mensajes de sistema, auto-replies, eventos; emite notificaciones.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos auditables mínimos (obligatorios)
- 7.2 Evento canónico de notificaciones
- Auditoría: eventos mínimos auditables.
- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado
- Fuente de verdad: “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
