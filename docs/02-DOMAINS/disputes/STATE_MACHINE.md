# STATE_MACHINE · disputes

## Estados detectados/derivados
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- Fuente de verdad: “Disputas y Resolución (Saga) — ESPECIFICACIÓN FINAL”.
- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Earned schedule del Platform Fee por estado real en la línea de tiempo.
- Orquestación Saga: refund, release/clawback, ledger adjustments, docs adjustments, trust/loyalty updates.
- Reglas fiscales específicas de cada país (se delegan a Facturación & Documentos, invocadas por evento).

## Transiciones y eventos de entrada/salida
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- Fuente de verdad: “Disputas y Resolución (Saga) — ESPECIFICACIÓN FINAL”.
- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Orquestación Saga: refund, release/clawback, ledger adjustments, docs adjustments, trust/loyalty updates.
- Reglas fiscales específicas de cada país (se delegan a Facturación & Documentos, invocadas por evento).
- SYSTEM/BOT: ejecuta saga, integra con provider, ledger, docs, trust, loyalty.
- disputes.saga.execute (system)
- 4.5 Ejecución Saga (steps idempotentes)

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
