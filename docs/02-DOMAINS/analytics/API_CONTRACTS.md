# API_CONTRACTS · analytics

## Endpoints

- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- RBAC + scoping al nivel de consulta: Seller solo lo suyo; Ops Lead su país/hubs; Admin global. No solo UI.
- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403. (aplicado a Analítica)
- Operación definida y validada endpoint/query analítico exige scope_context (country/hub/zone/seller_id) resuelto por claims.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Evento llega sin country/hub/zone: rechazado o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).
- fact_payments: intentos, success rate, error_codes, proveedor.
- fact_payments (intentos, éxito, error codes)
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Reintento de evento: dedupe por event_id (idempotencia).

## Auth

- Fuente de verdad: Documento “Sistema de Analítica (BI + Product Analytics + Ops Intelligence) — El HUB central”.Objetivo del rewrite: convertir la analítica en un sistema audit-able, multi-país, RBAC+scoping estricto, SSOT, con separación clara entre Analítica vs Observabilidad, y sin conflictos con el motor financiero/ledger, Jerarquía, Usuarios, App Camaleón/Policy Engine.
- RBAC + scoping al nivel de consulta: Seller solo lo suyo; Ops Lead su país/hubs; Admin global. No solo UI.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403. (aplicado a Analítica)
- Operación definida y validada endpoint/query analítico exige scope_context (country/hub/zone/seller_id) resuelto por claims.

## Códigos de error

- Evento llega sin country/hub/zone: rechazado o enviado a DLQ/tabla de errores para reparación (regla multi-país “no negociable”).
- fact_payments: intentos, success rate, error_codes, proveedor.
- fact_payments (intentos, éxito, error codes)

## Idempotency

- Backbone de eventos analíticos analytics_events_raw (append-only) con idempotencia.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Reintento de evento: dedupe por event_id (idempotencia).


## Control operativo verificable

- Owner: `Equipo analytics`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ANALYTICS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/analytics/dominio-analytics-operacion`
  - `https://jira.aventide.gift/browse/OPS-ANALYTICS-241`

## Trazabilidad

- Documento origen: `sistema-de-analitica-260206_2336.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
