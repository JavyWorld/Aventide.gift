# reputation-buyer

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- Integración consistente con Órdenes, Disputas, Moderación y Búsqueda: el score define fricción inteligente y límites (no mueve dinero directamente).
- 2) Alcance (incluye / excluye)
- Incluye
- Acciones por nivel: límites de cancelación tardía, fricción adicional en alto valor, hold de reviews si riesgo, verificación adicional, suspensión por chargebacks.
- Excluye

## Dependencias
- Integración consistente con Órdenes, Disputas, Moderación y Búsqueda: el score define fricción inteligente y límites (no mueve dinero directamente).
- Buyer Reviews (reviews_buyer) como insumo de integridad (no “rating público” del buyer).
- Motor completo de Moderación (solo integración).
- 4.4 Integridad de reviews (buyer)
- violaciones moderación⇒ baja review_integrity_score, puede poner review_hold temporal y envía CHAT_FLAGGED/MODERATION_ACTION como señales.

## Trazabilidad
- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
- Título extraído: "Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado".
