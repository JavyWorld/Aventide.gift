# DATA_CONTRACTS · messaging

## Entidades y campos
- UI muestra identidad marketplace-safe (nombre de tienda / alias).
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Campos explícitos:
- Estados de entrega (tabla separada):message_delivery_status(message_id, recipient_id, status, updated_at) con SENT/DELIVERED/READ/FAILED.
- Auditoría obligatoria de acciones clave y accesos.
- Sistema de Mensajería v2.0 (Chat in-app) — corregido y unificado
- Fuente de verdad: “Sistema de Mensajería (Chat in-app) — Silencio por defecto, señal bajo demanda”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora

## Constraints y claves de negocio
- AttachmentGuard (mime/size) + StorageGuard (URLs firmadas).
- URLs firmadas TTL corto
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.3 Idempotencia
- Send message: idempotencia por client_message_id por conversación (Suposición: el doc no lo nombra, pero evita duplicados en reintentos y es consistente con el resto del proyecto).
- Ticket create: idempotente por (order_id, conversation_id).
- Freeze: idempotente por (conversation_id, status=FROZEN).
- Adjuntos van a storage seguro con URLs firmadas TTL corto y ACL por conversación/orden.


## Control operativo verificable

- Owner: `Equipo messaging`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MESSAGING-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/messaging/dominio-messaging-operacion`
  - `https://jira.aventide.gift/browse/OPS-MESSAGING-241`

## Trazabilidad
- Documento origen: `sistema-de-mensajeria-260207_0925.docx`
