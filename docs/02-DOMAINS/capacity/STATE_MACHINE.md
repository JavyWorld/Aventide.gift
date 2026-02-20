# STATE_MACHINE · capacity

## Estados detectados/derivados
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- 4) Flujos end-to-end (happy path + edge cases)
- Doble confirmación de pago: consume es idempotente por reservation_id y estado.
- 7) Eventos y triggers + idempotencia
- Eventos mínimos
- Consume/release: idempotente por (reservation_id, desired_state)

## Transiciones y eventos de entrada/salida
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- 7) Eventos y triggers + idempotencia
- Eventos mínimos
- Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado
- Fuente de verdad: “Sistema #5 — Capacidad & Disponibilidad (Capacity, Scheduler, Stock, Cupos, Temporadas)”.
- 1) Definición y objetivos del sistema/módulo
- Objetivos (duros):
- Evitar promesas falsas: si el sistema dice “no hay cupo/stock/slot”, no se puede pagar.

## Trazabilidad
- Documento origen: `sistema-de-capacidad--disponibilidad-260207_0922.docx`
