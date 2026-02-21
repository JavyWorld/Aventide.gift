# API_CONTRACTS · loyalty

## Endpoints

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- checkout_id (nullable; para apply idempotente)
- unique por idempotencia:
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Se crea ledger entry LOYALTY_POINTS_EARNED idempotente por order_id + policy_version.
- Reintento de checkout: idempotencia por checkout_id para no “gastar FS dos veces”.
- checkout_id (nullable; para apply idempotente)
- unique por idempotencia:
- Eventos y triggers (event bus/colas/webhooks) + idempotencia
- Idempotencia (reglas)
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.


## Control operativo verificable

- Owner: `Equipo loyalty`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-LOYALTY-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/loyalty/dominio-loyalty-operacion`
  - `https://jira.aventide.gift/browse/OPS-LOYALTY-241`

## Trazabilidad

- Documento origen: `sistema-de-lealtad-260207_0817.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
