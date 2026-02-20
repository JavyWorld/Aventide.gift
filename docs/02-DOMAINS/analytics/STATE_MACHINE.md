# STATE_MACHINE · analytics

## Estados

- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- Eventos críticos server-side (inmutables, append-only).
- Estados finales de órdenes y snapshots financieros (para evitar descuadres ante cambios futuros de fees/reglas).
- SSOT: dashboards no dependen de “clicks sueltos”; derivan de transiciones confirmadas (PAYMENT_SUCCEEDED, ORDER_COMPLETED, PIN_VERIFIED, etc.).

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- SSOT: dashboards no dependen de “clicks sueltos”; derivan de transiciones confirmadas (PAYMENT_SUCCEEDED, ORDER_COMPLETED, PIN_VERIFIED, etc.).
- Flujos end-to-end (happy path + edge cases)
- Ingesta de eventos (server-side primero)
- Ocurre transición confirmada (ej. PAYMENT_SUCCEEDED).
- Reintento de evento: dedupe por event_id (idempotencia).

## Triggers

- Analítica ≠ Observabilidad: analítica = salud negocio/crecimiento/fraude/costos; observabilidad = salud técnica; se correlacionan por trace_id/request_id.
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- Backend emite evento analítico inmutable con event_id y trace_id/request_id.
- Evento llega sin country/hub/zone: rechazado o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).
- Eventos críticos server-side (inmutables, append-only).
- SYSTEM/BOT: inserción de eventos y jobs.
- Ingesta de eventos (server-side primero)
- Reintento de evento: dedupe por event_id (idempotencia).

## Trazabilidad

- Documento origen: `sistema-de-analitica-260206_2336.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
