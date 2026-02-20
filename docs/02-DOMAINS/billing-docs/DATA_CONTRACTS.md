# DATA_CONTRACTS · billing-docs

## Entidades y campos
- Definición: Sistema que genera, numera, sella, almacena, distribuye y audita documentos fiscales/legales derivados de una orden y sus eventos (pago, release, refund, disputa), con reglas multi-país. El documento es un artefacto sellado: Snapshot + Plantilla + Driver País, no una “vista” recalculada.
- Compatibilidad total con Motor Financiero/Pagos: la verdad financiera viene del snapshot; los documentos no recalculan.
- Multi-país real: soportar numeración/series, campos y facturación electrónica según país.
- Cálculo financiero: pertenece a Pagos/Motor Financiero; aquí solo se consume order_financial_snapshot.
- Evidencia forense completa (Black Box): Facturación referencia ledger_evidence_pack, pero no reemplaza Auditoría WORM del proyecto.
- Carga order_financial_snapshot + party snapshots (buyer/seller/ops/platform).
- valida campos fiscales (tax_id, address, etc.).
- Perfil fiscal incompleto (faltan tax_id/address): bloquear emisión y abrir tarea/CTA al usuario (y dejar audit trail de “issue_failed_profile_missing”). (No contradice doc: el sistema define perfil fiscal y drivers que exigen campos).

## Constraints y claves de negocio
- Anti-tampering y auditabilidad: PDFs + JSON canónico guardados en bóveda con WORM/Object Lock y hash.
- Drivers fiscales por país (plugins) que encapsulan numeración, firma electrónica/timbrado y reglas fiscales locales.
- Auditoría append-only: emisión, reenvío, descarga, anulación, reemplazo, notas de crédito.
- IdempotencyGuard (no duplicar emisión por reintentos)
- AuditGuard (evento append-only obligatorio)
- Document Vault guarda con hash SHA-256 + firma interna.
- Webhook pago repetido: emisión idempotente por document_key; se retorna el doc existente.
- firma electrónica/timbrado (si aplica),

## Trazabilidad
- Documento origen: `facturacion--documentos-260207_0805.docx`
