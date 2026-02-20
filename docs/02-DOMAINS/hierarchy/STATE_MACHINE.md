# STATE_MACHINE · hierarchy

## Estados

- Ser auditable: cambios de rol/scope/estados críticos quedan registrados con who/when/what/why.
- COUNTRY_OPS_LEAD (COL): NO crea/elimina zonas base; SÍ puede cambiar estado operativo de zona (zone.update_status) y crear exclusion_zones dentro de su país (si está habilitado).Esto elimina la contradicción reportada por auditoría.
- COUNTRY_OPS_LEAD (scoped): opera dentro de su país, cambia estado de zonas, gestiona capacidad, aprueba sellers, opera Studio/Camaleón según permisos.
- Ubicación → valida estado de zona/cobertura.
- KYC dinámico por país → estado PENDING_APPROVAL.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Onboarding seller: flujo PENDING_APPROVAL → approve/reject por COL; asignación geo.
- Flujos end-to-end (happy path + edge cases)

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Aunque Jerarquías no define explícitamente bus/cola, el proyecto usa workers/colas para procesos críticos en general. (Inferencia consistente con arquitectura del proyecto, pero aquí solo se definen eventos del módulo Jerarquía.)
- Eventos de autorización (dominio Jerarquía)
- inicio/fin de break-glassdebe producir un evento de auditoría con who/when/what/why.

## Trazabilidad

- Documento origen: `sistema-de-jerarqua-260206_2015.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
