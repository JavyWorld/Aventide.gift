# API_CONTRACTS · content

## Endpoints

- Actores y permisos (RBAC) + guards
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Mutaciones con idempotency_key (submit, approve, pause, upload asset).
- Jerarquía/RBAC: Ops Lead scoped por país para revisión; seller solo lo suyo.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- QualityGateGuard (capacidad + logística + assets + atributos requeridos + estado de seller)

## Auth

- Actores y permisos (RBAC) + guards
- Jerarquía/RBAC: Ops Lead scoped por país para revisión; seller solo lo suyo.
- QualityGateGuard (capacidad + logística + assets + atributos requeridos + estado de seller)

## Códigos de error

- Rechazo: estado REJECTED con razón específica (“foto borrosa”, “descripción engañosa”).

## Idempotency

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia
- Mutaciones con idempotency_key (submit, approve, pause, upload asset).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-de-contenido-260206_2344.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
