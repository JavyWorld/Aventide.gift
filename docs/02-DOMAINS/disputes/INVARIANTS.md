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


## Control operativo verificable

- Owner: `Equipo disputes`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-DISPUTES-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/disputes/dominio-disputes-operacion`
  - `https://jira.aventide.gift/browse/OPS-DISPUTES-241`

## Trazabilidad
- Documento origen: `disputas-260207_0809.docx`
