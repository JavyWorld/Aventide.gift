# API_CONTRACTS · geo-intelligence-map

## Endpoints y auth
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 3) Actores, permisos (RBAC) y guards
- Auth → Role → Scope → Permission → Policy
- Todas las APIs de mapa/tiles exigen country_code y pasan por ScopeGuard: countryCode ∈ scopes.countries[] (y opcional hub_id ∈ scopes.hubs[]).
- 7) Eventos y triggers (pipelines) + idempotencia
- Idempotencia: (country_code, dataset_version, cell_id)
- fetch_dataset(request): { raw_file_uri, dataset_version, metadata }
- download_method (API/FTP/portal)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- fallback_policy (last-known-good dataset_version)
- Fallback/rollback: si falla ingesta, mantener dataset_version_current y alertar; permitir rollback explícito auditado.
- Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0
- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
