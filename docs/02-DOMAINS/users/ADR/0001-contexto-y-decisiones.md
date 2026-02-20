# ADR-0001: Contexto y decisiones clave (users)

- **Estado**: Aprobado
- **Contexto**: App entra directo en modo comprador (no fuerza decisión seller).

## Decisiones
- App entra directo en modo comprador (no fuerza decisión seller).
- Riesgo/abuso: rate limiting y bloqueos temporales se aplican en edge/app layer (coherente con perímetro/WAF/rate limit).
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Objetivos:

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
