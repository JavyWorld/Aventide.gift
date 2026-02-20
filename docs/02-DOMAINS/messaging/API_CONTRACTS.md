# API_CONTRACTS · messaging

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- Send message: idempotencia por client_message_id por conversación (Suposición: el doc no lo nombra, pero evita duplicados en reintentos y es consistente con el resto del proyecto).
- Ticket create: idempotente por (order_id, conversation_id).
- Freeze: idempotente por (conversation_id, status=FROZEN).
- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado
- Fuente de verdad: “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Mensajería es un chat in-app, contextual a una orden, diseñado para que el flujo ideal sea cero conversación (“silencio por defecto”) y el chat se active solo por excepción, funcionando como puente hacia notificaciones externas (push/email) para que ninguna parte quede “a ciegas”. No es chat social.

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
