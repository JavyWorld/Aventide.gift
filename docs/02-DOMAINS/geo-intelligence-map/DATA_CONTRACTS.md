# DATA_CONTRACTS · geo-intelligence-map

## Entidades y campos
- validate(raw): schema + checksums + coverage
- Export (snapshot PNG/PDF + CSV agregados) debe quedar auditado como acceso/acción sensible (no exportar PII).
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 1) Definición y objetivos del sistema/módulo
- Definición: Geo Intelligence Map es un sistema independiente del Panel (Regional OS + SuperAdmin) que ofrece:
- Visualización de territorio (país/hub/zona) basado en polígonos PostGIS.
- Heatmaps/KPIs por densidad regional (órdenes, GMV, problemas, capacidad, etc.) renderizados por grid H3/tiles (no por puntos individuales).

## Constraints y claves de negocio
- Click zona → drawer/panel contextual → puede cambiar estado operativo (ACTIVE/PAUSED/SATURATED/CREATED_INACTIVE) si tiene permiso zone.update_status, registrando motivo y auditoría append-only.
- 7) Eventos y triggers (pipelines) + idempotencia
- Idempotencia: (country_code, dataset_version, cell_id)
- La documentación afirma explícitamente que NO está definido qué fuente oficial exacta usar por país y que debe ser pluggable por país (adapter), no hardcodeado.
- Cambios de zone.update_status, creación/edición de exclusion_zones, y overrides de datasets/versiones ⇒ auditoría append-only (WORM).
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
