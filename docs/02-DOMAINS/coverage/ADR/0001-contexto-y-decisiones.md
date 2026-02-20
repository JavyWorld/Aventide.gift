# ADR-0001: Contexto y decisiones clave (coverage)

- **Estado**: Aprobado
- **Contexto**: Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado

## Decisiones
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Objetivos:
- Evitar órdenes imposibles: sin cobertura no hay calendario, no hay checkout y no hay pago.

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
