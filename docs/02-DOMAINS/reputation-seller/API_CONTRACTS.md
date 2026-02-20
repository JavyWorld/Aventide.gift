# API_CONTRACTS · reputation-seller

## Endpoints y auth
- Métricas operativas seller: on-time (con tolerancia), cancelaciones at-fault, disputas perdidas at-fault, reclamos validados, chat response median.
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- Solo cancelaciones con cancel_reason atribuible al seller:OUT_OF_STOCK, CANNOT_FULFILL, NO_SHOW, SELLER_REQUESTED, ...
- Chat response time
- seller_metrics_rollup(seller_id, window(30|90|180), on_time_rate, cancel_at_fault_rate, disputes_lost_rate, complaint_rate, chat_median_response, updated_at)Índices:
- 7) Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que calcula y expone la Reputación del Seller (pública) y el Seller Score operativo (interno) usando únicamente “verdad verificada” (órdenes COMPLETED con PIN, outcomes de disputas, cancelaciones con culpa atribuida y señales auditables).

## Trazabilidad
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
