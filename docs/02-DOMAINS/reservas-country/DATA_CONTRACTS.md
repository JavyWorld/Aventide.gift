# DATA_CONTRACTS · reservas-country

## Entidades y campos
- “waterfall-engine-v10-260207_0941” (Waterfall de pérdidas, layers, loss_case, recovery al COL, guardrails, ledger doble-entry).
- Definición: La Reserva Nacional (por país) es una cuenta de ledger (COUNTRY_RESERVE_{country}) de custodia corporativa que:
- Determinismo contable: Operación definida y validada movimiento es doble-entry ledger, idempotente y reproducible; cada pérdida tiene expediente único (loss_case_id).
- Cuentas COUNTRY_RESERVE_{country} en ledger y su routing como beneficiario cuando el país está VACANT/LOCKDOWN o cuando policy lo determine.
- SYSTEM/WORKERS: ejecutan movimientos de ledger, aplican waterfall, corren recovery cycles.
- LedgerWORMGuard: doble-entry, append-only, nada “por fuera” del ledger.
- Nuevas órdenes snapshottean ops_fee_beneficiary_type = COUNTRY_RESERVE.
- Ledger postea el monto correspondiente al bucket ops a COUNTRY_RESERVE_{country} (append-only).

## Constraints y claves de negocio
- Determinismo contable: Operación definida y validada movimiento es doble-entry ledger, idempotente y reproducible; cada pérdida tiene expediente único (loss_case_id).
- Workflow de disbursement desde reserve con four-eyes y ejecución idempotente por worker.
- Gestión completa de disputas/chargebacks (eso es Disputas); este sistema solo recibe el “net_loss_amount” confirmado vía Loss Intake.
- LedgerWORMGuard: doble-entry, append-only, nada “por fuera” del ledger.
- IdempotencyGuard: mismo evento/pérdida no se aplica dos veces.
- Ledger postea el monto correspondiente al bucket ops a COUNTRY_RESERVE_{country} (append-only).
- Worker ejecuta idempotente:
- Auditoría WORM: request/approve/execute con hashes/evidencia.


## Control operativo verificable

- Owner: `Equipo reservas-country`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-RESERVASCOUN-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/reservas-country/dominio-reservas-country-operacion`
  - `https://jira.aventide.gift/browse/OPS-RESERVASCOUN-241`

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
