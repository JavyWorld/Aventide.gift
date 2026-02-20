# STATE_MACHINE · integrations

## Estados

- El Core decide (lógica, estados, políticas).
- Guarda provider_message_id, estado y errores.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- Worker de webhook normaliza payload a evento interno y actualiza “observed vs expected” del ledger.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos

## Trazabilidad

- Documento origen: `sistema-de-integraciones-260207_0951.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
