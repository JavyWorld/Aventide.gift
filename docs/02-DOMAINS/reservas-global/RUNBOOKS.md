# RUNBOOKS · reservas-global

## Operación
- LedgerWORMGuard: toda operación se expresa como transacción doble-entry.
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas mínimas
- Caída de global_reserve_balance por debajo de threshold interno (policy). (Suposición; el doc lista “min coverage” como KPI/alert)
- “Overwrites” manuales al waterfall → corregido: orden fijo inalterable; no hay operación manual para cambiar layers.
- Mantener GLOBAL_RESERVE por encima de un umbral de cobertura para absorber tail-risk sin romper operación multi-país.

## Incidentes, rollback y backfill
- Sistema de Reserva Global v2.0 (GLOBAL_RESERVE + GLOBAL_RECOVERY + CRISIS)
- Fuentes de verdad:
- Waterfall Engine v1.0 (orden fijo de cobertura, loss_case_id, doble-entry, idempotencia, recovery obligatorio).
- Continuidad / Country Governance (VACANT/LOCKDOWN, break-glass, four-eyes, WORM).
- Reserva Nacional v2.0 (Layer 1, workflow, prohibiciones, observabilidad).
- Resumen (marco global de split/ledger/policies y controles críticos).
- 1) Definición y objetivos del sistema/módulo
- Definición: La Reserva Global es la “caja de último recurso” del ecosistema multi-país, implementada como una cuenta central de ledger (GLOBAL_RESERVE) que actúa como Layer 3 del Waterfall de pérdidas. Solo entra cuando Country Reserve y COL Liability no alcanzan, y cuando entra, crea automáticamente una obligación de recuperación contra el COL vía GLOBAL_RECOVERY_RECEIVABLE_{country} + recovery_account (set-off sobre earnings futuros), con guardrails.

## Trazabilidad
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
