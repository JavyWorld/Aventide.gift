# RUNBOOKS · users

## Operación
- Cambios de RBAC + alertas por escaladas raras + impersonation log + four-eyes en capa de gobernanza.
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.

## Incidentes, rollback y backfill
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Objetivos:
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.
- Autorización estricta por claims y middleware (no por UI).
- Contexto geo-operativo consistente: Seller estático por “sorting hat” y Buyer dinámico por “Entregar en…”.
- Privacidad defendible (Admirador Secreto + Trust Badge) sin perder seguridad operativa.


## Control operativo verificable

- Owner: `Equipo users`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-USERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/users/dominio-users-operacion`
  - `https://jira.aventide.gift/browse/OPS-USERS-241`

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
