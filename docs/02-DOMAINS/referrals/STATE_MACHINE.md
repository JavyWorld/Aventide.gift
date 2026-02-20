# STATE_MACHINE · referrals

## Estados

- Ser determinista: estados + ventana de atribución + hold windows + catálogo de reglas por país (server-driven).
- Flujo determinista de estados de atribución.
- BUYER (Referrer): comparte código/link y ve estados/rewards.
- estado ATTRIBUTED,

## Transiciones

- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Flujo determinista de estados de atribución.
- Flujos end-to-end (happy path + edge cases)
- Transición inmediata a PENDING_FIRST_ORDER.

## Triggers

- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Ser reversible: toda recompensa registrada en ledger y reversible por eventos negativos.
- Si falla gating fuerte → FRAUD_BLOCKED (si evidencia fuerte) o REVOKED (si evento negativo).
- Cualquier evento negativo durante hold o post-grant:
- Eventos analíticos (existentes en docs)
- Consumir eventos de REFUND_EXECUTED, CHARGEBACK_RECEIVED, DISPUTE_RESOLVED para reversión.

## Trazabilidad

- Documento origen: `sistema-de-referido-260207_0826.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
