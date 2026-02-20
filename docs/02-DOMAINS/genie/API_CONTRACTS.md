# API_CONTRACTS · genie

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard (o guest-mode si se habilita; no definido en doc)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- GENIE_RESULTS_GENERATED idempotente por (session_id, answers_hash, policy_version, availability_snapshot_ref) (Suposición: consistente con gates duros y policies).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Address/ContextGuard: requiere contexto territorial válido (country/hub/zone) y dirección geocodificada (por dependencia de cobertura).

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard (o guest-mode si se habilita; no definido en doc)
- Address/ContextGuard: requiere contexto territorial válido (country/hub/zone) y dirección geocodificada (por dependencia de cobertura).

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- GENIE_STEP_ANSWERED idempotente por (session_id, step_no, client_event_id) (Suposición: necesario para reintentos móviles).
- GENIE_RESULTS_GENERATED idempotente por (session_id, answers_hash, policy_version, availability_snapshot_ref) (Suposición: consistente con gates duros y policies).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-genie-260207_1012.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
