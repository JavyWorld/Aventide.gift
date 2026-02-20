# INVARIANTS · billing-docs

Reglas no negociables del dominio:
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Anti-tampering y auditabilidad: PDFs + JSON canónico guardados en bóveda con WORM/Object Lock y hash.
- Consistencia con descuentos: Fee Credits solo reducen platform_fee y nunca tocan seller_net / ops_fee / processing / taxes.
- Distribución controlada: Document Center + email/link seguro + panel, con RBAC y eventos auditados.
- Auditoría append-only: emisión, reenvío, descarga, anulación, reemplazo, notas de crédito.
- Evidencia forense completa (Black Box): Facturación referencia ledger_evidence_pack, pero no reemplaza Auditoría WORM del proyecto.
- SUPER_ADMIN / FINANCE_ADMIN: emisión “on-demand”, correcciones controladas, auditorías.
- docs.audit.read (audit/finance/admin)
- IdempotencyGuard (no duplicar emisión por reintentos)
- AuditGuard (evento append-only obligatorio)

## Trazabilidad
- Documento origen: `facturacion--documentos-260207_0805.docx`
