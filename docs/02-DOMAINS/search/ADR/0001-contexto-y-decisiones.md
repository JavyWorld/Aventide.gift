# ADR-0001: Contexto y decisiones clave (search)

- **Estado**: Aprobado
- **Contexto**: Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.

## Decisiones
- Fuente de verdad: “Sistema: Búsqueda (Search)”.Objetivo del rewrite: consolidar Búsqueda como un motor único, contextual, multi-país, con filtros invisibles (guardrails) obligatorios, ranking por etapas controlable (incluye curaduría auditada), trending/suggest deterministas, y compatibilidad estricta con Jerarquía, Contenido, Órdenes, Capacidad/Logística y Analítica.
- Filtros visibles (facets) + filtros invisibles (guardrails).
- Motor de Capacidad/Logística (solo consume “puede llegar a tiempo / está disponible” como guardrail).
- Guardrails (filtros invisibles): status ACTIVE, zona ACTIVE, logística/tiempo, disponibilidad.
- Guardrails invisibles.
- 5.2 Guardrails invisibles (siempre)

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-busqueda-260207_0312.docx`
