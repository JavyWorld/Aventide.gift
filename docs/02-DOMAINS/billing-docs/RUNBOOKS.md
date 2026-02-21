# RUNBOOKS · billing-docs

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs) — aplicado a Facturación
- Alertas mínimas
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.

## Incidentes, rollback y backfill
- IdempotencyGuard (no duplicar emisión por reintentos)
- Reintentos devuelven el doc existente; no se crea uno nuevo.
- Duplicación de facturas por reintentos → eliminado: document_key idempotente + series con locking.
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Objetivos:


## Control operativo verificable

- Owner: `Equipo billing-docs`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-BILLINGDOCS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/billing-docs/dominio-billing-docs-operacion`
  - `https://jira.aventide.gift/browse/OPS-BILLINGDOCS-241`

## Trazabilidad
- Documento origen: `facturacion--documentos-260207_0805.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo billing-docs`
- **Owner negocio/regulatorio:** `Product + Compliance (billing-docs)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

