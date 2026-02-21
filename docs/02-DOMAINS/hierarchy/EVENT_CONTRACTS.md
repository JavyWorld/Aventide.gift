# EVENT_CONTRACTS · hierarchy

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Garantizar enforcement en backend (la UI solo refleja, no autoriza).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Aunque Jerarquías no define explícitamente bus/cola, el proyecto usa workers/colas para procesos críticos en general. (Inferencia consistente con arquitectura del proyecto, pero aquí solo se definen eventos del módulo Jerarquía.)
- 7.1 Eventos de autorización (dominio Jerarquía)
- inicio/fin de break-glassdebe producir un evento de auditoría con who/when/what/why.
- Sistema de Jerarquía v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: El Sistema de Jerarquía es el conjunto de reglas y mecanismos que determinan quién puede hacer qué y dónde (territorio) en Aventide Gift, combinando:
- RBAC: roles → permisos granulares.


## Control operativo verificable

- Owner: `Equipo hierarchy`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-HIERARCHY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/hierarchy/dominio-hierarchy-operacion`
  - `https://jira.aventide.gift/browse/OPS-HIERARCHY-241`

## Trazabilidad
- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
