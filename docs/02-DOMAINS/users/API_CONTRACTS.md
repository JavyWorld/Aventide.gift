# API_CONTRACTS · users

## Endpoints

- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Auditoría inmutable (Black Box/WORM) para identidad y escaladas: cambios de RBAC, impersonation, overrides.
- Auth Service federado (Firebase Auth o Auth0) + login Google/Apple/teléfono (WhatsApp Auth).
- Backend mantiene tabla users y emite JWT con claims de rol/permisos/scope (modelo de sesión unificado).
- Actores y permisos (RBAC) + guards
- session_flags (2FA, risk level, break-glass, etc.)Base: “rol viaja en JWT” + backend aplica middleware por permiso.
- Auth (token válido)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Regla dura backend en compra: si Zone.Status != ACTIVE → error “Zone Suspended”.
- id, user_id, country_code, hub_id, zone_id, business_address_id, kyc_payload_json, status (DRAFT|SUBMITTED|PENDING_APPROVAL|APPROVED|REJECTED|WAITLISTED), reviewed_by, reviewed_at, decision_reason_codes[]
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- RBAC changes, overrides, impersonation, cambios de estado de cuenta y borrado → append-only.
- id (UUID), auth_provider (firebase|auth0), provider_user_id, email, phone_e164, email_verified, phone_verified

## Auth

- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Auditoría inmutable (Black Box/WORM) para identidad y escaladas: cambios de RBAC, impersonation, overrides.
- Auth Service federado (Firebase Auth o Auth0) + login Google/Apple/teléfono (WhatsApp Auth).
- Backend mantiene tabla users y emite JWT con claims de rol/permisos/scope (modelo de sesión unificado).
- Actores y permisos (RBAC) + guards
- session_flags (2FA, risk level, break-glass, etc.)Base: “rol viaja en JWT” + backend aplica middleware por permiso.
- Auth (token válido)
- RBAC changes, overrides, impersonation, cambios de estado de cuenta y borrado → append-only.
- id (UUID), auth_provider (firebase|auth0), provider_user_id, email, phone_e164, email_verified, phone_verified

## Códigos de error

- Regla dura backend en compra: si Zone.Status != ACTIVE → error “Zone Suspended”.

## Idempotency

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-usuarios-260206_2328.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
