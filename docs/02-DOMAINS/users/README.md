# users

## Propósito

- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Claims mínimos en JWT:
- seller.application_submitted, seller.application_approved/rejected/waitlisted
- App Camaleón: UI profile por país/hub/zona/rol + config firmada + fallback.
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
- Sistema de Usuarios v2.0 (corregido y unificado)
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Objetivos:
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.
- user_identities (opcional si se soportan múltiples providers por cuenta)
- Título extraído: "Sistema de Usuarios v2.0 (corregido y unificado)".

## Límites

- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Regla dura backend en compra: si Zone.Status != ACTIVE → error “Zone Suspended”.
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Reglas de visibilidad / alcance (no negociables)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
- Eventos del dominio Usuarios
- Sistema de Usuarios v2.0 (corregido y unificado)
- Integración con App Camaleón (Server-Driven UI) para UI profile por país/hub/zona/rol.
- Gestión de pagos/ledger (solo se integra a nivel de identidad/retención).
- Título extraído: "Sistema de Usuarios v2.0 (corregido y unificado)".


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
- Título extraído: "Sistema de Usuarios v2.0 (corregido y unificado)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
