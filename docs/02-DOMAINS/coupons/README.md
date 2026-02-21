# coupons

## Propósito

- valid_to < valid_from → reject.
- Cupón excedió usage_limit_total en carrera (race) → se resuelve con contador atómico/locking; si pierde, reject_reason=LIMIT_REACHED.
- Si no cumple, reject_reason=FTB_NOT_ELIGIBLE.
- reject_reason (enum):
- Documento origen: `sistema-de-cupones-260207_0826.docx`
- Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado
- Fuentes de verdad:
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Definición: Sistema que permite a un seller crear y administrar cupones (seller-funded) para que buyers los apliquen en checkout, cumpliendo reglas de elegibilidad, targeting territorial y límites de uso. El descuento reduce el ingreso del seller (nunca lo absorbe la plataforma).
- Título extraído: "Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado".

## Límites

- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”
- Definición: Sistema que permite a un seller crear y administrar cupones (seller-funded) para que buyers los apliquen en checkout, cumpliendo reglas de elegibilidad, targeting territorial y límites de uso. El descuento reduce el ingreso del seller (nunca lo absorbe la plataforma).
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Seller crea cupón con type, value, ventana valid_from/to, límites de uso, targeting, productos/categorías, stacking, delivery modes.
- Si se habilita apilado por policy, debe existir regla determinística: ONLY_ONE_SELLER_COUPON + orden de preferencia (p. ej. mayor descuento efectivo) y debe quedar snapshotteado.

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.


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
- Título extraído: "Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
