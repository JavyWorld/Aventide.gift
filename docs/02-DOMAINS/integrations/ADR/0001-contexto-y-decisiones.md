# ADR-0001: Contexto y decisiones clave (integrations)

- **Estado**: Aprobado
- **Contexto**: Definición: Capa central que conecta el Core Aventide con proveedores externos (Pagos, Mensajería, Maps/Geocoding, Storage, Tax, etc.) bajo un patrón Hub & Spoke:

## Decisiones
- Definición: Capa central que conecta el Core Aventide con proveedores externos (Pagos, Mensajería, Maps/Geocoding, Storage, Tax, etc.) bajo un patrón Hub & Spoke:
- 5.1 Principio rector (arquitectura)
- Pagos (Rapyd) — patrón oficial
- Frontend llamando directo a proveedores (riesgo dinero/abuso) → prohibido: backend proxy para acciones críticas.
- Sistema de Integraciones v2.0 (Integration Ecosystem) — corregido y unificado
- Fuente de verdad: “Sistema de Integraciones (Integration Ecosystem) — Proveedores, Webhooks, Adapters, Workers, Auditoría”.Dependencia estructural: Auditoría Unificada (WORM, atribución, evidencia).

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-integraciones-260207_0951.docx`
