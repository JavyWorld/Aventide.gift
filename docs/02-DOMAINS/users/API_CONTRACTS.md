# API_CONTRACTS · users

## Endpoints y auth
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Auditoría inmutable (Black Box/WORM) para identidad y escaladas: cambios de RBAC, impersonation, overrides.
- Auth Service federado (Firebase Auth o Auth0) + login Google/Apple/teléfono (WhatsApp Auth).
- Backend mantiene tabla users y emite JWT con claims de rol/permisos/scope (modelo de sesión unificado).
- 3) Actores y permisos (RBAC) + guards
- Claims mínimos en JWT:
- session_flags (2FA, risk level, break-glass, etc.)Base: “rol viaja en JWT” + backend aplica middleware por permiso.
- Auth (token válido)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Regla dura backend en compra: si Zone.Status != ACTIVE → error “Zone Suspended”.
- id, user_id, country_code, hub_id, zone_id, business_address_id, kyc_payload_json, status (DRAFT|SUBMITTED|PENDING_APPROVAL|APPROVED|REJECTED|WAITLISTED), reviewed_by, reviewed_at, decision_reason_codes[]
- seller.application_submitted, seller.application_approved/rejected/waitlisted
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- App Camaleón: UI profile por país/hub/zona/rol + config firmada + fallback.

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
