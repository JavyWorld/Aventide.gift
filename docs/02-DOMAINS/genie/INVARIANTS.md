# INVARIANTS · genie

Reglas no negociables del dominio:
- No violar constraints del core: Genie nunca inventa logística; filtra por cobertura y disponibilidad real.
- 3.3 Guards (invariantes de seguridad/consistencia)
- Evitar repetir siempre lo mismo: novelty + diversity_penalty (ver 5.4).
- Checkout siempre presenta opción “pública/anónima”.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- GENIE_RESULTS_GENERATED idempotente por (session_id, answers_hash, policy_version, availability_snapshot_ref) (Suposición: consistente con gates duros y policies).
- 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)
- Decisiones relevantes (policy_context aplicado, modo premium, quality threshold) deben registrarse en audit/telemetría para reproducibilidad de recomendaciones en disputas (“por qué se mostró X”). (Inferencia: consistente con filosofía de auditoría y explicabilidad del doc).


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
