# API_CONTRACTS · billing-docs

## Endpoints

- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- IdempotencyGuard (no duplicar emisión por reintentos)
- Webhook pago repetido: emisión idempotente por document_key; se retorna el doc existente.
- Emisión idempotente (anti-duplicados)
- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- errores de WORM/Object Lock (alto riesgo compliance)
- AuditGuard (evento append-only obligatorio)
- Payout aún no ejecutado pero orden completada: Statement final se emite con payout_status=PENDING y se emite Payout Statement cuando ocurra PAYOUT_SENT (evento separado). (Consistente con “docs por eventos” y con pipeline de pagos).
- docs_driver_api_latency_p95{country}

## Auth

- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- IdempotencyGuard (no duplicar emisión por reintentos)
- AuditGuard (evento append-only obligatorio)

## Códigos de error

- errores de WORM/Object Lock (alto riesgo compliance)

## Idempotency

- IdempotencyGuard (no duplicar emisión por reintentos)
- Webhook pago repetido: emisión idempotente por document_key; se retorna el doc existente.
- Emisión idempotente (anti-duplicados)
- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo billing-docs`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-BILLINGDOCS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/billing-docs/dominio-billing-docs-operacion`
  - `https://jira.aventide.gift/browse/OPS-BILLINGDOCS-241`

## Trazabilidad

- Documento origen: `facturacion--documentos-260207_0805.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
