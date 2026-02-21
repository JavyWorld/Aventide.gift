# INVARIANTS · loyalty

Reglas no negociables del dominio:
- Ser auditable y reversible: ledger append-only por AP/FS con reversión ante refund/chargeback/disputa.
- Aplicación de FS en checkout como Fee Credit con límite: max_applied = platform_fee_amount (nunca más).
- Expiraciones determinísticas por lote/ventana (AP por lote; FS por ventana/mes).
- loyalty.ledger.read (finance/audit)
- AuditGuard (toda mutación crea ledger entry append-only)
- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- FS solo contra Platform Fee. Nunca taxes, processing, ops fee ni seller net.
- 6.2 loyalty_ledger (append-only, fuente de verdad)
- checkout_id (nullable; para apply idempotente)


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
