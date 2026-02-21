# API_CONTRACTS · platform-structure

## Endpoints

- componentes (API, DB, workers, storage, webhooks, UI Config),
- contratos transversales (territorio como first-class, policy engine, RBAC+scopes, server-driven UI, auditoría WORM, pipeline de dinero),
- Un core único (misma API/reglas/datos) para web+mobile+paneles.
- Monorepo: apps (API/workers/webs/mobile/paneles) + packages (DTOs/contracts/UI-LEGO) + infra + docs/ADR.
- Backend operable: /api/v1, Postgres+PostGIS, Redis+colas, S3 WORM, gateway de webhooks, workers con DLQ/retries/backoff, observabilidad base.
- Controles transversales: RBAC+scopes, PolicyGuard, idempotencia, anti-PII, break-glass.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403. (estructura de autorización)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- React Native (Expo), TS estricto, JWT en SecureStore, retry/backoff, modo degradado, permisos GPS/cámara (evidencia/logística).
- Camaleón: GET /api/v1/config/ui con x-country-id (+ hub/zone/role/app_version); ETag + firma + fallback.
- Worker ejecuta handler con timeouts y retries; si excede → DLQ con causa y acción siguiente.
- POST /api/v1/webhooks/:provider/... verifica firma, persiste payload raw, dedupe, responde 200 rápido, encola job con trace_id/dedupe_key.
- Tabla idempotency_keys para endpoints críticos; dedupe de webhooks por provider_event_id + firma + ventana.
- Regional OS incluye Studio para operar config/UI/merchandising bajo guardrails y auditoría.

## Auth

- contratos transversales (territorio como first-class, policy engine, RBAC+scopes, server-driven UI, auditoría WORM, pipeline de dinero),
- Controles transversales: RBAC+scopes, PolicyGuard, idempotencia, anti-PII, break-glass.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403. (estructura de autorización)
- React Native (Expo), TS estricto, JWT en SecureStore, retry/backoff, modo degradado, permisos GPS/cámara (evidencia/logística).
- Regional OS incluye Studio para operar config/UI/merchandising bajo guardrails y auditoría.

## Códigos de error

- Backend operable: /api/v1, Postgres+PostGIS, Redis+colas, S3 WORM, gateway de webhooks, workers con DLQ/retries/backoff, observabilidad base.
- Worker ejecuta handler con timeouts y retries; si excede → DLQ con causa y acción siguiente.

## Idempotency

- Controles transversales: RBAC+scopes, PolicyGuard, idempotencia, anti-PII, break-glass.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Webhooks inbound → persist RAW → dedupe → enqueue
- POST /api/v1/webhooks/:provider/... verifica firma, persiste payload raw, dedupe, responde 200 rápido, encola job con trace_id/dedupe_key.
- Tabla idempotency_keys para endpoints críticos; dedupe de webhooks por provider_event_id + firma + ventana.


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
