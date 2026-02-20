# RUNBOOKS · reputation-seller

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Aumento de cancel_at_fault por país/ciudad (operación rota)
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo

## Incidentes, rollback y backfill
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que calcula y expone la Reputación del Seller (pública) y el Seller Score operativo (interno) usando únicamente “verdad verificada” (órdenes COMPLETED con PIN, outcomes de disputas, cancelaciones con culpa atribuida y señales auditables).
- Objetivos:
- Reducir riesgo/fraude sin matar conversión (evitar hundir o inflar sellers con pocas reviews).
- Ser resistente a abuso: anti-represalias (blind reviews), anti-extorsión y anti-review bombing.
- Ser explicable y operable: historial diario con “drivers” (qué lo sube/baja) y penalizaciones progresivas.

## Trazabilidad
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
