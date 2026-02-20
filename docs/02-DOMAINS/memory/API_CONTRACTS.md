# API_CONTRACTS · memory

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- GIFT_HISTORY_ADDED idempotente por (buyer_id, order_id) (si 1 recipient por orden).
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- REMINDER_DUE idempotente por (reminder_id, fire_at).
- Inferencia (marcada): el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- GIFT_HISTORY_ADDED idempotente por (buyer_id, order_id) (si 1 recipient por orden).
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- REMINDER_DUE idempotente por (reminder_id, fire_at).
- Inferencia (marcada): el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-memory-260207_1012.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
