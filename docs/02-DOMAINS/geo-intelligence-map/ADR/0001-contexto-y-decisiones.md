# ADR-0001: Contexto y decisiones clave (geo-intelligence-map)

- **Estado**: Aprobado
- **Contexto**: Capas del mapa son datasets versionados; población debe tener census_dataset_version; el mapa sirve “current” por país con rollback si falla ingesta (patrón resiliencia).

## Decisiones
- Capas del mapa son datasets versionados; población debe tener census_dataset_version; el mapa sirve “current” por país con rollback si falla ingesta (patrón resiliencia).
- Mobile: react-native-maps (Google) o Mapbox GL; Web Panels: Mapbox/Google (la doc no fija librería web, fija patrón Map UI + PostGIS + H3/tiles).
- Conflictos/incoherencias corregidas (y decisión oficial del sistema)
- Riesgo de PII (pintar usuarios) → queda oficial: solo agregación por grid H3/tiles, nunca usuarios individuales.
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
