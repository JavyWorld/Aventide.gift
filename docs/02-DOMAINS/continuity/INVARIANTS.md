# INVARIANTS · continuity

Reglas no negociables del dominio:
- Definición: Continuidad es el sistema que garantiza que el negocio no se detenga cuando falta (temporal o permanentemente) un rol crítico por país —especialmente COUNTRY_OPS_LEAD (COL)— y que las operaciones, el control de riesgo y el flujo financiero sigan funcionando bajo gobernanza, auditoría fuerte y políticas multi-país, sin introducir retroactividad en dinero (snapshot).
- No romper el core económico: fees snapshotteados, split automático (seller / Aventide / COL), ledger inmutable.
- Control de riesgo/abuso: acciones críticas requieren break-glass + 2FA + motivo + TTL + auditoría; y cuando sube el riesgo existe LOCKDOWN.
- Reglas de delegación temporal (Acting Ops Lead) con TTL + subset de permisos + auditoría.
- Workflow de desembolso desde COUNTRY_RESERVE con four-eyes + ejecución idempotente por worker + auditoría WORM.
- SYSTEM/WORKERS: ejecutan jobs idempotentes (reroute colas, payouts, holds, disbursements).
- AUDIT/LEGAL: lectura y export de evidencia, con registros de acceso sensible.
- audit.read / audit.view_sensitive (scoped; con reason)
- Trigger: revocación del rol/scope o offboarding del usuario (auditado).
- idempotency_key

## Trazabilidad
- Documento origen: `sistema-de-continuidad-v2-260207_1030.docx`
