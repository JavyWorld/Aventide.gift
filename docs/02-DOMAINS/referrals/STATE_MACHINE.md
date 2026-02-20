# STATE_MACHINE · referrals

## Estados detectados/derivados
- Ser determinista: estados + ventana de atribución + hold windows + catálogo de reglas por país (server-driven).
- Ser reversible: toda recompensa registrada en ledger y reversible por eventos negativos.
- Flujo determinista de estados de atribución.
- BUYER (Referrer): comparte código/link y ve estados/rewards.
- 4) Flujos end-to-end (happy path + edge cases)
- estado ATTRIBUTED,

## Transiciones y eventos de entrada/salida
- Ser reversible: toda recompensa registrada en ledger y reversible por eventos negativos.
- Transición inmediata a PENDING_FIRST_ORDER.
- Si falla gating fuerte → FRAUD_BLOCKED (si evidencia fuerte) o REVOKED (si evento negativo).
- Cualquier evento negativo durante hold o post-grant:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- 7.1 Eventos analíticos (existentes en docs)
- Consumir eventos de REFUND_EXECUTED, CHARGEBACK_RECEIVED, DISPUTE_RESOLVED para reversión.
- Sistema de Referidos v2.0 (Referral Program) — corregido y unificado

## Trazabilidad
- Documento origen: `sistema-de-referido-260207_0826.docx`
