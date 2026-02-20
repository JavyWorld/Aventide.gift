# API_CONTRACTS · governance-cameleon

## Endpoints y auth
- APIs mínimas: resolve context, fetch config UI, evaluate policies, simulate checkout.
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Publish ruleset: idempotente por (ruleset_id, version)
- Publish ui_profile: idempotente por (profile_id, config_version)
- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Si firma inválida o schema incompatible: fallback local (modo degradado) con mínima funcionalidad y aviso.
- fallback local
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Firma de UI config obligatoria; app rechaza configs no firmadas o schema incompatible y entra en fallback.
- UI config vulnerable a tampering → corregido: firma + schema version + fallback + ETag cache.

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
