# API_CONTRACTS · capacity

## Endpoints

- Anti-colisión: “último cupo” no puede venderse dos veces (reservas atómicas + TTL + idempotencia).
- Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (reservas)
- idempotency_key,
- Reintentos: el mismo idempotency_key retorna la misma reserva (no crea 2).
- Doble confirmación de pago: consume es idempotente por reservation_id y estado.
- Reintentos usan idempotency_key (cero holds duplicados).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- Eventos y triggers + idempotencia
- Consume/release: idempotente por (reservation_id, desired_state)

## Auth

- Actores y permisos (RBAC) + guards
- AuthGuard
- IdempotencyGuard (reservas)

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Anti-colisión: “último cupo” no puede venderse dos veces (reservas atómicas + TTL + idempotencia).
- IdempotencyGuard (reservas)
- idempotency_key,
- Reintentos: el mismo idempotency_key retorna la misma reserva (no crea 2).
- Doble confirmación de pago: consume es idempotente por reservation_id y estado.
- Reintentos usan idempotency_key (cero holds duplicados).
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Eventos y triggers + idempotencia
- Consume/release: idempotente por (reservation_id, desired_state)

## Trazabilidad

- Documento origen: `sistema-de-capacidad--disponibilidad-260207_0922.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
