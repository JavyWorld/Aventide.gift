# INVARIANTS · disputes

Reglas no negociables del dominio:
- Sistema de Disputas v2.0 (Dispute Resolution + Saga determinística) — corregido y unificado
- ExternalCosts (processing/chargeback/dispute fee) como bucket formal (nunca ignorado),
- Ejecución mediante Saga idempotente con auditoría WORM obligatoria.
- Determinismo financiero: mismo caso + mismo snapshot + misma policy ⇒ mismos buckets.
- Contabilidad auditable: ledger append-only + evidencia WORM (paquete de disputa).
- Seguridad operativa: workers async, idempotencia por step, dedupe en provider, no doble refund/release.
- Cálculo de buckets desde order_financial_snapshot (inmutable) + policy.
- Auditoría WORM del paquete de evidencia y del settlement plan.
- disputes.audit.read (audit/finance/admin)
- AuditGuard (razón obligatoria + append-only)

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
