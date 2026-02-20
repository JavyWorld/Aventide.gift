# INVARIANTS · integrations

Reglas no negociables del dominio:
- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).
- El Ledger/Audit registra intención y evidencia.
- No bloquear UX: llamadas externas críticas nunca se ejecutan en request síncrono (salvo validate liviano).
- Evidencia y reconciliación: webhooks raw almacenados, dedupe, idempotencia y logs por handler.
- Seguridad: secrets en KMS/Secret Manager; frontend nunca habla directo con proveedores para acciones críticas.
- Webhook Gateway inbound: verificación firma, persistencia RAW, dedupe, encolado y procesamiento idempotente.
- Outbound webhooks a partners (si aplica): HMAC, retries, DLQ, payload con event_id/idempotency.
- FINANCE/AUDIT: lectura de reconciliación y evidencia (pagos).
- integrations.secrets.rotate (admin; auditado)
- integrations.webhooks.raw.read (support/finance; auditado)

## Trazabilidad
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
