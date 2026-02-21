# INVARIANTS · governance-cameleon

Reglas no negociables del dominio:
- Determinismo: misma entrada (PolicyContext) ⇒ misma salida (ResolvedPolicy + UI Profile).
- Snapshot inmutable de Operación definida y validada lo que afecte dinero/validaciones en la orden (pasado no cambia).
- Cero hardcode por país: UI y reglas cambian desde consola ops con auditoría + rollback.
- Policy Engine determinista: resuelve reglas operativas/financieras/compliance/UI constraints por contexto.
- Consola “Regional OS”: edición visual de UI + rulesets + simulador + auditoría + rollback.
- AUDIT/FINANCE/LEGAL: lectura de auditoría; vistas de diffs y snapshots.
- audit.read (audit/finance)
- AuditGuard (diffs + quién/cuándo/qué)
- Keys no permitidas en seller_overrides: se ignoran y se auditan como intento inválido (anti-“ifs infinitos”).
- Overlap policy: permitido solo con priority + auditoría.


## Control operativo verificable

- Owner: `Equipo governance-cameleon`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-GOVERNANCECA-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/governance-cameleon/dominio-governance-cameleon-operacion`
  - `https://jira.aventide.gift/browse/OPS-GOVERNANCECA-241`

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
