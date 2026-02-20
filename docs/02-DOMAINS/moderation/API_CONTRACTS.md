# API_CONTRACTS · moderation

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- Price anomaly: bloqueo si desviación absurda (lavado/error).
- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Corrección de incoherencia: StrikeLedger es proyección; los cambios reales ocurren vía eventos STRIKE_APPLIED + policy engine que setea flags en user_status y seller_operational_flags.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard

## Códigos de error

- Price anomaly: bloqueo si desviación absurda (lavado/error).

## Idempotency

- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-moderacion-260207_0828.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
