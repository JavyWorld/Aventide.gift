# INVARIANTS · support

Reglas no negociables del dominio:
- Fuente de verdad: “Sistema de Soporte (Support OS) — Especificación técnica (Aventide Gift)”.Objetivo del rewrite: eliminar improvisación (“call center infinito”), separar correctamente Incidencias vivas vs Disputas post-entrega, prohibir montos manuales, hacer ejecución financiera determinista + auditable, y alinear permisos, jerarquía, órdenes (state machine), evidencia (Tridente) y ledger/snapshots.
- Evidencia (Audit Timeline + Tridente),
- Ejecución financiera (Saga + idempotencia + ledger/auditoría WORM).
- Evidencia manda: PoD (PIN+GPS+Foto) y timeline auditado para resolver objetivamente.
- Determinar la “verdad de entrega” fuera del sistema de Órdenes: Support OS consume la máquina de estados y evidencia, no la reemplaza.
- AuditGuard (razón obligatoria + WORM append-only)
- Usar solo si falla automático (ej. GPS malo) pero hay evidencia fuerte (foto válida). Lo ejecuta L3 y queda auditado.
- B3) Resolución expresada en buckets (siempre)
- Nunca “% bonitos” ni “monto libre”; Operación definida y validada es bucket contable:
- 5.1 Invariantes no negociables


## Control operativo verificable

- Owner: `Equipo support`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-SUPPORT-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/support/dominio-support-operacion`
  - `https://jira.aventide.gift/browse/OPS-SUPPORT-241`

## Trazabilidad
- Documento origen: `sistema-de-soporte-260207_0731.docx`
