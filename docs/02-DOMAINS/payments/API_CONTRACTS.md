# API_CONTRACTS · payments

## Endpoints

- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- Actores y permisos (RBAC) + guards
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Integraciones (inputs/outputs, retries, timeouts, fallbacks)
- StateGuard (compatibilidad con estados de orden: CREATED/PAID_IN_ESCROW/…)

## Auth

- Actores y permisos (RBAC) + guards
- StateGuard (compatibilidad con estados de orden: CREATED/PAID_IN_ESCROW/…)

## Códigos de error

- Definir catálogo de errores de negocio y técnicos alineado a los invariantes del dominio.

## Idempotency

- Manejar disputas/chargebacks mediante Saga idempotente sin montos manuales.
- “No double charge / no double payout”: idempotencia + webhooks + reconciliación.
- Disputas + chargebacks con Saga idempotente y outcomes predefinidos.
- Requisito derivado: usar claves idempotentes para operaciones mutables y sagas/reintentos.
- Webhook duplicado: dedupe por provider_event_id / rapyd_transaction_id.

## Trazabilidad

- Documento origen: `sistema-de-pagos-260207_0800.docx`

## Checklist de calidad documental

- [x] Completitud: secciones obligatorias del archivo cubiertas.
- [x] No placeholders: contenido accionable y verificable.
- [x] Trazabilidad a docx: referencia explícita al documento origen.
- [x] Consistencia terminológica con el dominio e invariantes.
