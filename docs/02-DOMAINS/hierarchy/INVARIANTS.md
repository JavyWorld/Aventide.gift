# INVARIANTS · hierarchy

Reglas no negociables del dominio:
- Fuente de verdad: “Sistema de Jerarquías (RBAC + Scope geográfico + Workflows)” y secciones RBAC/Guards del documento del proyecto.Problema principal detectado: contradicción sobre quién “define” zonas (polígonos). La auditoría lo marca como conflicto estructural: Jerarquías decía que el Ops Lead define zonas, pero en Geo/Paneles se define que SuperAdmin crea/edita Countries/Hubs/Zones. Se fija una sola verdad.
- Definición: El Sistema de Jerarquía es el conjunto de reglas y mecanismos que determinan quién puede hacer qué y dónde (territorio) en Aventide Gift, combinando:
- Workflows: aprobación y operaciones con auditoría y separación de poderes.
- Ser auditable: cambios de rol/scope/estados críticos quedan registrados con who/when/what/why.
- COUNTRY_OPS_LEAD (COL): NO crea/elimina zonas base; SÍ puede cambiar estado operativo de zona (zone.update_status) y crear exclusion_zones dentro de su país (si está habilitado).Esto elimina la contradicción reportada por auditoría.
- FINANCE_AUDITOR (scoped o global): lectura de ledger/reportes/evidencia; sin permisos operativos.
- finance: finance.ledger.read (auditor/finance admin), finance.payouts.reconcile (finance admin).
- Claims mínimos en JWT/sesión (no negociable):
- Sistema exige razón y audita el cambio.
- Publica cambios (auditables por entidad).


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
