# DATA_CONTRACTS · disputes

## Entidades y campos
- Determinismo financiero: mismo caso + mismo snapshot + misma policy ⇒ mismos buckets.
- Contabilidad auditable: ledger append-only + evidencia WORM (paquete de disputa).
- Cálculo de buckets desde order_financial_snapshot (inmutable) + policy.
- Orquestación Saga: refund, release/clawback, ledger adjustments, docs adjustments, trust/loyalty updates.
- SYSTEM/BOT: ejecuta saga, integra con provider, ledger, docs, trust, loyalty.
- order_financial_snapshot inmutable,
- LEDGER_ADJUSTMENTS (append-only)
- 5.1 Snapshot financiero de la orden (SSOT)

## Constraints y claves de negocio
- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Contabilidad auditable: ledger append-only + evidencia WORM (paquete de disputa).
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- AuditGuard (razón obligatoria + append-only)
- Se crea dispute_case y dispute_events (append-only).
- Genera un settlement_plan idempotente (hash del input).
- 4.5 Ejecución Saga (steps idempotentes)
- LEDGER_ADJUSTMENTS (append-only)

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
