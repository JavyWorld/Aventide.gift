# DATA_CONTRACTS · capacity

## Entidades y campos
- Se genera “allocation final” que la Orden snapshottea.
- Campos:
- La orden snapshottea:
- delivery_type y slot influyen en delivery_fee/asap_fee (se snapshottea).
- Ledger/Escrow
- Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado
- Fuente de verdad: “Sistema #5 — Capacidad & Disponibilidad (Capacity, Scheduler, Stock, Cupos, Temporadas)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora

## Constraints y claves de negocio
- Anti-colisión: “último cupo” no puede venderse dos veces (reservas atómicas + TTL + idempotencia).
- IdempotencyGuard (reservas)
- idempotency_key,
- Reintentos: el mismo idempotency_key retorna la misma reserva (no crea 2).
- 4.3 Consumir Reservation (pago confirmado)
- Pago confirmado → POST /checkout/reservations/:id/consume.
- Doble confirmación de pago: consume es idempotente por reservation_id y estado.
- Nunca se confirma una orden pagada sin una Reservation CONSUMED cuando el modo lo requiere.


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
