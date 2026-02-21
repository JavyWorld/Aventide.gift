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

## Ownership & Escalation

- **Owner técnico:** `Equipo payments`
- **Owner negocio/regulatorio:** `Product + Compliance (payments)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

