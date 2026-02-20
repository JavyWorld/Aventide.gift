# rate-engine

## Qué resuelve
- 1) Definición y objetivos del sistema/módulo

## Límites del dominio
- 2) Alcance (incluye / excluye)
- Incluye
- ops_fee_cap_pct (fee buyer-facing para “Ops local” bajo límites)
- Excluye
- 5) Reglas y políticas (límites, expiraciones, caps, validaciones)

## Dependencias
- Cada time_window (ej. hourly/daily) por country_code + segment_key, el servicio:
- platform_fee_pct es independiente del bucket ops, pero sujeto a floors/ceilings por país/segmento.
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- 11) Compatibilidad con sistemas existentes (dependencias directas)
- Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)

## Trazabilidad
- Documento origen: `sistema-unificado-take-rate-engine--revenue-rate-engine-v20-260207_0946.docx`
- Título extraído: "Sistema Unificado “Take Rate Engine + Revenue Rate Engine” v2.0 (Rate Intelligence OS)".
