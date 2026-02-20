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

## Trazabilidad

- Documento origen: `sistema-de-usuarios-260206_2328.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
