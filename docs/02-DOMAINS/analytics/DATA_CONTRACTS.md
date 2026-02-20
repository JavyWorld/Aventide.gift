# DATA_CONTRACTS · analytics

## Entidades y campos
- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- Estados finales de órdenes y snapshots financieros (para evitar descuadres ante cambios futuros de fees/reglas).
- Gobernanza métrica: definiciones “de hierro”, versionadas, conciliables con ledger/snapshots.
- Evento llega sin country/hub/zone: rechazado o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).
- fact_orders: 1 fila por orden, con timestamps clave y snapshot financiero “locked”.
- Cambios futuros de fee rules: no cambian el pasado; se usa snapshot en la orden (evita descuadres).
- Revenue/GMV/ventas se calculan desde fact_orders + snapshots financieros y eventos server-side críticos.
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

## Constraints y claves de negocio
- Eventos críticos server-side (inmutables, append-only).
- SSOT: dashboards no dependen de “clicks sueltos”; derivan de transiciones confirmadas (PAYMENT_SUCCEEDED, ORDER_COMPLETED, PIN_VERIFIED, etc.).
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- Ocurre transición confirmada (ej. PAYMENT_SUCCEEDED).
- Se guarda en analytics_events_raw (append-only).
- Reintento de evento: dedupe por event_id (idempotencia).
- fact_orders: 1 fila por orden, con timestamps clave y snapshot financiero “locked”.
- event_id (UUID, unique) — idempotencia

## Trazabilidad
- Documento origen: `sistema-de-analitica-260206_2336.docx`
