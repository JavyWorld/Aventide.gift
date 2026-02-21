# DATA_CONTRACTS · internal-credit

## Entidades y campos
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Auditabilidad total: balances nunca se “editan”; solo ledger entries (mint/spend/revoke/expire).
- Ledger por wallet + balances materializados derivados del ledger (proyección).
- wallet.ledger.read.own
- AuditGuard (ledger + snapshots)
- Se crean ledger entries de SPEND (idempotente por checkout_id) y se produce promo_snapshot en la orden.
- Se registra ledger EXPIRE (no edita balance directo).
- se generan ledger REVOKE o “compensación” según el tipo y policy.

## Constraints y claves de negocio
- IdempotencyGuard (checkout_id/order_id/dispute_id)
- Se crean ledger entries de SPEND (idempotente por checkout_id) y se produce promo_snapshot en la orden.
- Reintentos/redoble click: no duplica spend (idempotencia por checkout_id).
- 6.2 wallet_ledger (append-only)
- wallet_ledger(id, wallet_id, type: MINT|SPEND|REVOKE|EXPIRE, amount, source_type, order_id, dispute_id, expires_at, created_at)Campos clave:
- unique idempotencia:
- spend: unique(wallet_id, order_id, type=SPEND) si spend se hace al confirmar orden, o unique(wallet_id, checkout_id) si spend se hace en checkout (recomendado al calcular).Suposición: el documento fija idempotencia conceptual, no el campo exacto; se mantiene consistencia con “idempotente por checkout”.
- promo_snapshot(order_id, json_snapshot, policy_versions_hash) con:


## Control operativo verificable

- Owner: `Equipo internal-credit`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-INTERNALCRED-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/internal-credit/dominio-internal-credit-operacion`
  - `https://jira.aventide.gift/browse/OPS-INTERNALCRED-241`

## Trazabilidad
- Documento origen: `sistema-de-credito-interno-260207_0827.docx`
