# RUNBOOKS · reputation-seller

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Aumento de cancel_at_fault por país/ciudad (operación rota)
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora

## Incidentes, rollback y backfill
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que calcula y expone la Reputación del Seller (pública) y el Seller Score operativo (interno) usando únicamente “verdad verificada” (órdenes COMPLETED con PIN, outcomes de disputas, cancelaciones con culpa atribuida y señales auditables).
- Objetivos:
- Reducir riesgo/fraude sin matar conversión (evitar hundir o inflar sellers con pocas reviews).
- Ser resistente a abuso: anti-represalias (blind reviews), anti-extorsión y anti-review bombing.
- Ser explicable y operable: historial diario con “drivers” (qué lo sube/baja) y penalizaciones progresivas.


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

## Ownership & Escalation

- **Owner técnico:** `Equipo reputation-seller`
- **Owner negocio/regulatorio:** `Product + Compliance (reputation-seller)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

