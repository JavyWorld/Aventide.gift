### Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado

**Fuente de verdad:** “Sistema de Copia de Seguridad (Backups + Continuidad + DR)”.

---

## 1) Definición y objetivos del sistema/módulo

**Definición:** Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando **retenciones legales multi-país** y reglas críticas del core: **ledger append-only**, **documentos WORM**, **snapshots financieros/fiscales**, y **crypto-shredding** sin “revivir” datos destruidos por política.

**Objetivos (duros):**

1. Backups verificables (no “backups que nunca se prueban”).

2. RPO/RTO por criticidad (tiers) y por país (policy engine).

3. DR real con failover controlado y drills periódicos.

4. Inmutabilidad de evidencia fiscal/legal (WORM) + replicación sin romper residencia de datos.

5. Restauración idempotente del Tier 0 (dinero): sin duplicar cobros/payouts/refunds.

---

## 2) Alcance (incluye / excluye)

### Incluye (qué protegemos)

- **DB Operativa (OLTP):** usuarios, sellers, catálogo, órdenes, mensajería, soporte, reputación, cobertura, disponibilidad, políticas por país.

- **Ledger/Finanzas:** movimientos, fees, payouts, refunds, disputas, snapshots financieros (inmutables).

- **Documentos legales/fiscales:** facturas, recibos, notas crédito, PoD y JSON/hash de snapshot en WORM/Object Lock.

- **Archivos no-WORM:** imágenes de producto, adjuntos chat/soporte, evidencias operativas.

- **Observabilidad y Auditoría:** logs técnicos, auditoría de acciones, trazas (según retención).

- **Analítica:** warehouse/event store (si existe) con RPO/RTO distinto.

### Excluye

- Redefinir retenciones legales específicas por país (el sistema asume “policy por país”).

- Resolver discrepancias de dinero automáticamente (solo ejecuta reconciliación/alerta; el core decide la acción).

---

## 3) Actores y permisos (RBAC) + guards

### 3.1 Actores

- **BackupOperator:** ejecuta restores y operaciones de DR (no lee data sensible sin necesidad).

- **BackupAuditor:** lee reportes, evidencia de backups, pruebas y DR drills (no restaura).

- **SecurityAdmin:** gestiona llaves/keys en KMS y crypto-shredding.

- **COUNTRY_OPS_LEAD:** configura policy por país (tiers/RPO/RTO/retención), ve salud.

- **SYSTEM/BOT:** jobs automáticos, smoke tests, monitor de replicación, enforcement de retención.

- **FINANCE/AUDIT/LEGAL:** lectura de exports y bóveda fiscal (auditado).

### 3.2 Permisos mínimos

- `backup.policy.read/write` (ops lead scoped)

- `backup.run.pitr_restore` (backupoperator)

- `backup.run.partial_restore` (backupoperator)

- `backup.run.entity_restore` (support/backupoperator, auditado)

- `backup.reports.read` (backupauditor)

- `backup.export.pack.create` (legal/finance/support)

- `backup.export.pack.download` (mfa + expiración)

- `kms.keys.manage` (securityadmin)

- `backup.break_glass` (dual approval + razón)

### 3.3 Guards

1. AuthGuard

2. ScopeGuard (país/cluster)

3. BreakGlassGuard (dual approval + logging inmutable)

4. KeyGuard (no restore sin llaves correctas; separación de llaves por clase)

5. WORMGuard (documentos emitidos no modificables/no borrables antes de retención)

6. AuditGuard (restore/export/lecturas bóveda y evidencias)

---

## 4) Flujos end-to-end (happy path + edge cases)

### 4.1 Backups OLTP (PITR + snapshots + export lógico)

**Happy path**

1. PITR continuo: WAL/journal se archiva a storage seguro.

2. Snapshot físico diario.

3. Export lógico semanal (SQL/Parquet) como último recurso multi-cloud.

4. Validación automática: checksum + verificación de consistencia post-backup.

**Edge cases**

- Inconsistencias: backup se marca `FAILED` y dispara alerta “restore smoketest” obligatorio antes de declarar OK.

### 4.2 Ledger/Finanzas (append-only + snapshots + reconciliación)

**Happy path**

1. Ledger tratado como append-only.

2. Snapshots financieros inmutables con hash + metadatos (idealmente WORM).

3. Reconciliation job diario/horario compara:

- totales OLTP vs ledger

- ledger vs payouts ejecutados

- órdenes vs documentos emitidos

**Edge cases**

- Restore Tier 0: requiere modo seguro financiero (ver 4.5) para evitar dobles payouts/refunds.

### 4.3 Documentos fiscales/PoD (WORM)

**Happy path**

- Al emitirse documento:

    - guardar PDF final + JSON snapshot (o hash+ref) en bucket WORM/Object Lock,

    - replicación cross-region respetando residencia por país,

    - inventario/manifest con hashes para detectar corrupción.

**Edge cases**

- “Backups clásicos” no sustituyen WORM: continuidad se logra con replicación + manifests; no con “copiar y pegar”.

### 4.4 Archivos no-WORM (media/adjuntos)

**Happy path**

- Versioning ON.

- Lifecycle por clase (evidencia disputas > adjuntos chat).

- Restauración típica: undelete por versión.

### 4.5 Restauración (runbooks obligatorios)

**Modos soportados**

- PITR full restore (volver a T-x).

- Restore parcial por país/tenant (si el diseño lo permite).

- Restore por entidad (orden específica, conversación, archivo puntual).

- Documentos WORM: no “restore”; se recupera acceso desde bucket replicado.

**Validación post-restore (gating)**

- checksums + conteos esperados

- integridad referencial (órdenes ↔ items ↔ pagos ↔ ledger)

- sanity de estados críticos (no dejar `PAID` sin ledger)

- comparación hashes snapshots/documentos contra manifest

**Modo seguro financiero (anti-catástrofe)**\
Al restaurar Tier 0:

1. Plataforma en “read-only de dinero”: permitir navegar/soporte, bloquear:

    - nuevos payouts

    - refunds automáticos

    - cambios de fee/tax

2. Reconciliación contra Rapyd/webhooks:

    - pagos confirmados fuera que faltan

    - intents duplicados

3. Rehabilitar dinero solo si reconciliación OK + auditoría del incidente registrada.

---

## 5) Reglas y políticas (retención, ciclos de vida, compliance)

### 5.1 Principios no negociables

- WORM real para fiscal/legal (no borrar antes de retención por país).

- Snapshot fiscal/financiero: facturas/recibos basados en datos congelados de la orden.

- GDPR/Privacy vs evidencia financiera:

    - perfiles/marketing: crypto-shredding inmediato si aplica,

    - cuentas con transacciones: `DELETED_PENDING_ARCHIVE` → bóveda fiscal (cold) por tiempo legal y luego purga.

- Backups no deben permitir “revivir” datos destruidos por crypto-shredding.

### 5.2 Tiers de criticidad (RPO/RTO) — estructura canónica

**Tier 0 (Dinero/Evidencia):** ledger, pagos, payouts, disputas, snapshots financieros, docs fiscales/PoD

- RPO: 0–5 min

- RTO: 30–120 min

- Regla extra: restore idempotente (sin duplicar cobros/payouts).

**Tier 1 (Operación marketplace):** órdenes, catálogo, usuarios, mensajería, soporte, reputación, cobertura/capacidad

- RPO: 15–30 min

- RTO: 4–8 h

**Tier 2 (Analítica/BI):** warehouse, cohortes, dashboards

- RPO: 24 h

- RTO: 24–72 h

**Regla de gobernanza:** RPO/RTO se vuelven policy por país (costos y jurisdicciones).

### 5.3 Matriz de retención (plantilla policy por país)

Estructura definida (valores exactos se parametrizan):

- Volátil: 7–30 días

- Operativo: 30–180 días

- Evidencia disputas/soporte: 1–3 años

- Fiscal/Legal (WORM): 5–10+ años

- KYC/AML: 5–10 años

- Bóveda fiscal: solo lo legalmente requerido para `DELETED_PENDING_ARCHIVE`, luego purga

---

## 6) Modelo de datos (policies + evidencia operativa)

### 6.1 backup_policies (por país)

**Suposición:** el doc define “policy por país” pero no fija tabla; se normaliza de forma consistente con Governance.

- `country_code`

- `tier0_rpo_minutes`, `tier0_rto_minutes`

- `tier1_rpo_minutes`, `tier1_rto_minutes`

- `tier2_rpo_hours`, `tier2_rto_hours`

- `retention_matrix_json`

- `data_residency_constraints_json`

- `worm_replication_profile`

- `effective_from`, `effective_to`, `version`

Índices:

- unique(`country_code`,`version`)

- (`country_code`,`effective_from desc`)

### 6.2 backup_runs

- `run_id`

- `resource_type` (OLTP_DB, LEDGER, WORM_BUCKET, NON_WORM_BUCKET, LOG_EXPORT, WAREHOUSE)

- `country_code`

- `strategy` (PITR, SNAPSHOT, LOGICAL_EXPORT, INVENTORY_MANIFEST)

- `status` (SUCCESS|FAILED)

- `checksum_hash`

- `started_at`, `ended_at`

- `details_json`

Índices:

- (`resource_type`,`status`,`ended_at desc`)

- (`country_code`,`ended_at desc`)

### 6.3 restore_runs

- `restore_id`

- `mode` (PITR_FULL, PARTIAL_COUNTRY, ENTITY_RESTORE)

- `target_timestamp`

- `country_code`

- `status`

- `validation_report_ref`

- `money_readonly_mode` (bool)

- `approved_by` (si break-glass)

- `created_at`

### 6.4 worm_manifests

- `manifest_id`

- `country_code`

- `bucket_id`

- `generated_at`

- `sha256_index_ref`

- `replication_lag_seconds`

---

## 7) Eventos y triggers (colas/jobs) + idempotencia

### Workers/cron jobs obligatorios (definidos)

- `backup.db.continuous_pitr`

- `backup.db.daily_snapshot`

- `backup.db.weekly_logical_export`

- `backup.object_inventory` (manifest + hashes)

- `backup.restore_smoketest` (restore a staging + checks)

- `backup.retention_enforcer`

- `backup.dr_replication_monitor`

### Eventos mínimos

- `BACKUP_SUCCEEDED` / `BACKUP_FAILED`

- `RESTORE_STARTED` / `RESTORE_VALIDATION_FAILED` / `RESTORE_COMPLETED`

- `WORM_MANIFEST_GENERATED`

- `WORM_REPLICATION_DEGRADED`

- `PITR_LAG_HIGH`

- `DR_FAILOVER_EXECUTED`

- `EXPORT_PACK_CREATED/DOWNLOADED`

### Idempotencia

- Cada job escribe `run_id` y es idempotente por `(resource_type, schedule_window, country_code)`.

- Restore smoketest idempotente por `(policy_version, latest_backup_ref)`.

---

## 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)

### Observabilidad + Resiliencia

- Backups/DR son “first-class”: métricas/alertas integradas (ver 9).

### Auditoría

- Todo restore/export/lectura de bóveda fiscal se audita (append-only) y, si es evidencia, se preserva inmutable.

### Integraciones externas (Pagos/Rapyd)

- Tras restore Tier 0, reconciliar contra webhooks/estado proveedor antes de reabrir dinero.

### Archivos (WORM/Non-WORM)

- WORM: replicación + manifests con hashes.

- Non-WORM: versioning + lifecycle + undelete por versión.

---

## 9) Observabilidad (métricas, alertas, SLOs)

### Métricas (SRE) definidas

- `backup_last_success_timestamp{resource}`

- `backup_age_minutes{resource}`

- `backup_success_rate_24h{resource}`

- `restore_smoketest_pass_rate`

- `pitr_lag_seconds`

- `worm_bucket_replication_lag`

- `dr_replication_health`

### Alertas definidas

- “no backup en X horas”

- “PITR lag > umbral”

- “restore smoketest falló”

- “replicación WORM degradada”

---

## 10) Seguridad y auditoría (quién hizo qué, evidencia, retención)

- Cifrado en tránsito y reposo para todo backup.

- Separación de roles (BackupOperator vs BackupAuditor vs SecurityAdmin).

- Break-glass con aprobación dual + justificación obligatoria + logging inmutable.

- Compatibilidad crypto-shredding:

    - no revivir lo destruido,

    - para finanzas retenidas por ley: no destruir llaves hasta fin de retención; mover a bóveda fiscal restringida.

---

## 11) Compatibilidad con sistemas existentes (dependencias directas)

- **Facturación & Documentos:** PDFs + snapshots a WORM; consistencia histórica por orden.

- **Auditoría:** registra restore/export/lecturas de bóveda; WORM para evidencia.

- **Seguridad:** crypto-shredding y bóveda fiscal para `DELETED_PENDING_ARCHIVE`.

- **Observabilidad:** jobs de backup/DR con métricas/alertas first-class.

- **Integraciones/Pagos:** reconciliación post-restore contra Rapyd/webhooks antes de reactivar dinero.

---

### Conflictos/incoherencias corregidas (dentro de Copia de Seguridad)

1. **“Backup = continuidad” ignorando WORM** → corregido: WORM es la caja fuerte; continuidad se logra con replicación + manifests; backups clásicos no sustituyen.

2. **Restores que duplican dinero** → corregido: Tier 0 exige restauración idempotente + “modo read-only de dinero” + reconciliación con proveedor.

3. **Retención única para todo (rompe compliance)** → corregido: retención diferenciada por clase + policy por país.

4. **GDPR/privacy destruyendo evidencia financiera** → corregido: `DELETED_PENDING_ARCHIVE` + bóveda fiscal (cold) por tiempo legal, luego purga.

5. **Backups “sin pruebas”** → corregido: `backup.restore_smoketest` + gating post-restore + métricas/alertas obligatorias.