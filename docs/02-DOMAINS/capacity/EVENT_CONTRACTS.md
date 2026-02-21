# EVENT_CONTRACTS · capacity

## Catálogo de eventos (nombre, payload, producer, consumer, guarantees)
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- 4.2 Crear Reservation (Soft Hold) — núcleo anti-sobreventa
- season_rules por país (event_key, fechas):
- 5.5 Anti-sobreventa (reglas invariantes)
- country_id, event_key, start_at, end_at
- unique(country_id,event_key,start_at)
- 7) Eventos y triggers + idempotencia
- Eventos mínimos
- season_event_key, surge_multiplier, asap_fee_flag (si aplica),
- season_queue_mode_enabled_total{country,event_key}


## Control operativo verificable

- Owner: `Equipo capacity`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-CAPACITY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/capacity/dominio-capacity-operacion`
  - `https://jira.aventide.gift/browse/OPS-CAPACITY-241`

## Trazabilidad
- Documento origen: `sistema-de-capacidad--disponibilidad-260207_0922.docx`
