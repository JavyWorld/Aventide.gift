# API_CONTRACTS · capacity

## Endpoints y auth
- Anti-colisión: “último cupo” no puede venderse dos veces (reservas atómicas + TTL + idempotencia).
- 3) Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (reservas)
- idempotency_key,
- Reintentos: el mismo idempotency_key retorna la misma reserva (no crea 2).
- Doble confirmación de pago: consume es idempotente por reservation_id y estado.
- Reintentos usan idempotency_key (cero holds duplicados).

## Idempotency keys
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.

## Errores
- 8) Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Sistema de Capacidad y Disponibilidad v2.0 (Capacity, Scheduler, Stock, Cupos, Temporadas) — corregido y unificado
- Fuente de verdad: “Sistema #5 — Capacidad & Disponibilidad (Capacity, Scheduler, Stock, Cupos, Temporadas)”.
- 1) Definición y objetivos del sistema/módulo
- Definición: Sistema que determina qué se puede vender (inventario), cuándo (scheduler), en qué ventana/slot (slots) y con qué protección anti-sobreventa (reservas TTL), incluyendo temporadas de alta demanda con overrides de capacidad, lead time, cutoff y disparadores de pricing. Su salida es una “verdad única” consumida por Búsqueda y Checkout.

## Trazabilidad
- Documento origen: `sistema-de-capacidad--disponibilidad-260207_0922.docx`
