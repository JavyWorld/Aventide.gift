# DATA_CONTRACTS · genie

## Entidades y campos
- No violar constraints del core: Genie nunca inventa logística; filtra por cobertura y disponibilidad real.
- 4.4 Checkout: identidad pública / anónima (Admirador Secreto)
- “Identidad pública” o “Anónima”.
- 5) Reglas y políticas (hard constraints, modos, límites)
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)
- Campos mínimos:
- Suposición: para latencia, se puede cachear por sesión; el doc define enfoque por etapas pero no tabla de cache.
- Campos:

## Constraints y claves de negocio
- No violar constraints del core: Genie nunca inventa logística; filtra por cobertura y disponibilidad real.
- 5) Reglas y políticas (hard constraints, modos, límites)
- candidates_hash
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- GENIE_RESULTS_GENERATED idempotente por (session_id, answers_hash, policy_version, availability_snapshot_ref) (Suposición: consistente con gates duros y policies).
- Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)


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
