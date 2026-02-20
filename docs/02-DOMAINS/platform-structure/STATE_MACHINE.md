# STATE_MACHINE · platform-structure

## Estados detectados/derivados
- /orders (máquina de estados)
- 5) Flujos end-to-end estructurales (plumbing obligatorio)
- Rutas de Studio + flujo draft→preview→publish + time machine + rollback con auditoría completa.
- Core registra intención/estado → workers llaman proveedor → webhooks confirman → handler reconcilia “observed vs expected” → transición de estados (ej. PAID_IN_ESCROW).
- 8) Eventos y triggers (estructura de integración)
- Emisión confiable de eventos por transiciones (Outbox Pattern) para notificaciones/analítica/workers y trazabilidad del “money journey”.

## Transiciones y eventos de entrada/salida
- componentes (API, DB, workers, storage, webhooks, UI Config),
- Backend operable: /api/v1, Postgres+PostGIS, Redis+colas, S3 WORM, gateway de webhooks, workers con DLQ/retries/backoff, observabilidad base.
- Service actors: workers/webhooks corren con service_id para trazabilidad/auditoría.
- Pagos: Rapyd (sessions por country_code, wallets/escrow, payouts + webhooks).
- 5.2 Webhooks inbound → persist RAW → dedupe → enqueue
- POST /api/v1/webhooks/:provider/... verifica firma, persiste payload raw, dedupe, responde 200 rápido, encola job con trace_id/dedupe_key.
- Core registra intención/estado → workers llaman proveedor → webhooks confirman → handler reconcilia “observed vs expected” → transición de estados (ej. PAID_IN_ESCROW).
- Tabla idempotency_keys para endpoints críticos; dedupe de webhooks por provider_event_id + firma + ventana.

## Trazabilidad
- Documento origen: `estructura-v2-260207_1049.docx`
