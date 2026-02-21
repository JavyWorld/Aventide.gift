# RUNBOOKS · coverage

## Operación
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Scheduler de slots/capacidad (solo dependencia; Coverage decide si llega o no).
- aplica reglas temporales (available_days, cutoff_time, blackout_dates) para entregar a Scheduler (no decide slots; solo habilita/inhabilita).
- 5.2 Regla dura #2: Coverage Guard corre antes de slots/capacidad
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas

## Incidentes, rollback y backfill
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Objetivos:
- Evitar órdenes imposibles: sin cobertura no hay calendario, no hay checkout y no hay pago.
- Multi-modal sin romper modelo: soportar hoy HYPER_LOCAL (radio) y mañana WORLDWIDE_SHIPPING (courier) con reglas separadas.
- Consistencia total con Búsqueda/Catálogo: lo “comprable” debe ser exactamente lo que Coverage Guard aprobaría.


## Control operativo verificable

- Owner: `Equipo coverage`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-COVERAGE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/coverage/dominio-coverage-operacion`
  - `https://jira.aventide.gift/browse/OPS-COVERAGE-241`

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo coverage`
- **Owner negocio/regulatorio:** `Product + Compliance (coverage)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

