# INVARIANTS · users

Reglas no negociables del dominio:
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Auditoría inmutable (Black Box/WORM) para identidad y escaladas: cambios de RBAC, impersonation, overrides.
- SUPERADMIN: configura reglas globales, países, accesos, auditoría.
- 3.2 Reglas de visibilidad / alcance (no negociables)
- Seller ve solo lo suyo (nunca finanzas globales).
- SuperAdmin ve/configura Operación definida y validada, Operación definida y validada auditado.
- user_scopes(user_id, scope_type, scope_id, assigned_by, reason, assigned_at)Base: rol viaja en JWT y middleware por permiso; auditoría de gobernanza.
- 6.5 Auditoría WORM (Black Box)
- audit_logs append-only con actor_id, actor_role, action_type, resource_type/id, changes(old/new), metadata (IP/UA/geo/reason), created_at. Retenciones diferenciadas.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia


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
