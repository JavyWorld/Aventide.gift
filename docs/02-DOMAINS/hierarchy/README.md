# hierarchy

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance
- Incluye
- Excluye
- 5) Reglas y políticas (límites, expiraciones, validaciones)
- Sistema de Jerarquía v2.0 (corregido y unificado)

## Dependencias
- SUPER_ADMIN (global owner): define estructura territorial, reglas macro, integraciones, break-glass.
- SYSTEM/BOT: servicios internos con permisos mínimos.
- Los docs sugieren namespaces para permisos (global/geo/policy/cms/finance/risk/support/moderation/analytics/sre/backups/integrations). Se fijan como estándar.
- APIs de mapas/tiles y operaciones requieren country_code y se filtran por scope; además se recomienda enforcement a nivel query (RLS / filtros server-side), no solo UI.
- zones.created_by_role debe ser SUPER_ADMIN (o servicio autorizado) para zonas base.

## Trazabilidad
- Documento origen: `sistema-de-jerarqua-260206_2015.docx`
- Título extraído: "Sistema de Jerarquía v2.0 (corregido y unificado)".
