# RUNBOOKS · coupons

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos → 10.2 Cupones del Seller”
- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”

## Incidentes, rollback y backfill
- Reintento/redoble click → no “consume” dos veces: idempotencia por checkout_id.
- Aplicación duplicada por reintentos → idempotencia por checkout_id + consumo por order_id.
- Sistema de Cupones v2.0 (Seller-funded Coupons) — corregido y unificado
- Fuentes de verdad:
- “Aventide Version 1.1 — Sistema #10 Lealtad y Promos → 10.2 Cupones del Seller”
- “Fases de Desarrollo v1.1 — Cupones: reglas + torre de precios + modelo de datos + eventos”
- “Sistema de Pagos — Torre de Precios (orden de cálculo)”
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora


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
