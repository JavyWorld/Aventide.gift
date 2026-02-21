# EVENT_CONTRACTS · memory

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Integración limpia: Memory no duplica Users; referencia IDs canónicos y emite eventos.
- AuditGuard: cambios y lecturas sensibles generan eventos WORM-style (coherente con Auditoría).
- Se escribe evento MEMORY_PROFILE_UPDATED con diff.
- 6.6 memory_signals (event-sourced ligero)
- source_event_type (VIEW|SAVE|ORDER_COMPLETED|REFUND)
- (source_event_type,created_at desc)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Memory
- MEMORY_SIGNAL_INGESTED idempotente por (source_event_id, entity_type, entity_id) (Suposición: el doc no fija claves; necesario para reintentos).
- memory_signals_ingested_total{source_event}


## Control operativo verificable

- Owner: `Equipo memory`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-MEMORY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/memory/dominio-memory-operacion`
  - `https://jira.aventide.gift/browse/OPS-MEMORY-241`

## Trazabilidad
- Documento origen: `sistema-de-memory-260207_1012.docx`
