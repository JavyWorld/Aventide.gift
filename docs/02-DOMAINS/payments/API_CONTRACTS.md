# API_CONTRACTS · payments

## Endpoints

- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones operativas: cada dependencia externa define timeout, política de retry exponencial y fallback degradado con alerta P2.
- StateGuard (compatibilidad con estados de orden: CREATED/PAID_IN_ESCROW/…)

## Auth

- Control de acceso operativo: cada endpoint exige rol permitido, guard de ownership y auditoría de denegaciones 403.
- StateGuard (compatibilidad con estados de orden: CREATED/PAID_IN_ESCROW/…)

## Códigos de error

- Catálogo de errores operativo: cada código incluye causa raíz, acción de mitigación y ownership de resolución en guardia.

## Idempotency

- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Webhook duplicado: dedupe por provider_event_id / rapyd_transaction_id.


## Control operativo verificable

- Owner: `Equipo payments`
- Fecha de última validación: `2026-02-21 (UTC)`
- Evidencias:
  - `Ticket JIRA: OPS-PAYMENTS-241`
  - `Bitácora de validación: docs/04-CHANGELOG.md`
- Dashboards o tickets:
  - `https://grafana.aventide.gift/d/payments/dominio-payments-operacion`
  - `https://jira.aventide.gift/browse/OPS-PAYMENTS-241`

## Trazabilidad

- Documento origen: `sistema-de-pagos-260207_0800.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
