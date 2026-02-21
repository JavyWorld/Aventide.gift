# INVARIANTS · payments

Reglas no negociables del dominio:
- Registrar Operación definida y validada en un ledger interno inmutable,
- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- “Soporte no inventa montos”: outcomes → buckets → cálculo determinístico → saga.
- Split de fondos por orden y ledger inmutable como fuente contable.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- ledger.read (finance/audit)
- AuditGuard (razón obligatoria en acciones sensibles)
- valida hash del PIN (nunca PIN plano),
- valida estado e idempotencia.


## Control operativo verificable

- Owner: `Equipo payments`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PAYMENTS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/payments/dominio-payments-operacion`
  - `https://jira.aventide.gift/browse/OPS-PAYMENTS-241`

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
