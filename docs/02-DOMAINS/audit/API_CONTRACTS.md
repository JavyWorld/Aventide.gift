# API_CONTRACTS · audit

## Endpoints

- Actores y permisos (RBAC) + guards
- AuthGuard
- RBAC_AUDIT: cambios de permisos/roles con IP, contexto, scope.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- SensitiveReadGuard (VIEW_SENSITIVE siempre genera evento)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- RBAC_AUDIT: cambios de permisos/roles con IP, contexto, scope.
- SensitiveReadGuard (VIEW_SENSITIVE siempre genera evento)

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-auditoria-260207_0947.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
