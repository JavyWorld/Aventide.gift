# DATA_CONTRACTS · reputation-seller

## Entidades y campos
- Corrección clave: reputación no ejecuta pagos; solo emite penalty_event que Policy Engine/Pagos traduce a flags (reserve/hold).
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Score daily snapshot idempotente por (seller_id, date)
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que calcula y expone la Reputación del Seller (pública) y el Seller Score operativo (interno) usando únicamente “verdad verificada” (órdenes COMPLETED con PIN, outcomes de disputas, cancelaciones con culpa atribuida y señales auditables).
- Objetivos:

## Constraints y claves de negocio
- Corrección clave: reputación no ejecuta pagos; solo emite penalty_event que Policy Engine/Pagos traduce a flags (reserve/hold).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Rollup update idempotente por (seller_id, window, event_id)
- Score daily snapshot idempotente por (seller_id, date)
- Badge assignment idempotente por (seller_id, badge_code, window_key)
- Penalty event idempotente por (seller_id, penalty_code, window_key)
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado


## Control operativo verificable

- Owner: `Equipo reputation-seller`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-REPUTATIONSE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reputation-seller/dominio-reputation-seller-operacion`
  - `https://jira.aventide.gift/browse/OPS-REPUTATIONSE-241`

## Trazabilidad
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
