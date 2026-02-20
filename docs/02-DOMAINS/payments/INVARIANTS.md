# INVARIANTS · payments

Reglas no negociables del dominio:
- Registrar todo en un ledger interno inmutable,
- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- “Soporte no inventa montos”: outcomes → buckets → cálculo determinístico → saga.
- Split de fondos por orden y ledger inmutable como fuente contable.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- ledger.read (finance/audit)
- AuditGuard (razón obligatoria en acciones sensibles)
- valida hash del PIN (nunca PIN plano),
- valida estado e idempotencia.

## Trazabilidad
- Documento origen: `sistema-de-pagos-260207_0800.docx`
