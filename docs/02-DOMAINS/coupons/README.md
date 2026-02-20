# coupons

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- Definición: Sistema que permite a un seller crear y administrar cupones (seller-funded) para que buyers los apliquen en checkout, cumpliendo reglas de elegibilidad, targeting territorial y límites de uso. El descuento reduce el ingreso del seller (nunca lo absorbe la plataforma).
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- Seller crea cupón con type, value, ventana valid_from/to, límites de uso, targeting, productos/categorías, stacking, delivery modes.

## Dependencias
- Stacking policy (por defecto NO apilable).
- stacking_policy (default NO apilable)
- Default: NO apilable.
- Si se habilita apilado por policy, debe existir regla determinística: ONLY_ONE_SELLER_COUPON + orden de preferencia (p. ej. mayor descuento efectivo) y debe quedar snapshotteado.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Trazabilidad
- Documento origen: `sistema-de-cupones-260207_0826.docx`
- Título extraído: "Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado".
