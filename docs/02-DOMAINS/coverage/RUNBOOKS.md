# RUNBOOKS · coverage

## Operación
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Scheduler de slots/capacidad (solo dependencia; Coverage decide si llega o no).
- aplica reglas temporales (available_days, cutoff_time, blackout_dates) para entregar a Scheduler (no decide slots; solo habilita/inhabilita).
- 5.2 Regla dura #2: Coverage Guard corre antes de slots/capacidad
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas

## Incidentes, rollback y backfill
- Sistema de Cobertura v2.0 (Coverage & Logistics Engine) — corregido y unificado
- Fuente de verdad: “Sistema de Cobertura (Coverage & Logistics Engine) — Ficha técnica”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que valida si una entrega es físicamente viable antes de mostrar disponibilidad, antes de permitir crear orden y antes de permitir pago/escrow. Es el “portero físico” del marketplace y define el contexto territorial canónico de toda operación: country_id + hub_id + zone_id?.
- Objetivos:
- Evitar órdenes imposibles: sin cobertura no hay calendario, no hay checkout y no hay pago.
- Multi-modal sin romper modelo: soportar hoy HYPER_LOCAL (radio) y mañana WORLDWIDE_SHIPPING (courier) con reglas separadas.
- Consistencia total con Búsqueda/Catálogo: lo “comprable” debe ser exactamente lo que Coverage Guard aprobaría.

## Trazabilidad
- Documento origen: `sistema-de-cobertura-260207_0907.docx`
