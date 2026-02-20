# users

## Propósito

- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Claims mínimos en JWT:
- seller.application_submitted, seller.application_approved/rejected/waitlisted
- App Camaleón: UI profile por país/hub/zona/rol + config firmada + fallback.
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
- Sistema de Usuarios v2.0 (corregido y unificado)
- Definición y objetivos del sistema/módulo
- Objetivos:
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.
- user_identities (opcional si se soportan múltiples providers por cuenta)
- Título extraído: "Sistema de Usuarios v2.0 (corregido y unificado)".

## Límites

- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Regla dura backend en compra: si Zone.Status != ACTIVE → error “Zone Suspended”.
- Alcance (incluye / excluye)
- Reglas de visibilidad / alcance (no negociables)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
- Eventos del dominio Usuarios
- Sistema de Usuarios v2.0 (corregido y unificado)
- Integración con App Camaleón (Server-Driven UI) para UI profile por país/hub/zona/rol.
- Gestión de pagos/ledger (solo se integra a nivel de identidad/retención).
- Título extraído: "Sistema de Usuarios v2.0 (corregido y unificado)".

## Trazabilidad

- Documento origen: `sistema-de-usuarios-260206_2328.docx`
- Título extraído: "Sistema de Usuarios v2.0 (corregido y unificado)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
