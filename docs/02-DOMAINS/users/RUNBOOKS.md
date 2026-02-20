# RUNBOOKS · users

## Operación
- Cambios de RBAC + alertas por escaladas raras + impersonation log + four-eyes en capa de gobernanza.
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.

## Incidentes, rollback y backfill
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Objetivos:
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.
- Autorización estricta por claims y middleware (no por UI).
- Contexto geo-operativo consistente: Seller estático por “sorting hat” y Buyer dinámico por “Entregar en…”.
- Privacidad defendible (Admirador Secreto + Trust Badge) sin perder seguridad operativa.

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
