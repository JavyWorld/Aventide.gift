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
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Objetivos (duros):
- Backups verificables (no “backups que nunca se prueban”).
- RPO/RTO por criticidad (tiers) y por país (policy engine).


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

## Ownership & Escalation

- **Owner técnico:** `Equipo backup`
- **Owner negocio/regulatorio:** `Product + Compliance (backup)`
- **Rotación on-call:** `24x7 · primaria semanal · secundaria de respaldo`

### Matriz de severidad y tiempos de respuesta

| Severidad | Definición operativa | Ack inicial | Mitigación/contención | Actualizaciones |
| --- | --- | --- | --- | --- |
| **SEV0** | Caída total o riesgo crítico legal/financiero. | ≤ 5 min (24x7) | ≤ 30 min | Cada 15 min |
| **SEV1** | Degradación severa con impacto alto en transacciones/SLA. | ≤ 10 min (24x7) | ≤ 60 min | Cada 30 min |
| **SEV2** | Impacto parcial con workaround disponible. | ≤ 30 min (horario operativo + guardia) | ≤ 4 h | Cada 2 h |

> Este dominio adopta el estándar transversal de severidades, SLA operativos y handoff en `docs/02-DOMAINS/_shared/SEVERITY-SLA-HANDOFF-STANDARD.md`.

