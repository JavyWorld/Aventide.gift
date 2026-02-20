# reputation-seller

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye (Seller Only)
- Excluye
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)
- Sistema de Reputación v2.0 (Seller Only) — corregido y unificado

## Dependencias
- Integrarse sin romper invariantes: Órdenes (solo COMPLETED), Disputas (outcomes), Moderación (review/media), Búsqueda/Ranking (performance multipliers) y Pagos (rolling reserve/freeze por policy, no por acción manual).
- Contratos de integración con Búsqueda: multiplicadores por score y penalizaciones activas.
- Motor de Moderación y su cola (se consume como dependencia).
- Review bombing: ráfagas de 1 estrella (anómalas) → hold + señal a moderación + ajuste de Buyer-side (fuera de este módulo) y protección a score (ver 5.7 “integridad”).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

## Trazabilidad
- Documento origen: `sistema-de-reputacion-seller-260207_0839.docx`
- Título extraído: "Sistema de Reputación v2.0 (Seller Only) — corregido y unificado".
