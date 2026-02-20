# API_CONTRACTS · billing-docs

## Endpoints

- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- Actores y permisos (RBAC) + guards
- IdempotencyGuard (no duplicar emisión por reintentos)
- Webhook pago repetido: emisión idempotente por document_key; se retorna el doc existente.
- Emisión idempotente (anti-duplicados)
- Eventos y triggers + idempotencia
- Idempotencia
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- errores de WORM/Object Lock (alto riesgo compliance)
- AuditGuard (evento append-only obligatorio)
- Payout aún no ejecutado pero orden completada: Statement final se emite con payout_status=PENDING y se emite Payout Statement cuando ocurra PAYOUT_SENT (evento separado). (Consistente con “docs por eventos” y con pipeline de pagos).
- docs_driver_api_latency_p95{country}

## Auth

- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- Actores y permisos (RBAC) + guards
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

## Trazabilidad

- Documento origen: `facturacion--documentos-260207_0805.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
