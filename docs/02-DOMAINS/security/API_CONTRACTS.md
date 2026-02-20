# API_CONTRACTS · security

## Endpoints y auth
- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Gobernanza fuerte: RBAC + scopes geográficos + kill switches + auditoría WORM.
- Perímetro (WAF/DDoS/CDN + rate limiting) y seguridad de API (gateway).
- Identidad/autenticación (Firebase/Auth0) + sesión/JWT propio con claims + RBAC.
- Implementación específica de proveedores (p.ej. reglas exactas de Rapyd/otros) más allá de los invariantes (idempotencia, dedupe, firma, etc.).
- 3) Actores y permisos (RBAC) + guards
- SYSTEM/BOT (workers, webhook handlers).
- Claims de rol viajan en JWT; backend aplica middleware por permiso (no UI).

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Ops Lead puede forzar finalización solo por error técnico, exigiendo motivo+evidencia y auditándolo.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Seguridad v2.0 (Defense in Depth + Money/Delivery Zero-Trust) — corregido y unificado
- Fuente de verdad: “Sistema de Seguridad (Aventide Gift)”.

## Trazabilidad
- Documento origen: `sistema-de-seguridad-260207_0756.docx`
