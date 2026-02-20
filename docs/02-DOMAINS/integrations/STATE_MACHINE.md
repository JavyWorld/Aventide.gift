# STATE_MACHINE · integrations

## Estados detectados/derivados
- El Core decide (lógica, estados, políticas).
- 4) Flujos end-to-end (happy path + edge cases)
- Worker de webhook normaliza payload a evento interno y actualiza “observed vs expected” del ledger.
- Guarda provider_message_id, estado y errores.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos

## Transiciones y eventos de entrada/salida
- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).
- Un pool de Workers asíncronos ejecuta llamadas externas y procesa confirmaciones vía Webhooks.
- Evidencia y reconciliación: webhooks raw almacenados, dedupe, idempotencia y logs por handler.
- Adapters por proveedor: PaymentsProvider, MessagingProvider, MapsProvider, StorageProvider + WebhookVerifier.
- Webhook Gateway inbound: verificación firma, persistencia RAW, dedupe, encolado y procesamiento idempotente.
- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- SYSTEM/WORKERS: ejecutan jobs y procesan webhooks.
- integrations.webhooks.raw.read (support/finance; auditado)

## Trazabilidad
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
