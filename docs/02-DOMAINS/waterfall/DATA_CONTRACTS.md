# DATA_CONTRACTS · waterfall

## Entidades y campos
- movimientos ledger
- No retroactividad: cada orden usa su snapshot financiero inmutable.
- Doble-entry ledger obligatorio: nada se “ajusta por fuera”.
- Tabla loss_cases
- Tabla waterfall_applications
- ledger_txn_id
- Tabla recovery_accounts
- Tabla col_rate_modes

## Constraints y claves de negocio
- Toda pérdida tiene expediente único (loss_case_id) con trazabilidad completa de:
- Idempotencia estricta: mismo evento no puede cobrarse dos veces.
- fraude confirmado
- hash de evidencia
- evidence_hash
- score transaccional previo a confirmación
- idempotency-key
- Brutal, mi Jav. Vamos a dejar ese Waterfall de pérdidas como tanque de guerra empresarial: claro, auditable, difícil de explotar y listo para implementación real. ⚙️🛡️


## Control operativo verificable

- Owner: `Equipo waterfall`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-WATERFALL-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/waterfall/dominio-waterfall-operacion`
  - `https://jira.aventide.gift/browse/OPS-WATERFALL-241`

## Trazabilidad
- Documento origen: `waterfall-engine-v10-260207_0941.docx`
