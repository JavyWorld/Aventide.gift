# EVENT_CONTRACTS · coupons

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”
- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- SYSTEM/BOT: valida, calcula descuento, emite eventos, snapshottea la orden.
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos (mínimos)
- Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos → 10.2 Cupones del Seller”
- “Sistema de Pagos — Torre de Precios (orden de cálculo)”

## Trazabilidad
- Documento origen: `sistema-de-cupones-260207_0826.docx`
