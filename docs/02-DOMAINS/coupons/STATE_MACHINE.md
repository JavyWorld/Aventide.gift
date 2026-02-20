# STATE_MACHINE · coupons

## Estados detectados/derivados
- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”
- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- SYSTEM/BOT: valida, calcula descuento, emite eventos, snapshottea la orden.
- 4) Flujos end-to-end (happy path + edge cases)
- Backend guarda code_hash (no el código plano) y estado ACTIVE.
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.

## Transiciones y eventos de entrada/salida
- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”
- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- SYSTEM/BOT: valida, calcula descuento, emite eventos, snapshottea la orden.
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos (mínimos)
- Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado
- Fuentes de verdad:

## Trazabilidad
- Documento origen: `sistema-de-cupones-260207_0826.docx`
