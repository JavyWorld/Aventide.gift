# DATA_CONTRACTS · referrals

## Entidades y campos
- Definición: Programa de adquisición y activación que atribuye un referrer (buyer existente) a un referred (buyer nuevo) y paga recompensas solo después de una “primera orden válida”, usando AP (Aventide Points) y opcionalmente FS (Fee Shields), con ledger auditable y reversión por fraude/refund/chargeback/disputa.
- Ser reversible: toda recompensa registrada en ledger y reversible por eventos negativos.
- SYSTEM/BOT: atribución, evaluación de primera orden, holds, aprobación, ledger, reversión.
- referrals.ledger.read (finance/audit)
- Colisión de código: regenerar (unique constraint).
- 4.5 Aprobación y pago de recompensas (ledger)
- Se crean ledger entries (AP):
- Campos mínimos (default del doc):

## Constraints y claves de negocio
- Generación de referral_code único por buyer (AG-XXXXXX).
- IdempotencyGuard (no duplica atribución ni grants)
- Al crear buyer se asigna referral_code único: AG-XXXXXX.
- Colisión de código: regenerar (unique constraint).
- fraude confirmado⇒ status = REVOKED y ledger de reversión.
- unique(referred_id) WHERE status IN (ATTRIBUTED,PENDING_FIRST_ORDER,FIRST_ORDER_COMPLETED,HOLDING,APPROVED) (o único absoluto y solo 1 fila con updates)
- 6.4 referral_events (append-only)
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia

## Trazabilidad
- Documento origen: `sistema-de-referido-260207_0826.docx`
