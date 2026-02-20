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
- 1) Definición y objetivos del sistema/módulo
- Definición: Genie es el sistema que transforma “no sé qué regalar” en una selección comprable en 30–60 segundos, mediante un Wizard de 3 preguntas (Quién / Cuándo / Vibe) que orquesta sistemas existentes (Cobertura, Capacidad/Disponibilidad, Policies por país, calidad/moderación) y devuelve resultados realizables (cero humo logístico).
- Objetivos (duros):
- Conversión rápida: entregar lista rankeada lista-para-checkout con explicabilidad (“por qué te lo recomiendo”).
- No violar constraints del core: Genie nunca inventa logística; filtra por cobertura y disponibilidad real.

## Trazabilidad
- Documento origen: `sistema-de-genie-260207_1012.docx`
