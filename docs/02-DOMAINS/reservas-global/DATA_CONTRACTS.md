# DATA_CONTRACTS · reservas-global

## Entidades y campos
- Resumen (marco global de split/ledger/policies y controles críticos).
- Definición: La Reserva Global es la “caja de último recurso” del ecosistema multi-país, implementada como una cuenta central de ledger (GLOBAL_RESERVE) que actúa como Layer 3 del Waterfall de pérdidas. Solo entra cuando Country Reserve y COL Liability no alcanzan, y cuando entra, crea automáticamente una obligación de recuperación contra el COL vía GLOBAL_RECOVERY_RECEIVABLE_{country} + recovery_account (set-off sobre earnings futuros), con guardrails.
- Cuenta de ledger GLOBAL_RESERVE y su uso como Layer 3 del Waterfall.
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- LedgerWORMGuard: toda operación se expresa como transacción doble-entry.
- Global Reserve (Layer 3): post_ledger(GLOBAL_RESERVE → LOSS_EXPENSE_{country}, c)
- post_ledger(GLOBAL_RECOVERY_RECEIVABLE_{country} → GLOBAL_RESERVE, c)
- Moneda: si el ledger es multi-currency, la política de FX/settlement no está definida en los docs; se mantiene en currency del caso y se reporta por currency (sin inventar conversión). (Suposición mínima)

## Constraints y claves de negocio
- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.
- 5.3 Idempotencia estricta
- Recovery cycles con idempotency keys por (recovery_id, settlement_cycle_id). (Suposición operativa necesaria)
- loss_case_id, country_code, col_id, loss_type, gross_amount, recoveries_external, net_loss_amount, currency, source_ref, evidence_hash, status, timestamps.
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
