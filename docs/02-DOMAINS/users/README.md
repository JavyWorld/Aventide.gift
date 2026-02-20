# users

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 3.2 Reglas de visibilidad / alcance (no negociables)
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Integración con App Camaleón (Server-Driven UI) para UI profile por país/hub/zona/rol.
- Gestión de pagos/ledger (solo se integra a nivel de identidad/retención).
- id (UUID), auth_provider (firebase|auth0), provider_user_id, email, phone_e164, email_verified, phone_verified
- user_identities (opcional si se soportan múltiples providers por cuenta)

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
- Título extraído: "Sistema de Usuarios v2.0 (corregido y unificado)".
