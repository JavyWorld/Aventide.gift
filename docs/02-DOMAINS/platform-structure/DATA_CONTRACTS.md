# DATA_CONTRACTS · platform-structure

## Entidades y campos
- /finance (ledger/taxes/proveedor pagos)
- El frontend nunca mueve dinero ni habla directo con Rapyd para mover fondos; Operación definida y validada pasa por backend + ledger/pipeline auditable.
- Response contiene: ui_profile + feature_flags + dictionary + modules + validation_rules + ui_schema_version + signature + ETag.
- Edge cases obligatorios: 304, firma inválida → fallback last-good, fetch fail → fallback, schema no soportado → safe profile.
- Tabla idempotency_keys para endpoints críticos; dedupe de webhooks por provider_event_id + firma + ventana.
- ui_profiles versionadas (config_version), scheduling, rollback, auditoría; entrega por contrato (profile/flags/dictionary/modules/validation_rules/schema_version/signature/ETag).
- idempotency_keys(key, scope, request_hash, status, response_snapshot, expires_at)
- Logs JSON obligatorios con campos estándar (trace_id, request_id, job_id, country/hub/zone, ids dominio, provider_event_id, idempotency_key, status/error/retry/latency).

## Constraints y claves de negocio
- Un core único (misma API/reglas/datos) para web+mobile+paneles.
- Trazabilidad y evidencia (logs anti-PII + auditoría append-only + WORM) como base transversal.
- Client Camaleón: boot config, ETag, firma, fallback, modo degradado.
- Controles transversales: RBAC+scopes, PolicyGuard, idempotencia, anti-PII, break-glass.
- Orquestación exacta “multi-servicio” en un único workspace/deploy (explícitamente no definida).
- Camaleón: GET /api/v1/config/ui con x-country-id (+ hub/zone/role/app_version); ETag + firma + fallback.
- S3 con Object Lock (WORM), inmutabilidad + retención; bóveda de documentos con hash/firma anti-tampering y links temporales.
- POST /api/v1/webhooks/:provider/... verifica firma, persiste payload raw, dedupe, responde 200 rápido, encola job con trace_id/dedupe_key.


## Control operativo verificable

- Owner: `Equipo platform-structure`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PLATFORMSTRU-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/platform-structure/dominio-platform-structure-operacion`
  - `https://jira.aventide.gift/browse/OPS-PLATFORMSTRU-241`

## Trazabilidad
- Documento origen: `estructura-v2-260207_1049.docx`
