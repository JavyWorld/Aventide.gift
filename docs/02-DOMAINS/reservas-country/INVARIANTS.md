# INVARIANTS · reservas-country

Reglas no negociables del dominio:
- Cubre pérdidas de forma determinística como primera capa del Waterfall (antes de cargar al COL o a la Reserva Global).
- Se gobierna con workflow formal (request/approve/execute), auditoría WORM y controles break-glass para cualquier movimiento sensible.
- Determinismo contable: todo movimiento es doble-entry ledger, idempotente y reproducible; cada pérdida tiene expediente único (loss_case_id).
- Cuentas COUNTRY_RESERVE_{country} en ledger y su routing como beneficiario cuando el país está VACANT/LOCKDOWN o cuando policy lo determine.
- Workflow de disbursement desde reserve con four-eyes y ejecución idempotente por worker.
- AUDIT/LEGAL: lectura y export de evidencia (WORM).
- reserve.balance.read{country} (finance/audit; COL opcional y limitado)
- reserve.loss_case.read (finance/audit)
- reserve.export.sensitive (audit/legal; VIEW_SENSITIVE auditado)
- LedgerWORMGuard: doble-entry, append-only, nada “por fuera” del ledger.

## Trazabilidad
- Documento origen: `sistema-de-reserva-nacional-260207_1031.docx`
