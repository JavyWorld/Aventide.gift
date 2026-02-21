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

## Ownership & Escalation

- **Owner técnico:** `Equipo coupons`
- **Owner negocio/regulatorio:** `Product + Compliance (coupons)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

