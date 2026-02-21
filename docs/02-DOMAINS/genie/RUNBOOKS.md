# RUNBOOKS · genie

## Operación
- AvailabilityGate (hard): lead time + slots/cutoffs reales.
- Usuario elige “Fecha exacta”: Genie solo devuelve items con slots disponibles en scheduler.
- Scheduler/availability gate (slots/cutoff/lead time),
- Si “fecha exacta”: debe existir slot real y pasar cutoff/pausas.
- Input: target_date/intent, lead_time, slots/cutoffs/pausas.
- Output: elegibilidad/slots (hard gate).

## Incidentes, rollback y backfill
- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Genie/Wizard y sus reglas.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Genie es el sistema que transforma “no sé qué regalar” en una selección comprable en 30–60 segundos, mediante un Wizard de 3 preguntas (Quién / Cuándo / Vibe) que orquesta sistemas existentes (Cobertura, Capacidad/Disponibilidad, Policies por país, calidad/moderación) y devuelve resultados realizables (cero humo logístico).
- Objetivos (duros):
- Conversión rápida: entregar lista rankeada lista-para-checkout con explicabilidad (“por qué te lo recomiendo”).
- No violar constraints del core: Genie nunca inventa logística; filtra por cobertura y disponibilidad real.


## Control operativo verificable

- Owner: `Equipo genie`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GENIE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/genie/dominio-genie-operacion`
  - `https://jira.aventide.gift/browse/OPS-GENIE-241`

## Trazabilidad
- Documento origen: `sistema-de-genie-260207_1012.docx`

## Ownership & Escalation

- **Owner técnico:** `Equipo genie`
- **Owner negocio/regulatorio:** `Product + Compliance (genie)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

