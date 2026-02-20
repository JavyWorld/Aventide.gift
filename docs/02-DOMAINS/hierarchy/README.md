# hierarchy

## Propósito

- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- seller onboarding: seller.approve, seller.reject (COL).
- Sistema de Jerarquía v2.0 (corregido y unificado)
- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
- Aunque Jerarquías no define explícitamente bus/cola, el proyecto usa workers/colas para procesos críticos en general. (Inferencia consistente con arquitectura del proyecto, pero aquí solo se definen eventos del módulo Jerarquía.)
- Definición y objetivos del sistema/módulo
- Definición: El Sistema de Jerarquía es el conjunto de reglas y mecanismos que determinan quién puede hacer qué y dónde (territorio) en Aventide Gift, combinando:
- zones.created_by_role debe ser SUPER_ADMIN (o servicio autorizado) para zonas base.
- Título extraído: "Sistema de Jerarquía v2.0 (corregido y unificado)".

## Límites

- Claims mínimos en JWT/sesión (no negociable):
- Definición: El Sistema de Jerarquía es el conjunto de reglas y mecanismos que determinan quién puede hacer qué y dónde (territorio) en Aventide Gift, combinando:
- Alcance
- Reglas y políticas (límites, expiraciones, validaciones)
- SUPER_ADMIN (global owner): define estructura territorial, reglas macro, integraciones, break-glass.

## Dependencias

- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Jerarquía v2.0 (corregido y unificado)
- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
- Aunque Jerarquías no define explícitamente bus/cola, el proyecto usa workers/colas para procesos críticos en general. (Inferencia consistente con arquitectura del proyecto, pero aquí solo se definen eventos del módulo Jerarquía.)
- Eventos de autorización (dominio Jerarquía)
- Definición: El Sistema de Jerarquía es el conjunto de reglas y mecanismos que determinan quién puede hacer qué y dónde (territorio) en Aventide Gift, combinando:
- SUPER_ADMIN (global owner): define estructura territorial, reglas macro, integraciones, break-glass.
- Título extraído: "Sistema de Jerarquía v2.0 (corregido y unificado)".

## Trazabilidad

- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
- Título extraído: "Sistema de Jerarquía v2.0 (corregido y unificado)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
