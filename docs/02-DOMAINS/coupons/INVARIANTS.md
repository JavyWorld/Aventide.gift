# INVARIANTS · coupons

Reglas no negociables del dominio:
- Definición: Sistema que permite a un seller crear y administrar cupones (seller-funded) para que buyers los apliquen en checkout, cumpliendo reglas de elegibilidad, targeting territorial y límites de uso. El descuento reduce el ingreso del seller (nunca lo absorbe la plataforma).
- No romper invariantes: no afecta taxes/processing/ops fee/FS; solo afecta la porción “items” del seller (o delivery si el tipo es free delivery y el delivery es seller-funded).
- Auditabilidad: snapshot por orden y eventos analíticos; idempotencia por checkout_id en la aplicación.
- OPS LEAD / ADMIN: auditoría y enforcement (p.ej. suspender coupon por abuso) con scope. (El rol ops/admin ya es estándar del proyecto).
- AuditGuard (cambios y acciones de enforcement)
- Persiste el estado del checkout idempotente y emite evento analítico SELLER_COUPON_APPLIED.
- Reintento/redoble click → no “consume” dos veces: idempotencia por checkout_id.
- 5.1 Principio duro (invariante)
- Si se habilita apilado por policy, debe existir regla determinística: ONLY_ONE_SELLER_COUPON + orden de preferencia (p. ej. mayor descuento efectivo) y debe quedar snapshotteado.
- unique(checkout_id, coupon_id) para idempotencia

## Trazabilidad
- Documento origen: `sistema-de-cupones-260207_0826.docx`
