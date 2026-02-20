# API_CONTRACTS · billing-docs

## Endpoints y auth
- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- 3) Actores y permisos (RBAC) + guards
- Auth
- IdempotencyGuard (no duplicar emisión por reintentos)
- Webhook pago repetido: emisión idempotente por document_key; se retorna el doc existente.
- 5.6 Emisión idempotente (anti-duplicados)
- 7) Eventos y triggers + idempotencia
- 7.2 Idempotencia

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- errores de WORM/Object Lock (alto riesgo compliance)
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- 1) Definición y objetivos del sistema/módulo

## Trazabilidad
- Documento origen: `facturacion--documentos-260207_0805.docx`
