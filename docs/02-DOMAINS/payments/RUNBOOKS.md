# RUNBOOKS · payments

## Operación
- 3 fallos / 10 min → lockout + alerta Ops Lead.
- 9) Observabilidad (logs, métricas, alertas, SLOs) — aplicado a Pagos
- Alertas mínimas
- SLOs
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Fuente de verdad: “Sistema de Pagos — Aventide Gift”.

## Incidentes, rollback y backfill
- Sistema de Pagos v2.0 (Checkout Financial Engine + Escrow + Split + Ledger + Payouts) — corregido y unificado
- Fuente de verdad: “Sistema de Pagos — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema responsable de:
- Cobrar al buyer con métodos locales,
- Retener fondos en escrow,
- Liberar fondos solo con prueba de entrega (Tridente) pero separando validación vs ejecución,
- Ejecutar split automático (Seller / Aventide / Country Ops Lead),


## Control operativo verificable

- Owner: `Equipo payments`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PAYMENTS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/payments/dominio-payments-operacion`
  - `https://jira.aventide.gift/browse/OPS-PAYMENTS-241`

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
