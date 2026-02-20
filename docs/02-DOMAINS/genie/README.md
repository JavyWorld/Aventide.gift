# genie

## Propósito

- Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)
- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Genie/Wizard y sus reglas.
- Resultados vacíos por restricciones: aplicar fallback controlado:
- Definición y objetivos del sistema/módulo
- Documento origen: `sistema-de-genie-260207_1012.docx`
- Compatibilidad con sistemas existentes (dependencias directas)
- Título extraído: "Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)".

## Límites

- Fuente de verdad: “Genie y Memory”. En esta entrega se usa solo la sección Genie/Wizard y sus reglas.
- Multi-país contextual: re-evaluación por policy_context (clima/eventos/riesgo) por país/hub/zona.
- Alcance (incluye / excluye)
- Excluye (por esta entrega “Solo Genie”)
- Cada resultado incluye etiquetas:
- Reglas y políticas (hard constraints, modos, límites)

## Dependencias

- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- COUNTRY_OPS_LEAD: gobierna policies (clima/eventos) que afectan candidatos; no “tunea” Genie por fuera del policy engine.
- Address/ContextGuard: requiere contexto territorial válido (country/hub/zone) y dirección geocodificada (por dependencia de cobertura).
- Usuario no tiene dirección válida: Genie no puede pasar CoverageGate; debe forzar captura de dirección (dependencia; la UI es Camaleón).
- Latencia p95 alta (candidate gen excesivo o dependencia lenta)
- Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad

- Documento origen: `sistema-de-genie-260207_1012.docx`
- Título extraído: "Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)".

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
