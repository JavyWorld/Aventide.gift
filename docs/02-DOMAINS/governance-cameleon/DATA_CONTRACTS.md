# DATA_CONTRACTS · governance-cameleon

## Entidades y campos
- Snapshot inmutable de todo lo que afecte dinero/validaciones en la orden (pasado no cambia).
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

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
