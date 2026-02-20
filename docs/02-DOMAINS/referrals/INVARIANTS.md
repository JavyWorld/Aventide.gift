# INVARIANTS · referrals

Reglas no negociables del dominio:
- Definición: Programa de adquisición y activación que atribuye un referrer (buyer existente) a un referred (buyer nuevo) y paga recompensas solo después de una “primera orden válida”, usando AP (Aventide Points) y opcionalmente FS (Fee Shields), con ledger auditable y reversión por fraude/refund/chargeback/disputa.
- Ser determinista: estados + ventana de atribución + hold windows + catálogo de reglas por país (server-driven).
- Flujo determinista de estados de atribución.
- “Créditos internos” (BSC/GCC) como sistema general de wallets: aquí solo se usa AP y opcional FS (y siempre bajo reglas de FS).
- referrals.ledger.read (finance/audit)
- IdempotencyGuard (no duplica atribución ni grants)
- AuditGuard (toda acción sensible se registra)
- gating mínimo para liberar FS y para referrer siempre:
- y FS queda en PENDING_BUDGET (sub-estado interno) o se omite (según policy país; se define en policy).Suposición: el documento define el budget pero no el comportamiento exacto al agotarse; se mantiene determinismo via policy.
- Una vez que el referred hace FIRST_ORDER_COMPLETED, la atribución queda “locked” (no más overwrite).Suposición: el doc no define explícitamente el lock post-primera orden, pero es consistente con la máquina de estados determinista y evita manipulación.

## Trazabilidad
- Documento origen: `sistema-de-referido-260207_0826.docx`
