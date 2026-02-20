# RUNBOOKS · orders

## Operación
- SLA: aceptación rápida, producción, pickup, entrega, con alertas/acciones.
- En orden se persiste promises y items_snapshot con add-ons (operación).
- 9) Observabilidad (logs, métricas, alertas, SLOs)
- Alertas
- Sistema de Órdenes v2.0 (corregido y unificado)
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.

## Incidentes, rollback y backfill
- Reintentos: idempotencia por payment_attempt_id.
- Sistema de Órdenes v2.0 (corregido y unificado)
- Fuente de verdad: documento “Sistema de Órdenes (Aventide Gift)”.Objetivo del rewrite: convertir Órdenes en un motor operativo determinista (state machine + escrow + evidencias + SLA + cancelaciones + timeline), eliminando improvisación y evitando conflictos con Contenido/Capacidad/Logística, Soporte/Disputas, Auditoría y Analítica.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que convierte un checkout en una entrega real con:
- Snapshot inmutable de precios/fees/items/dirección/promesa.
- Máquina de estados estricta (no saltos).
- Reglas cerradas de cancelación por estado (y ventanas).

## Trazabilidad
- Documento origen: `sistema-de-ordenes-260207_0037.docx`
