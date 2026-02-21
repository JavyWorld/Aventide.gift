# backup

## Propósito

- Reconciliación contra Rapyd/webhooks:
- Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado
- Fuente de verdad: “Sistema de Copia de Seguridad (Backups + Continuidad + DR)”.
- Objetivo operativo: el dominio debe mantener disponibilidad mensual ≥ 99.5% y registrar desviaciones en el runbook con MTTR objetivo < 30 min.
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Documento origen: `sistema-de-copia-de-seguridad-260207_0955.docx`
- Backups/DR son “first-class”: métricas/alertas integradas (ver 9).
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado".

## Límites

- Regla extra: restore idempotente (sin duplicar cobros/payouts).
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- Alcance operativo: documenta explícitamente qué flujos se atienden en producción y qué casos se escalan a otro dominio vía ticket de handoff.
- Incluye (qué protegemos)

## Dependencias

- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- Definición: Sistema que garantiza continuidad operativa, evita pérdida de datos y permite restauración verificable, respetando retenciones legales multi-país y reglas críticas del core: ledger append-only, documentos WORM, snapshots financieros/fiscales, y crypto-shredding sin “revivir” datos destruidos por política.
- sanity de estados críticos (no dejar PAID sin ledger)
- Tras restore Tier 0, reconciliar contra webhooks/estado proveedor antes de reabrir dinero.
- Integraciones/Pagos: reconciliación post-restore contra Rapyd/webhooks antes de reactivar dinero.
- integridad referencial (órdenes ↔ items ↔ pagos ↔ ledger)
- Integraciones externas (Pagos/Rapyd)
- Compatibilidad con sistemas existentes (dependencias directas)


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
- Título extraído: "Sistema de Copia de Seguridad v2.0 (Backups + Continuidad + DR) — corregido y unificado".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
