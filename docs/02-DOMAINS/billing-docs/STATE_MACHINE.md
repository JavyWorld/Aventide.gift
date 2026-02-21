# STATE_MACHINE · billing-docs

## Estados

- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- AuditGuard (evento append-only obligatorio)

## Transiciones

- IdempotencyGuard (no duplicar emisión por reintentos)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Triggers

- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- Eventos y triggers + idempotencia
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Emisión automática de documentos por eventos del ciclo de orden/pagos: PAID_IN_ESCROW, COMPLETED, REFUND, DISPUTE_OUTCOME.
- SYSTEM/BOT: generación automática por eventos, almacenamiento, envío de notificaciones.
- AuditGuard (evento append-only obligatorio)
- Evento PAID_IN_ESCROW llega a Document Service.
- Payout aún no ejecutado pero orden completada: Statement final se emite con payout_status=PENDING y se emite Payout Statement cuando ocurra PAYOUT_SENT (evento separado). (Consistente con “docs por eventos” y con pipeline de pagos).


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
