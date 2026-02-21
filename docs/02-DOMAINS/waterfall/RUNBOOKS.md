# RUNBOOKS · waterfall

## Operación
- Orden fijo de cobertura (no alterable por operación manual):Country Reserve -> COL Liability -> Global Reserve -> Recovery obligatorio al COL
- penalidad regulatoria atribuible a operación país (si aplica en política)
- Protege operación:
- Alertas:
- alertas y comité automático
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️

## Incidentes, rollback y backfill
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️
- Waterfall Engine v1.0
- Objetivo: cubrir pérdidas de forma determinística, proteger caja global y forzar recuperación automática al nivel correcto de responsabilidad (COL).
- 1) Principios no negociables
- Orden fijo de cobertura (no alterable por operación manual):Country Reserve -> COL Liability -> Global Reserve -> Recovery obligatorio al COL
- Toda pérdida tiene expediente único (loss_case_id) con trazabilidad completa de:
- origen
- monto


## Control operativo verificable

- Owner: `Equipo waterfall`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-WATERFALL-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/waterfall/dominio-waterfall-operacion`
  - `https://jira.aventide.gift/browse/OPS-WATERFALL-241`

## Trazabilidad
- Documento origen: `waterfall-engine-v10-260207_0941.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo waterfall`
- **Owner negocio/regulatorio:** `Product + Compliance (waterfall)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

