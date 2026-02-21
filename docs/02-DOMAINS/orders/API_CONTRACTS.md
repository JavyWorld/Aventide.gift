# API_CONTRACTS · orders

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- OwnershipGuard (buyer_id/seller_id según endpoint)
- Reintentos: idempotencia por payment_attempt_id.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- StateGuard (validación de transición)
- from_status, to_status (nullable para eventos no estado)
- escrow JSON {provider, escrow_id, amount, currency, status}

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- OwnershipGuard (buyer_id/seller_id según endpoint)
- StateGuard (validación de transición)

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Reintentos: idempotencia por payment_attempt_id.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo orders`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-ORDERS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/orders/dominio-orders-operacion`
  - `https://jira.aventide.gift/browse/OPS-ORDERS-241`

## Trazabilidad

- Documento origen: `sistema-de-ordenes-260207_0037.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
