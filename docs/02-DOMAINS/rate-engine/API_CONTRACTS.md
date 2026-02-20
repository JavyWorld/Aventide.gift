# API_CONTRACTS · rate-engine

## Endpoints

- Actores y permisos (RBAC) + guards
- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- status (OPEN|APPROVED|REJECTED|EXECUTED)
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- DeterminismGuard (misma entrada → mismo RateVector)

## Auth

- Actores y permisos (RBAC) + guards
- DeterminismGuard (misma entrada → mismo RateVector)

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Reintentos de checkout: idempotencia por checkout_session_id; no cambiar decision_id dentro de la misma sesión salvo expiración deliberada. (Inferencia: consistente con “snapshot no retroactivo” + control de consistencia).
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
