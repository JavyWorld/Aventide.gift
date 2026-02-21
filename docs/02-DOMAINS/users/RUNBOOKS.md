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

## Ownership & Escalation

- **Owner técnico:** `Equipo users`
- **Owner negocio/regulatorio:** `Product + Compliance (users)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

