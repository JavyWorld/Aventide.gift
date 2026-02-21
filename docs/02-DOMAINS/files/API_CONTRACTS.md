# API_CONTRACTS · files

## Endpoints

- control estricto RBAC+ABAC (“need-to-know”),
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- Sistema valida RBAC+ABAC + data_class.
- si hay error: no se edita; se emite Nota de Crédito + nueva factura.
- Eventos y triggers + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.

## Auth

- control estricto RBAC+ABAC (“need-to-know”),
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- AuthGuard
- Sistema valida RBAC+ABAC + data_class.

## Códigos de error

- si hay error: no se edita; se emite Nota de Crédito + nueva factura.
- checksum mismatch: rechaza y mantiene estado PENDING_UPLOAD con TTL de limpieza.

## Idempotency

- Eventos y triggers + idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo files`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-FILES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/files/dominio-files-operacion`
  - `https://jira.aventide.gift/browse/OPS-FILES-241`

## Trazabilidad

- Documento origen: `sistema-de-archivos-260207_0840.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
