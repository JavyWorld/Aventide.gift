# DATA_CONTRACTS · loyalty

## Entidades y campos
- Sistema de Lealtad v2.0 (AP + FS “Fee Shields” + Ledger-first) — corregido y unificado
- “Fases de Desarrollo v1.1 — Loyalty (ledger-first) + eventos + modelo de datos”
- Ser auditable y reversible: ledger append-only por AP/FS con reversión ante refund/chargeback/disputa.
- loyalty.ledger.read (finance/audit)
- AuditGuard (toda mutación crea ledger entry append-only)
- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Soporta misiones “baratas” con caps: streak semanal, explorador por categoría, review verificada (con caps).Regla dura: Operación definida y validada earn adicional también pasa por ledger y caps para no romper presupuesto.
- Ledger: LOYALTY_POINTS_REDEEMED_TO_FEE_CREDIT (AP–, FS+).

## Constraints y claves de negocio
- Ser auditable y reversible: ledger append-only por AP/FS con reversión ante refund/chargeback/disputa.
- AuditGuard (toda mutación crea ledger entry append-only)
- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- 6.2 loyalty_ledger (append-only, fuente de verdad)
- checkout_id (nullable; para apply idempotente)
- unique por idempotencia:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia


## Control operativo verificable

- Owner: `Equipo loyalty`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-LOYALTY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/loyalty/dominio-loyalty-operacion`
  - `https://jira.aventide.gift/browse/OPS-LOYALTY-241`

## Trazabilidad
- Documento origen: `sistema-de-lealtad-260207_0817.docx`
