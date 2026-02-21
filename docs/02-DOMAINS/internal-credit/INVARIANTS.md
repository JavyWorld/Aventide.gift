# INVARIANTS · internal-credit

Reglas no negociables del dominio:
- Definición: “Créditos internos” son saldos no-cash gestionados por la plataforma y representados como pasivos (“Customer_Credit_Liability”), con ledger auditable y reglas estrictas de aplicabilidad. Se dividen por tipo porque no todos se usan igual.
- Integración determinística con la Torre de Precios: orden de cálculo fijo y no negociable.
- Auditabilidad total: balances nunca se “editan”; solo ledger entries (mint/spend/revoke/expire).
- ADMIN/FINANCE: auditoría, configuraciones por país, ajustes administrativos (si se permite).
- wallet.admin.adjust (solo si el proyecto permite ajustes admin; siempre auditado)
- wallet.audit.read (finance/audit)
- IdempotencyGuard (checkout_id/order_id/dispute_id)
- AuditGuard (ledger + snapshots)
- Origen permitido: solo por Soporte/Disputas (outcomes predefinidos).Uso: compensación no-cash para items (y delivery si policy), pero nunca taxes/ops/processing.
- Se crean ledger entries de SPEND (idempotente por checkout_id) y se produce promo_snapshot en la orden.


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
