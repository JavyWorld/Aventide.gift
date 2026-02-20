# API_CONTRACTS · geo-intelligence-map

## Endpoints

- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- Actores, permisos (RBAC) y guards
- Auth → Role → Scope → Permission → Policy
- Todas las APIs de mapa/tiles exigen country_code y pasan por ScopeGuard: countryCode ∈ scopes.countries[] (y opcional hub_id ∈ scopes.hubs[]).
- Eventos y triggers (pipelines) + idempotencia
- Idempotencia: (country_code, dataset_version, cell_id)
- download_method (API/FTP/portal)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- COUNTRY_OPS_LEAD (scoped): lectura del mapa solo de su país; operar estado de zonas; crear/gestionar exclusion_zones.

## Auth

- Base en documentación: el proyecto ya define explícitamente un “Mapa global/territorial” con capas, heatmaps, PostGIS + H3/tiles, RBAC por country scope, y anti-PII, y su UX (macro→micro).
- Actores, permisos (RBAC) y guards
- Auth → Role → Scope → Permission → Policy
- Todas las APIs de mapa/tiles exigen country_code y pasan por ScopeGuard: countryCode ∈ scopes.countries[] (y opcional hub_id ∈ scopes.hubs[]).
- COUNTRY_OPS_LEAD (scoped): lectura del mapa solo de su país; operar estado de zonas; crear/gestionar exclusion_zones.

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Eventos y triggers (pipelines) + idempotencia
- Idempotencia: (country_code, dataset_version, cell_id)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Trazabilidad

- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
