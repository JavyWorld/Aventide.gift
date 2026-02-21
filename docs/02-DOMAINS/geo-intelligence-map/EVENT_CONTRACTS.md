# EVENT_CONTRACTS · geo-intelligence-map

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Pipeline de usuarios: consume eventos de órdenes geolocalizadas y agrega gps_verified_users por H3/ventana temporal (30d/90d).
- 7) Eventos y triggers (pipelines) + idempotencia
- Consumir eventos order_created/paid/delivered/canceled/dispute_opened, normalizar hub/zone por point-in-polygon, actualizar agregados incrementalmente.
- Analytics backbone alimenta geo_metrics_agg y heatmaps; el mapa consume agregados, no eventos crudos.
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Geo Intelligence Map es un sistema independiente del Panel (Regional OS + SuperAdmin) que ofrece:
- Visualización de territorio (país/hub/zona) basado en polígonos PostGIS.
- Heatmaps/KPIs por densidad regional (órdenes, GMV, problemas, capacidad, etc.) renderizados por grid H3/tiles (no por puntos individuales).


## Control operativo verificable

- Owner: `Equipo geo-intelligence-map`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GEOINTELLIGE-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/geo-intelligence-map/dominio-geo-intelligence-map-operacion`
  - `https://jira.aventide.gift/browse/OPS-GEOINTELLIGE-241`

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
