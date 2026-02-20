# INVARIANTS · search

Reglas no negociables del dominio:
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- Curaduría (merchandising) por Ops/Admin con auditoría y expiración.
- Contexto siempre: no existe búsqueda “global sin país/zona”.
- Herramientas de curaduría: boosts, pins, blocklist, spotlight con expiración y audit trail.
- RBAC (solo para endpoints admin/ops de merchandising, con auditoría).
- Se audita: quién, cuándo, qué, alcance (country/hub/zone), expiración.
- Blocklist (términos/productos) no se permite sin razón y ticket interno (audit trail obligatorio).
- 5.2 Guardrails invisibles (siempre)
- 6) Modelo de datos (índice + configuración + auditoría)
- 6.3 Merchandising overrides (auditables, con expiración)

## Trazabilidad
- Documento origen: `sistema-de-busqueda-260207_0312.docx`
