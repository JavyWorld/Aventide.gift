# STATE_MACHINE · hierarchy

## Estados detectados/derivados
- Ser auditable: cambios de rol/scope/estados críticos quedan registrados con who/when/what/why.
- COUNTRY_OPS_LEAD (COL): NO crea/elimina zonas base; SÍ puede cambiar estado operativo de zona (zone.update_status) y crear exclusion_zones dentro de su país (si está habilitado).Esto elimina la contradicción reportada por auditoría.
- COUNTRY_OPS_LEAD (scoped): opera dentro de su país, cambia estado de zonas, gestiona capacidad, aprueba sellers, opera Studio/Camaleón según permisos.
- 4) Flujos end-to-end (happy path + edge cases)
- Ubicación → valida estado de zona/cobertura.
- KYC dinámico por país → estado PENDING_APPROVAL.

## Transiciones y eventos de entrada/salida
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Aunque Jerarquías no define explícitamente bus/cola, el proyecto usa workers/colas para procesos críticos en general. (Inferencia consistente con arquitectura del proyecto, pero aquí solo se definen eventos del módulo Jerarquía.)
- 7.1 Eventos de autorización (dominio Jerarquía)
- inicio/fin de break-glassdebe producir un evento de auditoría con who/when/what/why.
- Sistema de Jerarquía v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- 1) Definición y objetivos del sistema/módulo
- Definición: El Sistema de Jerarquía es el conjunto de reglas y mecanismos que determinan quién puede hacer qué y dónde (territorio) en Aventide Gift, combinando:

## Trazabilidad
- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
