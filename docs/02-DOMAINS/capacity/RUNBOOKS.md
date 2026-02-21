# RUNBOOKS · capacity

## Operación
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- Evitar promesas falsas: si el sistema dice “no hay cupo/stock/slot”, no se puede pagar.
- Soportar inventario polimórfico: STOCK, CAPACITY, SLOTS, HYBRID.
- Inventario por producto: stock físico, cupos diarios (capacidad), slots por ventana horaria y combinaciones híbridas.
- BUYER: consulta calendario/slots, crea Reservation, paga y consume.
- SELLER: configura stock, capacidad, slots, horarios, vacaciones, temporada, pausas.

## Incidentes, rollback y backfill
- si cualquiera falla: rechaza sin side effects (rollback).
- Reintentos: el mismo idempotency_key retorna la misma reserva (no crea 2).
- Reintentos usan idempotency_key (cero holds duplicados).
- Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado
- Fuente de verdad: “Sistema #5 — Capacidad & Disponibilidad (Capacity, Scheduler, Stock, Cupos, Temporadas)”.
- 1) Objetivo operativo con SLO documentado y validación mensual registrada en bitácora
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.
- Objetivos (duros):


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
