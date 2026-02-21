# RUNBOOKS · internal-credit

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas mínimas
- Spike en wallet_mint_total{source_type=SUPPORT_OUTCOME} (posible problema de calidad/operación)
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora

## Incidentes, rollback y backfill
- Reintentos/redoble click: no duplica spend (idempotencia por checkout_id).
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Objetivos:
- Eliminar incoherencia “crédito genérico”: wallets separadas por tipo con reglas duras.
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.


## Control operativo verificable

- Owner: `Equipo internal-credit`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-INTERNALCRED-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/internal-credit/dominio-internal-credit-operacion`
  - `https://jira.aventide.gift/browse/OPS-INTERNALCRED-241`

## Trazabilidad
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo internal-credit`
- **Owner negocio/regulatorio:** `Product + Compliance (internal-credit)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

