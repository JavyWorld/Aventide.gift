# EVENT_CONTRACTS · users

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos del dominio Usuarios
- Entrega/Tridente: identidad del evento de entrega ligada a evidencia; confirmación robusta.
- Sistema de Usuarios v2.0 (corregido y unificado)
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Objetivos:
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.
- Autorización estricta por claims y middleware (no por UI).
- Contexto geo-operativo consistente: Seller estático por “sorting hat” y Buyer dinámico por “Entregar en…”.


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
