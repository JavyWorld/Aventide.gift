# EVENT_CONTRACTS · integrations

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- dedupe por (provider_event_id + country_code) o dedupe_key,
- Worker de webhook normaliza payload a evento interno y actualiza “observed vs expected” del ledger.
- Webhooks dedupe por provider_event_id o dedupe_key; duplicados responden OK sin efectos.
- 6.2 provider_events (webhooks RAW)
- external_event_id
- unique(provider,country_code,external_event_id)
- event_ref
- (event_ref,attempt desc)
- 6.4 integration_jobs (outbox/queue tracking interno)

## Trazabilidad
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
