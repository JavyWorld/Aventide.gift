# API_CONTRACTS · moderation

## Endpoints y auth
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- Price anomaly: bloqueo si desviación absurda (lavado/error).
- 7) Eventos y triggers + idempotencia
- Idempotencia
- Sistema de Moderación v2.0 (Trust & Compliance Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Moderación y Cumplimiento (Trust & Compliance Engine) — Aventide Gift”.
- 1) Definición y objetivos del sistema/módulo

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- moderation.decision.publish/reject
- AUTO_REJECT
- REJECT (con motivo educativo)
- Leakage en imagen (teléfono/URL): AUTO_REJECT con mensaje educativo.
- Price anomaly: bloqueo si desviación absurda (lavado/error).

## Trazabilidad
- Documento origen: `sistema-de-moderacion-260207_0828.docx`
