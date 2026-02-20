# reservas-global

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- Excluye
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)
- No tocar lo buyer-facing fuera de límites: el motor decide rates, pero el snapshot por orden es inmutable y no retroactivo.

## Dependencias
- plan de recapitalización/priorización.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- 8.1 Waterfall Engine (dependencia directa)
- 11) Compatibilidad con sistemas existentes (dependencias directas)
- Sistema de Capitalización de Reserva Global v2.0 (integrado con Motor Unificado “Take Rate Engine + Revenue Rate Engine”)

## Trazabilidad
- Documento origen: `sistema-de-reserva-global-260207_1041.docx`
- Título extraído: "Sistema de Reserva Global v2.0 (GLOBAL_RESERVE + GLOBAL_RECOVERY + CRISIS)".
