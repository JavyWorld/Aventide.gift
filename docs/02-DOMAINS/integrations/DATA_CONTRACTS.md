# DATA_CONTRACTS · integrations

## Entidades y campos
- El Ledger/Audit registra intención y evidencia.
- Antes de llamar al proveedor, registra intención en Ledger/Audit (“observed vs expected”).
- Worker de webhook normaliza payload a evento interno y actualiza “observed vs expected” del ledger.
- Hub & Spoke obligatorio: Core decide, Ledger/Audit registra, Workers ejecutan.
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Campos explícitos
- Suposición: el doc define workers/cola/DLQ pero no fija tabla; se agrega un tracking mínimo consistente.
- Core registra intención en ledger antes de ejecutar con Rapyd.

## Constraints y claves de negocio
- Un pool de Workers asíncronos ejecuta llamadas externas y procesa confirmaciones vía Webhooks.
- Evidencia y reconciliación: webhooks raw almacenados, dedupe, idempotencia y logs por handler.
- Webhook Gateway inbound: verificación firma, persistencia RAW, dedupe, encolado y procesamiento idempotente.
- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- IdempotencyGuard (jobs y webhooks)
- Encola job al payments-worker con idempotency_key.
- Resultado se persiste y se esperan webhooks para confirmación (cuando aplique).
- Doble job: idempotency_key evita doble efecto.


## Control operativo verificable

- Owner: `Equipo integrations`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-INTEGRATIONS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/integrations/dominio-integrations-operacion`
  - `https://jira.aventide.gift/browse/OPS-INTEGRATIONS-241`

## Trazabilidad
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
