# DATA_CONTRACTS · users

## Entidades y campos
- Definición: Sistema responsable de identidad unificada, autenticación, sesiones/JWT, perfil + direcciones, roles/permisos (RBAC/ABAC), contexto multi-país (Buyer dinámico / Seller estático por geo), ciclo de vida (suspensión/borrado/archivo) y señales de confianza integradas con entrega/auditoría.
- Una sola cuenta para Buyer/Seller (modo dual), sin duplicar identidades.
- Borrado/retención coherente: crypto-shredding para perfil/marketing, pero NO para ledger/AML; usar DELETED_PENDING_ARCHIVE + bóveda fiscal.
- Auditoría inmutable (Black Box/WORM) para identidad y escaladas: cambios de RBAC, impersonation, overrides.
- Backend mantiene tabla users y emite JWT con claims de rol/permisos/scope (modelo de sesión unificado).
- Gestión de pagos/ledger (solo se integra a nivel de identidad/retención).
- Corrección clave de coherencia (heredada de Jerarquía):
- Auth Service (Firebase/Auth0) valida identidad.

## Constraints y claves de negocio
- BUYER: compra, confirma recepción, reporta incidencias.
- Corrección clave de coherencia (heredada de Jerarquía):
- Confirmación de entrega requiere PIN+GPS+Foto con validaciones duras; PIN hasheado; anti-replay nonce; rate limiting por fallos.
- id, user_id, country_code, address_fields_json, lat, lng, normalized_hash, is_default, created_at
- Índices: (user_id, is_default), normalized_hash, geohash opcional
- audit_logs append-only con actor_id, actor_role, action_type, resource_type/id, changes(old/new), metadata (IP/UA/geo/reason), created_at. Retenciones diferenciadas.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.2 Idempotencia (obligatorio)

## Trazabilidad
- Documento origen: `sistema-de-usuarios-260206_2328.docx`
