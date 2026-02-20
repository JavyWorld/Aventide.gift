# API_CONTRACTS · internal-credit

## Endpoints y auth
- fee_credits_requested (FS)
- store_credit_requested (BSC) (si policy lo permite como tender)
- (opcional) gcc_credit_requested si GCC está habilitado.
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (checkout_id/order_id/dispute_id)
- store_credit_requested (BSC/GCC si policy lo permite)
- bsc_applied = min(bsc_balance, eligible_base_for_bsc, store_credit_requested)

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Crédito Interno v2.0 (Internal Credits / Wallets) — corregido y unificado
- Fuente de verdad: “Sistema de Referido y Crédito Interno” (sección 10.X F).
- 1) Definición y objetivos del sistema/módulo
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.

## Trazabilidad
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
