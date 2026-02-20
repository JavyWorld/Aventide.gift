# STATE_MACHINE · reputation-buyer

## Estados detectados/derivados
- BUYER: crea órdenes, puede reseñar; ve su estado básico (sin revelar score exacto si no se desea).
- SYSTEM/BOT: calcula score, aplica fricción y límites, genera eventos, mantiene historial.
- 4) Flujos end-to-end (happy path + edge cases)
- 4.1 Cálculo continuo por eventos (event-driven)
- Eventos relevantes actualizan buyer_metrics_rollup (ventanas 30/90/180) y luego recalculan score:
- “Eventos tardíos” (chargeback meses después): recalcula ventanas afectadas y emite BUYER_TRUST_RECALCULATED con audit trail.

## Transiciones y eventos de entrada/salida
- SYSTEM/BOT: calcula score, aplica fricción y límites, genera eventos, mantiene historial.
- 4.1 Cálculo continuo por eventos (event-driven)
- Eventos relevantes actualizan buyer_metrics_rollup (ventanas 30/90/180) y luego recalculan score:
- “Eventos tardíos” (chargeback meses después): recalcula ventanas afectadas y emite BUYER_TRUST_RECALCULATED con audit trail.
- 7) Eventos y triggers + idempotencia
- Eventos mínimos (buyer trust)
- Eventos derivados:
- eventos de cancelación tardía / PIN withheld, etc.

## Trazabilidad
- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
