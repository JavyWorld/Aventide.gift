# geo-intelligence-map

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- Edge: mapa incluye zonas inactivas (no se ocultan, cambian simbología). Esto aplica también en vista país para expansion planning.
- 5) Reglas y políticas (límites, validaciones, privacidad)

## Dependencias
- Definición: Geo Intelligence Map es un sistema independiente del Panel (Regional OS + SuperAdmin) que ofrece:
- Integración multi-país: datasets de población deben ser pluggable por país (adapter por país) y versionados/rollback si falla ingesta.
- Todas las APIs de mapa/tiles exigen country_code y pasan por ScopeGuard: countryCode ∈ scopes.countries[] (y opcional hub_id ∈ scopes.hubs[]).
- 8) Integraciones (Map UI + Census/Population Provider)
- 8.2 “Census/Population Provider” (por país, pluggable)

## Trazabilidad
- Documento origen: `sistema-geo-intelligence-map-260207_1103.docx`
- Título extraído: "Sistema: Geo Intelligence Map (Geofencing + Heatmaps + Penetración Poblacional) v2.0".
