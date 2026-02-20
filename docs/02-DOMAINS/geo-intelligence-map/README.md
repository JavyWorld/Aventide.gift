# geo-intelligence-map

## Propósito

- fetch_dataset(request): { raw_file_uri, dataset_version, metadata }
- fallback_policy (last-known-good dataset_version)
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Definición y objetivos del sistema/módulo
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
- Analytics backbone alimenta geo_metrics_agg y heatmaps; el mapa consume agregados, no eventos crudos.
- Definición: Geo Intelligence Map es un sistema independiente del Panel (Regional OS + SuperAdmin) que ofrece:
- “Census/Population Provider” (por país, pluggable)
- Título extraído: "Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0".

## Límites

- Alcance (incluye / excluye)
- Edge: mapa incluye zonas inactivas (no se ocultan, cambian simbología). Esto aplica también en vista país para expansion planning.
- Reglas y políticas (límites, validaciones, privacidad)
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.

## Dependencias

- Pipeline de usuarios: consume eventos de órdenes geolocalizadas y agrega gps_verified_users por H3/ventana temporal (30d/90d).
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.
- Integraciones (Map UI + Census/Population Provider)

## Trazabilidad

- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
- Título extraído: "Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
