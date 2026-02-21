# EVENT_CONTRACTS · billing-docs

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- Emisión automática de documentos por eventos del ciclo de orden/pagos: PAID_IN_ESCROW, COMPLETED, REFUND, DISPUTE_OUTCOME.
- SYSTEM/BOT: generación automática por eventos, almacenamiento, envío de notificaciones.
- AuditGuard (evento append-only obligatorio)
- Evento PAID_IN_ESCROW llega a Document Service.
- Payout aún no ejecutado pero orden completada: Statement final se emite con payout_status=PENDING y se emite Payout Statement cuando ocurra PAYOUT_SENT (evento separado). (Consistente con “docs por eventos” y con pipeline de pagos).
- 6.3 document_events (append-only)
- document_events
- event_id


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
