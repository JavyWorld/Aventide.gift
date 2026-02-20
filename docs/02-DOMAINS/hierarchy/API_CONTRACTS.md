# API_CONTRACTS · hierarchy

## Endpoints y auth
- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- RBAC: roles → permisos granulares.
- Claims de seguridad y guard chain canónica: Auth → Role → Scope → Permission → Policy.
- 3) Actores y permisos (RBAC) + guards
- Claims mínimos en JWT/sesión (no negociable):
- AuthGuard: sesión válida
- PermissionGuard: permiso requerido por endpoint/acción
- APIs de mapas/tiles y operaciones requieren country_code y se filtran por scope; además se recomienda enforcement a nivel query (RLS / filtros server-side), no solo UI.

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- seller onboarding: seller.approve, seller.reject (COL).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Onboarding seller: flujo PENDING_APPROVAL → approve/reject por COL; asignación geo.
- Sistema de Jerarquía v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.

## Trazabilidad
- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
