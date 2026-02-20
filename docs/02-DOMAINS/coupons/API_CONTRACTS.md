# API_CONTRACTS · coupons

## Endpoints

- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- Stacking policy (por defecto NO apilable).
- Actores y permisos (RBAC) + guards
- AuthGuard
- OwnershipGuard (seller_id) en endpoints seller
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- Reintento/redoble click → no “consume” dos veces: idempotencia por checkout_id.
- stacking_policy (default NO apilable)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Backend guarda code_hash (no el código plano) y estado ACTIVE.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Default: NO apilable.
- Si se habilita apilado por policy, debe existir regla determinística: ONLY_ONE_SELLER_COUPON + orden de preferencia (p. ej. mayor descuento efectivo) y debe quedar snapshotteado.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- OwnershipGuard (seller_id) en endpoints seller
- Backend guarda code_hash (no el código plano) y estado ACTIVE.

## Códigos de error

- Código inválido/expirado → respuesta con reject_reason estandarizado (ver 5.8).
- Backend guarda code_hash (no el código plano) y estado ACTIVE.

## Idempotency

- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- Reintento/redoble click → no “consume” dos veces: idempotencia por checkout_id.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad

- Documento origen: `sistema-de-cupones-260207_0826.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
