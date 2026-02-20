# INVARIANTS · reputation-buyer

Reglas no negociables del dominio:
- Ser explicable y auditable: score con subscores, historial diario y reason codes.
- buyer.trust.penalties.enforce (system/admin; auditado)
- buyer.trust.audit.read (audit/admin)
- AuditGuard (cambios de score/penalty/badge)
- Duplicados: idempotencia por (buyer_id, event_id) en rollups.
- “Eventos tardíos” (chargeback meses después): recalcula ventanas afectadas y emite BUYER_TRUST_RECALCULATED con audit trail.
- Corrección de incoherencia: estas acciones no se aplican “a mano”; se expresan como policy flags (limits/friction) consumidos por Órdenes/Checkout/Moderación, con auditoría.
- penalty_events(entity_type=Buyer, entity_id, penalty_code, severity, reason_codes[], starts_at, ends_at, created_by(AUTO|ADMIN), audit_ref)
- 7) Eventos y triggers + idempotencia
- Idempotencia

## Trazabilidad
- Documento origen: `sistema-de-reputacion-buyer-260207_0839.docx`
