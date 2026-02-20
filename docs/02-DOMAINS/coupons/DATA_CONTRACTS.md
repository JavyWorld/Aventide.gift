# DATA_CONTRACTS · coupons

## Entidades y campos
- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- Cálculo de seller_coupon_discount respetando max_discount_amount en cupones % y demás constraints.
- SYSTEM/BOT: valida, calcula descuento, emite eventos, snapshottea la orden.
- En ORDER_CREATED→PAID_IN_ESCROW, el sistema snapshottea:
- coupon_id, discount_amount, coupon_policy_version en order_promo_snapshot.
- El cupón ya aplicado no “se devuelve” como crédito: era descuento seller-funded y ya afectó el net del seller en el snapshot de la orden.
- La reversión financiera ocurre vía Disputas/Refunds según buckets; el cupón permanece como dato histórico del snapshot.
- Si se habilita apilado por policy, debe existir regla determinística: ONLY_ONE_SELLER_COUPON + orden de preferencia (p. ej. mayor descuento efectivo) y debe quedar snapshotteado.

## Constraints y claves de negocio
- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- Cálculo de seller_coupon_discount respetando max_discount_amount en cupones % y demás constraints.
- Backend guarda code_hash (no el código plano) y estado ACTIVE.
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- Reintento/redoble click → no “consume” dos veces: idempotencia por checkout_id.
- code_hash
- unique(seller_id, code_hash)
- unique(checkout_id, coupon_id) para idempotencia

## Trazabilidad
- Documento origen: `sistema-de-cupones-260207_0826.docx`
