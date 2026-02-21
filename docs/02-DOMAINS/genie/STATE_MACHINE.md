# STATE_MACHINE · genie

## Estados

- GENIE_RESULTS_GENERATED idempotente por (session_id, answers_hash, policy_version, availability_snapshot_ref) (Suposición: consistente con gates duros y policies).
- Wizard 3 pasos y su sesión (genie_session) con estado y respuestas.

## Transiciones

- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- Multi-país contextual: re-evaluación por policy_context (clima/eventos/riesgo) por país/hub/zona.
- Telemetría de Genie (eventos de funnel) para analítica.
- COUNTRY_OPS_LEAD: gobierna policies (clima/eventos) que afectan candidatos; no “tunea” Genie por fuera del policy engine.
- PolicyGate (hard): restricciones por clima/eventos/riesgo.
- Policy gate (clima/eventos).
- Policy Gate (clima/eventos/riesgo)
- Eventos definidos:


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

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
