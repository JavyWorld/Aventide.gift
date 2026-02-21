# INVARIANTS · capacity

Reglas no negociables del dominio:
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- Anti-colisión: “último cupo” no puede venderse dos veces (reservas atómicas + TTL + idempotencia).
- COUNTRY_OPS_LEAD / ADMIN: define season_rules por país, activa queue mode, audita disponibilidad y reservas, throttle manual temporal.
- admin.availability.audit.read
- IdempotencyGuard (reservas)
- AuditGuard (reservas, consumo, release, autopause, throttling)
- idempotency_key,
- Reintentos: el mismo idempotency_key retorna la misma reserva (no crea 2).
- Doble confirmación de pago: consume es idempotente por reservation_id y estado.
- 5.5 Anti-sobreventa (reglas invariantes)


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
