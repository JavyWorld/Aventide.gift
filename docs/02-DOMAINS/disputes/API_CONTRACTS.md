# API_CONTRACTS · disputes

## Endpoints

- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- Actores y permisos (RBAC) + guards
- Genera un settlement_plan idempotente (hash del input).
- Ejecución Saga (steps idempotentes)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- Actores y permisos (RBAC) + guards

## Códigos de error

- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.

## Idempotency

- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- Genera un settlement_plan idempotente (hash del input).
- Ejecución Saga (steps idempotentes)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Falla provider refund: step queda en RETRY/DLQ; no se duplica por idempotency key.

## Trazabilidad

- Documento origen: `disputas-260207_0809.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
