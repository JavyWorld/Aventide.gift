# RUNBOOKS · backup

## Operación
- DR real con failover controlado y drills periódicos.
- Resolver discrepancias de dinero automáticamente (solo ejecuta reconciliación/alerta; el core decide la acción).
- BackupAuditor: lee reportes, evidencia de backups, pruebas y DR drills (no restaura).
- SYSTEM/BOT: jobs automáticos, smoke tests, monitor de replicación, enforcement de retención.
- Inconsistencias: backup se marca FAILED y dispara alerta “restore smoketest” obligatorio antes de declarar OK.
- 4.5 Restauración (runbooks obligatorios)

## Incidentes, rollback y backfill
- Rehabilitar dinero solo si reconciliación OK + auditoría del incidente registrada.
- Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado
- Fuente de verdad: “Sistema de Copia de Seguridad (Backups + Continuidad + DR)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Objetivos (duros):
- Backups verificables (no “backups que nunca se prueban”).
- RPO/RTO por criticidad (tiers) y por país (policy engine).

## Trazabilidad
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
