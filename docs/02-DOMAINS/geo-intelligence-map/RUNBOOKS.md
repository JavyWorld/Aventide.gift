# RUNBOOKS · geo-intelligence-map

## Operación
- Ops Lead ve el mapa solo dentro de su operación (país completo, zonas activas e inactivas visibles) y opera cambios permitidos (ej. estado de zona).
- SuperAdmin/Global Management ve el mundo completo y puede “drill down” Mundo→País→Hub→Zona→Seller.
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.
- Operación de zona: cambiar estado de zona (kill switch / paused / saturated) desde el mapa, con motivo y auditoría.
- Regla “solo ve su operación”
- 5.4 Versionado/rollback de capas

## Incidentes, rollback y backfill
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.
- 5.4 Versionado/rollback de capas
- Capas del mapa son datasets versionados; población debe tener census_dataset_version; el mapa sirve “current” por país con rollback si falla ingesta (patrón resiliencia).
- Fallback/rollback: si falla ingesta, mantener dataset_version_current y alertar; permitir rollback explícito auditado.
- Si quieres que quede 100% cerrado “por país” (CO/USA/RD), hace falta que indiques qué fuente oficial usar en cada uno; el sistema ya queda definido para soportarlo vía Integration Registry + adapters + versionado/rollback.
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
