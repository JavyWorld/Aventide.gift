# STATE_MACHINE · memory

## Estados

- Inferencia (marcada): el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).

## Transiciones

- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- Inferencia (marcada): el documento describe entidades y comportamientos de Memory, pero no fija claves de idempotencia ni tablas exactas; se normalizó el modelo y claves mínimas para soportar reintentos móviles, auditoría y no-duplicación, consistente con el estilo del proyecto (outbox/idempotencia/auditoría/snapshots).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- Integración limpia: Memory no duplica Users; referencia IDs canónicos y emite eventos.
- AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).
- Se escribe evento MEMORY_PROFILE_UPDATED con diff.
- Eventos del dominio Memory
- Auditoría: eventos y lecturas sensibles trazables.

## Trazabilidad

- Documento origen: `sistema-de-memory-260207_1012.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
