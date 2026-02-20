# INVARIANTS · reservas-global

Reglas no negociables del dominio:
- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Contabilidad determinística: doble-entry, append-only, idempotencia estricta; sin ajustes por fuera.
- SYSTEM/WORKERS: ejecutan waterfall, postings ledger, y recovery cycles idempotentes.
- AUDIT/LEGAL: acceso de lectura a evidencia WORM (view_sensitive auditado).
- audit.view_sensitive (audit/legal con reason)
- IdempotencyGuard: un loss_case no se aplica dos veces; recovery cycle no duplica transferencias.
- 5.2 No retroactividad
- Las órdenes usan snapshot financiero inmutable; el sistema de reservas no “recalcula” órdenes pasadas.
- 5.3 Idempotencia estricta
- Recovery cycles con idempotency keys por (recovery_id, settlement_cycle_id). (Suposición operativa necesaria)

## Trazabilidad
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
