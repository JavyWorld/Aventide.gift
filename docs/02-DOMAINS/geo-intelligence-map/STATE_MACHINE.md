# STATE_MACHINE · geo-intelligence-map

## Estados detectados/derivados
- Capa de cobertura (zonas operativas, estado, y superposición de cobertura de sellers).
- Ops Lead ve el mapa solo dentro de su operación (país completo, zonas activas e inactivas visibles) y opera cambios permitidos (ej. estado de zona).
- Capas toggleables: zonas (polígonos y estado), sellers (pins/clusters), heatmaps de KPIs (orders, GMV, problemas), cobertura y gaps, lead-time risk, etc.
- Operación de zona: cambiar estado de zona (kill switch / paused / saturated) desde el mapa, con motivo y auditoría.
- COUNTRY_OPS_LEAD (scoped): lectura del mapa solo de su país; operar estado de zonas; crear/gestionar exclusion_zones.
- 4) Flujos end-to-end (happy path + edge cases)

## Transiciones y eventos de entrada/salida
- Pipeline de usuarios: consume eventos de órdenes geolocalizadas y agrega gps_verified_users por H3/ventana temporal (30d/90d).
- 7) Eventos y triggers (pipelines) + idempotencia
- Consumir eventos order_created/paid/delivered/canceled/dispute_opened, normalizar hub/zone por point-in-polygon, actualizar agregados incrementalmente.
- Analytics backbone alimenta geo_metrics_agg y heatmaps; el mapa consume agregados, no eventos crudos.
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 1) Definición y objetivos del sistema/módulo
- Definición: Geo Intelligence Map es un sistema independiente del Panel (Regional OS + SuperAdmin) que ofrece:

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
