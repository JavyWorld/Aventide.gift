# DATA_CONTRACTS · continuity

## Entidades y campos
- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- No romper el core económico: fees snapshotteados, split automático (seller / Aventide / COL), ledger inmutable.
- se snapshottea en orden,
- Money-plane: las nuevas órdenes siguen cobrando ops_fee_pct snapshotteado, pero su beneficiario pasa a COUNTRY_RESERVE.
- 5.1 Principio clave: separación Control Plane vs Money Plane
- ops_lead_fee_pct es config por país y se snapshottea en la orden; no cambia retrospectivamente.
- En snapshot financiero por orden (extensión mínima):
- 6) Modelo de datos (tablas/colecciones, campos, índices, relaciones)

## Constraints y claves de negocio
- Workflow de desembolso desde COUNTRY_RESERVE con four-eyes + ejecución idempotente por worker + auditoría WORM.
- SYSTEM/WORKERS: ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).
- 5.1 Principio clave: separación Control Plane vs Money Plane
- Constraint: TTL máximo por policy.
- idempotency_key
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (mínima)
- Disbursement: idempotency_key por request (worker ejecuta una vez).

## Trazabilidad
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
