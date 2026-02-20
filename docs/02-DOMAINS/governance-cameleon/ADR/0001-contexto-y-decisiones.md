# ADR-0001: Contexto y decisiones clave (governance-cameleon)

- **Estado**: Aprobado
- **Contexto**: Coverage y decisión “puede entregar aquí” usa lat/lng + zones.

## Decisiones
- Coverage y decisión “puede entregar aquí” usa lat/lng + zones.
- latencia de policy_evaluate sube (riesgo UX y checkout)
- Sistema de Gobernanza multi-país + App Camaleón v2.0 (Policy Engine + Server-Driven UI) — corregido y unificado
- Fuente de verdad: “Sistema: Gobernanza multi-país + App Camaleón (Policy Engine + Server-Driven UI)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema central que resuelve qué reglas aplican y qué UI se renderiza en tiempo real según un contexto: país → hub/ciudad → zona, rol (buyer/seller/ops/admin), intención (ASAP/programada), flags/experimentos y compliance. Es la “columna vertebral” para operar multi-país sin hardcode y sin releases constantes: App Camaleón (server-driven UI).

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `Sistema Gobernanza multi-país + App Camaleón.docx`
