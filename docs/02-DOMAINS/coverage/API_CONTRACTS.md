# API_CONTRACTS · coverage

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- Devuelve PASS/FAIL + ETA estimado (3–5 días hábiles) y exige tracking/POD por webhook (sin PIN).
- Snapshot de orden marca coverage_result=OVERRIDDEN con actor/razónSuposición: el documento no define el endpoint exacto del override; se especifica el control mínimo para no romper auditoría.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- addresses/validate: idempotente por (buyer_id, raw_address_hash) si se cachea.
- coverage/check: idempotente por (seller_id, address_id, date_bucket, algo_version) para caching controlado.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
