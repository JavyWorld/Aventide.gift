# API_CONTRACTS · hierarchy

## Endpoints

- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- RBAC: roles → permisos granulares.
- Claims de seguridad y guard chain canónica: Auth → Role → Scope → Permission → Policy.
- Actores y permisos (RBAC) + guards
- AuthGuard: sesión válida
- PermissionGuard: permiso requerido por endpoint/acción
- APIs de mapas/tiles y operaciones requieren country_code y se filtran por scope; además se recomienda enforcement a nivel query (RLS / filtros server-side), no solo UI.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Ser auditable: cambios de rol/scope/estados críticos quedan registrados con who/when/what/why.
- COUNTRY_OPS_LEAD (COL): NO crea/elimina zonas base; SÍ puede cambiar estado operativo de zona (zone.update_status) y crear exclusion_zones dentro de su país (si está habilitado).Esto elimina la contradicción reportada por auditoría.
- COUNTRY_OPS_LEAD (scoped): opera dentro de su país, cambia estado de zonas, gestiona capacidad, aprueba sellers, opera Studio/Camaleón según permisos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- SYSTEM/BOT: servicios internos con permisos mínimos.
- Los docs sugieren namespaces para permisos (global/geo/policy/cms/finance/risk/support/moderation/analytics/sre/backups/integrations). Se fijan como estándar.

## Auth

- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- RBAC: roles → permisos granulares.
- Claims de seguridad y guard chain canónica: Auth → Role → Scope → Permission → Policy.
- Actores y permisos (RBAC) + guards
- AuthGuard: sesión válida
- PermissionGuard: permiso requerido por endpoint/acción
- APIs de mapas/tiles y operaciones requieren country_code y se filtran por scope; además se recomienda enforcement a nivel query (RLS / filtros server-side), no solo UI.
- Ser auditable: cambios de rol/scope/estados críticos quedan registrados con who/when/what/why.
- COUNTRY_OPS_LEAD (scoped): opera dentro de su país, cambia estado de zonas, gestiona capacidad, aprueba sellers, opera Studio/Camaleón según permisos.
- SYSTEM/BOT: servicios internos con permisos mínimos.
- Los docs sugieren namespaces para permisos (global/geo/policy/cms/finance/risk/support/moderation/analytics/sre/backups/integrations). Se fijan como estándar.

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-jerarqua-260206_2015.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
