# genie

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye (por esta entrega “Solo Genie”)
- Cada resultado incluye etiquetas:
- 5) Reglas y políticas (hard constraints, modos, límites)

## Dependencias
- Address/ContextGuard: requiere contexto territorial válido (country/hub/zone) y dirección geocodificada (por dependencia de cobertura).
- Usuario no tiene dirección válida: Genie no puede pasar CoverageGate; debe forzar captura de dirección (dependencia; la UI es Camaleón).
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Latencia p95 alta (candidate gen excesivo o dependencia lenta)
- 11) Compatibilidad con sistemas existentes (dependencias directas)

## Trazabilidad
- Documento origen: `sistema-de-genie-260207_1012.docx`
- Título extraído: "Sistema Genie v2.0 (Gift Wizard / “Pregúntale al Genie”) — Solo Genie (sin Memory)".
