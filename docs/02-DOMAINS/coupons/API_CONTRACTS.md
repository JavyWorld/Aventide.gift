# API_CONTRACTS · coupons

## Endpoints y auth
- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- Stacking policy (por defecto NO apilable).
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- OwnershipGuard (seller_id) en endpoints seller
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- Reintento/redoble click → no “consume” dos veces: idempotencia por checkout_id.
- stacking_policy (default NO apilable)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- valid_to < valid_from → reject.
- Código inválido/expirado → respuesta con reject_reason estandarizado (ver 5.8).
- Cupón excedió usage_limit_total en carrera (race) → se resuelve con contador atómico/locking; si pierde, reject_reason=LIMIT_REACHED.
- Si no cumple, reject_reason=FTB_NOT_ELIGIBLE.
- reject_reason (enum):

## Trazabilidad
- Documento origen: `sistema-de-cupones-260207_0826.docx`
