# STATE_MACHINE · users

## Estados

- Estados de cuenta + suspensión/restricción + borrado diferenciado.
- Estado PENDING_APPROVAL y revisión por Ops Lead (Kanban).
- RBAC changes, overrides, impersonation, cambios de estado de cuenta y borrado → append-only.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos del dominio Usuarios
- Entrega/Tridente: identidad del evento de entrega ligada a evidencia; confirmación robusta.


## Control operativo verificable

- Owner: `Equipo users`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-USERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/users/dominio-users-operacion`
  - `https://jira.aventide.gift/browse/OPS-USERS-241`

## Trazabilidad

- Documento origen: `sistema-de-usuarios-260206_2328.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
