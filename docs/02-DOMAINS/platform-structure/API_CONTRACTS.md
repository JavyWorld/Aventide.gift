# API_CONTRACTS · platform-structure

## Endpoints y auth
- componentes (API, DB, workers, storage, webhooks, UI Config),
- contratos transversales (territorio como first-class, policy engine, RBAC+scopes, server-driven UI, auditoría WORM, pipeline de dinero),
- Un core único (misma API/reglas/datos) para web+mobile+paneles.
- Multi-país/territorio como “primera clase” en requests, UI, reglas, búsqueda, pagos, auditoría y analítica.
- Monorepo: apps (API/workers/webs/mobile/paneles) + packages (DTOs/contracts/UI-LEGO) + infra + docs/ADR.
- Backend operable: /api/v1, Postgres+PostGIS, Redis+colas, S3 WORM, gateway de webhooks, workers con DLQ/retries/backoff, observabilidad base.
- Controles transversales: RBAC+scopes, PolicyGuard, idempotencia, anti-PII, break-glass.
- 3) Actores y permisos (RBAC) + guards (estructura de autorización)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Client Camaleón: boot config, ETag, firma, fallback, modo degradado.
- React Native (Expo), TS estricto, JWT en SecureStore, retry/backoff, modo degradado, permisos GPS/cámara (evidencia/logística).
- Camaleón: GET /api/v1/config/ui con x-country-id (+ hub/zone/role/app_version); ETag + firma + fallback.
- Worker ejecuta handler con timeouts y retries; si excede → DLQ con causa y acción siguiente.
- 5.4 Camaleón (Server-driven UI) boot + caching + fallback + hot reload

## Trazabilidad
- Documento origen: `estructura-v2-260207_1049.docx`
