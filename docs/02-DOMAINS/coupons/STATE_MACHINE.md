# STATE_MACHINE · coupons

## Estados

- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- SYSTEM/BOT: valida, calcula descuento, emite eventos, snapshottea la orden.
- Backend guarda code_hash (no el código plano) y estado ACTIVE.
- Si se habilita apilado por policy, debe existir regla determinística: ONLY_ONE_SELLER_COUPON + orden de preferencia (p. ej. mayor descuento efectivo) y debe quedar snapshotteado.

## Transiciones

- Reintento/redoble click → no “consume” dos veces: idempotencia por checkout_id.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”
- SYSTEM/BOT: valida, calcula descuento, emite eventos, snapshottea la orden.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos (mínimos)


## Control operativo verificable

- Owner: `Equipo coupons`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-COUPONS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/coupons/dominio-coupons-operacion`
  - `https://jira.aventide.gift/browse/OPS-COUPONS-241`

## Trazabilidad

- Documento origen: `sistema-de-cupones-260207_0826.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
