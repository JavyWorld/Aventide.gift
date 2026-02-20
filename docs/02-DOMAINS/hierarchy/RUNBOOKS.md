# RUNBOOKS · hierarchy

## Operación
- Soportar operación multi-país y paneles Global vs Regional OS con rutas scoping.
- B) Roles internos (operación y control)
- 4.3 Operación diaria del país (COL)
- Finanzas/Auditoría: lectura o acciones financieras específicas; sin operación territorial.
- Zone.status (operación):
- 9) Observabilidad (logs, métricas, alertas, SLOs)

## Incidentes, rollback y backfill
- Resultado exigido: un cambio no puede duplicarse por reintentos; auditoría registra una sola verdad por acción.
- Sistema de Jerarquía v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- 1) Definición y objetivos del sistema/módulo
- Definición: El Sistema de Jerarquía es el conjunto de reglas y mecanismos que determinan quién puede hacer qué y dónde (territorio) en Aventide Gift, combinando:
- RBAC: roles → permisos granulares.
- Scope territorial: país / hub / zona (y variantes).
- Policy Engine: condiciones por país/feature flags (App Camaleón).

## Trazabilidad
- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
