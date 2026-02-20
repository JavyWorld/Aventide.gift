# API_CONTRACTS · analytics

## Endpoints y auth
- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- RBAC + scoping al nivel de consulta: Seller solo lo suyo; Ops Lead su país/hubs; Admin global. No solo UI.
- Analítica ≠ Observabilidad: analítica = salud negocio/crecimiento/fraude/costos; observabilidad = salud técnica; se correlacionan por trace_id/request_id.
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- 3) Actores y permisos (RBAC) + guards (aplicado a Analítica)
- Todo endpoint/query analítico exige scope_context (country/hub/zone/seller_id) resuelto por claims.
- Auth
- Backend emite evento analítico inmutable con event_id y trace_id/request_id.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Evento llega sin country/hub/zone: rechazado o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).
- fact_payments: intentos, success rate, error_codes, proveedor.
- fact_payments (intentos, éxito, error codes)
- Cupones seller-driven:SELLER_COUPON_CREATED/UPDATED/EXPIRED, SELLER_COUPON_APPLIED/REJECTED, SELLER_COUPON_COST_BOOKED
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Trazabilidad
- Documento origen: `sistema-de-analitica-260206_2336.docx`
