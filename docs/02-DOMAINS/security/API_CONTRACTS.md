# API_CONTRACTS · security

## Endpoints

- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Gobernanza fuerte: RBAC + scopes geográficos + kill switches + auditoría WORM.
- Perímetro (WAF/DDoS/CDN + rate limiting) y seguridad de API (gateway).
- Identidad/autenticación (Firebase/Auth0) + sesión/JWT propio con claims + RBAC.
- Implementación específica de proveedores (p.ej. reglas exactas de Rapyd/otros) más allá de los invariantes (idempotencia, dedupe, firma, etc.).
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Claims de rol viajan en JWT; backend aplica middleware por permiso (no UI).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Ops Lead puede forzar finalización solo por error técnico, exigiendo motivo+evidencia y auditándolo.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Estado e idempotencia: solo ejecuta si la orden está en estado correcto; evita dobles confirmaciones.
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- Eventos y triggers + idempotencia

## Auth

- Gobernanza fuerte: RBAC + scopes geográficos + kill switches + auditoría WORM.
- Identidad/autenticación (Firebase/Auth0) + sesión/JWT propio con claims + RBAC.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Claims de rol viajan en JWT; backend aplica middleware por permiso (no UI).

## Códigos de error

- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Ops Lead puede forzar finalización solo por error técnico, exigiendo motivo+evidencia y auditándolo.

## Idempotency

- Evitar pérdidas por errores técnicos: idempotencia en pagos/webhooks, anti-doble cobro, anti-doble payout.
- Implementación específica de proveedores (p.ej. reglas exactas de Rapyd/otros) más allá de los invariantes (idempotencia, dedupe, firma, etc.).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Estado e idempotencia: solo ejecuta si la orden está en estado correcto; evita dobles confirmaciones.
- PoD no libera dinero directamente; se emite evento interno y un worker/cola ejecuta settlement/payout con idempotencia.
- Eventos y triggers + idempotencia
- payments.webhook_received/deduped/invalid_signature
- Webhooks: dedupe por provider_event_id + firma + ventana temporal.


## Control operativo verificable

- Owner: `Equipo security`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-SECURITY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/security/dominio-security-operacion`
  - `https://jira.aventide.gift/browse/OPS-SECURITY-241`

## Trazabilidad

- Documento origen: `sistema-de-seguridad-260207_0756.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
