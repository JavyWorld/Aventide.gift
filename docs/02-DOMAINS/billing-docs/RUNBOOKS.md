# RUNBOOKS · billing-docs

## Operación
- 9) Observabilidad (logs, métricas, alertas, SLOs) — aplicado a Facturación
- Alertas mínimas
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.

## Incidentes, rollback y backfill
- IdempotencyGuard (no duplicar emisión por reintentos)
- Reintentos devuelven el doc existente; no se crea uno nuevo.
- Duplicación de facturas por reintentos → eliminado: document_key idempotente + series con locking.
- Sistema: Facturación & Documentos v2.0 (Billing Engine + Document Vault) — corregido y unificado
- Fuente de verdad: “Sistema: Facturación & Documentos (Legal/Fiscal)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Objetivos:

## Trazabilidad
- Documento origen: `facturacion--documentos-260207_0805.docx`
