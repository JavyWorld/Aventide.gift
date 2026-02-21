# DATA_CONTRACTS · governance-cameleon

## Entidades y campos
- Snapshot inmutable de Operación definida y validada lo que afecte dinero/validaciones en la orden (pasado no cambia).
- Policy Engine determinista: resuelve reglas operativas/financieras/compliance/UI constraints por contexto.
- Server-Driven UI (“App Camaleón”): devuelve ui_profile firmado versionado con ui_schema_version, módulos y diccionario.
- AUDIT/FINANCE/LEGAL: lectura de auditoría; vistas de diffs y snapshots.
- UIConfigSecurityGuard (schema_version + firma + constraints)
- ui_constraints (qué pantallas/inputs son obligatorios),
- ui_schema_version,
- Si firma inválida o schema incompatible: fallback local (modo degradado) con mínima funcionalidad y aviso.

## Constraints y claves de negocio
- Policy Engine determinista: resuelve reglas operativas/financieras/compliance/UI constraints por contexto.
- Server-Driven UI (“App Camaleón”): devuelve ui_profile firmado versionado con ui_schema_version, módulos y diccionario.
- SYSTEM/BOT: resolver contexto, evaluar policy, firmar configs, cache invalidation.
- UIConfigSecurityGuard (schema_version + firma + constraints)
- ui_constraints (qué pantallas/inputs son obligatorios),
- Si firma inválida o schema incompatible: fallback local (modo degradado) con mínima funcionalidad y aviso.
- Corrección de incoherencia: esta precedencia es el único mecanismo permitido; se prohíben reglas “ad-hoc” fuera de la cascada.
- config firmada (server signature)


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
