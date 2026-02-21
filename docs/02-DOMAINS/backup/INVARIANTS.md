# INVARIANTS · backup

Reglas no negociables del dominio:
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Backups verificables (no “backups que nunca se prueban”).
- Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.
- Ledger/Finanzas: movimientos, fees, payouts, refunds, disputas, snapshots financieros (inmutables).
- Observabilidad y Auditoría: logs técnicos, auditoría de acciones, trazas (según retención).
- BackupAuditor: lee reportes, evidencia de backups, pruebas y DR drills (no restaura).
- FINANCE/AUDIT/LEGAL: lectura de exports y bóveda fiscal (auditado).
- backup.run.entity_restore (support/backupoperator, auditado)
- backup.reports.read (backupauditor)
- BreakGlassGuard (dual approval + logging inmutable)


## Control operativo verificable

- Owner: `Equipo backup`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-BACKUP-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/backup/dominio-backup-operacion`
  - `https://jira.aventide.gift/browse/OPS-BACKUP-241`

## Trazabilidad
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
