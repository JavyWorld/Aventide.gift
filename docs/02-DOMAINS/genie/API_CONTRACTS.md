# API_CONTRACTS · genie

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- AuthGuard (o guest-mode si se habilita; no definido en doc)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- GENIE_RESULTS_GENERATED idempotente por (session_id, answers_hash, policy_version, availability_snapshot_ref) (Suposición: consistente con gates duros y policies).
- Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Genie/Wizard y sus reglas.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Resultados vacíos por restricciones: aplicar fallback controlado:
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Genie/Wizard y sus reglas.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-de-genie-260207_1012.docx`
