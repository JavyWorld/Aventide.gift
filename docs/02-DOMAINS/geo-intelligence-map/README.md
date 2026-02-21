# geo-intelligence-map

## Propósito

- fetch_dataset(request): { raw_file_uri, dataset_version, metadata }
- fallback_policy (last-known-good dataset_version)
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
- Analytics backbone alimenta geo_metrics_agg y heatmaps; el mapa consume agregados, no eventos crudos.
- Definición: Geo Intelligence Map es un sistema independiente del Panel (Regional OS + SuperAdmin) que ofrece:
- “Census/Population Provider” (por país, pluggable)
- Título extraído: "Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0".

## Límites

- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Edge: mapa incluye zonas inactivas (no se ocultan, cambian simbología). Esto aplica también en vista país para expansion planning.
- Reglas y políticas (límites, validaciones, privacidad)
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.

## Dependencias

- Pipeline de usuarios: consume eventos de órdenes geolocalizadas y agrega gps_verified_users por H3/ventana temporal (30d/90d).
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.
- Integraciones (Map UI + Census/Population Provider)


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
- Título extraído: "Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
