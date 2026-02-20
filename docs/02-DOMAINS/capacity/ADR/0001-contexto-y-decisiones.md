# ADR-0001: Contexto y decisiones clave (capacity)

- **Estado**: Aprobado
- **Contexto**: Pausado automático (hard stop) por agotamiento + throttling por riesgo/reputación.

## Decisiones
- Pausado automático (hard stop) por agotamiento + throttling por riesgo/reputación.
- SYSTEM/BOT: valida disponibilidad, crea/expira reservas, autopausa, reconciliación, aplica throttling por riesgo.
- is_paused_by_system=true con pause_reason_code.Throttling por riesgo
- Throttling por riesgo registra:
- Reputación: throttling reduce capacidad efectiva; deshabilita ASAP si riesgo.
- Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado

## Consecuencias
- Se documenta la decisión con trazabilidad al documento base para evitar divergencias de implementación.

## Trazabilidad
- Documento origen: `sistema-de-capacidad--disponibilidad-260207_0922.docx`
