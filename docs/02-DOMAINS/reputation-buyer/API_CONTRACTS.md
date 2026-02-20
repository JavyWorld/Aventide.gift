# API_CONTRACTS · reputation-buyer

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- Duplicados: idempotencia por (buyer_id, event_id) en rollups.
- 7) Eventos y triggers + idempotencia
- Idempotencia
- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Reputación v2.0 (Buyer Only) — corregido y unificado
- Fuente de verdad: “Sistema de Reputación (Trust Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que calcula un Buyer Trust Score (0–100) y lo expone al seller como Trust Level + Trust Badge (semi-visible) para equilibrar privacidad (incl. “Admirador Secreto”) con seguridad operacional. No es público ni “humilla” al buyer; es un control de riesgo para sellers y plataforma.

## Trazabilidad
- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
