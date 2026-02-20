# STATE_MACHINE · reputation-seller

## Estados detectados/derivados
- 4) Flujos end-to-end (happy path + edge cases)
- Review entra a estado BLIND: no se publica hasta que:
- MODERATION_ACTION → actualiza estados de review (removed/hold).
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (seller reputation)
- Disputas (Saga)

## Transiciones y eventos de entrada/salida
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Eventos mínimos (seller reputation)
- Disputas (Saga)
- Solo “verdad verificada” cuenta: review y métricas derivan de eventos auditables (COMPLETED, outcomes, cancel_reason).
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que calcula y expone la Reputación del Seller (pública) y el Seller Score operativo (interno) usando únicamente “verdad verificada” (órdenes COMPLETED con PIN, outcomes de disputas, cancelaciones con culpa atribuida y señales auditables).

## Trazabilidad
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
