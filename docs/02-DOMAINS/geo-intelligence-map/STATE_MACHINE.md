# STATE_MACHINE · geo-intelligence-map

## Estados

- Capa de cobertura (zonas operativas, estado, y superposición de cobertura de sellers).
- Ops Lead ve el mapa solo dentro de su operación (país completo, zonas activas e inactivas visibles) y opera cambios permitidos (ej. estado de zona).
- Capas toggleables: zonas (polígonos y estado), sellers (pins/clusters), heatmaps de KPIs (orders, GMV, problemas), cobertura y gaps, lead-time risk, etc.
- Operación de zona: cambiar estado de zona (kill switch / paused / saturated) desde el mapa, con motivo y auditoría.
- COUNTRY_OPS_LEAD (scoped): lectura del mapa solo de su país; operar estado de zonas; crear/gestionar exclusion_zones.

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Fallback/rollback: si falla ingesta, mantener dataset_version_current y alertar; permitir rollback explícito auditado.
- Flujos end-to-end (happy path + edge cases)
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.

## Triggers

- Eventos y triggers (pipelines) + idempotencia
- Pipeline de usuarios: consume eventos de órdenes geolocalizadas y agrega gps_verified_users por H3/ventana temporal (30d/90d).
- Consumir eventos order_created/paid/delivered/canceled/dispute_opened, normalizar hub/zone por point-in-polygon, actualizar agregados incrementalmente.
- Analytics backbone alimenta geo_metrics_agg y heatmaps; el mapa consume agregados, no eventos crudos.

## Trazabilidad

- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
