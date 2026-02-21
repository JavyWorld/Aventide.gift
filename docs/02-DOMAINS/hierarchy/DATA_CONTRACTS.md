# DATA_CONTRACTS · hierarchy

## Entidades y campos
- FINANCE_AUDITOR (scoped o global): lectura de ledger/reportes/evidencia; sin permisos operativos.
- finance: finance.ledger.read (auditor/finance admin), finance.payouts.reconcile (finance admin).
- Publica cambios (auditables por entidad).
- 6) Modelo de datos (tablas, campos, índices, relaciones)
- 6.1 Entidades territoriales
- Para “exclusion zones”, tabla separada: exclusion_zones(...) con created_by_role = COUNTRY_OPS_LEAD y FK a country.
- 6.2 Identidad interna / autorización
- Campos mínimos para operaciones jerárquicas:

## Constraints y claves de negocio
- 6.3 Auditoría (append-only)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia
- idempotency_key (por request)
- Resolución: se modelan como catálogo único con permisos granulares; roles “admin” se expresan como bundles de permisos (no como superpoder implícito).
- Sistema de Jerarquía v2.0 (corregido y unificado)
- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora


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
