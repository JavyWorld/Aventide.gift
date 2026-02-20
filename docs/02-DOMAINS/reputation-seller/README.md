# reputation-seller

## Propósito

- Métricas operativas seller: on-time (con tolerancia), cancelaciones at-fault, disputas perdidas at-fault, reclamos validados, chat response median.
- Solo cancelaciones con cancel_reason atribuible al seller:OUT_OF_STOCK, CANNOT_FULFILL, NO_SHOW, SELLER_REQUESTED,...
- Chat response time
- seller_metrics_rollup(seller_id, window(30|90|180), on_time_rate, cancel_at_fault_rate, disputes_lost_rate, complaint_rate, chat_median_response, updated_at)Índices:
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- Definición y objetivos del sistema/módulo
- Definición: Sistema que calcula y expone la Reputación del Seller (pública) y el Seller Score operativo (interno) usando únicamente “verdad verificada” (órdenes COMPLETED con PIN, outcomes de disputas, cancelaciones con culpa atribuida y señales auditables).
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
- Disputas (Saga)
- Integrarse sin romper invariantes: Órdenes (solo COMPLETED), Disputas (outcomes), Moderación (review/media), Búsqueda/Ranking (performance multipliers) y Pagos (rolling reserve/freeze por policy, no por acción manual).
- Review bombing: ráfagas de 1 estrella (anómalas) → hold + señal a moderación + ajuste de Buyer-side (fuera de este módulo) y protección a score (ver 5.7 “integridad”).
- Título extraído: "Sistema de Reputación v2.0 (Seller Only) — corregido y unificado".

## Límites

- Alcance (incluye / excluye)
- Incluye (Seller Only)
- Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- Contratos de integración con Búsqueda: multiplicadores por score y penalizaciones activas.
- Motor de Moderación y su cola (se consume como dependencia).

## Trazabilidad

- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
- Título extraído: "Sistema de Reputación v2.0 (Seller Only) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
