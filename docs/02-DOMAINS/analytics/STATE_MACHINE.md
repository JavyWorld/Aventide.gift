# STATE_MACHINE · analytics

## Estados detectados/derivados
- Eventos críticos server-side (inmutables, append-only).
- Estados finales de órdenes y snapshots financieros (para evitar descuadres ante cambios futuros de fees/reglas).
- SSOT: dashboards no dependen de “clicks sueltos”; derivan de transiciones confirmadas (PAYMENT_SUCCEEDED, ORDER_COMPLETED, PIN_VERIFIED, etc.).
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- SYSTEM/BOT: inserción de eventos y jobs.
- 4) Flujos end-to-end (happy path + edge cases)

## Transiciones y eventos de entrada/salida
- Eventos críticos server-side (inmutables, append-only).
- SSOT: dashboards no dependen de “clicks sueltos”; derivan de transiciones confirmadas (PAYMENT_SUCCEEDED, ORDER_COMPLETED, PIN_VERIFIED, etc.).
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- SYSTEM/BOT: inserción de eventos y jobs.
- 4.1 Ingesta de eventos (server-side primero)
- Ocurre transición confirmada (ej. PAYMENT_SUCCEEDED).
- Backend emite evento analítico inmutable con event_id y trace_id/request_id.
- Reintento de evento: dedupe por event_id (idempotencia).

## Trazabilidad
- Documento origen: `sistema-de-analitica-260206_2336.docx`
