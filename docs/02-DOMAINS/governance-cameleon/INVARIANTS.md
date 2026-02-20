# INVARIANTS · governance-cameleon

Reglas no negociables del dominio:
- Determinismo: misma entrada (PolicyContext) ⇒ misma salida (ResolvedPolicy + UI Profile).
- Snapshot inmutable de todo lo que afecte dinero/validaciones en la orden (pasado no cambia).
- Cero hardcode por país: UI y reglas cambian desde consola ops con auditoría + rollback.
- Policy Engine determinista: resuelve reglas operativas/financieras/compliance/UI constraints por contexto.
- Consola “Regional OS”: edición visual de UI + rulesets + simulador + auditoría + rollback.
- AUDIT/FINANCE/LEGAL: lectura de auditoría; vistas de diffs y snapshots.
- audit.read (audit/finance)
- AuditGuard (diffs + quién/cuándo/qué)
- Keys no permitidas en seller_overrides: se ignoran y se auditan como intento inválido (anti-“ifs infinitos”).
- Overlap policy: permitido solo con priority + auditoría.

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
